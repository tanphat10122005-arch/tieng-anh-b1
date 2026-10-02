import os, fitz

os.makedirs('scratch', exist_ok=True)
doc = fitz.open('Sach_B1_clean.pdf')

# Let's save page 26, 27 (Test 1 listening), page 37, 38 (Test 2 listening)
p26 = doc[25].get_pixmap(dpi=150)
p26.save('scratch/clean_p26.png')

p27 = doc[26].get_pixmap(dpi=150)
p27.save('scratch/clean_p27.png')

p37 = doc[36].get_pixmap(dpi=150)
p37.save('scratch/clean_p37.png')

p38 = doc[37].get_pixmap(dpi=150)
p38.save('scratch/clean_p38.png')

print("Page 26 size:", p26.width, p26.height)
print("Page 37 size:", p37.width, p37.height)
