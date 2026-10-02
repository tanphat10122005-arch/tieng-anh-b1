import os
from PIL import Image

os.makedirs('assets/listening', exist_ok=True)

# Page 24 (Questions 1, 2, 3)
p24 = Image.open('scratch/doc_p24.png')
# Page 25 (Questions 4, 5, 6, 7)
p25 = Image.open('scratch/doc_p25.png')

crops_t1 = {
    "t1_q1": (p24, (40, 680, 1180, 970)),
    "t1_q2": (p24, (40, 1010, 1180, 1300)),
    "t1_q3": (p24, (40, 1340, 1180, 1660)),
    "t1_q4": (p25, (40, 160, 1180, 480)),
    "t1_q5": (p25, (40, 540, 1180, 860)),
    "t1_q6": (p25, (40, 920, 1180, 1240)),
    "t1_q7": (p25, (40, 1310, 1180, 1630)),
}

for name, (img, box) in crops_t1.items():
    cropped = img.crop(box)
    cropped.save(f'assets/listening/{name}.png')
    print(f'Saved assets/listening/{name}.png, size: {cropped.size}')
