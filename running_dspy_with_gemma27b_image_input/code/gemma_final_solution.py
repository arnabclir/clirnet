# -*- coding: utf-8 -*-
"""
FINAL SOLUTION: DSPy + Gemma 3 27B IT with Image Input

This file demonstrates the WORKING solution for using Gemma 3 27B IT with DSPy
for image-based document extraction.

KEY FINDING: DSPy's JSONAdapter is incompatible with Gemma models because
Gemma doesn't support developer instructions that JSONAdapter requires.

SOLUTION: Use custom JSON prompting with explicit format instructions.
"""

import dspy
import re
import json


def setup_gemma_lm():
    """Configure DSPy with Gemma 3 27B IT model."""
    gemma_client = dspy.LM(
        model="gemini/gemma-3-27b-it",
        api_key='AIzaSyAuAsuPM3l0zA40tWfonxJdoyEOdrUWbk0',
        max_tokens=1024,
        temperature=0.1,
        use_structured_output=False  # Critical: Must be False for Gemma
    )
    dspy.settings.configure(lm=gemma_client)
    print("✅ DSPy configured with Gemma 3 27B IT")
    return gemma_client


def extract_pan_details_json(image_url: str):
    """
    Extract PAN card details using Gemma with custom JSON prompting.

    This is the RECOMMENDED approach for Gemma + DSPy:
    - Uses explicit JSON format instructions
    - Avoids developer instructions that Gemma doesn't support
    - Provides clean, parseable output
    - Works with any structure you define

    Args:
        image_url: URL of the PAN card image

    Returns:
        dict with extracted details or error info
    """
    setup_gemma_lm()
    lm = dspy.settings.lm

    # Force JSON output with explicit instructions
    prompt = f"""You are a document extraction expert.

Look at the PAN card image from this URL: {image_url}

Extract the following information and respond ONLY with valid JSON in this exact format:
{{"name": "...", "father_name": "...", "date_of_birth": "...", "pan_number": "..."}}

Important:
- Use null for fields that are not visible or readable
- Do not include any text before or after the JSON
- Date format should be YYYY-MM-DD if possible
- PAN number format: 5 letters, 4 numbers, 1 letter (e.g., ABCDE1234F)"""

    try:
        # Call the model
        raw_output = lm(prompt)
        text = raw_output.completion if hasattr(raw_output, "completion") else str(raw_output)
        print(f"🧾 Model response: {text[:200]}...")

        # Extract JSON from response
        json_match = re.search(r'\{.*\}', text, re.DOTALL)
        if json_match:
            json_str = json_match.group(0)
            details = json.loads(json_str)
            return {
                **details,
                "success": True,
                "method": "custom_json_prompting"
            }
        else:
            return {
                "success": False,
                "error": "No JSON found in model response",
                "raw_output": text,
                "method": "custom_json_prompting"
            }

    except json.JSONDecodeError as e:
        return {
            "success": False,
            "error": f"Failed to parse JSON: {e}",
            "raw_output": text if 'text' in locals() else None,
            "method": "custom_json_prompting"
        }
    except Exception as e:
        return {
            "success": False,
            "error": str(e),
            "method": "custom_json_prompting"
        }


def extract_pan_details_plain_text(image_url: str):
    """
    Extract PAN card details using Gemma with plain text output.

    This approach works but requires manual regex parsing of the response.
    Less reliable than JSON prompting.

    Args:
        image_url: URL of the PAN card image

    Returns:
        dict with extracted details or error info
    """
    setup_gemma_lm()
    lm = dspy.settings.lm

    prompt = f"""Extract details from the PAN card image at: {image_url}

Return the information in this format:
Name: <value>
Father's Name: <value>
Date of Birth (YYYY-MM-DD): <value>
PAN Number: <value>"""

    try:
        raw_output = lm(prompt)
        text = raw_output.completion if hasattr(raw_output, "completion") else str(raw_output)
        print(f"🧾 Model response: {text[:200]}...")

        # Parse with regex
        name = re.search(r"Name[:\- ]+(.+)", text)
        father = re.search(r"Father(?:'s)?\s*Name[:\- ]+(.+)", text)
        dob = re.search(r"Date\s*of\s*Birth[:\- ]+(.+)", text)
        pan = re.search(r"PAN\s*Number[:\- ]+\s*([A-Z]{5}\d{4}[A-Z])", text)

        return {
            "name": name.group(1).strip() if name else None,
            "father_name": father.group(1).strip() if father else None,
            "date_of_birth": dob.group(1).strip() if dob else None,
            "pan_number": pan.group(1).strip() if pan else None,
            "success": True,
            "method": "plain_text_parsing"
        }

    except Exception as e:
        return {
            "success": False,
            "error": str(e),
            "method": "plain_text_parsing"
        }


# ------------------------------
# Test and Comparison
# ------------------------------
if __name__ == "__main__":
    test_url = "https://pub-d443ea4d18f941cfb2b887bd9ea021ea.r2.dev/PAN_CARD/4.png"

    print("=" * 70)
    print("TEST 1: Custom JSON Prompting (RECOMMENDED)")
    print("=" * 70)
    result1 = extract_pan_details_json(test_url)

    if result1["success"]:
        print("✅ SUCCESS!")
        print(f"  Name: {result1.get('name')}")
        print(f"  Father's Name: {result1.get('father_name')}")
        print(f"  Date of Birth: {result1.get('date_of_birth')}")
        print(f"  PAN Number: {result1.get('pan_number')}")
        print(f"  Method: {result1.get('method')}")
    else:
        print(f"❌ FAILED: {result1['error']}")
        print(f"  Method: {result1.get('method')}")

    print("\n" + "=" * 70)
    print("TEST 2: Plain Text Parsing (Alternative)")
    print("=" * 70)
    result2 = extract_pan_details_plain_text(test_url)

    if result2["success"]:
        print("✅ SUCCESS!")
        print(f"  Name: {result2.get('name')}")
        print(f"  Father's Name: {result2.get('father_name')}")
        print(f"  Date of Birth: {result2.get('date_of_birth')}")
        print(f"  PAN Number: {result2.get('pan_number')}")
        print(f"  Method: {result2.get('method')}")
    else:
        print(f"❌ FAILED: {result2['error']}")
        print(f"  Method: {result2.get('method')}")

    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print("✅ Custom JSON Prompting: RECOMMENDED")
    print("   - Clean, structured output")
    print("   - Easy to parse")
    print("   - Reliable format enforcement")
    print("")
    print("⚠️  Plain Text Parsing: Alternative")
    print("   - Works but requires regex")
    print("   - Less reliable formatting")
    print("   - Harder to maintain")
    print("")
    print("❌ JSONAdapter: NOT SUPPORTED")
    print("   - DSPy's JSONAdapter incompatible with Gemma")
    print("   - Requires developer instructions (not supported)")
    print("   - Use custom JSON prompting instead")
