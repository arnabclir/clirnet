# Code Directory

## 🎯 Production Code

### `gemma_final_solution.py`
**➡️ USE THIS FILE**

This is the **production-ready solution** that implements:
- ✅ Custom JSON prompting approach (recommended)
- ✅ Plain text parsing approach (alternative)
- ✅ Proper error handling
- ✅ Clean, documented code

**To run:**
```bash
python gemma_final_solution.py
```

## 📚 Reference Code

### `gemma_dspy.py`
Experimental/testing code with 3 different approaches:
1. Direct LM call (plain text) - Works
2. JSONAdapter - Fails with Gemma
3. Custom JSON prompting - Works

Use this to understand what doesn't work and why.

## 🔑 Key Pattern (Copy-Paste Ready)

```python
import dspy

# Configure Gemma
gemma_client = dspy.LM(
    model="gemini/gemma-3-27b-it",
    api_key='YOUR_API_KEY',
    use_structured_output=False  # Critical!
)
dspy.settings.configure(lm=gemma_client)

# Custom JSON prompting
prompt = f"""Look at the image: {image_url}
Respond ONLY with JSON: {{"field1": "...", "field2": "..."}}"""

raw_output = lm(prompt)
text = raw_output.completion

# Parse JSON
import re, json
json_match = re.search(r'\{.*\}', text, re.DOTALL)
details = json.loads(json_match.group(0))
```

---

**See the root README.md for complete documentation.**
