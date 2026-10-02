import json
import re

print("Generating tests 4 to 10...")

with open('all_reading_keys.json', encoding='utf-8') as f:
    all_keys = json.load(f)

# Load test 3
with open('digital_test_3.json', encoding='utf-8') as f:
    test_3 = json.load(f)

# Import test 4 from earlier file
from generate_tests_4_to_10 import test_4

all_tests = [test_3, test_4]

# ----------------- BUILD TEST 5 -----------------
t5_k = all_keys['5']
test_5 = {
  "id": "test_5",
  "title": "Practice Test 5",
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
            "context": "LABEL\nFRUIT SMOOTHIE: Shake well before opening. Keep refrigerated at 2°C - 5°C. Do not freeze.",
            "question": "What is the advice regarding the fruit smoothie?",
            "options": [
              {"key": "A", "text": "Chill the drink in the fridge before you use it."},
              {"key": "B", "text": "The drink should be served at room temperature."},
              {"key": "C", "text": "Store the drink in a refrigerator before opening."}
            ],
            "correct": t5_k['1'],
            "explanation": "Nhãn hướng dẫn bảo quản đồ uống trong tủ lạnh ('Keep refrigerated')."
          },
          {
            "number": 2,
            "context": "SIGN\nPRIVATE ACCESS ROAD. NO UNAUTHORIZED VEHICLES AT ANY TIME. CLAMPING IN OPERATION.",
            "question": "What does this road sign indicate?",
            "options": [
              {"key": "A", "text": "The car park is open to the public 24 hours."},
              {"key": "B", "text": "It is forbidden to use, or stop on, this road without permission."},
              {"key": "C", "text": "Private cars are not allowed to use the road at night only."}
            ],
            "correct": t5_k['2'],
            "explanation": "Đường nội bộ cấm phương tiện không được cấp phép lưu thông hoặc dừng đỗ ('No unauthorized vehicles')."
          },
          {
            "number": 3,
            "context": "NOTICE\nSECURITY CAMERAS IN OPERATION 24/7. SHOPLIFTERS WILL BE PROSECUTED AND REPORTED TO POLICE.",
            "question": "What does this store notice warn customers?",
            "options": [
              {"key": "A", "text": "The police will be informed of any stealing."},
              {"key": "B", "text": "The police are watching customers directly inside."},
              {"key": "C", "text": "Cameras are only active during night hours."}
            ],
            "correct": t5_k['3'],
            "explanation": "Mọi hành vi trộm cắp sẽ bị báo cảnh sát ('reported to police')."
          },
          {
            "number": 4,
            "context": "E-MAIL\nTo: Staff\nFrom: Mr. Clinton\nMr. Smith from the Municipal Heritage Museum will host our school educational excursion next Tuesday at 10 am.",
            "question": "What does Mr. Clinton explain in the email?",
            "options": [
              {"key": "A", "text": "Mr. Smith works for the local museum and will lead the tour."},
              {"key": "B", "text": "Mr. Clinton wants to cancel the school visit."},
              {"key": "C", "text": "The museum will be closed next Tuesday."}
            ],
            "correct": t5_k['4'],
            "explanation": "Mr. Smith từ bảo tàng sẽ phụ trách chuyến tham quan học tập của trường."
          },
          {
            "number": 5,
            "context": "STORE SIGN\nFRESH CROISSANTS, SOURDOUGH BREAD & PASTRIES BAKED DAILY FROM 6 AM.",
            "question": "Where would you typically see this sign?",
            "options": [
              {"key": "A", "text": "In a bakery."},
              {"key": "B", "text": "In a bookstore."},
              {"key": "C", "text": "In a clothing boutique."}
            ],
            "correct": t5_k['5'],
            "explanation": "Biển báo về bánh sừng bò, bánh mì men tự nhiên và bánh ngọt nướng tươi thường thấy ở tiệm bánh (bakery)."
          }
        ]
      },
      {
        "partNumber": 2,
        "title": "Part 2: Questions 6 - 10 (Ghép du khách với khu nghỉ dưỡng Hy Lạp phù hợp)",
        "instruction": "These people (6-10) are looking for a holiday destination in Greece. Look at the eight reviews (A-H). Decide which resort would be the most suitable for each person.",
        "teenagers": [
          {
            "number": 6,
            "name": "Elena",
            "demand": "Elena is fascinated by ancient archaeology and classical Greek temples. She wants guided cultural tours and historical museums within walking distance.",
            "correct": t5_k['6'],
            "explanation": f"Địa điểm {t5_k['6']} nổi tiếng với các di tích đền đài cổ đại Hy Lạp và bảo tàng khảo cổ phong phú."
          },
          {
            "number": 7,
            "name": "Marcus & Chloe",
            "demand": "Marcus and Chloe want windsurfing and scuba diving with certified instructors, along with lively beach bars and watersport rental shops.",
            "correct": t5_k['7'],
            "explanation": f"Khu nghỉ dưỡng {t5_k['7']} là thiên đường lướt ván buồm và lặn biển với các trung tâm huấn luyện chuyên nghiệp."
          },
          {
            "number": 8,
            "name": "The Henderson Family",
            "demand": "The Henderson family have young toddlers. They need shallow sandy beaches with calm waters, a kids' club, and family-friendly buffet restaurants.",
            "correct": t5_k['8'],
            "explanation": f"Resort {t5_k['8']} sở hữu bãi cát thoai thoải an toàn cho trẻ nhỏ và dịch vụ trông giữ trẻ chu đáo."
          },
          {
            "number": 9,
            "name": "Tobias",
            "demand": "Tobias seeks total peace and tranquility in an authentic fishing village, far from mass tourism, where he can sketch whitewashed houses and write.",
            "correct": t5_k['9'],
            "explanation": f"Ngôi làng {t5_k['9']} giữ nguyên nét mộc mạc thanh bình của làng chài truyền thống Hy Lạp, cách xa các tụ điểm du lịch ồn ào."
          },
          {
            "number": 10,
            "name": "Liam and friends",
            "demand": "Liam and his college friends want non-stop nightlife, open-air nightclubs, world-famous DJ events, and beach pool parties until sunrise.",
            "correct": t5_k['10'],
            "explanation": f"Hòn đảo {t5_k['10']} là trung tâm tiệc tùng sôi động bậc nhất với các câu lạc bộ đêm và quán bar bên hồ bơi náo nhiệt."
          }
        ],
        "places": [
          {"code": "A", "title": "Athens Heritage Plaza", "desc": "Stay in the heart of historic Athens near the Acropolis, Parthenon and the world-renowned National Archaeological Museum with daily guided walking lectures."},
          {"code": "B", "title": "Rhodes Wind & Wave Bay", "desc": "Consistent Mediterranean crosswinds make this bay a premier windsurfing, kitesurfing and PADI certified deep-sea scuba diving haven with top-tier gear rental."},
          {"code": "C", "title": "Crete Sunbeam Family Haven", "desc": "Sheltered shallow lagoon with soft golden sand, kid-safe splash zones, certified English-speaking childminders, and dedicated family suites."},
          {"code": "D", "title": "Folegandros Quiet Cliff Village", "desc": "An unspoiled Cycladic gem with sleepy harbours, crystal waters, cliffside tavernas, no tour buses, and peaceful silence for artists and authors."},
          {"code": "E", "title": "Mykonos Paradise Palms", "desc": "Glamorous nightlife capital boasting international guest DJs, beach club foam parties, upscale cocktail lounges, and chic music festivals all summer long."},
          {"code": "F", "title": "Olympia Valley Retreat", "desc": "Quiet pine-shaded bungalows situated near the birthplace of the Olympic Games with olive groves and mountain bike tracks."},
          {"code": "G", "title": "Corfu Emerald Spa Hotel", "desc": "Adults-only luxury wellness resort offering sea-salt thalassotherapy, yoga pavilions, and organic Mediterranean cuisine."},
          {"code": "H", "title": "Santorini Sunset Terraces", "desc": "Iconic caldera-facing suites designed for couples seeking dramatic volcanic sunsets and fine local wine tasting."}
        ]
      },
      {
        "partNumber": 3,
        "title": "Part 3: Questions 11 - 20 (East Anglia Transport Museum - Đúng / Sai)",
        "instruction": "Look at the sentences below about the East Anglia Transport Museum. Read the text to decide if each sentence is correct or incorrect. If it is correct, mark A. If it is not correct, mark B.",
        "passageTitle": "The Transport Museum of East Anglia",
        "passage": "Set in pleasant countryside near Lowestoft, the East Anglia Transport Museum is the only museum in Britain where visitors can not only view historic vehicles, but actually ride on vintage electric trams, trolleybuses, and narrow-gauge steam locomotives in an authentic period street setting.\n\nThe museum was established in the 1960s by a group of enthusiastic transport preservationists who rescued decommissioned double-decker trams from scrap yards across the UK. Today, the collection spans over a century of transport history, featuring horse-drawn carriages, 1930s motor buses, and rare electric delivery vans.\n\nAll public rides are included in the price of admission, allowing guests unlimited journeys throughout the day. Visitors can stroll down reconstructed cobbled 1930s streets complete with vintage streetlights, a working penny arcade, an old-fashioned sweet shop, and a tea room serving homemade scones. The museum is operated entirely by volunteers who gladly share their historical knowledge with visitors of all ages.",
        "questions": [
          {"number": 11, "statement": "Visitors are allowed to ride on historic vehicles at the museum.", "correct": t5_k['11'], "explanation": "Đúng (A): Du khách thực sự được đi thử trên các xe điện và xe lửa hơi nước cổ ('actually ride on vintage electric trams')."},
          {"number": 12, "statement": "The museum only displays modern petrol-powered buses.", "correct": t5_k['12'], "explanation": "Sai (B): Bảo tàng trưng bày nhiều loại phương tiện lịch sử từ xe ngựa kéo, xe điện đến xe hơi nước cổ."},
          {"number": 13, "statement": "Enthusiasts founded the museum to preserve disappearing transport heritage.", "correct": t5_k['13'], "explanation": "Đúng (A): Được thành lập bởi nhóm những người đam mê bảo tồn xe điện cổ."},
          {"number": 14, "statement": "All trams on display were built in the last five years.", "correct": t5_k['14'], "explanation": "Sai (B): Các phương tiện đều có tuổi đời hàng chục đến cả trăm năm."},
          {"number": 15, "statement": "You must pay extra for every single tram ride you take.", "correct": t5_k['15'], "explanation": "Sai (B): Vé vào cổng đã bao gồm số lần đi không giới hạn trong ngày ('unlimited journeys throughout the day')."},
          {"number": 16, "statement": "The museum features an authentically recreated 1930s street scene.", "correct": t5_k['16'], "explanation": "Đúng (A): Con phố đá cuội thập niên 1930 được phục dựng sinh động với đèn đường cổ và tiệm kẹo."},
          {"number": 17, "statement": "There is a traditional tea room where visitors can enjoy food.", "correct": t5_k['17'], "explanation": "Đúng (A): Có phòng trà phục vụ bánh nướng tự làm ('tea room serving homemade scones')."},
          {"number": 18, "statement": "The museum is run entirely by unpaid volunteers.", "correct": t5_k['18'], "explanation": "Đúng (A): 'operated entirely by volunteers'."},
          {"number": 19, "statement": "Staff members refuse to talk to guests about transport history.", "correct": t5_k['19'], "explanation": "Sai (B): Các tình nguyện viên rất vui mừng chia sẻ kiến thức lịch sử với khách ('gladly share their knowledge')."},
          {"number": 20, "statement": "The museum is open to visitors of all ages.", "correct": t5_k['20'], "explanation": "Đúng (A): Phù hợp và chào đón khách tham quan ở mọi lứa tuổi ('visitors of all ages')."}
        ]
      },
      {
        "partNumber": 4,
        "title": "Part 4: Questions 21 - 25 (Đọc hiểu văn bản trắc nghiệm 4 lựa chọn)",
        "instruction": "Read the text and questions below. For each question, choose the correct letter A, B, C or D.",
        "passageTitle": "Job Interviews - How to Make the Best First Impression",
        "passage": "Job interviews can be nerve-racking, but thorough preparation is the surest way to transform anxiety into confident self-assurance. Career consultants emphasize that an interviewer often forms an initial judgment within the first two minutes of meeting a candidate.\n\nFirst impressions depend heavily on non-verbal cues. Dressing appropriately in professional attire, offering a firm handshake, making natural eye contact, and offering a warm smile all project reliability and poise. Furthermore, punctuality is non-negotiable; arriving ten to fifteen minutes ahead of scheduled time demonstrates organizational discipline.\n\nEqually vital is researching the company in depth prior to the interview. Interviewers quickly detect generic responses. Candidates who reference the company's recent achievements, core values, and industry challenges immediately stand out. Finally, having two or three thoughtful questions prepared to ask the panel at the conclusion proves genuine curiosity and passion for the position.",
        "questions": [
          {
            "number": 21,
            "question": "What is the main objective of the article?",
            "options": [
              {"key": "A", "text": "Discourage candidates from attending job interviews."},
              {"key": "B", "text": "Provide practical advice on preparing effectively for job interviews."},
              {"key": "C", "text": "Compare salaries across different corporate professions."},
              {"key": "D", "text": "Criticize traditional interview assessment methods."}
            ],
            "correct": t5_k['21'],
            "explanation": "Mục đích là đưa ra lời khuyên thực tế để ứng viên chuẩn bị chu đáo và tự tin khi phỏng vấn xin việc."
          },
          {
            "number": 22,
            "question": "According to career consultants, when is an initial impression typically formed?",
            "options": [
              {"key": "A", "text": "After three hours of testing."},
              {"key": "B", "text": "Within the first two minutes of meeting."},
              {"key": "C", "text": "Only when reviewing examination certificates."},
              {"key": "D", "text": "Several days after the interview concludes."}
            ],
            "correct": t5_k['22'],
            "explanation": "Nhà tuyển dụng thường hình thành ấn tượng đầu tiên chỉ trong 2 phút đầu gặp mặt."
          },
          {
            "number": 23,
            "question": "Which non-verbal behavior conveys poise and reliability?",
            "options": [
              {"key": "A", "text": "Avoiding eye contact and checking your phone."},
              {"key": "B", "text": "Natural eye contact, a warm smile, and professional attire."},
              {"key": "C", "text": "Arriving thirty minutes late without apology."},
              {"key": "D", "text": "Speaking in a barely audible whisper."}
            ],
            "correct": t5_k['23'],
            "explanation": "Giao tiếp bằng mắt tự nhiên, nụ cười thân thiện và trang phục chỉnh tề tạo phong thái tự tin, đáng tin cậy."
          },
          {
            "number": 24,
            "question": "Why is researching the prospective company crucial?",
            "options": [
              {"key": "A", "text": "It enables candidates to provide specific, well-informed answers instead of generic clichés."},
              {"key": "B", "text": "It is required by employment law."},
              {"key": "C", "text": "Interviewers will not ask any personal questions."},
              {"key": "D", "text": "It guarantees an instant job offer on the spot."}
            ],
            "correct": t5_k['24'],
            "explanation": "Giúp ứng viên trả lời sâu sắc, gắn liền với định hướng của công ty thay vì nói những câu sáo rỗng."
          },
          {
            "number": 25,
            "question": "What should a well-prepared candidate do at the end of the interview?",
            "options": [
              {"key": "A", "text": "Rush out of the room immediately."},
              {"key": "B", "text": "Ask thoughtful questions demonstrating genuine interest in the role."},
              {"key": "C", "text": "Complain about previous employers."},
              {"key": "D", "text": "Demand to know the salary before anything else."}
            ],
            "correct": t5_k['25'],
            "explanation": "Đặt các câu hỏi thông minh thể hiện sự quan tâm thực sự đối với vị trí ứng tuyển."
          }
        ]
      },
      {
        "partNumber": 5,
        "title": "Part 5: Questions 26 - 35 (Điền từ vào chỗ trống đoạn văn)",
        "instruction": "Read the text below and choose the correct word for each space. For each question, choose the correct letter A, B, C or D.",
        "passageTitle": "The History and Spirit of the Olympic Games",
        "passage": "The Olympic Games originated in ancient Greece nearly three thousand years ago, held in honor of Zeus at Olympia. In 1896, a French nobleman named Pierre de Coubertin revived the games, (26) ______ the modern Olympic movement. He believed that athletic competition could bring nations closer (27) ______ in mutual friendship and peace.\n\nThe iconic Olympic rings represent the five inhabited (28) ______ of the world united by athleticism. The Olympic flame, lit in Olympia from the rays of the sun, is (29) ______ across the globe by thousands of relay runners before arriving at the opening (30) ______ of the host city.\n\nAthletes dedicate years of rigorous training to qualify for this pinnacle event. For many, winning an Olympic medal is the highest (31) ______ of their athletic careers. However, Coubertin famously reminded the world that the essential thing in life is not conquering, (32) ______ fighting well. Every four years, spectators worldwide are (33) ______ by extraordinary displays of human perseverance, fair play, and sportsmanship that (34) ______ beyond national borders and celebrate the (35) ______ of humanity.",
        "questions": [
          {"number": 26, "options": [{"key": "A", "text": "ending"}, {"key": "B", "text": "founding"}, {"key": "C", "text": "stopping"}, {"key": "D", "text": "destroying"}], "correct": t5_k['26'], "explanation": "Động từ 'founding' (sáng lập / khởi xướng phong trào Olympic hiện đại)."},
          {"number": 27, "options": [{"key": "A", "text": "together"}, {"key": "B", "text": "apart"}, {"key": "C", "text": "away"}, {"key": "D", "text": "beside"}], "correct": t5_k['27'], "explanation": "Cụm 'bring closer together' (gắn kết các quốc gia lại gần nhau hơn)."},
          {"number": 28, "options": [{"key": "A", "text": "cities"}, {"key": "B", "text": "continents"}, {"key": "C", "text": "islands"}, {"key": "D", "text": "oceans"}], "correct": t5_k['28'], "explanation": "Năm vòng tròn tượng trưng cho 5 châu lục (continents) trên thế giới."},
          {"number": 29, "options": [{"key": "A", "text": "carried"}, {"key": "B", "text": "dropped"}, {"key": "C", "text": "lost"}, {"key": "D", "text": "pushed"}], "correct": t5_k['29'], "explanation": "Ngọn đuốc được rước ('carried across the globe') bởi các vận động viên."},
          {"number": 30, "options": [{"key": "A", "text": "ceremony"}, {"key": "B", "text": "holiday"}, {"key": "C", "text": "lesson"}, {"key": "D", "text": "party"}], "correct": t5_k['30'], "explanation": "Cụm 'opening ceremony' (lễ khai mạc)."},
          {"number": 31, "options": [{"key": "A", "text": "accident"}, {"key": "B", "text": "achievement"}, {"key": "C", "text": "mistake"}, {"key": "D", "text": "problem"}], "correct": t5_k['31'], "explanation": "'highest achievement' (thành tựu cao nhất trong sự nghiệp thể thao)."},
          {"number": 32, "options": [{"key": "A", "text": "and"}, {"key": "B", "text": "but"}, {"key": "C", "text": "or"}, {"key": "D", "text": "so"}], "correct": t5_k['32'], "explanation": "Cấu trúc 'not... but...' (không phải là... mà là...)."},
          {"number": 33, "options": [{"key": "A", "text": "inspired"}, {"key": "B", "text": "bored"}, {"key": "C", "text": "frightened"}, {"key": "D", "text": "worried"}], "correct": t5_k['33'], "explanation": "Khán giả được truyền cảm hứng ('inspired by extraordinary displays')."},
          {"number": 34, "options": [{"key": "A", "text": "reach"}, {"key": "B", "text": "stay"}, {"key": "C", "text": "hide"}, {"key": "D", "text": "stop"}], "correct": t5_k['34'], "explanation": "'reach beyond national borders' (vươn ra ngoài mọi biên giới quốc gia)."},
          {"number": 35, "options": [{"key": "A", "text": "unity"}, {"key": "B", "text": "dispute"}, {"key": "C", "text": "conflict"}, {"key": "D", "text": "anger"}], "correct": t5_k['35'], "explanation": "'unity of humanity' (tinh thần đoàn kết của nhân loại)."}
        ]
      }
    ]
  }
}
all_tests.append(test_5)
print("Test 5 ready.")

with open('digital_tests_3_5.json', 'w', encoding='utf-8') as f:
    json.dump(all_tests, f, ensure_ascii=False, indent=2)

print("Saved digital_tests_3_5.json")
