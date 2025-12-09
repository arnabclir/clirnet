"""Test extraction with a sample article."""

import json
from extractor import ExtractionPipeline
import dspy


def test_extraction():
    """Test DSPy extraction with sample medical article."""

    # Setup MiniMax-M2
    api_key = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJHcm91cE5hbWUiOiJBcm5hYiBTYWhhIiwiVXNlck5hbWUiOiJBcm5hYiBTYWhhIiwiQWNjb3VudCI6IiIsIlN1YmplY3RJRCI6IjE5ODI3MzczNjYwNjU4ODExMzciLCJQaG9uZSI6IiIsIkdyb3VwSUQiOiIxOTgyNzM3MzY2MDYxNjgyNzM3IiwiUGFnZU5hbWUiOiIiLCJNYWlsIjoiYXJuYWIuc2FoYUBjbGlybmV0LmNvbSIsIkNyZWF0ZVRpbWUiOiIyMDI1LTExLTAxIDIwOjE2OjM0IiwiVG9rZW5UeXBlIjoxLCJpc3MiOiJtaW5pbWF4In0.m3XeUnVbGE9jojnNGWTy-kGar55vqSf1mVLOapIx2DUkjNVlvMpqVcELeL1f8d6AVkRiZFCV60K9ZEmRHUmHhCj3dgVA8CZGr_Mr5J9CmnXZC3CxpaNh2Bdobve8t8fGX4Xp3Gsq8EEFPBu15vsJC7BTnA2NIoE-D7a_wpvb3Na7-aA7lz-hwlB7oNlZJM4ppp0xIAhlLIWyf_oH3NqHmXTM22xcvYcC61qLDDJV5tjX25ALgHpfCmWttUnBjnOAr5m_z7Fe2MBHm2iyCKPT68QnprmE4vbvf9g9QUT_7KZY1ewsY8X0eVh8GGP2_fh9GFFB7i15jCGxXy4jejKn0Q"

    lm = dspy.LM(
        model="openai/MiniMax-M2",
        api_key=api_key,
        api_base="https://api.minimax.io/v1",
    )
    dspy.settings.configure(lm=lm)

    pipeline = ExtractionPipeline()

    # Sample article (one from the CSV)
    sample_title = "Bilateral nephrectomy was done in a critically ill male patient"
    sample_desc = """The person should continue to be on dialysis. The patient has ascites and pleural
    effusion which indicates he is not getting adequate dialysis. The most common cause for the patient
    developing arthritis and pleural fluid would be attributed to the quality of dialysis and inadequate
    removal of excess water from the patient's body."""

    print("🧪 Testing extraction with sample article...")
    print(f"Title: {sample_title}")
    print()

    try:
        result = pipeline.forward(title=sample_title, description=sample_desc)

        print("✅ Extraction successful!")
        print()
        print("Summary:")
        print(f"  {result.summary}")
        print()
        print("Key Facts:")
        for i, fact in enumerate(result.key_facts, 1):
            print(f"  {i}. {fact.fact}")
            print(f"     Supporting: {fact.supporting_statement}")
        print()
        print("Topics:", ", ".join(result.topics))
        print("Keywords:", ", ".join(result.keywords))
        print()

        # Save sample output
        sample_output = {
            "title": sample_title,
            "summary": result.summary,
            "key_facts": [
                {
                    "fact": fact.fact,
                    "supporting_statement": fact.supporting_statement,
                }
                for fact in result.key_facts
            ],
            "topics": result.topics,
            "keywords": result.keywords,
        }

        with open("sample_output.json", "w", encoding="utf-8") as f:
            json.dump(sample_output, f, indent=2, ensure_ascii=False)

        print("💾 Sample output saved to sample_output.json")
        return True

    except Exception as e:
        print(f"❌ Error during extraction: {str(e)}")
        import traceback

        traceback.print_exc()
        return False


if __name__ == "__main__":
    test_extraction()
