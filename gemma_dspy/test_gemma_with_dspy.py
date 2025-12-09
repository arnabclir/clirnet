"""
Pure DSPy implementation for Gemma models that don't support system prompts.

This script demonstrates how to use DSPy with Gemma models by using the
GemmaAdapter which works around Gemma's limitation of not supporting
system prompts/developer instructions.

Key Components:
1. GemmaAdapter (from gemma_adapter.py): Custom adapter for Gemma models
2. PANCardExtraction: Standard DSPy Signature for the task
3. GemmaPANExtractor: Standard DSPy Module using Predict
"""

import dspy

from gemma_adapter import GemmaAdapter

# Configure DSPy with Gemma model and custom adapter
lm = dspy.LM(
    model="gemini/gemma-3-27b-it",
    api_key="AIzaSyAuAsuPM3l0zA40tWfonxJdoyEOdrUWbk0",
    cache=False,
)

dspy.settings.configure(lm=lm, adapter=GemmaAdapter())


# Define the task using standard DSPy Signature
# class PANCardExtraction(dspy.Signature):
#     """Extract information from a PAN card image and validate it."""


#     image_url: str = dspy.InputField(desc="URL of the PAN card image to analyze")
#     name: str = dspy.OutputField(
#         desc="Full name of the PAN card holder (not father's name), exactly as shown on the card"
#     )
#     fathername: str = dspy.OutputField(
#         desc="Father's name of the PAN card holder, exactly as shown on the card"
#     )
#     is_valid_pan: str = dspy.OutputField(
#         desc="1 if the PAN card appears valid, 0 otherwise"
#     )
class PANCardExtraction(dspy.Signature):
    image_url = dspy.InputField(desc="PAN card image URL")
    name = dspy.OutputField(desc="Full name of cardholder")
    date_of_birth = dspy.OutputField(desc="Date of birth in YYYY-MM-DD format")
    id_number = dspy.OutputField(desc="PAN number (5 letters, 4 numbers, 1 letter)")
    father_name = dspy.OutputField(desc="Father's name of cardholder")
    has_income_tax_logo = dspy.OutputField(
        desc="TRUE if Income Tax Department logo visible"
    )
    has_gov_logo = dspy.OutputField(desc="TRUE if Govt. of India logo visible")
    has_photo = dspy.OutputField(desc="TRUE if cardholder photo visible")
    has_hologram_qrcode = dspy.OutputField(desc="TRUE if hologram or QR code visible")
    has_national_emblem = dspy.OutputField(desc="TRUE if national emblem visible")
    has_signature = dspy.OutputField(desc="TRUE if signature visible")
    is_valid_pan = dspy.OutputField(desc="1 if PAN is valid, 0 if invalid")


# Create a DSPy Module using standard patterns
class GemmaPANExtractor(dspy.Module):
    """Standard DSPy Module for PAN card extraction using Gemma."""

    def __init__(self):
        super().__init__()
        # Use standard DSPy Predict with our custom adapter
        self.extract = dspy.Predict(PANCardExtraction)

    def forward(self, image_url: str):
        """
        Extract PAN card information from an image URL.

        Args:
            image_url: URL of the PAN card image

        Returns:
            DSPy Prediction with name and is_valid_pan fields
        """
        return self.extract(image_url=image_url)


# Example usage
if __name__ == "__main__":
    # Initialize the extractor
    extractor = GemmaPANExtractor()

    # Test with a sample PAN card image
    print("Testing Gemma with Pure DSPy (Custom Adapter)...")
    try:
        result = extractor(
            image_url="https://pub-d443ea4d18f941cfb2b887bd9ea021ea.r2.dev/PAN_CARD/34.png"
        )
        print(f"Name: {result}")
    except Exception as e:
        print(f"Error: {e}")
        import traceback

        traceback.print_exc()
