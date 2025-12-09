"""Very simple test to check API connectivity."""

import dspy
import sys
import time

print("[1] Importing modules...", flush=True)
try:
    from extractor import ExtractArticleSignature

    print("[OK] Modules imported", flush=True)
except Exception as e:
    print(f"[ERROR] Import failed: {e}", flush=True)
    sys.exit(1)

print("[2] Setting up LM...", flush=True)
api_key = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJHcm91cE5hbWUiOiJBcm5hYiBTYWhhIiwiVXNlck5hbWUiOiJBcm5hYiBTYWhhIiwiQWNjb3VudCI6IiIsIlN1YmplY3RJRCI6IjE5ODI3MzczNjYwNjU4ODExMzciLCJQaG9uZSI6IiIsIkdyb3VwSUQiOiIxOTgyNzM3MzY2MDYxNjgyNzM3IiwiUGFnZU5hbWUiOiIiLCJNYWlsIjoiYXJuYWIuc2FoYUBjbGlybmV0LmNvbSIsIkNyZWF0ZVRpbWUiOiIyMDI1LTExLTAxIDIwOjE2OjM0IiwiVG9rZW5UeXBlIjoxLCJpc3MiOiJtaW5pbWF4In0.m3XeUnVbGE9jojnNGWTy-kGar55vqSf1mVLOapIx2DUkjNVlvMpqVcELeL1f8d6AVkRiZFCV60K9ZEmRHUmHhCj3dgVA8CZGr_Mr5J9CmnXZC3CxpaNh2Bdobve8t8fGX4Xp3Gsq8EEFPBu15vsJC7BTnA2NIoE-D7a_wpvb3Na7-aA7lz-hwlB7oNlZJM4ppp0xIAhlLIWyf_oH3NqHmXTM22xcvYcC61qLDDJV5tjX25ALgHpfCmWttUnBjnOAr5m_z7Fe2MBHm2iyCKPT68QnprmE4vbvf9g9QUT_7KZY1ewsY8X0eVh8GGP2_fh9GFFB7i15jCGxXy4jejKn0Q"

try:
    lm = dspy.LM(
        model="openai/MiniMax-M2",
        api_key=api_key,
        api_base="https://api.minimax.io/v1",
    )
    dspy.settings.configure(lm=lm)
    print("[OK] LM configured", flush=True)
except Exception as e:
    print(f"[ERROR] LM setup failed: {e}", flush=True)
    sys.exit(1)

print("[3] Creating ChainOfThought...", flush=True)
try:
    chain = dspy.ChainOfThought(ExtractArticleSignature)
    print("[OK] ChainOfThought created", flush=True)
except Exception as e:
    print(f"[ERROR] ChainOfThought creation failed: {e}", flush=True)
    sys.exit(1)

print("[4] Calling LM (this may take 30-60 seconds)...", flush=True)
print("     Timeout in 90 seconds if no response", flush=True)

try:
    start = time.time()
    result = chain(
        title="Test Article",
        description="This is a test description for the LM to process.",
    )
    elapsed = time.time() - start
    print(f"[OK] LM responded in {elapsed:.1f}s", flush=True)
    print(f"[RESULT] Summary: {result.summary[:50]}", flush=True)
except Exception as e:
    print(f"[ERROR] LM call failed: {e}", flush=True)
    import traceback

    traceback.print_exc()
    sys.exit(1)

print("[DONE] Test completed successfully!", flush=True)
