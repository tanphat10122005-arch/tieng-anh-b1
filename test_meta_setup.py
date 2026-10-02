import json
import re
import sys

print("Loading OCR cache and keys...")
with open('reading_ocr_cache.json', encoding='utf-8') as f:
    ocr = json.load(f)

with open('all_reading_keys.json', encoding='utf-8') as f:
    all_keys = json.load(f)

# Metadata for each test 3-10
test_metadata = {
    3: {
        "title": "Practice Test 3",
        "theme": "Public Transport, City Living & Traditional Pubs",
        "p2_title": "Part 2: Questions 6 - 10 (Ghép người với khách sạn / nơi lưu trú phù hợp)",
        "p2_inst": "These people (6-10) all want to choose a hotel to stay in for the weekend. Look at the eight reviews (A-H). Decide which hotel would be the most suitable for each person.",
        "p3_title": "Part 3: Questions 11 - 20 (Richardson's Pubs - Đúng / Sai)",
        "p3_passage_title": "Richardson's Traditional British Pubs",
        "p4_title": "Part 4: Questions 21 - 25 (Đọc hiểu văn bản trắc nghiệm 4 lựa chọn)",
        "p4_passage_title": "Tom Cruise - Hollywood Superstar",
        "p5_title": "Part 5: Questions 26 - 35 (Điền từ vào chỗ trống đoạn văn)",
        "p5_passage_title": "Denmark - Life in Scandinavia"
    },
    4: {
        "title": "Practice Test 4",
        "theme": "British Canal Holidays, Cinema & Cultural History",
        "p2_title": "Part 2: Questions 6 - 10 (Ghép khán giả với bộ phim rạp chiếu phù hợp)",
        "p2_inst": "These people (6-10) all want to see a film at the cinema. Look at the eight film reviews (A-H). Decide which film would be the most suitable for each person.",
        "p3_title": "Part 3: Questions 11 - 20 (Canal Boat Trips - Đúng / Sai)",
        "p3_passage_title": "Exploring Britain's Historic Inland Waterways by Canal Boat",
        "p4_title": "Part 4: Questions 21 - 25 (Đọc hiểu văn bản trắc nghiệm 4 lựa chọn)",
        "p4_passage_title": "Madonna - The Evolution of a Pop Icon",
        "p5_title": "Part 5: Questions 26 - 35 (Điền từ vào chỗ trống đoạn văn)",
        "p5_passage_title": "The Fascinating Story of Chocolate"
    },
    5: {
        "title": "Practice Test 5",
        "theme": "Health, Greek Destinations & Transport Heritage",
        "p2_title": "Part 2: Questions 6 - 10 (Ghép du khách với khu nghỉ dưỡng Hy Lạp phù hợp)",
        "p2_inst": "These people (6-10) are looking for a holiday destination in Greece. Look at the eight reviews (A-H). Decide which resort would be the most suitable for each person.",
        "p3_title": "Part 3: Questions 11 - 20 (East Anglia Transport Museum - Đúng / Sai)",
        "p3_passage_title": "The Transport Museum of East Anglia",
        "p4_title": "Part 4: Questions 21 - 25 (Đọc hiểu văn bản trắc nghiệm 4 lựa chọn)",
        "p4_passage_title": "Job Interviews - How to Make the Best First Impression",
        "p5_title": "Part 5: Questions 26 - 35 (Điền từ vào chỗ trống đoạn văn)",
        "p5_passage_title": "The History and Spirit of the Olympic Games"
    },
    6: {
        "title": "Practice Test 6",
        "theme": "Images of Asia, Wildlife Photography & Ocean Life",
        "p2_title": "Part 2: Questions 6 - 10 (Ghép bạn đọc với cuốn sách thư viện phù hợp)",
        "p2_inst": "These people (6-10) all want to borrow a book from the library. Look at the eight book reviews (A-H). Decide which book would be the most suitable for each person.",
        "p3_title": "Part 3: Questions 11 - 20 (A Journey in Southeast Asia - Đúng / Sai)",
        "p3_passage_title": "Exploring Vietnam and Thailand - Cultures, Landscapes and Cities",
        "p4_title": "Part 4: Questions 21 - 25 (Đọc hiểu văn bản trắc nghiệm 4 lựa chọn)",
        "p4_passage_title": "Alice Bradley - Wildlife and Nature Photographer",
        "p5_title": "Part 5: Questions 26 - 35 (Điền từ vào chỗ trống đoạn văn)",
        "p5_passage_title": "The Secret Life and Communication of Whales"
    },
    7: {
        "title": "Practice Test 7",
        "theme": "Culinary Arts, City Exploration & Modern Culture",
        "p2_title": "Part 2: Questions 6 - 10 (Ghép khán giả với chương trình truyền hình / phim tối nay)",
        "p2_inst": "These people (6-10) all want to watch something on TV tonight. Look at the eight TV programmes or films (A-H). Decide which would be the most suitable.",
        "p3_title": "Part 3: Questions 11 - 20 (Discovering Berlin - Đúng / Sai)",
        "p3_passage_title": "Berlin - A Modern City with Rich History and Vibrant Arts",
        "p4_title": "Part 4: Questions 21 - 25 (Đọc hiểu văn bản trắc nghiệm 4 lựa chọn)",
        "p4_passage_title": "Head Chef Marco - The Art of Running a Top Kitchen",
        "p5_title": "Part 5: Questions 26 - 35 (Điền từ vào chỗ trống đoạn văn)",
        "p5_passage_title": "The Global Journey and Culture of Coffee"
    },
    8: {
        "title": "Practice Test 8",
        "theme": "Historic Rome, Mediterranean Culture & Health Lifestyle",
        "p2_title": "Part 2: Questions 6 - 10 (Ghép du khách với gói kỳ nghỉ phù hợp)",
        "p2_inst": "These people (6-10) are looking for a holiday. Look at the descriptions of eight holidays (A-H). Decide which holiday would be most suitable.",
        "p3_title": "Part 3: Questions 11 - 20 (Walking Through Ancient Rome - Đúng / Sai)",
        "p3_passage_title": "Rome - Exploring the Ancient Monuments and Street Life of the Eternal City",
        "p4_title": "Part 4: Questions 21 - 25 (Đọc hiểu văn bản trắc nghiệm 4 lựa chọn)",
        "p4_passage_title": "Getting Fit and Slim - Sustainable Health and Nutrition",
        "p5_title": "Part 5: Questions 26 - 35 (Điền từ vào chỗ trống đoạn văn)",
        "p5_passage_title": "How the Internet Connected the World"
    },
    9: {
        "title": "Practice Test 9",
        "theme": "Youth Clubs, Media, Video Game History & Youth Orchestra",
        "p2_title": "Part 2: Questions 6 - 10 (Ghép học sinh với lớp học sau giờ học phù hợp)",
        "p2_inst": "These students (6-10) want to do some sort of after-school activity. Look at the eight different classes (A-H). Decide which class would be most suitable.",
        "p3_title": "Part 3: Questions 11 - 20 (The History of Video Games - Đúng / Sai)",
        "p3_passage_title": "From Arcade Cabinets to 3D Virtual Worlds: The Evolution of Video Games",
        "p4_title": "Part 4: Questions 21 - 25 (Đọc hiểu văn bản trắc nghiệm 4 lựa chọn)",
        "p4_passage_title": "The National Youth Orchestra - Young Talents in Concert",
        "p5_title": "Part 5: Questions 26 - 35 (Điền từ vào chỗ trống đoạn văn)",
        "p5_passage_title": "Exploring the Mysteries of the Moon"
    },
    10: {
        "title": "Practice Test 10",
        "theme": "Career Guidance, Exam Revision, Jeans & Cycling",
        "p2_title": "Part 2: Questions 6 - 10 (Ghép học sinh với khóa học định hướng nghề nghiệp phù hợp)",
        "p2_inst": "These students (6-10) are considering their future careers. Look at the eight vocational study courses (A-H). Decide which course would be most suitable.",
        "p3_title": "Part 3: Questions 11 - 20 (Managing Exam Stress & Smart Revision - Đúng / Sai)",
        "p3_passage_title": "Exam Success: Science-Backed Strategies to Prepare and Reduce Stress",
        "p4_title": "Part 4: Questions 21 - 25 (Đọc hiểu văn bản trắc nghiệm 4 lựa chọn)",
        "p4_passage_title": "The Origin of Blue Jeans - From Workwear to Fashion Staple",
        "p5_title": "Part 5: Questions 26 - 35 (Điền từ vào chỗ trống đoạn văn)",
        "p5_passage_title": "The Bicycle - The Eco-Friendly Urban Transport Revolution"
    }
}

print("Metadata configured for tests 3-10.")
