import os
from PIL import Image

os.makedirs('assets/listening', exist_ok=True)

# Page 36 (Questions 1, 2, 3)
p36 = Image.open('scratch/clean_p36.png')
# Page 37 (Questions 4, 5, 6, 7)
p37 = Image.open('scratch/clean_p37.png')

# On page 36:
# Top header is up to y=670
# Q1: approx y=680 to 950
# Q2: approx y=1010 to 1280
# Q3: approx y=1340 to 1640

# On page 37:
# Q4: approx y=160 to 480
# Q5: approx y=540 to 860
# Q6: approx y=920 to 1240
# Q7: approx y=1310 to 1630

crops_t2 = {
    "t2_q1": (p36, (40, 680, 1180, 970)),
    "t2_q2": (p36, (40, 1010, 1180, 1300)),
    "t2_q3": (p36, (40, 1340, 1180, 1660)),
    "t2_q4": (p37, (40, 160, 1180, 480)),
    "t2_q5": (p37, (40, 540, 1180, 860)),
    "t2_q6": (p37, (40, 920, 1180, 1240)),
    "t2_q7": (p37, (40, 1310, 1180, 1630)),
}

for name, (img, box) in crops_t2.items():
    cropped = img.crop(box)
    cropped.save(f'assets/listening/{name}.png')
    print(f'Saved assets/listening/{name}.png, size: {cropped.size}')
