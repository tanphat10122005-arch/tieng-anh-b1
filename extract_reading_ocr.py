import pymupdf
from rapidocr_onnxruntime import RapidOCR
import json
import os
import time

print("Starting RapidOCR on reading pages for Tests 3 to 10...")
start_time = time.time()

doc = pymupdf.open('Sach_B1_clean.pdf')
engine = RapidOCR()

# Tests 3 to 10 page ranges (1-based: 40 to 121, 0-based: 39 to 120)
# For each test, 5 reading pages:
# Part 1, Part 2, Part 3, Part 4, Part 5
tests_pages = {}
for test_num in range(3, 11):
    base_page = 18 + (test_num - 1) * 11
    # 5 reading pages
    reading_pages = [base_page + offset for offset in range(5)]
    tests_pages[test_num] = reading_pages

ocr_results = {}

total_pages = sum(len(pages) for pages in tests_pages.values())
done = 0

for test_num, pages in tests_pages.items():
    ocr_results[test_num] = {}
    for part_idx, p_num in enumerate(pages):
        # p_num is 1-based
        page = doc[p_num - 1]
        pix = page.get_pixmap(dpi=150)
        img_bytes = pix.tobytes('png')
        res, _ = engine(img_bytes)
        
        lines = []
        if res:
            for item in res:
                box, text, score = item[0], item[1], item[2]
                lines.append({
                    "text": text.strip(),
                    "box": box,
                    "score": float(score)
                })
        
        part_num = part_idx + 1
        ocr_results[test_num][part_num] = {
            "page": p_num,
            "lines": lines
        }
        done += 1
        print(f"[{done}/{total_pages}] Test {test_num} Part {part_num} (Page {p_num}) - {len(lines)} lines")

with open('reading_ocr_cache.json', 'w', encoding='utf-8') as f:
    json.dump(ocr_results, f, ensure_ascii=False, indent=2)

print(f"Finished in {time.time() - start_time:.1f}s. Saved to reading_ocr_cache.json")
