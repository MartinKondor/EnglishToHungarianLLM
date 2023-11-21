from typing import List
from jsonl import jsonl


with open("raw.txt", "r") as file:
    contents = file.read()


lines: List[str] = [line.strip() for line in contents.split("```") if line.strip()]
for idx in range(0, len(lines), 2):
    #print("Hu:")
    #print()
    #print("En:")
    #print(lines[idx + 1])
    #print(42*"-")

    jsonl.append({
        "hu": lines[idx],
        "en": lines[idx + 1]
    }, "data.jsonl")
