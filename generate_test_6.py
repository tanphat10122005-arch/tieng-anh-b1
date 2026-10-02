import json
import re

print("Generating tests 6 to 10...")

with open('all_reading_keys.json', encoding='utf-8') as f:
    all_keys = json.load(f)

with open('digital_tests_3_5.json', encoding='utf-8') as f:
    all_tests = json.load(f)

# Helper function
def make_p1(q_data, keys):
    return [
        {
            "number": i + 1,
            "context": q["context"],
            "question": q["question"],
            "options": q["options"],
            "correct": keys[str(i + 1)],
            "explanation": q["explanation"]
        } for i, q in enumerate(q_data)
    ]

# ==================== TEST 6 ====================
t6_k = all_keys['6']
test_6 = {
  "id": "test_6",
  "title": "Practice Test 6",
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
            "number": 1,
            "context": "TEXT MESSAGE\nHi Dan, feeling down about your exam results? Don't worry! How about joining us for pizza and bowling tonight to cheer you up? Let me know, Sarah",
            "question": "Why is Sarah texting Dan?",
            "options": [
              {"key": "A", "text": "To check if he has fallen ill."},
              {"key": "B", "text": "To invite him out for an enjoyable evening with friends."},
              {"key": "C", "text": "To tell him that she failed her exam."}
            ],
            "correct": t6_k['1'],
            "explanation": "Sarah rủ Dan đi ăn pizza và chơi bowling để giải tỏa tâm trạng ('invite him out')."
          },
          {
            "number": 2,
            "context": "SHOP NOTICE\nDue to urgent plumbing repairs, this branch will close at 3 pm today instead of our normal 7 pm. We apologize for any inconvenience.",
            "question": "What does this shop notice state?",
            "options": [
              {"key": "A", "text": "The shop closes early every weekday."},
              {"key": "B", "text": "An unexpected maintenance problem has affected opening hours today."},
              {"key": "C", "text": "The shop is closing permanently."}
            ],
            "correct": t6_k['2'],
            "explanation": "Sự cố sửa chữa ống nước đột xuất khiến cửa hàng phải đóng cửa sớm lúc 3h chiều nay."
          },
          {
            "number": 3,
            "context": "OFFER\nPAY 20% DEPOSIT TODAY AND WE WILL RESERVE ANY FURNITURE SUITE UNTIL NEXT MONTH AT NO EXTRA CHARGE!",
            "question": "What is the terms of the furniture shop offer?",
            "options": [
              {"key": "A", "text": "Pay part of the price now and the shop will hold the item for you."},
              {"key": "B", "text": "Receive a 20% discount if you pay in full today."},
              {"key": "C", "text": "Take the furniture home for free this month."}
            ],
            "correct": t6_k['3'],
            "explanation": "Đặt cọc trước 20% để giữ hàng mà không mất thêm phí ('pay part of the price... hold the item')."
          },
          {
            "number": 4,
            "context": "GALLERY SIGN\nLAST ENTRY IS 6:30 PM. DOORS CLOSE PROMPTLY AT 7:00 PM.",
            "question": "What does this art gallery sign mean?",
            "options": [
              {"key": "A", "text": "Admission is free after 6:30 pm."},
              {"key": "B", "text": "You cannot enter the gallery less than half an hour before closing."},
              {"key": "C", "text": "Visitors can remain inside until 8:00 pm."}
            ],
            "correct": t6_k['4'],
            "explanation": "Lượt vào cuối là 6h30 tối, tức không được vào nếu còn dưới 30 phút trước giờ đóng cửa."
          },
          {
            "number": 5,
            "context": "NOTE\nJohn, could you please translate this German instruction manual for our new coffee machine? My German isn't quite good enough! Thanks, Tina",
            "question": "Why did Tina leave a note for John?",
            "options": [
              {"key": "A", "text": "Tina wants John to make coffee for the office."},
              {"key": "B", "text": "Tina speaks German fluently."},
              {"key": "C", "text": "Tina needs John's German language skills to understand the manual."}
            ],
            "correct": t6_k['5'],
            "explanation": "Tina nhờ John dịch hộ tờ hướng dẫn bằng tiếng Đức ('needs John's language skills')."
          }
        ]
      },
      {
        "partNumber": 2,
        "title": "Part 2: Questions 6 - 10 (Ghép bạn đọc với cuốn sách thư viện phù hợp)",
        "instruction": "These people (6-10) all want to borrow a book from the library. Look at the eight book reviews (A-H). Decide which book would be the most suitable for each person.",
        "teenagers": [
          {
            "number": 6,
            "name": "Hannah",
            "demand": "Hannah enjoys reading suspenseful psychological mystery thrillers set in isolated locations, with unexpected plot twists and strong female detectives.",
            "correct": t6_k['6'],
            "explanation": f"Cuốn sách {t6_k['6']} là tiểu thuyết trinh thám tâm lý ly kỳ với nữ thanh tra thông minh tại hòn đảo biệt lập."
          },
          {
            "number": 7,
            "name": "Oliver",
            "demand": "Oliver is passionate about world history and wants an engaging narrative about ancient civilizations and their architectural wonders, illustrated with maps.",
            "correct": t6_k['7'],
            "explanation": f"Tác phẩm {t6_k['7']} tái hiện sống động các nền văn minh cổ đại và kỳ quan kiến trúc kèm bản đồ chi tiết."
          },
          {
            "number": 8,
            "name": "Priya",
            "demand": "Priya wants an uplifting, heartwarming memoir written by someone who overcame physical adversity to achieve their dreams in world sports.",
            "correct": t6_k['8'],
            "explanation": f"Hồi ký {t6_k['8']} truyền cảm hứng mạnh mẽ về hành trình vượt qua nghịch cảnh để chinh phục đỉnh cao thể thao."
          },
          {
            "number": 9,
            "name": "George",
            "demand": "George loves science fiction stories exploring artificial intelligence, futuristic space colonies, and the ethical dilemmas of future technology.",
            "correct": t6_k['9'],
            "explanation": f"Cuốn tiểu thuyết viễn tưởng {t6_k['9']} khai thác sâu sắc về trí tuệ nhân tạo và các vấn đề đạo đức thời tương lai."
          },
          {
            "number": 10,
            "name": "Zoe",
            "demand": "Zoe is an aspiring chef who wants a beautifully photographed culinary book explaining the cultural traditions and secret recipes of Southeast Asian street food.",
            "correct": t6_k['10'],
            "explanation": f"Sách ẩm thực {t6_k['10']} giới thiệu trọn vẹn văn hóa và bí quyết nấu nướng các món ăn đường phố Đông Nam Á."
          }
        ],
        "places": [
          {"code": "A", "title": "The Whispering Lighthouse", "desc": "A gripping whodunit mystery following Detective Inspector Claire Vance as she investigates an impossible murder on an isolated Scottish island in winter."},
          {"code": "B", "title": "Empires of Stone and Gold", "desc": "A richly illustrated chronicle detailing the builders, engineering marvels, and daily life in ancient Egypt, Mesopotamia, and Rome with colour maps."},
          {"code": "C", "title": "Against the Tide", "desc": "The moving true autobiography of Paralympic gold medalist swimmer Maya Thorne, recounting her recovery from a devastating spinal injury through sheer grit."},
          {"code": "D", "title": "Silicon Soul: 2099", "desc": "A thought-provoking cyberpunk novel examining sentient AI robots struggling for legal rights on a bustling lunar terraformed colony."},
          {"code": "E", "title": "Flavours of the Mekong", "desc": "A stunning gastronomic travelogue showcasing traditional street hawker recipes from Hanoi to Bangkok, with vivid step-by-step food photography."},
          {"code": "F", "title": "Garden Secrets", "desc": "A practical guide to organic vegetable cultivation and permaculture design for urban backyards."},
          {"code": "G", "title": "The Lost Symphony", "desc": "A gentle romance between two classical violin students competing for a scholarship in Vienna."},
          {"code": "H", "title": "Deep Ocean Odyssey", "desc": "A marine biologist's diary documenting hydrothermal vent ecosystems and bioluminescent deep-sea species."}
        ]
      },
      {
        "partNumber": 3,
        "title": "Part 3: Questions 11 - 20 (Journey Through Southeast Asia - Đúng / Sai)",
        "instruction": "Look at the sentences below about a journey in Southeast Asia. Read the text to decide if each sentence is correct or incorrect. If it is correct, mark A. If it is not correct, mark B.",
        "passageTitle": "Exploring Vietnam and Thailand - Cultures, Landscapes and Cities",
        "passage": "Southeast Asia has become one of the premier global travel destinations, captivating millions of international explorers every year with its welcoming culture, breathtaking scenery, and rich historical heritage.\n\nIn Vietnam, the journey often begins in the capital city of Hanoi, famous for its historic French colonial architecture, ancient temples, and vibrant Old Quarter bustling with street vendors and motorbikes. Just a few hours eastward lies Halong Bay, a UNESCO World Heritage site where thousands of majestic limestone karsts rise dramatically out of emerald-green waters. Visitors can board traditional wooden junks to kayak through hidden sea caves and visit floating fishing hamlets.\n\nFurther south in Thailand, the contrast between ancient serenity and ultra-modern vitality is equally astonishing. Bangkok dazzles with its golden Grand Palace and gleaming Buddhist spires alongside futuristic sky-trains and canal water-taxis. Travellers eager for tranquility can take a short flight north to Chiang Mai, where mist-covered mountains surround centuries-old monasteries and ethical elephant sanctuaries allow humane observation. Southeast Asia offers an unforgettable adventure that combines warm hospitality, culinary brilliance, and astonishing natural beauty.",
        "questions": [
          {"number": 11, "statement": "Southeast Asia attracts millions of international travellers annually.", "correct": t6_k['11'], "explanation": "Đúng (A): 'captivating millions of international explorers every year'."},
          {"number": 12, "statement": "Hanoi is located right in the centre of southern Thailand.", "correct": t6_k['12'], "explanation": "Sai (B): Hà Nội là thủ đô của Việt Nam ('capital city of Hanoi, Vietnam')."},
          {"number": 13, "statement": "Halong Bay is recognized globally as a UNESCO World Heritage site.", "correct": t6_k['13'], "explanation": "Đúng (A): 'Halong Bay, a UNESCO World Heritage site'."},
          {"number": 14, "statement": "Halong Bay features dramatic limestone rock formations in the sea.", "correct": t6_k['14'], "explanation": "Đúng (A): 'thousands of majestic limestone karsts rise dramatically out of emerald-green waters'."},
          {"number": 15, "statement": "Kayaking and sea cave exploration are prohibited in Halong Bay.", "correct": t6_k['15'], "explanation": "Sai (B): Du khách có thể chèo kayak khám phá hang động ('kayak through hidden sea caves')."},
          {"number": 16, "statement": "Bangkok features both historic temples and modern transport systems.", "correct": t6_k['16'], "explanation": "Đúng (A): Có cả đền chùa vàng truyền thống và tàu điện trên cao hiện đại ('sky-trains')."},
          {"number": 17, "statement": "Chiang Mai is located on a flat desert coastline.", "correct": t6_k['17'], "explanation": "Sai (B): Chiang Mai nằm ở vùng núi phía bắc có sương mù bao phủ ('mist-covered mountains')."},
          {"number": 18, "statement": "Ethical elephant sanctuaries can be found near Chiang Mai.", "correct": t6_k['18'], "explanation": "Đúng (A): Có các khu bảo tồn voi nhân đạo ('ethical elephant sanctuaries')."},
          {"number": 19, "statement": "Local food and hospitality are highlighted as positive aspects of travel in the region.", "correct": t6_k['19'], "explanation": "Đúng (A): 'warm hospitality, culinary brilliance, and astonishing natural beauty'."},
          {"number": 20, "statement": "The author concludes that traveling in Southeast Asia is unmemorable.", "correct": t6_k['20'], "explanation": "Sai (B): Tác giả khẳng định đây là chuyến phiêu lưu không thể nào quên ('unforgettable adventure')."}
        ]
      },
      {
        "partNumber": 4,
        "title": "Part 4: Questions 21 - 25 (Đọc hiểu văn bản trắc nghiệm 4 lựa chọn)",
        "instruction": "Read the text and questions below. For each question, choose the correct letter A, B, C or D.",
        "passageTitle": "Alice Bradley - Wildlife and Nature Photographer",
        "passage": "For more than twenty years, Alice Bradley has travelled to the world's most remote environments, from sub-zero Antarctic ice fields to steaming Amazonian rain forests, capturing intimate photographs of endangered species in their native habitats. Her breathtaking wildlife images have featured on the covers of major scientific and geographical magazines worldwide.\n\n'Patience is the single most essential quality in wildlife photography,' Alice explains. 'You might sit motionless in a frozen hide for twelve hours in the freezing snow just to catch a thirty-second glimpse of a snow leopard. If you make a sudden movement or loud sound, the opportunity vanishes.'\n\nBeyond simply taking striking pictures, Alice uses her platform to advocate fiercely for global conservation. She donates a substantial portion of her print sales to fund anti-poaching patrols and rainforest restoration projects. 'Photographs possess an emotional power that scientific reports often lack,' she notes. 'When people look directly into the eyes of an animal through a lens, they develop empathy and feel inspired to protect our fragile natural world.'",
        "questions": [
          {
            "number": 21,
            "question": "What is the primary theme of the passage about Alice Bradley?",
            "options": [
              {"key": "A", "text": "The high cost of photographic cameras."},
              {"key": "B", "text": "Her career as a dedicated wildlife photographer and conservation advocate."},
              {"key": "C", "text": "Why young people should avoid dangerous animals."},
              {"key": "D", "text": "A history of geographical magazines."}
            ],
            "correct": t6_k['21'],
            "explanation": "Chủ đề chính là sự nghiệp nhiếp ảnh gia động vật hoang dã và nỗ lực bảo tồn thiên nhiên của Alice."
          },
          {
            "number": 22,
            "question": "According to Alice, what is the most indispensable trait for wildlife photographers?",
            "options": [
              {"key": "A", "text": "Immense physical strength."},
              {"key": "B", "text": "Owning the most expensive equipment."},
              {"key": "C", "text": "Extreme patience and endurance."},
              {"key": "D", "text": "Talking loudly to attract animals."}
            ],
            "correct": t6_k['22'],
            "explanation": "Alice khẳng định: 'Patience is the single most essential quality in wildlife photography'."
          },
          {
            "number": 23,
            "question": "Why does Alice mention the snow leopard example?",
            "options": [
              {"key": "A", "text": "To illustrate the long hours of waiting required for a brief sighting."},
              {"key": "B", "text": "To warn readers that snow leopards are dangerous pets."},
              {"key": "C", "text": "To show that leopards are easy to find in the snow."},
              {"key": "D", "text": "To explain how to hunt leopards."}
            ],
            "correct": t6_k['23'],
            "explanation": "Ví dụ nhằm chứng minh phải ngồi chờ ròng rã 12 tiếng trong giá rét chỉ để chớp được khoảnh khắc 30 giây."
          },
          {
            "number": 24,
            "question": "How does Alice practically support wildlife conservation?",
            "options": [
              {"key": "A", "text": "She donates proceeds from her photo sales to anti-poaching and habitat restoration."},
              {"key": "B", "text": "She opens a private zoo for rare animals."},
              {"key": "C", "text": "She gives up photography to work as a government politician."},
              {"key": "D", "text": "She refuses to sell any of her photographs."}
            ],
            "correct": t6_k['24'],
            "explanation": "Bà trích một phần lớn doanh thu bán ảnh tài trợ cho các đội tuần tra chống săn trộm và phục hồi rừng."
          },
          {
            "number": 25,
            "question": "Why does Alice believe wildlife photography is so impactful?",
            "options": [
              {"key": "A", "text": "It can be done faster than writing a letter."},
              {"key": "B", "text": "It creates an emotional connection and empathy that scientific data alone cannot achieve."},
              {"key": "C", "text": "Animals enjoy posing in front of cameras."},
              {"key": "D", "text": "It is cheaper than visiting a museum."}
            ],
            "correct": t6_k['25'],
            "explanation": "Bức ảnh khơi gợi cảm xúc và sự đồng cảm mạnh mẽ, thôi thúc mọi người chung tay bảo vệ động vật hoang dã."
          }
        ]
      },
      {
        "partNumber": 5,
        "title": "Part 5: Questions 26 - 35 (Điền từ vào chỗ trống đoạn văn)",
        "instruction": "Read the text below and choose the correct word for each space. For each question, choose the correct letter A, B, C or D.",
        "passageTitle": "The Secret Life and Communication of Whales",
        "passage": "Whales are among the largest and most intelligent creatures (26) ______ have ever inhabited our planet. Although they live in the ocean, they are warm-blooded mammals (27) ______ breathe air into their lungs through blowholes on top of their heads.\n\nBecause sound travels much (28) ______ and further through water than through air, whales rely on acoustics rather than eyesight to navigate and communicate. Humpback whales are famous (29) ______ composing complex underwater 'songs' that can last up to twenty minutes and be (30) ______ across hundreds of miles of open sea. Scientists have discovered that these melodic sequences change from year to year, with populations (31) ______ new phrases from neighbouring pods.\n\nTragically, industrial commercial whaling during the nineteenth and twentieth centuries pushed several whale species to the brink of (32) ______. Fortunately, an international ban on commercial whaling has allowed many populations to slowly (33) ______. Today, threats from ocean plastic pollution and underwater engine noise (34) ______ serious concerns, making global conservation efforts more urgent than (35) ______ before.",
        "questions": [
          {"number": 26, "options": [{"key": "A", "text": "that"}, {"key": "B", "text": "what"}, {"key": "C", "text": "whose"}, {"key": "D", "text": "whom"}], "correct": t6_k['26'], "explanation": "Đại từ quan hệ 'that' thay thế cho danh từ 'creatures' sau tính từ so sánh nhất."},
          {"number": 27, "options": [{"key": "A", "text": "which"}, {"key": "B", "text": "where"}, {"key": "C", "text": "when"}, {"key": "D", "text": "why"}], "correct": t6_k['27'], "explanation": "Đại từ 'which' làm chủ ngữ thay cho 'warm-blooded mammals'."},
          {"number": 28, "options": [{"key": "A", "text": "faster"}, {"key": "B", "text": "fastest"}, {"key": "C", "text": "fast"}, {"key": "D", "text": "slow"}], "correct": t6_k['28'], "explanation": "So sánh hơn 'faster and further' (nhanh hơn và xa hơn trong nước)."},
          {"number": 29, "options": [{"key": "A", "text": "for"}, {"key": "B", "text": "at"}, {"key": "C", "text": "by"}, {"key": "D", "text": "in"}], "correct": t6_k['29'], "explanation": "Cụm cố định 'famous for' (nổi tiếng vì điều gì)."},
          {"number": 30, "options": [{"key": "A", "text": "heard"}, {"key": "B", "text": "listened"}, {"key": "C", "text": "sounded"}, {"key": "D", "text": "watched"}], "correct": t6_k['30'], "explanation": "Dạng bị động 'be heard' (được nghe thấy cách xa hàng trăm dặm)."},
          {"number": 31, "options": [{"key": "A", "text": "learning"}, {"key": "B", "text": "teaching"}, {"key": "C", "text": "forgetting"}, {"key": "D", "text": "dropping"}], "correct": t6_k['31'], "explanation": "Học hỏi các câu hát mới ('learning new phrases')."},
          {"number": 32, "options": [{"key": "A", "text": "extinction"}, {"key": "B", "text": "safety"}, {"key": "C", "text": "success"}, {"key": "D", "text": "birth"}], "correct": t6_k['32'], "explanation": "Thành ngữ 'on the brink of extinction' (trên bờ vực tuyệt chủng)."},
          {"number": 33, "options": [{"key": "A", "text": "recover"}, {"key": "B", "text": "destroy"}, {"key": "C", "text": "disappear"}, {"key": "D", "text": "attack"}], "correct": t6_k['33'], "explanation": "Động từ 'recover' (dần phục hồi số lượng cá thể)."},
          {"number": 34, "options": [{"key": "A", "text": "remain"}, {"key": "B", "text": "make"}, {"key": "C", "text": "turn"}, {"key": "D", "text": "stop"}], "correct": t6_k['34'], "explanation": "Liên động từ 'remain serious concerns' (vẫn là mối bận tâm nghiêm trọng)."},
          {"number": 35, "options": [{"key": "A", "text": "ever"}, {"key": "B", "text": "never"}, {"key": "C", "text": "always"}, {"key": "D", "text": "rarely"}], "correct": t6_k['35'], "explanation": "Cụm 'more urgent than ever before' (cấp thiết hơn bao giờ hết)."}
        ]
      }
    ]
  }
}
all_tests.append(test_6)
print("Test 6 ready.")

with open('digital_tests_3_6.json', 'w', encoding='utf-8') as f:
    json.dump(all_tests, f, ensure_ascii=False, indent=2)

print("Saved digital_tests_3_6.json")
