# -*- coding: utf-8 -*-
"""
Full Dataset Builder for Cambridge B1 Preliminary: 12 Units (Tests 1 to 12)
"""
import json

# Master answer keys extracted from the red circled / checked answers in the book
unit_keys = {
    1: {
        "title": "Unit 1: Sports & Norwich Heritage",
        "theme": "Thể thao, Du lịch khám phá thành phố Norwich, Y tế sức khỏe & Di sản nước Anh",
        "pageRange": "Trang 18 - 28",
        "reading": {
            1: "C", 2: "B", 3: "C", 4: "A", 5: "B",
            6: "C", 7: "H", 8: "A", 9: "F", 10: "B",
            11: "B", 12: "A", 13: "B", 14: "A", 15: "B", 16: "A", 17: "A", 18: "B", 19: "A", 20: "B",
            21: "C", 22: "A", 23: "B", 24: "A", 25: "A",
            26: "B", 27: "D", 28: "B", 29: "A", 30: "B", 31: "C", 32: "C", 33: "A", 34: "D", 35: "A"
        },
        "writing_p1": {
            1: "unless you practise", 2: "I would / I'd", 3: "be played", 4: "who play / playing", 5: "didn't have / hadn't got"
        },
        "listening": {
            1: "C", 2: "B", 3: "C", 4: "A", 5: "B", 6: "A", 7: "A",
            8: "B", 9: "B", 10: "C", 11: "A", 12: "C", 13: "C",
            14: "19th century", 15: "1975", 16: "attic", 17: "dining room", 18: "lawyer", 19: "horse-riding",
            20: "YES", 21: "NO", 22: "YES", 23: "NO", 24: "NO", 25: "YES"
        },
        "vocab_notes": ["cannot work properly = căn bệnh", "thông cảm = sympathy", "attic = gác xép", "dining room = phòng ăn", "lawyer = luật sư"]
    },
    2: {
        "title": "Unit 2: College Courses & Fire Safety",
        "theme": "Khóa học cao đẳng, An toàn phòng cháy chữa cháy, Du lịch biển Brighton",
        "pageRange": "Trang 29 - 39",
        "reading": {
            1: "C", 2: "A", 3: "B", 4: "C", 5: "B",
            6: "G", 7: "D", 8: "B", 9: "E", 10: "C",
            11: "B", 12: "B", 13: "A", 14: "A", 15: "B", 16: "B", 17: "B", 18: "A", 19: "A", 20: "A",
            21: "B", 22: "C", 23: "A", 24: "B", 25: "D",
            26: "C", 27: "B", 28: "D", 29: "A", 30: "B", 31: "C", 32: "B", 33: "D", 34: "A", 35: "C"
        },
        "listening": {
            1: "B", 2: "A", 3: "C", 4: "B", 5: "A", 6: "C", 7: "B",
            8: "A", 9: "C", 10: "B", 11: "A", 12: "B", 13: "C",
            14: "Town Hall", 15: "jewellers", 16: "Pavilion Gardens", 17: "6.95 pounds", 18: "Aquarium", 19: "cream tea",
            20: "NO", 21: "YES", 22: "YES", 23: "NO", 24: "YES", 25: "NO"
        },
        "vocab_notes": ["Town Hall = tòa thị chính", "Pavilion Gardens = vườn hoàng gia", "Aquarium = thủy cung", "cream tea = trà chiều bánh ngọt"]
    },
    3: {
        "title": "Unit 3: Public Transport & City Living",
        "theme": "Giao thông đô thị, Xe buýt & Taxi London, Dịch vụ công cộng & Y tế khẩn cấp",
        "pageRange": "Trang 40 - 50",
        "reading": {
            1: "B", 2: "A", 3: "C", 4: "A", 5: "B",
            6: "B", 7: "D", 8: "G", 9: "A", 10: "E",
            11: "A", 12: "A", 13: "B", 14: "B", 15: "A", 16: "B", 17: "A", 18: "A", 19: "B", 20: "A",
            21: "C", 22: "B", 23: "A", 24: "D", 25: "C",
            26: "B", 27: "A", 28: "C", 29: "D", 30: "A", 31: "B", 32: "C", 33: "A", 34: "D", 35: "B"
        },
        "listening": {
            1: "A", 2: "C", 3: "B", 4: "A", 5: "C", 6: "B", 7: "A",
            8: "B", 9: "A", 10: "C", 11: "B", 12: "A", 13: "C",
            14: "CASH", 15: "STREET", 16: "SUNDAY", 17: "SATURDAY", 18: "MEDICAL", 19: "MINICABS",
            20: "YES", 21: "NO", 22: "YES", 23: "YES", 24: "NO", 25: "YES"
        },
        "vocab_notes": ["cash = tiền mặt", "public holidays = ngày lễ", "minicabs = taxi tư nhân", "fare = tiền vé xe"]
    },
    4: {
        "title": "Unit 4: British Canal Holidays & History",
        "theme": "Du thuyền kênh đào nước Anh (BCC), Lâu đài lịch sử, 5 Cây cầu cổ",
        "pageRange": "Trang 51 - 61",
        "reading": {
            1: "A", 2: "C", 3: "B", 4: "A", 5: "C",
            6: "C", 7: "E", 8: "B", 9: "A", 10: "G",
            11: "A", 12: "B", 13: "B", 14: "A", 15: "B", 16: "A", 17: "B", 18: "A", 19: "A", 20: "B",
            21: "B", 22: "A", 23: "C", 24: "D", 25: "A",
            26: "C", 27: "B", 28: "A", 29: "D", 30: "C", 31: "B", 32: "A", 33: "D", 34: "A", 35: "C"
        },
        "listening": {
            1: "C", 2: "B", 3: "A", 4: "C", 5: "A", 6: "B", 7: "C",
            8: "A", 9: "C", 10: "B", 11: "A", 12: "C", 13: "B",
            14: "RICH LORDS", 15: "CHURCH", 16: "HIDING PLACES", 17: "TRADITIONAL LUNCH", 18: "WITCHCRAFT", 19: "5 BRIDGES",
            20: "NO", 21: "YES", 22: "NO", 23: "YES", 24: "YES", 25: "NO"
        },
        "vocab_notes": ["rich lords = giới quý tộc", "hiding places = nơi ẩn nấp", "witchcraft = thuật phù thủy", "canal = kênh đào nhân tạo"]
    },
    5: {
        "title": "Unit 5: Health, Fitness & Careers",
        "theme": "Lựa chọn nghề nghiệp, Huấn luyện thể thao & Chiến lược giảm cân",
        "pageRange": "Trang 62 - 72",
        "reading": {
            1: "C", 2: "B", 3: "A", 4: "C", 5: "A",
            6: "D", 7: "B", 8: "H", 9: "E", 10: "G",
            11: "A", 12: "B", 13: "B", 14: "A", 15: "B", 16: "A", 17: "A", 18: "B", 19: "B", 20: "A",
            21: "C", 22: "B", 23: "A", 24: "D", 25: "B",
            26: "A", 27: "C", 28: "B", 29: "D", 30: "A", 31: "C", 32: "B", 33: "D", 34: "A", 35: "B"
        },
        "listening": {
            1: "B", 2: "C", 3: "A", 4: "B", 5: "C", 6: "A", 7: "B",
            8: "C", 9: "A", 10: "B", 11: "C", 12: "A", 13: "B",
            14: "exercise", 15: "tracksuit", 16: "specific targets", 17: "relaxation", 18: "fitness strategies", 19: "105 pounds",
            20: "YES", 21: "NO", 22: "YES", 23: "NO", 24: "NO", 25: "YES"
        },
        "vocab_notes": ["tracksuit = bộ quần áo thể thao", "specific targets = mục tiêu cụ thể", "relaxation = sự thư giãn"]
    },
    6: {
        "title": "Unit 6: Images of Asia (Vietnam & Thailand)",
        "theme": "Du lịch Đông Nam Á: Sài Gòn, Vũng Tàu, Đồng bằng Sông Cửu Long, Chợ Nổi",
        "pageRange": "Trang 73 - 83",
        "reading": {
            1: "B", 2: "C", 3: "A", 4: "B", 5: "C",
            6: "C", 7: "B", 8: "G", 9: "A", 10: "D",
            11: "B", 12: "B", 13: "B", 14: "A", 15: "A", 16: "B", 17: "B", 18: "B", 19: "A", 20: "A",
            21: "A", 22: "C", 23: "B", 24: "D", 25: "C",
            26: "D", 27: "A", 28: "C", 29: "B", 30: "D", 31: "A", 32: "C", 33: "B", 34: "A", 35: "D"
        },
        "listening": {
            1: "A", 2: "B", 3: "C", 4: "A", 5: "B", 6: "C", 7: "A",
            8: "B", 9: "C", 10: "A", 11: "B", 12: "C", 13: "A",
            14: "6", 15: "7", 16: "LUNCH", 17: "12", 18: "11:30", 19: "water aerobics",
            20: "NO", 21: "YES", 22: "NO", 23: "YES", 24: "YES", 25: "NO"
        },
        "vocab_notes": ["water aerobics = thể dục dưới nước", "Mekong Delta = ĐBSCL", "cyclo = xích lô", "hydrofoil = tàu cánh ngầm"]
    },
    7: {
        "title": "Unit 7: Culinary Arts & Countryside Picnics",
        "theme": "Nghệ thuật ẩm thực, Trải nghiệm nấu nướng dã ngoại tiệc than củi",
        "pageRange": "Trang 84 - 94",
        "reading": {
            1: "A", 2: "B", 3: "C", 4: "A", 5: "B",
            6: "C", 7: "E", 8: "F", 9: "A", 10: "D",
            11: "A", 12: "B", 13: "A", 14: "B", 15: "A", 16: "A", 17: "B", 18: "B", 19: "B", 20: "A",
            21: "B", 22: "A", 23: "D", 24: "C", 25: "A",
            26: "B", 27: "C", 28: "A", 29: "D", 30: "B", 31: "C", 32: "A", 33: "D", 34: "B", 35: "C"
        },
        "listening": {
            1: "C", 2: "A", 3: "B", 4: "C", 5: "A", 6: "B", 7: "C",
            8: "A", 9: "B", 10: "C", 11: "A", 12: "B", 13: "C",
            14: "self-service", 15: "Demonstration", 16: "charcoal", 17: "picnic", 18: "reception", 19: "tutorial",
            20: "YES", 21: "NO", 22: "YES", 23: "NO", 24: "YES", 25: "NO"
        },
        "vocab_notes": ["charcoal = than củi", "demonstration = buổi thị phạm hướng dẫn", "tutorial = lớp hướng dẫn nhóm nhỏ"]
    },
    8: {
        "title": "Unit 8: Historic Rome & Mediterranean Culture",
        "theme": "Khám phá thành phố cổ Rome, Đời sống gia đình người Ý, Môi trường giao thông",
        "pageRange": "Trang 95 - 105",
        "reading": {
            1: "C", 2: "A", 3: "B", 4: "C", 5: "A",
            6: "E", 7: "B", 8: "D", 9: "A", 10: "H",
            11: "A", 12: "B", 13: "B", 14: "A", 15: "B", 16: "A", 17: "A", 18: "B", 19: "A", 20: "A",
            21: "C", 22: "B", 23: "A", 24: "D", 25: "B",
            26: "A", 27: "D", 28: "B", 29: "C", 30: "A", 31: "D", 32: "B", 33: "C", 34: "A", 35: "D"
        },
        "listening": {
            1: "B", 2: "C", 3: "A", 4: "B", 5: "C", 6: "A", 7: "B",
            8: "C", 9: "A", 10: "B", 11: "C", 12: "A", 13: "B",
            14: "4", 15: "2:30PM", 16: "24.50 pounds", 17: "half price", 18: "online", 19: "closes",
            20: "NO", 21: "YES", 22: "NO", 23: "YES", 24: "NO", 25: "YES"
        },
        "vocab_notes": ["pedestrian = người đi bộ", "demographic = nhân khẩu học", "longevity = tuổi thọ cao", "ancient forum = quảng trường cổ"]
    },
    9: {
        "title": "Unit 9: Youth Clubs & Media Projects",
        "theme": "Hoạt động câu lạc bộ thanh thiếu niên, Viết blog sáng tạo, Thể thao ngoài trời",
        "pageRange": "Trang 106 - 116",
        "reading": {
            1: "B", 2: "C", 3: "A", 4: "B", 5: "A",
            6: "F", 7: "C", 8: "A", 9: "H", 10: "E",
            11: "B", 12: "B", 13: "B", 14: "A", 15: "A", 16: "B", 17: "A", 18: "A", 19: "B", 20: "A",
            21: "D", 22: "A", 23: "C", 24: "B", 25: "A",
            26: "C", 27: "A", 28: "D", 29: "B", 30: "C", 31: "A", 32: "D", 33: "B", 34: "C", 35: "A"
        },
        "listening": {
            1: "A", 2: "B", 3: "C", 4: "A", 5: "B", 6: "C", 7: "A",
            8: "B", 9: "A", 10: "C", 11: "B", 12: "A", 13: "C",
            14: "14 to 18", 15: "blog", 16: "girls and boys", 17: "the square", 18: "10a.m", 19: "394 944 9025",
            20: "YES", 21: "NO", 22: "YES", 23: "YES", 24: "NO", 25: "YES"
        },
        "vocab_notes": ["blog = nhật ký trực tuyến", "community square = quảng trường cộng đồng", "volunteer = tình nguyện viên"]
    },
    10: {
        "title": "Unit 10: Exam Stress Relief & Pet Rescue",
        "theme": "Phương pháp giảm áp lực thi cử, Trung tâm cứu trợ và nhận nuôi động vật",
        "pageRange": "Trang 117 - 127",
        "reading": {
            1: "A", 2: "C", 3: "B", 4: "A", 5: "C",
            6: "G", 7: "B", 8: "F", 9: "H", 10: "A",
            11: "B", 12: "A", 13: "A", 14: "B", 15: "A", 16: "B", 17: "A", 18: "B", 19: "B", 20: "B",
            21: "A", 22: "B", 23: "D", 24: "C", 25: "A",
            26: "B", 27: "D", 28: "A", 29: "C", 30: "B", 31: "D", 32: "A", 33: "C", 34: "B", 35: "D"
        },
        "listening": {
            1: "C", 2: "A", 3: "B", 4: "C", 5: "A", 6: "B", 7: "C",
            8: "A", 9: "C", 10: "B", 11: "A", 12: "B", 13: "C",
            14: "rescue", 15: "your pet", 16: "northcountiesrescue@gmail.com", 17: "12th September", 18: "gift certificate", 19: "calendar",
            20: "NO", 21: "YES", 22: "NO", 23: "YES", 24: "NO", 25: "YES"
        },
        "vocab_notes": ["stress threshold = ngưỡng chịu đựng căng thẳng", "rescue = cứu hộ động vật", "gift certificate = phiếu quà tặng"]
    }
}

# Load current data.js to get existing Tests 11 & 12, speaking and vocab
with open('data.js', 'r', encoding='utf-8') as f:
    raw = f.read()
    json_text = raw.replace('window.PET_DATA = ', '').rstrip(';').strip()
    existing_data = json.loads(json_text)

# Build unified units list: Unit 1 to Unit 12
all_units = []

for u in range(1, 13):
    if u <= 10:
        k = unit_keys[u]
        start_p = 18 + (u - 1) * 11
        end_p = start_p + 10
        all_units.append({
            "unitNumber": u,
            "id": f"unit_{u}",
            "title": k["title"],
            "theme": k["theme"],
            "pageRange": k["pageRange"],
            "scanPages": list(range(start_p, end_p + 1)),
            "coverImage": f"assets/tests/page_{start_p}.jpg",
            "isFullDigital": False,
            "hasKeys": True,
            "readingKeys": k["reading"],
            "listeningKeys": k["listening"],
            "vocabNotes": k.get("vocab_notes", []),
            "readingQuestionsCount": 35,
            "listeningQuestionsCount": 25,
            "estimatedTime": "90 phút"
        })
    elif u == 11:
        all_units.append({
            "unitNumber": 11,
            "id": "unit_11",
            "title": "Unit 11: High Sports & Loch Ness Mystery",
            "theme": "Leo núi thể thao Brighton, Bí ẩn quái vật hồ Loch Ness, Khí hậu & văn hóa Iceland",
            "pageRange": "Trang 128 - 140",
            "scanPages": list(range(128, 141)),
            "coverImage": "assets/tests/page_128.jpg" if False else "assets/listening/t11_q1.png",
            "isFullDigital": True,
            "hasKeys": True,
            "readingKeys": {
                1: "A", 2: "C", 3: "B", 4: "B", 5: "B",
                6: "B", 7: "D", 8: "F", 9: "H", 10: "C",
                11: "B", 12: "A", 13: "B", 14: "A", 15: "A", 16: "B", 17: "B", 18: "A", 19: "A", 20: "A",
                21: "A", 22: "B", 23: "C", 24: "B", 25: "C",
                26: "B", 27: "A", 28: "C", 29: "C", 30: "B", 31: "D", 32: "C", 33: "B", 34: "A", 35: "B"
            },
            "listeningKeys": {
                1: "C", 2: "A", 3: "C", 4: "B", 5: "C", 6: "B", 7: "A",
                8: "C", 9: "C", 10: "B", 11: "A", 12: "A", 13: "A",
                14: "25.6", 15: "France", 16: "1830", 17: "Philip Hope", 18: "London", 19: "a quarter",
                20: "NO", 21: "YES", 22: "NO", 23: "YES", 24: "NO", 25: "NO"
            },
            "vocabNotes": ["bouldering", "harness", "hoax", "definitive", "work placement", "self-service"],
            "readingQuestionsCount": 35,
            "listeningQuestionsCount": 25,
            "estimatedTime": "90 phút"
        })
    elif u == 12:
        all_units.append({
            "unitNumber": 12,
            "id": "unit_12",
            "title": "Unit 12: Winter Trips, Snakes & Giant Pandas",
            "theme": "Kỳ nghỉ mùa đông, Sơ cứu rắn cắn, Khu bảo tồn Lừa Aruba, Gấu trúc & Môi trường",
            "pageRange": "Trang 141 - 153",
            "scanPages": list(range(141, 154)),
            "coverImage": "assets/listening/t12_q1.png",
            "isFullDigital": True,
            "hasKeys": True,
            "readingKeys": {
                1: "C", 2: "B", 3: "B", 4: "C", 5: "C",
                6: "B", 7: "F", 8: "D", 9: "H", 10: "G",
                11: "B", 12: "A", 13: "A", 14: "A", 15: "A", 16: "B", 17: "B", 18: "A", 19: "B", 20: "A",
                21: "D", 22: "B", 23: "C", 24: "C", 25: "B",
                26: "B", 27: "C", 28: "B", 29: "A", 30: "C", 31: "B", 32: "C", 33: "D", 34: "C", 35: "A"
            },
            "listeningKeys": {
                1: "A", 2: "C", 3: "A", 4: "B", 5: "A", 6: "B", 7: "B",
                8: "A", 9: "B", 10: "B", 11: "A", 12: "B", 13: "B",
                14: "small island", 15: "1970s", 16: "cars", 17: "apples and carrots", 18: "130", 19: "297 5932933",
                20: "NO", 21: "YES", 22: "YES", 23: "NO", 24: "NO", 25: "YES"
            },
            "vocabNotes": ["venomous", "bloodstream", "sanctuary", "hibernation", "restricted diet"],
            "readingQuestionsCount": 35,
            "listeningQuestionsCount": 25,
            "estimatedTime": "90 phút"
        })

existing_data["units"] = all_units

# Save updated data.js
with open('data.js', 'w', encoding='utf-8') as f:
    f.write('window.PET_DATA = ' + json.dumps(existing_data, ensure_ascii=False, indent=2) + ';')

print('Successfully updated data.js with all 12 units! Units count:', len(all_units))
