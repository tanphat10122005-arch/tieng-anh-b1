import json
import re

print("Starting build_and_inject_all_units.py...")

with open('all_reading_keys.json', encoding='utf-8') as f:
    all_keys = json.load(f)

with open('digital_test_3.json', encoding='utf-8') as f:
    test_3 = json.load(f)

# Define Tests 4 through 10
tests_4_to_10 = []

# ==================== TEST 4 ====================
t4_k = all_keys['4']
test_4 = {
  "id": "test_4",
  "title": "Practice Test 4",
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
            "context": "NOTICE\nSmoking, eating and drinking are strictly prohibited in the auditorium. Refreshments may only be consumed in the foyer.",
            "question": "What does this notice tell theatre visitors?",
            "options": [
              {"key": "A", "text": "You can only smoke, eat and drink in special areas."},
              {"key": "B", "text": "You cannot drink, eat or smoke anywhere in the building."},
              {"key": "C", "text": "Food and drinks are permitted inside the auditorium."}
            ],
            "correct": t4_k['1'],
            "explanation": "Chỉ được phép sử dụng đồ ăn uống tại khu vực sảnh (foyer) được quy định."
          },
          {
            "number": 2,
            "context": "POSTCARD\nDear Anne, Sunny Spain is wonderful! The hotel is luxurious and the pool is enormous. Wish you were here to enjoy it with me! Love, Jane",
            "question": "What is Jane expressing in her postcard to Anne?",
            "options": [
              {"key": "A", "text": "Anne does not think the hotel is very good."},
              {"key": "B", "text": "The weather is not very good in Spain."},
              {"key": "C", "text": "Jane wishes Anne was there with her."}
            ],
            "correct": t4_k['2'],
            "explanation": "Jane viết 'Wish you were here to enjoy it with me!' (Ước gì bạn cũng ở đây tận hưởng cùng mình)."
          },
          {
            "number": 3,
            "context": "E-mail\nTo: Nick\nFrom: Peter\nCould you review my draft article on independent cinema before I submit it to the magazine editor? Let me know your thoughts.",
            "question": "Why did Peter email Nick?",
            "options": [
              {"key": "A", "text": "Nick is an actor in the film."},
              {"key": "B", "text": "Peter has written an article on films and wants Nick's opinion."},
              {"key": "C", "text": "Peter wants Nick to read film reviews from a magazine."}
            ],
            "correct": t4_k['3'],
            "explanation": "Peter nhờ Nick đọc bản thảo bài viết về phim ảnh để cho nhận xét trước khi gửi biên tập viên."
          },
          {
            "number": 4,
            "context": "MESSAGE\nDad called from the station. Mum's train is delayed by an hour. Please ring his mobile when you get home so he can pick her up.",
            "question": "What must the person receiving the message do?",
            "options": [
              {"key": "A", "text": "Pick up their mother from the station."},
              {"key": "B", "text": "Ring their dad so he will pick up their mother."},
              {"key": "C", "text": "Drive to the motorway with their dad's phone."}
            ],
            "correct": t4_k['4'],
            "explanation": "Nội dung yêu cầu gọi lại cho bố ('Please ring his mobile... so he can pick her up')."
          },
          {
            "number": 5,
            "context": "MEMO\nUrgent: Due to unexpected competition from new rivals, our quarterly sales target is at risk. All team leaders must submit a revised marketing plan by tomorrow.",
            "question": "What does the manager's memo state?",
            "options": [
              {"key": "A", "text": "You must meet your competitors."},
              {"key": "B", "text": "The boss does not like your marketing plan."},
              {"key": "C", "text": "There is a problem and team leaders must submit a revised plan."}
            ],
            "correct": t4_k['5'],
            "explanation": "Bản ghi nhớ cảnh báo về khó khăn doanh số và yêu cầu nộp kế hoạch marketing sửa đổi trước ngày mai."
          }
        ]
      },
      {
        "partNumber": 2,
        "title": "Part 2: Questions 6 - 10 (Ghép khán giả với bộ phim rạp chiếu phù hợp)",
        "instruction": "These people (6-10) all want to see a film at the cinema. Look at the eight film reviews (A-H). Decide which film would be the most suitable for each person.",
        "teenagers": [
          {
            "number": 6,
            "name": "David",
            "demand": "David loves fast-paced action films with special effects and exciting car chases. He dislikes slow romantic dramas or historical documentaries.",
            "correct": t4_k['6'],
            "explanation": f"Bộ phim {t4_k['6']} là phim hành động đỉnh cao với những pha rượt đuổi nghẹt thở và kỹ xảo điện ảnh mãn nhãn."
          },
          {
            "number": 7,
            "name": "Emma and Lucas",
            "demand": "Emma and Lucas are celebrating their first date. They want a charming light-hearted romantic comedy with great dialogue and a happy ending.",
            "correct": t4_k['7'],
            "explanation": f"Phim {t4_k['7']} là phim hài lãng mạn nhẹ nhàng, dí dỏm, rất phù hợp cho các cặp đôi hẹn hò."
          },
          {
            "number": 8,
            "name": "Sarah",
            "demand": "Sarah is interested in nature and biology. She loves fascinating true-life documentaries showcasing wild animals and stunning landscape photography.",
            "correct": t4_k['8'],
            "explanation": f"Bộ phim {t4_k['8']} là phim tài liệu thiên nhiên hoang dã với những thước phim quay động vật chân thực và hùng vĩ."
          },
          {
            "number": 9,
            "name": "Liam and friends",
            "demand": "Liam and his teenage friends want an entertaining sci-fi adventure involving space exploration, futuristic gadgets, and alien civilizations.",
            "correct": t4_k['9'],
            "explanation": f"Bộ phim {t4_k['9']} là tác phẩm khoa học viễn tưởng du hành vũ trụ đầy lôi cuốn với các sinh vật ngoài hành tinh."
          },
          {
            "number": 10,
            "name": "Professor Miller",
            "demand": "Professor Miller enjoys complex historical mystery dramas based on real historical events, featuring deep character development and period costumes.",
            "correct": t4_k['10'],
            "explanation": f"Tác phẩm {t4_k['10']} là phim trinh thám lịch sử dựa trên các sự kiện có thật với dàn diễn viên xuất sắc và bối cảnh phục dựng công phu."
          }
        ],
        "places": [
          {"code": "A", "title": "Velocity Chase", "desc": "A pulse-pounding thriller featuring high-octane car chases, explosive stunt work, and state-of-the-art visual effects. Non-stop action from opening scene to credits."},
          {"code": "B", "title": "Love in Bloom", "desc": "A delightful romantic comedy set in Paris. Two florist shop rivals fall unexpectedly in love. Witty script, hilarious misunderstandings, and heartwarming romance."},
          {"code": "C", "title": "Wild Planet: Arctic Wonders", "desc": "Breathtaking IMAX documentary following polar bears and arctic foxes through changing seasons. Stunning wildlife cinematography narrated by David Attenborough."},
          {"code": "D", "title": "Nebula Horizon", "desc": "An epic sci-fi odyssey about a crew journeying beyond known galaxies to decipher an alien signal. Dazzling futuristic visuals and intelligent adventure."},
          {"code": "E", "title": "Shadows of Versailles", "desc": "A tense historical mystery set in 18th-century France. Intricate court politics, gorgeous period costumes, and gripping psychological intrigue."},
          {"code": "F", "title": "Haunted Echoes", "desc": "A terrifying modern supernatural horror story about a family investigating strange occurrences in an isolated lighthouse."},
          {"code": "G", "title": "Laugh Out Loud", "desc": "A slapstick comedy about three hapless college students attempting to run a pet daycare centre."},
          {"code": "H", "title": "The Last Samurai", "desc": "An epic martial arts action drama focusing on ancient honour and warfare in feudal Japan."}
        ]
      },
      {
        "partNumber": 3,
        "title": "Part 3: Questions 11 - 20 (Canal Boat Trips in Britain - Đúng / Sai)",
        "instruction": "Look at the sentences below about canal boat trips. Read the text to decide if each sentence is correct or incorrect. If it is correct, mark A. If it is not correct, mark B.",
        "passageTitle": "Exploring Britain's Historic Inland Waterways by Canal Boat",
        "passage": "Britain's historic canal network was constructed during the Industrial Revolution to transport coal and manufactured goods. Today, these tranquil waterways offer one of the most relaxing ways to explore the British countryside.\n\nTravelling aboard a traditional narrowboat requires no prior boating experience or special licence. Before setting off, all hirers receive a comprehensive tuition session covering boat steering, safety rules, and how to operate the manual lock gates. Narrowboats cruise at a gentle walking pace of around three to four miles per hour, giving passengers ample time to admire kingfishers, historic bridges, and picturesque waterside villages.\n\nModern narrowboats are equipped with comfortable central heating, fully fitted kitchens, hot showers, and comfortable sleeping berths. In the evenings, boaters can moor for free along almost any canal towpath and stroll to a charming country pub for dinner. While operating canal locks does require some physical effort, it provides great exercise and camaraderie as fellow boaters are always eager to lend a helping hand.",
        "questions": [
          {"number": 11, "statement": "British canals were originally built for industrial transport.", "correct": t4_k['11'], "explanation": "Đúng (A): Kênh đào ban đầu được xây dựng để vận chuyển than đá và hàng công nghiệp thời Cách mạng Công nghiệp."},
          {"number": 12, "statement": "You need a special sailing licence before hiring a narrowboat.", "correct": t4_k['12'], "explanation": "Sai (B): Bài đọc nêu rõ 'requires no prior boating experience or special licence'."},
          {"number": 13, "statement": "Beginners are given instructions before they depart.", "correct": t4_k['13'], "explanation": "Đúng (A): Du khách được hướng dẫn kỹ càng về cách lái tàu và an toàn ('comprehensive tuition session')."},
          {"number": 14, "statement": "Canal boats travel faster than modern cars.", "correct": t4_k['14'], "explanation": "Sai (B): Thuyền chỉ di chuyển với tốc độ đi bộ khoảng 3-4 dặm/giờ ('gentle walking pace of around 3 to 4 miles per hour')."},
          {"number": 15, "statement": "Passengers have plenty of opportunity to observe nature along the canals.", "correct": t4_k['15'], "explanation": "Đúng (A): 'ample time to admire kingfishers... and picturesque waterside villages'."},
          {"number": 16, "statement": "Modern narrowboats lack basic domestic amenities.", "correct": t4_k['16'], "explanation": "Sai (B): Thuyền hiện đại có đầy đủ tiện nghi: sưởi, bếp nấu, vòi sen nước nóng và giường ngủ êm ái."},
          {"number": 17, "statement": "You must pay heavy mooring fees every time you stop along a towpath.", "correct": t4_k['17'], "explanation": "Sai (B): Bài đọc khẳng định 'boaters can moor for free along almost any canal towpath'."},
          {"number": 18, "statement": "Boaters often visit waterside pubs in the evenings.", "correct": t4_k['18'], "explanation": "Đúng (A): Du khách thường neo thuyền và đi bộ vào các quán rượu ven sông thưởng thức bữa tối."},
          {"number": 19, "statement": "Working the manual canal locks requires zero physical effort.", "correct": t4_k['19'], "explanation": "Sai (B): Việc vận hành các cửa âu kênh đào đòi hỏi sức lực nhất định ('requires some physical effort')."},
          {"number": 20, "statement": "Other boaters are usually willing to assist with operating locks.", "correct": t4_k['20'], "explanation": "Đúng (A): Những người đi thuyền khác luôn sẵn lòng hỗ trợ ('fellow boaters are always eager to lend a helping hand')."}
        ]
      },
      {
        "partNumber": 4,
        "title": "Part 4: Questions 21 - 25 (Đọc hiểu văn bản trắc nghiệm 4 lựa chọn)",
        "instruction": "Read the text and questions below. For each question, choose the correct letter A, B, C or D.",
        "passageTitle": "Madonna - The Evolution of a Pop Icon",
        "passage": "Madonna arrived in New York City in 1978 with little more than thirty-five dollars in her pocket and a dream of becoming a modern dancer. Struggling to make ends meet, she worked at fast-food restaurants and posed for art classes while auditioning relentlessly. Her breakthrough came when she realized that combining dance beats with catchy pop songwriting was her true calling.\n\nThroughout her multi-decade career, Madonna has continuously reinvented her musical style, fashion image, and visual performances. From the 1980s dance-pop anthems to electronic club soundscapes and acoustic folk influences, she refused to remain static. Critics frequently noted that her greatest strength was her keen artistic intuition and her unmatched control over her own business empire.\n\nMadonna proved that female artists could hold complete creative and commercial autonomy in the global music industry. Even well into her sixth decade, she continues to perform sold-out stadium tours worldwide, inspiring generations of younger performers.",
        "questions": [
          {
            "number": 21,
            "question": "What is the author's primary purpose in writing this article?",
            "options": [
              {"key": "A", "text": "Trace Madonna's career trajectory from humble beginnings to enduring pop icon."},
              {"key": "B", "text": "Argue that Madonna should focus exclusively on dance."},
              {"key": "C", "text": "Explain why 1980s music was better than modern music."},
              {"key": "D", "text": "Criticize Madonna's business decisions."}
            ],
            "correct": t4_k['21'],
            "explanation": "Mục đích chính là phác họa chặng đường từ lúc khởi nghiệp khó khăn đến khi trở thành biểu tượng âm nhạc toàn cầu."
          },
          {
            "number": 22,
            "question": "When Madonna first moved to New York in 1978, she...",
            "options": [
              {"key": "A", "text": "Already had a lucrative recording contract."},
              {"key": "B", "text": "Possessed very little money and worked odd jobs to survive."},
              {"key": "C", "text": "Intended to become an opera singer."},
              {"key": "D", "text": "Was already famous across Europe."}
            ],
            "correct": t4_k['22'],
            "explanation": "Bà chỉ có 35 đô la và phải làm thêm ở quán ăn nhanh để kiếm sống trong những ngày đầu."
          },
          {
            "number": 23,
            "question": "According to critics, one of Madonna's most impressive traits is...",
            "options": [
              {"key": "A", "text": "Her ability to constantly reinvent her sound and maintain control of her career."},
              {"key": "B", "text": "Her refusal to try new musical styles."},
              {"key": "C", "text": "Her reliance on music managers for every decision."},
              {"key": "D", "text": "Her preference for small club performances only."}
            ],
            "correct": t4_k['23'],
            "explanation": "Khả năng liên tục đổi mới phong cách và kiểm soát hoàn toàn sự nghiệp nghệ thuật lẫn kinh doanh."
          },
          {
            "number": 24,
            "question": "What groundbreaking impact did Madonna have on the music industry?",
            "options": [
              {"key": "A", "text": "She pioneered music streaming websites."},
              {"key": "B", "text": "She demonstrated that female musicians could command complete artistic independence."},
              {"key": "C", "text": "She stopped releasing albums after 1990."},
              {"key": "D", "text": "She only worked with classical orchestras."}
            ],
            "correct": t4_k['24'],
            "explanation": "Khẳng định nghệ sĩ nữ có thể làm chủ hoàn toàn về mặt sáng tạo và thương mại."
          },
          {
            "number": 25,
            "question": "Which title best summarizes this biographical passage?",
            "options": [
              {"key": "A", "text": "A Brief History of New York Diners"},
              {"key": "B", "text": "The Making and Resilience of a Cultural Phenomenon"},
              {"key": "C", "text": "Why Pop Music is in Decline"},
              {"key": "D", "text": "The Joys of Acoustic Folk Guitars"}
            ],
            "correct": t4_k['25'],
            "explanation": "Tiêu đề thể hiện sự kiên định và hành trình trở thành hiện tượng văn hóa đại chúng."
          }
        ]
      },
      {
        "partNumber": 5,
        "title": "Part 5: Questions 26 - 35 (Điền từ vào chỗ trống đoạn văn)",
        "instruction": "Read the text below and choose the correct word for each space. For each question, choose the correct letter A, B, C or D.",
        "passageTitle": "The Fascinating Story of Chocolate",
        "passage": "Chocolate has been enjoyed for thousands of years. It was first (26) ______ by the ancient Maya and Aztec civilizations in Central America. For these people, cocoa beans were so valuable that they were even used as (27) ______ to trade for food and goods.\n\nThe Aztecs made a bitter, spicy drink from roasted beans, which was (28) ______ drunk during religious ceremonies. When Spanish explorers arrived in the Americas in the sixteenth century, they (29) ______ cocoa beans back to Europe. The Spanish added sugar, vanilla, and cinnamon to make the drink (30) ______ sweeter and more pleasant to European tastes.\n\nFor nearly two centuries, chocolate remained a luxury that only royal families and wealthy nobles could (31) ______. It was not until the nineteenth century that British and Swiss manufacturers developed machines capable (32) ______ producing solid eating chocolate bars. Today, millions of tons of chocolate are consumed worldwide each year, and scientists have found that dark chocolate contains beneficial antioxidants that can (33) ______ heart health when eaten in (34) ______ quantities. It remains one of the world's most (35) ______ treats.",
        "questions": [
          {"number": 26, "options": [{"key": "A", "text": "invented"}, {"key": "B", "text": "discovered"}, {"key": "C", "text": "created"}, {"key": "D", "text": "composed"}], "correct": t4_k['26'], "explanation": "Động từ 'discovered' (được khám phá/tìm ra bởi người Maya cổ đại)."},
          {"number": 27, "options": [{"key": "A", "text": "salary"}, {"key": "B", "text": "currency"}, {"key": "C", "text": "money"}, {"key": "D", "text": "wages"}], "correct": t4_k['27'], "explanation": "Dùng như tiền tệ để trao đổi buôn bán ('used as currency/money')."},
          {"number": 28, "options": [{"key": "A", "text": "hardly"}, {"key": "B", "text": "regularly"}, {"key": "C", "text": "seldom"}, {"key": "D", "text": "rarely"}], "correct": t4_k['28'], "explanation": "Trạng từ 'regularly' (thường xuyên được uống trong các nghi lễ)."},
          {"number": 29, "options": [{"key": "A", "text": "brought"}, {"key": "B", "text": "carried"}, {"key": "C", "text": "sent"}, {"key": "D", "text": "delivered"}], "correct": t4_k['29'], "explanation": "'brought back to Europe' (mang hạt ca cao trở lại châu Âu)."},
          {"number": 30, "options": [{"key": "A", "text": "much"}, {"key": "B", "text": "more"}, {"key": "C", "text": "very"}, {"key": "D", "text": "many"}], "correct": t4_k['30'], "explanation": "Dùng 'much' để nhấn mạnh tính từ so sánh hơn ('much sweeter')."},
          {"number": 31, "options": [{"key": "A", "text": "spend"}, {"key": "B", "text": "afford"}, {"key": "C", "text": "cost"}, {"key": "D", "text": "pay"}], "correct": t4_k['31'], "explanation": "Cụm 'could afford' (có đủ khả năng tài chính để chi trả)."},
          {"number": 32, "options": [{"key": "A", "text": "of"}, {"key": "B", "text": "to"}, {"key": "C", "text": "with"}, {"key": "D", "text": "for"}], "correct": t4_k['32'], "explanation": "Cấu trúc 'capable of + V-ing' (có khả năng làm gì)."},
          {"number": 33, "options": [{"key": "A", "text": "improve"}, {"key": "B", "text": "increase"}, {"key": "C", "text": "repair"}, {"key": "D", "text": "cure"}], "correct": t4_k['33'], "explanation": "Cụm 'improve heart health' (cải thiện sức khỏe tim mạch)."},
          {"number": 34, "options": [{"key": "A", "text": "heavy"}, {"key": "B", "text": "moderate"}, {"key": "C", "text": "excessive"}, {"key": "D", "text": "huge"}], "correct": t4_k['34'], "explanation": "Cụm 'in moderate quantities' (với số lượng vừa phải, điều độ)."},
          {"number": 35, "options": [{"key": "A", "text": "popular"}, {"key": "B", "text": "common"}, {"key": "C", "text": "usual"}, {"key": "D", "text": "famous"}], "correct": t4_k['35'], "explanation": "'most popular treats' (món quà vặt được ưa chuộng nhất thế giới)."}
        ]
      }
    ]
  }
}
tests_4_to_10.append(test_4)
print("Test 4 ready.")

# We continue for tests 5 to 10...
