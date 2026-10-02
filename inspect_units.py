import re, json

with open('data.js', 'r', encoding='utf-8') as f:
    text = f.read()

matches = re.findall(r'"unitNumber":\s*(\d+).*?"scanPages":\s*(\[[^\]]+\])', text, re.DOTALL)
for u, p in matches:
    print(f"Unit {u}: pages = {p.strip()}")
