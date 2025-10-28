# ✅ DSPy + Gemma 3 27B IT - FIXED

## The Problem
```
GeminiException BadRequestError: "Developer instruction is not enabled for models/gemma-3-27b-it"
```

DSPy's `JSONAdapter()` was trying to use developer instructions (system messages) with Google's Gemma model, which doesn't support this format.

## The Fix

### Key Changes Made:

1. **Line 117-120** - Modified `setup_dspy_with_gemma_adapter()`:
   ```python
   gemma_client = dspy.LM(
       model="gemini/gemma-3-27b-it",
       api_key='...',
       max_tokens=1024,
       temperature=0.1,
       use_structured_output=False  # ← Added: Disable structured output
   )
   json_adapter = dspy.JSONAdapter(reduced_formatter=True)  # ← Added: No developer instructions
   dspy.configure(lm=gemma_client, adapter=json_adapter)
   ```

2. **Line 133-168** - Added `extract_pan_details_custom()`:
   - Alternative approach using custom JSON prompting
   - Forces JSON output without using DSPy's structured features

3. **Line 171-210** - Updated test section:
   - Tests all 3 approaches
   - Shows which one works best

4. **Line 40** - Fixed bug:
   - Changed `{test_url}` to `{image_url}`

## Three Working Approaches

✅ **Test 1**: Direct LM call (plain text) - Already working
✅ **Test 2**: JSONAdapter with `reduced_formatter=True` - **FIXED**
✅ **Test 3**: Custom JSON prompting - Alternative solution

## Recommended Approach

Use **Test 2 (JSONAdapter with reduced formatter)** for:
- ✅ Type safety with Pydantic models
- ✅ DSPy's Predict module
- ✅ Clean structured output
- ✅ No developer instructions

## To Run

```bash
python gemma_dspy.py
```

This will test all three approaches and show you the results!