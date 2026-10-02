import json
import re
import sys

with open('reading_ocr_cache.json', encoding='utf-8') as f:
    ocr_data = json.load(f)

with open('all_reading_keys.json', encoding='utf-8') as f:
    all_keys = json.load(f)

def clean_text(lines):
    # filter out header junk like TEST X, PAPER 1, etc.
    filtered = []
    for l in lines:
        t = l.strip()
        if not t: continue
        if re.match(r'^(TEST\s*\d+|PAPER\s*1.*|PART\s*\d+|Questions\s*\d+-\d+)', t, re.I):
            continue
        filtered.append(t)
    return filtered

parsed_tests = {}

for t_num in range(3, 11):
    t_str = str(t_num)
    t_ocr = ocr_data[t_str]
    t_keys = all_keys[t_str]
    
    # ------------------ PART 1 (Q1-5) ------------------
    p1_lines = [l['text'] for l in t_ocr['1']['lines']]
    # Let's inspect p1_lines
    p1_text = '\n'.join(p1_lines)
    
    # We can structure questions 1 to 5
    # Look for patterns of options A, B, C
    q_list_p1 = []
    for q_n in range(1, 6):
        corr = t_keys.get(str(q_n), 'A')
        q_list_p1.append({
            "number": q_n,
            "context": f"Thông báo / Biển báo câu {q_n} (Đề thi Test {t_num})",
            "question": f"What does this text say?",
            "options": [
                {"key": "A", "text": "Option A"},
                {"key": "B", "text": "Option B"},
                {"key": "C", "text": "Option C"}
            ],
            "correct": corr,
            "explanation": f"Đáp án đúng là {corr} theo chuẩn bài thi Cambridge Preliminary PET Test {t_num}."
        })
    
    # ------------------ PART 2 (Q6-10) ------------------
    # 5 people (6-10) and places A-H
    p2_people = []
    for q_n in range(6, 11):
        corr = t_keys.get(str(q_n), 'A')
        p2_people.append({
            "number": q_n,
            "name": f"Person {q_n}",
            "demand": f"Requirements and preferences for question {q_n}",
            "correct": corr,
            "explanation": f"Lựa chọn phù hợp nhất cho câu {q_n} là {corr}."
        })
    
    p2_places = []
    for code in ['A','B','C','D','E','F','G','H']:
        p2_places.append({
            "code": code,
            "title": f"Option {code}",
            "desc": f"Description for review {code}."
        })
        
    # ------------------ PART 3 (Q11-20) ------------------
    p3_questions = []
    for q_n in range(11, 21):
        corr = t_keys.get(str(q_n), 'A')
        p3_questions.append({
            "number": q_n,
            "statement": f"Statement for sentence {q_n} (Test {t_num})",
            "correct": corr,
            "explanation": f"Câu này là {'ĐÚNG (A - Correct)' if corr == 'A' else 'SAI (B - Incorrect)'} theo nội dung bài đọc."
        })
        
    # ------------------ PART 4 (Q21-25) ------------------
    p4_questions = []
    for q_n in range(21, 26):
        corr = t_keys.get(str(q_n), 'A')
        p4_questions.append({
            "number": q_n,
            "question": f"Reading comprehension question {q_n}",
            "options": [
                {"key": "A", "text": "Option A"},
                {"key": "B", "text": "Option B"},
                {"key": "C", "text": "Option C"},
                {"key": "D", "text": "Option D"}
            ],
            "correct": corr,
            "explanation": f"Đáp án đúng là {corr}."
        })
        
    # ------------------ PART 5 (Q26-35) ------------------
    p5_questions = []
    for q_n in range(26, 36):
        corr = t_keys.get(str(q_n), 'A')
        p5_questions.append({
            "number": q_n,
            "options": [
                {"key": "A", "text": "Option A"},
                {"key": "B", "text": "Option B"},
                {"key": "C", "text": "Option C"},
                {"key": "D", "text": "Option D"}
            ],
            "correct": corr,
            "explanation": f"Từ điền đúng vào chỗ trống ({q_n}) là phương án {corr}."
        })
        
    parsed_tests[t_num] = {
        "p1": q_list_p1,
        "p2_people": p2_people,
        "p2_places": p2_places,
        "p3_questions": p3_questions,
        "p4_questions": p4_questions,
        "p5_questions": p5_questions
    }

print("Base parser template ready.")
