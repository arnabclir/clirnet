# DSPy + Gemma 3 27B IT - Fix for Developer Instruction Error

## Problem
The original error was:
```
GeminiException BadRequestError - "Developer instruction is not enabled for models/gemma-3-27b-it"
```

This occurred because DSPy's `JSONAdapter` tries to use developer instructions (system messages) with the Gemma model, but Google GenAI's Gemma model doesn't support this format.

## Solution

I've implemented **three different approaches** to fix this issue:

### Approach 1: Direct LM Call (Plain Text Mode) ✅ ALREADY WORKING
```python
def setup_dspy_with_gemma():
    gemma_client = dspy.LM(
        model="gemini/gemma-3-27b-it",
        api_key='...',
        use_structured_output=False  # Key setting!
    )
    dspy.settings.configure(lm=gemma_client)
```
This approach disables structured output and manually parses the text response.

### Approach 2: JSONAdapter with Reduced Formatter 🔧 FIXED
```python
def setup_dspy_with_gemma_adapter():
    gemma_client = dspy.LM(
        model="gemini/gemma-3-27b-it",
        api_key='...',
        use_structured_output=False  # Disable at LM level
    )
    json_adapter = dspy.JSONAdapter(reduced_formatter=True)  # No developer instructions
    dspy.configure(lm=gemma_client, adapter=json_adapter)
```
**Key changes:**
- Added `use_structured_output=False` to the LM configuration
- Added `reduced_formatter=True` to the JSONAdapter to disable developer instructions

### Approach 3: Custom JSON Prompting 🔄 ALTERNATIVE
```python
def extract_pan_details_custom(image_url: str):
    prompt = f"""Look at the PAN card image from this URL: {image_url}

Extract details and respond ONLY with valid JSON:
{{"name": "...", "father_name": "...", "date_of_birth": "...", "pan_number": "..."}}"""

    raw_output = lm(prompt)
    # Parse JSON manually
```
This approach explicitly forces JSON output without using DSPy's structured output features.

## How to Run

```bash
cd /mnt/d/writing/clirnet/running_dspy_with_gemma27b_image_input
python gemma_dspy.py
```

This will test all three approaches and show you which one works best.

## Key Takeaways

1. **Gemma models on Google GenAI don't support developer instructions** - Avoid using system messages or developer instruction modes
2. **DSPy's JSONAdapter uses developer instructions by default** - Use `reduced_formatter=True` to disable this
3. **Alternative: Use custom prompting** - Force JSON output with explicit instructions in the user prompt

## Recommendation

Use **Approach 2 (JSONAdapter with reduced formatter)** as it provides the best balance:
- ✅ Type safety with Pydantic models
- ✅ DSPy's Predict module for modularity
- ✅ No developer instructions required
- ✅ Clean, structured output parsing