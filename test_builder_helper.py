import json
import re

print("Building all digital tests 4 to 10...")

with open('all_reading_keys.json', encoding='utf-8') as f:
    all_keys = json.load(f)

# Helper function to generate clean parts
def build_test(t_num, theme, p1_data, p2_data, p3_data, p4_data, p5_data):
    keys = all_keys[str(t_num)]
    return {
        "id": f"test_{t_num}",
        "title": f"Practice Test {t_num}",
        "reading": {
            "title": "Paper 1 - Reading (Part 1 to Part 5)",
            "duration": 50,
            "parts": [
                {
                    "partNumber": 1,
                    "title": "Part 1: Questions 1 - 5 (Thông báo & Tin nhắn ngắn)",
                    "instruction": "Look at the text in each question. What does it say? Mark the correct letter A, B or C.",
                    "questions": [
                        {
                            "number": i + 1,
                            "context": q["context"],
                            "question": q["question"],
                            "options": q["options"],
                            "correct": keys[str(i + 1)],
                            "explanation": q["explanation"]
                        } for i, q in enumerate(p1_data)
                    ]
                },
                {
                    "partNumber": 2,
                    "title": f"Part 2: Questions 6 - 10 ({p2_data['title']})",
                    "instruction": p2_data["instruction"],
                    "teenagers": [
                        {
                            "number": i + 6,
                            "name": p["name"],
                            "demand": p["demand"],
                            "correct": keys[str(i + 6)],
                            "explanation": p["explanation"]
                        } for i, p in enumerate(p2_data["people"])
                    ],
                    "places": p2_data["places"]
                },
                {
                    "partNumber": 3,
                    "title": f"Part 3: Questions 11 - 20 ({p3_data['title']} - Đúng / Sai)",
                    "instruction": "Look at the sentences below. Read the text to decide if each sentence is correct or incorrect. If it is correct, mark A. If it is not correct, mark B.",
                    "passageTitle": p3_data["passageTitle"],
                    "passage": p3_data["passage"],
                    "questions": [
                        {
                            "number": i + 11,
                            "statement": s["statement"],
                            "correct": keys[str(i + 11)],
                            "explanation": s["explanation"]
                        } for i, s in enumerate(p3_data["statements"])
                    ]
                },
                {
                    "partNumber": 4,
                    "title": f"Part 4: Questions 21 - 25 (Đọc hiểu văn bản trắc nghiệm 4 lựa chọn)",
                    "instruction": "Read the text and questions below. For each question, choose the correct letter A, B, C or D.",
                    "passageTitle": p4_data["passageTitle"],
                    "passage": p4_data["passage"],
                    "questions": [
                        {
                            "number": i + 21,
                            "question": q["question"],
                            "options": q["options"],
                            "correct": keys[str(i + 21)],
                            "explanation": q["explanation"]
                        } for i, q in enumerate(p4_data["questions"])
                    ]
                },
                {
                    "partNumber": 5,
                    "title": "Part 5: Questions 26 - 35 (Điền từ vào chỗ trống đoạn văn)",
                    "instruction": "Read the text below and choose the correct word for each space. For each question, choose the correct letter A, B, C or D.",
                    "passageTitle": p5_data["passageTitle"],
                    "passage": p5_data["passage"],
                    "questions": [
                        {
                            "number": i + 26,
                            "options": q["options"],
                            "correct": keys[str(i + 26)],
                            "explanation": q["explanation"]
                        } for i, q in enumerate(p5_data["questions"])
                    ]
                }
            ]
        }
    }

print("Helper setup completed.")
