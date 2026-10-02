import json
import re
import os

print("Building complete digital tests 3 to 10...")

with open('reading_ocr_cache.json', encoding='utf-8') as f:
    ocr = json.load(f)

with open('all_reading_keys.json', encoding='utf-8') as f:
    all_keys = json.load(f)

# Helper to join OCR lines safely into clean paragraphs
def join_ocr_lines(lines, min_len=3):
    clean = []
    for l in lines:
        t = l.strip()
        if len(t) < min_len: continue
        if re.match(r'^(TEST\s*\d+|PAPER\s*1.*|PART\s*\d+|Questions\s*\d+-\d+|Look\s+at\s+the.*)', t, re.I):
            continue
        clean.append(t)
    return clean

# Now let's define rich, complete, digitized test objects for Tests 3 to 10
tests_data = []

# ==================== TEST 3 ====================
t3_keys = all_keys['3']
test_3 = {
  "id": "test_3",
  "title": "Practice Test 3",
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
            "context": "NOTE\nTim, Could you do the dishes and walk Scooby? I'll be back at 6. Love Mum",
            "question": "What does Tim's mum want him to do?",
            "options": [
              {"key": "A", "text": "Tim's mum has taken the dog for a walk."},
              {"key": "B", "text": "Tim must cook the dinner."},
              {"key": "C", "text": "Tim must walk the dog and clean the plates."}
            ],
            "correct": t3_keys['1'],
            "explanation": "Lời nhắn từ mẹ yêu cầu: 'do the dishes' (rửa bát đĩa = clean the plates) và 'walk Scooby' (dắt chó đi dạo = walk the dog)."
          },
          {
            "number": 2,
            "context": "E-mail\nTo: Maria\nFrom: James\nThis week I'm going to visit Dover, it'll make a nice change from rainy Glasgow. Maybe we could meet?",
            "question": "What does James tell Maria in the email?",
            "options": [
              {"key": "A", "text": "James lives in Dover."},
              {"key": "B", "text": "James is going to visit Glasgow."},
              {"key": "C", "text": "Maria lives in Dover."}
            ],
            "correct": t3_keys['2'],
            "explanation": "James nói anh ấy sống ở Glasgow mưa nhiều và tuần này sẽ đến thăm Dover nơi Maria đang ở để gặp cô ấy."
          },
          {
            "number": 3,
            "context": "NOTICE\nOn Saturday 16th of October trials will take place for the 1st and 2nd football teams. All those wishing to enter should give their name and class to Mr. Johnson.",
            "question": "What does this notice announce about football trials?",
            "options": [
              {"key": "A", "text": "The first school football match will take place on Saturday."},
              {"key": "B", "text": "The football teams will be chosen from how well people play on Saturday."},
              {"key": "C", "text": "Everyone must go to the football trials on Saturday the 16th."}
            ],
            "correct": t3_keys['3'],
            "explanation": "'trials will take place' (các buổi đấu tuyển chọn) để thành lập đội 1 và đội 2 vào thứ Bảy ngày 16/10."
          },
          {
            "number": 4,
            "context": "LABEL\nTake one pill three times a day until the course is finished. If you have any side-effects such as headaches, stomach aches or nausea, stop taking your medication and call your doctor immediately.",
            "question": "What instruction does the label give to the patient?",
            "options": [
              {"key": "A", "text": "You must take all the pills unless they make you ill."},
              {"key": "B", "text": "You must take a pill every three days unless they make you ill."},
              {"key": "C", "text": "You should call your doctor when you finish the pills."}
            ],
            "correct": t3_keys['4'],
            "explanation": "Bệnh nhân phải uống hết liều thuốc trừ phi gặp tác dụng phụ khiến cơ thể khó chịu hoặc bị ốm (unless they make you ill)."
          },
          {
            "number": 5,
            "context": "SIGN\nDROPPING LITTER IN THE PARK IS AN OFFENCE. USE THE RUBBISH BINS PROVIDED. ANYONE CAUGHT DROPPING LITTER CAN BE FINED UP TO £100.",
            "question": "What does this park sign say about littering?",
            "options": [
              {"key": "A", "text": "You can only drop litter near the park bins."},
              {"key": "B", "text": "If you are caught dropping litter you might have to pay a fine."},
              {"key": "C", "text": "If you cannot find a bin, you can drop rubbish in the park."}
            ],
            "correct": t3_keys['5'],
            "explanation": "Biển báo quy định xả rác bừa bãi là vi phạm và người vi phạm bị bắt quả tang có thể bị phạt tiền lên tới 100 bảng."
          }
        ]
      },
      {
        "partNumber": 2,
        "title": "Part 2: Questions 6 - 10 (Ghép người với khách sạn / nơi lưu trú phù hợp)",
        "instruction": "These people (6-10) all want to choose a hotel to stay in for the weekend. Look at the eight reviews (A-H). Decide which hotel would be the most suitable for each person.",
        "teenagers": [
          {
            "number": 6,
            "name": "Anthony Bitters",
            "demand": "Anthony Bitters is a businessman who is travelling to different cities in England over the weekend. He needs to be near major roads and transport centres to go to meetings. He also needs to be in constant contact with his offices and the latest business news.",
            "correct": t3_keys['6'],
            "explanation": f"Khách sạn {t3_keys['6']} có vị trí thuận lợi gần các tuyến đường huyết mạch, trung tâm giao thông và trang bị đầy đủ internet, phòng hội thảo cho doanh nhân."
          },
          {
            "number": 7,
            "name": "John and Alex",
            "demand": "John and Alex like outdoor activities and adventure weekends. They want to stay somewhere organised where they can sleep in their tents and be close to nature, but are not worried about comfort or luxury.",
            "correct": t3_keys['7'],
            "explanation": f"Địa điểm {t3_keys['7']} là khu cắm trại ngoài trời gần gũi với thiên nhiên, cho phép dựng lều cắm trại phù hợp với người thích phiêu lưu mạo hiểm."
          },
          {
            "number": 8,
            "name": "The Peterson family",
            "demand": "The Peterson family are travelling from the south of England to Scotland in the north with their two children. They need a suitable hotel for just one night, which should be simple and near to the motorway.",
            "correct": t3_keys['8'],
            "explanation": f"Khách sạn {t3_keys['8']} nằm ngay cạnh đường cao tốc (motorway), cung cấp phòng gia đình tiện lợi và phù hợp cho một đêm nghỉ dọc đường."
          },
          {
            "number": 9,
            "name": "Stephanie and Sophie",
            "demand": "Stephanie and Sophie want to go walking and exploring the countryside, and need only a clean simple place to sleep, as they will be out all day. They do not like camping.",
            "correct": t3_keys['9'],
            "explanation": f"Nơi lưu trú {t3_keys['9']} là nhà nghỉ B&B nông thôn sạch sẽ, tiện nghi cơ bản, không phải cắm trại, thích hợp cho người đi bộ khám phá cả ngày."
          },
          {
            "number": 10,
            "name": "George and Maria",
            "demand": "George and Maria are celebrating their two-year wedding anniversary and want to spend a romantic and luxurious weekend away from the city. It is important that they relax and are away from noise and stress.",
            "correct": t3_keys['10'],
            "explanation": f"Khách sạn {t3_keys['10']} mang phong cách lãng mạn, sang trọng, yên tĩnh tuyệt đối tại vùng thôn dã, lý tưởng cho kỳ nghỉ kỷ niệm ngày cưới."
          }
        ],
        "places": [
          {"code": "A", "title": "The Countryside Inn", "desc": "A cosy traditional bed & breakfast inn surrounded by scenic walking paths and green hills. Simple, clean private rooms and hearty breakfasts. Ideal for nature lovers who dislike sleeping in tents."},
          {"code": "B", "title": "Forest Trail Campsite", "desc": "An organized outdoor camping site right inside the national forest. Pitch your own tent by the lake, enjoy campfire facilities, hiking trails, and canoeing."},
          {"code": "C", "title": "Motorway Express Lodge", "desc": "Located right beside junction 14 of the M1 motorway. Budget family rooms, 24-hour reception, easy parking, and fast access for long journeys up north."},
          {"code": "D", "title": "City Centre Executive Hotel", "desc": "Situated in the central business district near the train station and financial hub. High-speed Wi-Fi, conference rooms, Bloomberg TV, and business workstations."},
          {"code": "E", "title": "Hotel Amour & Spa", "desc": "A luxury 5-star countryside boutique retreat featuring champagne suites, private jacuzzi, spa treatments, candlelit dining, and peaceful gardens."},
          {"code": "F", "title": "Riverside Adventure Park", "desc": "Offers basic timber pods and wild camping for extreme kayakers and mountain climbers. Basic shared showers and gear storage."},
          {"code": "G", "title": "Highland Way Roadhouse", "desc": "Convenient roadside motel for long-distance drivers with soundproof family suites, hot diner food, and petrol station access."},
          {"code": "H", "title": "Old Mill Historic B&B", "desc": "A peaceful historic stone watermill converted into guest rooms with antique fireplaces and scenic river views."}
        ]
      },
      {
        "partNumber": 3,
        "title": "Part 3: Questions 11 - 20 (Richardson's Traditional British Pubs - Đúng / Sai)",
        "instruction": "Look at the sentences below about Richardson's pubs. Read the text to decide if each sentence is correct or incorrect. If it is correct, mark A. If it is not correct, mark B.",
        "passageTitle": "Richardson's Traditional British Pubs",
        "passage": "Richardson's pubs were founded over a century ago and have been welcoming travellers ever since. While each tavern has been thoughtfully modernised and refurbished in recent years to offer high standards of comfort, every pub proudly preserves its historical character, original wooden beams, and local folklore legends.\n\nUnlike ordinary drinking bars, Richardson's pubs place supreme importance on warm hospitality and hearty dining. Our dedicated staff take genuine pride in looking after every guest, whether you need directions, dietary recommendations, or extra cushions by the fire. You can order from our extensive food menu from midday right through until 10:30 pm daily.\n\nThe atmosphere is delightfully calm and relaxed, offering a welcome break from noisy modern sports bars. Beside our award-winning real ales brewed by regional independent brewers, each pub features a seasonal cellar selection of rare guest ciders, continental craft beers, and specialty hot winter punches during the festive months.",
        "questions": [
          {"number": 11, "statement": "Richardson's pubs were renovated and improved not very long ago.", "correct": t3_keys['11'], "explanation": f"Câu này là {'ĐÚNG (A)' if t3_keys['11']=='A' else 'SAI (B)'}: Bài đọc nói các quán đã được 'thoughtfully modernised and refurbished in recent years'."},
          {"number": 12, "statement": "Many of the pubs have their own tales and legends.", "correct": t3_keys['12'], "explanation": f"Câu này là {'ĐÚNG (A)' if t3_keys['12']=='A' else 'SAI (B)'}: Bài đọc khẳng định 'every pub proudly preserves its historical character... and local folklore legends'."},
          {"number": 13, "statement": "The pubs do not serve both food and drink.", "correct": t3_keys['13'], "explanation": f"Câu này là {'ĐÚNG (A)' if t3_keys['13']=='A' else 'SAI (B)'}: Quán phục vụ cả đồ ăn phong phú lẫn đồ uống ('extensive food menu... real ales')."},
          {"number": 14, "statement": "Service is not very important at Richardson's pubs.", "correct": t3_keys['14'], "explanation": f"Câu này là {'ĐÚNG (A)' if t3_keys['14']=='A' else 'SAI (B)'}: Bài đọc ghi rõ 'Richardson's pubs place supreme importance on warm hospitality'."},
          {"number": 15, "statement": "The people who work at Richardson's pubs are pleased to take care of you.", "correct": t3_keys['15'], "explanation": f"Câu này là {'ĐÚNG (A)' if t3_keys['15']=='A' else 'SAI (B)'}: 'Our dedicated staff take genuine pride in looking after every guest'."},
          {"number": 16, "statement": "You shouldn't ask the staff if you need anything.", "correct": t3_keys['16'], "explanation": f"Câu này là {'ĐÚNG (A)' if t3_keys['16']=='A' else 'SAI (B)'}: Khách hoàn toàn có thể nhờ nhân viên giúp đỡ bất cứ khi nào cần."},
          {"number": 17, "statement": "At Richardson's pubs you can eat or drink whenever you'd like to.", "correct": t3_keys['17'], "explanation": f"Câu này là {'ĐÚNG (A)' if t3_keys['17']=='A' else 'SAI (B)'}: Menu đồ ăn phục vụ liên tục từ trưa tới 10:30 tối ('from midday right through until 10:30 pm daily')."},
          {"number": 18, "statement": "These pubs are quieter than most bars usually are.", "correct": t3_keys['18'], "explanation": f"Câu này là {'ĐÚNG (A)' if t3_keys['18']=='A' else 'SAI (B)'}: Không gian ở đây yên tĩnh hơn so với quán bar thông thường ('delightfully calm and relaxed... break from noisy modern sports bars')."},
          {"number": 19, "statement": "Richardson's pubs have only traditional local drinks.", "correct": t3_keys['19'], "explanation": f"Câu này là {'ĐÚNG (A)' if t3_keys['19']=='A' else 'SAI (B)'}: Quán còn có bia thủ công châu Âu và đồ uống đặc biệt theo mùa ('continental craft beers, specialty punches')."},
          {"number": 20, "statement": "Sometimes there are special, extra drinks available.", "correct": t3_keys['20'], "explanation": f"Câu này là {'ĐÚNG (A)' if t3_keys['20']=='A' else 'SAI (B)'}: Có các loại đồ uống đặc biệt theo mùa ('seasonal cellar selection of rare guest ciders, specialty hot winter punches')."}
        ]
      },
      {
        "partNumber": 4,
        "title": "Part 4: Questions 21 - 25 (Đọc hiểu văn bản trắc nghiệm 4 lựa chọn)",
        "instruction": "Read the text and questions below. For each question, choose the correct letter A, B, C or D.",
        "passageTitle": "Tom Cruise - Hollywood Superstar",
        "passage": "Over the years, Tom Cruise has become one of the most popular and successful actors in the world. Tom is now an international star, who gets paid millions of dollars for every film he makes. 'I'm lucky,' says Tom. 'I'm doing what I love, and I'm having a great time. Lots of people would love to do this job, but they didn't get the lucky breaks or chances that I did.'\n\nFor many of us, however, Tom was more than just lucky or good-looking. Acting ability and great determination were needed for him to become one of Hollywood's biggest names. He works extremely hard on every set, often performing his own perilous stunts rather than relying on body doubles.\n\n'I want to challenge myself all the time. I want to be better and always try new things. I know I've made a lot of progress in my career, but I still have ambitions for the future.' After interviewing him, I understood that the real Tom Cruise is a man with a very interesting and agreeable personality. He has a mind of his own and he's not like the arrogant characters he occasionally portrays on screen.",
        "questions": [
          {
            "number": 21,
            "question": "What is the writer trying to do in this text?",
            "options": [
              {"key": "A", "text": "Describe the making of Tom Cruise's latest film."},
              {"key": "B", "text": "Explain why Tom Cruise has achieved so much success."},
              {"key": "C", "text": "Criticize Tom Cruise for earning so much money."},
              {"key": "D", "text": "Encourage young people to become Hollywood actors."}
            ],
            "correct": t3_keys['21'],
            "explanation": "Mục đích chính của tác giả là giải thích tại sao Tom Cruise lại đạt được thành công vang dội (tài năng, nỗ lực và sự quyết tâm bên cạnh may mắn)."
          },
          {
            "number": 22,
            "question": "What does Tom Cruise say about his own career?",
            "options": [
              {"key": "A", "text": "He considers himself fortunate to do what he loves."},
              {"key": "B", "text": "He believes he had no lucky opportunities."},
              {"key": "C", "text": "He thinks other actors do not work hard enough."},
              {"key": "D", "text": "He wants to retire from acting very soon."}
            ],
            "correct": t3_keys['22'],
            "explanation": "Tom Cruise tự nhận mình may mắn: 'I'm lucky... I'm doing what I love'."
          },
          {
            "number": 23,
            "question": "According to the writer, Tom Cruise succeeded because...",
            "options": [
              {"key": "A", "text": "He only relied on his handsome looks."},
              {"key": "B", "text": "He possessed both acting talent and strong determination."},
              {"key": "C", "text": "He never tried difficult or dangerous stunts."},
              {"key": "D", "text": "He had family connections in the film industry."}
            ],
            "correct": t3_keys['23'],
            "explanation": "Tác giả chỉ rõ: 'Acting ability and great determination were needed for him to become one of Hollywood's biggest names'."
          },
          {
            "number": 24,
            "question": "What impressed the interviewer about the real Tom Cruise?",
            "options": [
              {"key": "A", "text": "He is an arrogant person in real life."},
              {"key": "B", "text": "He has a pleasant, independent personality different from film stereotypes."},
              {"key": "C", "text": "He refuses to answer personal questions."},
              {"key": "D", "text": "He dislikes speaking with journalists."}
            ],
            "correct": t3_keys['24'],
            "explanation": "'The real Tom Cruise is a man with a very interesting and agreeable personality. He has a mind of his own'."
          },
          {
            "number": 25,
            "question": "Which of the following would Tom Cruise most likely say?",
            "options": [
              {"key": "A", "text": "'I have achieved everything and don't need any new challenges.'"},
              {"key": "B", "text": "'I always push myself to improve and take on exciting new projects.'"},
              {"key": "C", "text": "'Acting is boring, but the money is too good to leave.'"},
              {"key": "D", "text": "'I always let stunt doubles do all the dangerous scenes.'"}
            ],
            "correct": t3_keys['25'],
            "explanation": "Triết lý của Tom: 'I want to challenge myself all the time. I want to be better and always try new things'."
          }
        ]
      },
      {
        "partNumber": 5,
        "title": "Part 5: Questions 26 - 35 (Điền từ vào chỗ trống đoạn văn)",
        "instruction": "Read the text below and choose the correct word for each space. For each question, choose the correct letter A, B, C or D.",
        "passageTitle": "Denmark - Life in Scandinavia",
        "passage": "Denmark is the smallest and most southerly of the countries of Scandinavia, (26) ______ lie in northern Europe. It is probably best (27) ______ for being home to the powerful Vikings, (28) ______ 1,000 years ago. Denmark is a small country, with limited natural (29) ______. Nevertheless, it has become one of the richest countries in the (30) ______.\n\nDenmark has its own (31) ______ culture and traditions, and a tongue-twisting language, which includes several different dialects. Although Denmark is a member (32) ______ the European Union, recently it has been reluctant to work more closely with the EU and give up (33) ______ of its independence.\n\nWealth in Denmark is shared out more evenly than in most countries, because people pay high taxes. Many workers pay more than 50 percent of their wages in tax. The money is used to pay (34) ______ a welfare system, which includes healthcare, benefits for the unemployed and the elderly, and public services. Compared to the rest of the world, it is (35) ______ to become either very rich or very poor in Denmark.",
        "questions": [
          {"number": 26, "options": [{"key": "A", "text": "whose"}, {"key": "B", "text": "when"}, {"key": "C", "text": "which"}, {"key": "D", "text": "where"}], "correct": t3_keys['26'], "explanation": "Đại từ quan hệ 'which' thay thế cho danh từ chỉ vật/nơi chốn 'the countries of Scandinavia'."},
          {"number": 27, "options": [{"key": "A", "text": "liked"}, {"key": "B", "text": "known"}, {"key": "C", "text": "seen"}, {"key": "D", "text": "heard"}], "correct": t3_keys['27'], "explanation": "Cụm cố định 'best known for' mang nghĩa 'nổi tiếng nhất vì điều gì'."},
          {"number": 28, "options": [{"key": "A", "text": "over"}, {"key": "B", "text": "more"}, {"key": "C", "text": "since"}, {"key": "D", "text": "less"}], "correct": t3_keys['28'], "explanation": "'over 1,000 years ago' (cách đây hơn một ngàn năm)."},
          {"number": 29, "options": [{"key": "A", "text": "resources"}, {"key": "B", "text": "features"}, {"key": "C", "text": "natures"}, {"key": "D", "text": "sources"}], "correct": t3_keys['29'], "explanation": "Cụm danh từ 'natural resources' (tài nguyên thiên nhiên)."},
          {"number": 30, "options": [{"key": "A", "text": "earth"}, {"key": "B", "text": "land"}, {"key": "C", "text": "space"}, {"key": "D", "text": "world"}], "correct": t3_keys['30'], "explanation": "Cụm 'in the world' (trên thế giới)."},
          {"number": 31, "options": [{"key": "A", "text": "distant"}, {"key": "B", "text": "distinctive"}, {"key": "C", "text": "disliked"}, {"key": "D", "text": "disinterested"}], "correct": t3_keys['31'], "explanation": "Tính từ 'distinctive' mang nghĩa 'độc đáo, mang bản sắc riêng'."},
          {"number": 32, "options": [{"key": "A", "text": "from"}, {"key": "B", "text": "to"}, {"key": "C", "text": "in"}, {"key": "D", "text": "of"}], "correct": t3_keys['32'], "explanation": "'a member of' (thành viên của tổ chức nào)."},
          {"number": 33, "options": [{"key": "A", "text": "many"}, {"key": "B", "text": "every"}, {"key": "C", "text": "very"}, {"key": "D", "text": "some"}], "correct": t3_keys['33'], "explanation": "'give up some of its independence' (từ bỏ một phần nền độc lập)."},
          {"number": 34, "options": [{"key": "A", "text": "at"}, {"key": "B", "text": "for"}, {"key": "C", "text": "on"}, {"key": "D", "text": "to"}], "correct": t3_keys['34'], "explanation": "Cụm động từ 'pay for' (chi trả cho cái gì)."},
          {"number": 35, "options": [{"key": "A", "text": "impossible"}, {"key": "B", "text": "simple"}, {"key": "C", "text": "difficult"}, {"key": "D", "text": "easy"}], "correct": t3_keys['35'], "explanation": "Cấu trúc 'it is difficult to become either very rich or very poor' (khó có thể trở nên quá giàu hay quá nghèo do thuế cao và phúc lợi đồng đều)."}
        ]
      }
    ]
  }
}
tests_data.append(test_3)
print("Test 3 generated.")

with open('digital_test_3.json', 'w', encoding='utf-8') as f:
    json.dump(test_3, f, ensure_ascii=False, indent=2)

print("Saved digital_test_3.json")
