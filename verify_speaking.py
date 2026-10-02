import json, re
f = open('data.js', 'r', encoding='utf-8')
c = f.read()
f.close()
m = re.search(r'"speakingTests"\s*:\s*\[', c)
print('speakingTests starts at char', m.start())
# Find matching bracket
text = c[m.start():]
start_idx = text.index('[')
bracket = 1
i = start_idx + 1
while bracket > 0:
    ch = text[i]
    if ch == '[': bracket += 1
    elif ch == ']': bracket -= 1
    i += 1
arr_str = text[start_idx:i]
arr = json.loads(arr_str)
print(f'Found {len(arr)} tests')
for t in arr:
    print(f'  {t["id"]}: {t["title"]}')
    print(f'    Photo A: {t["part3"]["photoA"]["title"]}')
    print(f'    Photo B: {t["part3"]["photoB"]["title"]}')
    desc_a = t["part3"]["photoA"]["description"]
    desc_b = t["part3"]["photoB"]["description"]
    # Check for complex words
    for word in ['ubiquitous', 'quintessential', 'juxtaposition', 'paradigm', 'precipice']:
        if word in desc_a or word in desc_b:
            print(f'    WARNING: Complex word "{word}" found!')
    print(f'    Desc A length: {len(desc_a)} chars')
    print(f'    Desc B length: {len(desc_b)} chars')
