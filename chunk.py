import json
import os

os.makedirs("chunks", exist_ok=True)

with open("markdown/sample.md", "r", encoding="utf-8") as f:
    text = f.read()

chunk_size = 500
chunks = []

for i in range(0, len(text), chunk_size):
    chunks.append(text[i:i + chunk_size])

with open("chunks/chunks.json", "w", encoding="utf-8") as f:
    json.dump(chunks, f, indent=4)

print(f"Created {len(chunks)} chunks successfully!")