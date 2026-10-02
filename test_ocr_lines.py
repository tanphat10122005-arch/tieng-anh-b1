import json
import re
import os

print("Building all 12 digital tests for Cambridge B1 PET...")

with open('reading_ocr_cache.json', encoding='utf-8') as f:
    ocr = json.load(f)

with open('all_reading_keys.json', encoding='utf-8') as f:
    keys = json.load(f)

# Helper to get clean lines from OCR
def get_lines(test_num, part_num):
    t_str = str(test_num)
    p_str = str(part_num)
    return [item['text'] for item in ocr[t_str][p_str]['lines']]

# Let's inspect test 3 lines
print("Test 3 P1 lines count:", len(get_lines(3, 1)))
print("Test 3 P2 lines count:", len(get_lines(3, 2)))
print("Test 3 P3 lines count:", len(get_lines(3, 3)))
print("Test 3 P4 lines count:", len(get_lines(3, 4)))
print("Test 3 P5 lines count:", len(get_lines(3, 5)))
