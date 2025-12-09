"""Quick test to verify extraction works."""

import dspy
import json
from extractor import ExtractionPipeline

# Setup MiniMax-M2
api_key = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJHcm91cE5hbWUiOiJBcm5hYiBTYWhhIiwiVXNlck5hbWUiOiJBcm5hYiBTYWhhIiwiQWNjb3VudCI6IiIsIlN1YmplY3RJRCI6IjE5ODI3MzczNjYwNjU4ODExMzciLCJQaG9uZSI6IiIsIkdyb3VwSUQiOiIxOTgyNzM3MzY2MDYxNjgyNzM3IiwiUGFnZU5hbWUiOiIiLCJNYWlsIjoiYXJuYWIuc2FoYUBjbGlybmV0LmNvbSIsIkNyZWF0ZVRpbWUiOiIyMDI1LTExLTAxIDIwOjE2OjM0IiwiVG9rZW5UeXBlIjoxLCJpc3MiOiJtaW5pbWF4In0.m3XeUnVbGE9jojnNGWTy-kGar55vqSf1mVLOapIx2DUkjNVlvMpqVcELeL1f8d6AVkRiZFCV60K9ZEmRHUmHhCj3dgVA8CZGr_Mr5J9CmnXZC3CxpaNh2Bdobve8t8fGX4Xp3Gsq8EEFPBu15vsJC7BTnA2NIoE-D7a_wpvb3Na7-aA7lz-hwlB7oNlZJM4ppp0xIAhlLIWyf_oH3NqHmXTM22xcvYcC61qLDDJV5tjX25ALgHpfCmWttUnBjnOAr5m_z7Fe2MBHm2iyCKPT68QnprmE4vbvf9g9QUT_7KZY1ewsY8X0eVh8GGP2_fh9GFFB7i15jCGxXy4jejKn0Q"

lm = dspy.LM(
    model="openai/MiniMax-M2",
    api_key=api_key,
    api_base="https://api.minimax.io/v1",
)
dspy.settings.configure(lm=lm)

print("[INIT] Setting up extraction pipeline...")
pipeline = ExtractionPipeline()

print("[TEST] Article 1: Bilateral nephrectomy")
result = pipeline(
    title="Bilateral nephrectomy was done in a critically ill male patient",
    description="The person should continue to be on dialysis. The patient has ascites and pleural effusion.",
)

print("[RESULT] Summary:", result.summary[:50])
print("[RESULT] Facts:", len(result.key_facts))
print("[RESULT] Topics:", result.topics)
print("[RESULT] Keywords:", result.keywords[:3])

print("[OK] Test passed!")
