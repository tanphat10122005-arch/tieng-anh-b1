import fitz, os
from PIL import Image

os.makedirs('assets/listening', exist_ok=True)
doc = fitz.open('Sach_B1_clean.pdf')

# Test listening page pairs (page1, page2):
# We know:
# Test 1: p. 25, 26 (doc index 24, 25)
# Test 2: p. 36, 37 (doc index 35, 36)
# Test 3: p. 47, 48 (doc index 46, 47)
# Test 4: p. 58, 59 (doc index 57, 58)
# Test 5: p. 69, 70 (doc index 68, 69)
# Test 6: p. 80, 81 (doc index 79, 80)
# Test 7: p. 91, 92 (doc index 90, 91)
# Test 8: p. 102, 103 (doc index 101, 102)
# Test 9: p. 113, 114 (doc index 112, 113)
# Test 10: p. 124, 125 (doc index 123, 124)
# Test 11: p. 136, 137 (doc index 135, 136)
# Test 12: p. 149, 150 (doc index 148, 149)

tests_pages = {
    1: (24, 25),
    2: (35, 36),
    3: (46, 47),
    4: (57, 58),
    5: (68, 69),
    6: (79, 80),
    7: (90, 91),
    8: (101, 102),
    9: (112, 113),
    10: (123, 124),
    11: (135, 136),
    12: (148, 149)
}

# Standard bounding boxes for 150 DPI page (1240 x 1754):
box_q1 = (40, 680, 1180, 970)
box_q2 = (40, 1010, 1180, 1300)
box_q3 = (40, 1340, 1180, 1660)

box_q4 = (40, 160, 1180, 480)
box_q5 = (40, 540, 1180, 860)
box_q6 = (40, 920, 1180, 1240)
box_q7 = (40, 1310, 1180, 1630)

for t_num, (p1_idx, p2_idx) in tests_pages.items():
    if p1_idx >= len(doc) or p2_idx >= len(doc):
        continue
    
    # render pages
    pix1 = doc[p1_idx].get_pixmap(dpi=150)
    pix2 = doc[p2_idx].get_pixmap(dpi=150)
    
    img1 = Image.frombytes("RGB", [pix1.width, pix1.height], pix1.samples)
    img2 = Image.frombytes("RGB", [pix2.width, pix2.height], pix2.samples)
    
    img1.crop(box_q1).save(f'assets/listening/t{t_num}_q1.png')
    img1.crop(box_q2).save(f'assets/listening/t{t_num}_q2.png')
    img1.crop(box_q3).save(f'assets/listening/t{t_num}_q3.png')
    
    img2.crop(box_q4).save(f'assets/listening/t{t_num}_q4.png')
    img2.crop(box_q5).save(f'assets/listening/t{t_num}_q5.png')
    img2.crop(box_q6).save(f'assets/listening/t{t_num}_q6.png')
    img2.crop(box_q7).save(f'assets/listening/t{t_num}_q7.png')
    print(f"Test {t_num} Part 1 cropped (q1..q7)")

print("All tests Part 1 cropped successfully!")
