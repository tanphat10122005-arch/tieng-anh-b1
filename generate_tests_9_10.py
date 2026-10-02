import json
import re

print("Generating tests 9 and 10...")

with open('all_reading_keys.json', encoding='utf-8') as f:
    all_keys = json.load(f)

with open('digital_tests_3_8.json', encoding='utf-8') as f:
    all_tests = json.load(f)

# ==================== TEST 9 ====================
t9_k = all_keys['9']
test_9 = {
  "id": "test_9",
  "title": "Practice Test 9",
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
            "context": "NOTICE\nWET FLOOR: PLEASE WALK CAREFULLY WHEN ENTERING THE SWIMMING POOL CHANGING ROOMS.",
            "question": "What is the advice for swimmers entering the changing rooms?",
            "options": [
              {"key": "A", "text": "Swimmers should take off their shoes before entering."},
              {"key": "B", "text": "People should walk with extra care because the floor is slippery."},
              {"key": "C", "text": "The changing rooms are currently closed for cleaning."}
            ],
            "correct": t9_k['1'],
            "explanation": "Biển báo sàn ướt nhắc nhở mọi người đi lại cẩn thận ('walk carefully')."
          },
          {
            "number": 2,
            "context": "TEXT MESSAGE\nHi Ben, can you let me know if band practice is still on for Thursday evening? Need to confirm my bus ride home. Thanks, Alex",
            "question": "Why is Alex sending this text message to Ben?",
            "options": [
              {"key": "A", "text": "To check if band practice is still taking place on Thursday."},
              {"key": "B", "text": "To ask Ben for money to buy a bus ticket."},
              {"key": "C", "text": "To cancel his band membership."}
            ],
            "correct": t9_k['2'],
            "explanation": "Alex hỏi xem buổi tập ban nhạc có diễn ra như lịch không để sắp xếp xe buýt về nhà."
          },
          {
            "number": 3,
            "context": "EMAIL\nDear Cinema Club Members, Great news! Two-for-one movie tickets available this weekend for all student cardholders on all afternoon screenings!",
            "question": "What special promotion does the cinema email announce?",
            "options": [
              {"key": "A", "text": "Special two-for-one ticket offer for students at afternoon screenings."},
              {"key": "B", "text": "The cinema is closed to the public this weekend."},
              {"key": "C", "text": "Free popcorn for all morning moviegoers."}
            ],
            "correct": t9_k['3'],
            "explanation": "Khuyến mãi mua 1 tặng 1 vé cho sinh viên vào các suất chiếu buổi chiều cuối tuần."
          },
          {
            "number": 4,
            "context": "LUGGAGE TAG\nPLEASE ATTACH THIS NAME & FLIGHT TAG SECURELY TO THE OUTSIDE HANDLE OF YOUR CHECKED BAGGAGE.",
            "question": "What instruction is given to air passengers?",
            "options": [
              {"key": "A", "text": "Place all name tags inside your suitcase."},
              {"key": "B", "text": "Fasten the identification tag firmly to the outside of your luggage."},
              {"key": "C", "text": "Hand your tags to the flight attendants upon boarding."}
            ],
            "correct": t9_k['4'],
            "explanation": "Hành khách cần gắn chặt thẻ tên bên ngoài quai xách của hành lý ký gửi."
          },
          {
            "number": 5,
            "context": "NOTE\nMike, don't forget to take the carton of fresh milk to school for your science experiment today! Left it in the fridge door. Mum",
            "question": "What is Mike reminded to do?",
            "options": [
              {"key": "A", "text": "Take milk from the fridge to school for a science class."},
              {"key": "B", "text": "Buy milk at the supermarket after school."},
              {"key": "C", "text": "Drink all the milk before leaving home."}
            ],
            "correct": t9_k['5'],
            "explanation": "Mẹ nhắc Mike mang hộp sữa từ tủ lạnh đến trường cho thí nghiệm khoa học."
          }
        ]
      },
      {
        "partNumber": 2,
        "title": "Part 2: Questions 6 - 10 (Ghép học sinh với lớp học sau giờ học phù hợp)",
        "instruction": "These students (6-10) want to do some sort of after-school activity. Look at the eight different classes (A-H). Decide which class would be most suitable.",
        "teenagers": [
          {
            "number": 6,
            "name": "Leo",
            "demand": "Leo wants to learn computer programming and coding to create his own indie video games, but has no previous programming experience.",
            "correct": t9_k['6'],
            "explanation": f"Lớp học {t9_k['6']} dạy lập trình game cơ bản từ đầu cho học sinh chưa có kinh nghiệm."
          },
          {
            "number": 7,
            "name": "Maya",
            "demand": "Maya loves expressive theatrical acting, vocal improvisation, and wants to audition for youth theatre stage plays with professional drama coaches.",
            "correct": t9_k['7'],
            "explanation": f"Câu lạc bộ kịch nghệ {t9_k['7']} rèn luyện kỹ năng diễn xuất sân khấu và chuẩn bị cho các buổi thử vai kịch."
          },
          {
            "number": 8,
            "name": "Sam",
            "demand": "Sam is interested in photography and wants to learn digital image editing, lighting techniques, and framing street portraits with a DSLR camera.",
            "correct": t9_k['8'],
            "explanation": f"Khóa học nhiếp ảnh {t9_k['8']} hướng dẫn kỹ thuật ánh sáng, chụp chân dung đường phố và chỉnh sửa ảnh số."
          },
          {
            "number": 9,
            "name": "Zack",
            "demand": "Zack wants an energetic martial arts discipline that teaches self-defense, mental focus, discipline, and builds physical stamina in a safe dojo.",
            "correct": t9_k['9'],
            "explanation": f"Lớp võ thuật {t9_k['9']} dạy kỹ năng tự vệ, rèn luyện thể lực và kỷ luật tập trung cho học sinh."
          },
          {
            "number": 10,
            "name": "Amina",
            "demand": "Amina loves creative writing, poetry, and storytelling. She wants constructive feedback from published authors and opportunities to enter writing contests.",
            "correct": t9_k['10'],
            "explanation": f"Xưởng sáng tác văn học {t9_k['10']} giúp phát triển kỹ năng viết truyện, làm thơ và gửi bài dự thi dưới sự hướng dẫn của nhà văn."
          }
        ],
        "places": [
          {"code": "A", "title": "GameCode Academy", "desc": "Beginner-friendly coding workshops teaching Python and Scratch to build 2D arcade games and mobile apps. No prior programming background necessary."},
          {"code": "B", "title": "Spotlight Youth Theatre", "desc": "Dynamic drama and improv workshops led by West End actors. Stage presence, voice projection, character development, and annual musical productions."},
          {"code": "C", "title": "ShutterCraft Photo Studio", "desc": "Master camera manual controls, studio portrait lighting, shutter speed techniques, and Adobe Lightroom editing with experienced photographers."},
          {"code": "D", "title": "Zen Martial Arts Dojo", "desc": "Traditional Taekwondo and self-defense training emphasizing respect, mental discipline, flexibility, and physical endurance for all belt ranks."},
          {"code": "E", "title": "WordSmith Creative Writers Guild", "desc": "Weekly creative writing circle focusing on short stories, poetry, and world-building with mentor feedback and entry into national youth anthologies."},
          {"code": "F", "title": "Culinary Kids Kitchen", "desc": "Hands-on bakery and international cuisine cooking lessons for young gourmets."},
          {"code": "G", "title": "RoboTech Engineering Lab", "desc": "Building automated LEGO Mindstorms robots and mechanical circuits."},
          {"code": "H", "title": "Harmony Guitar Ensemble", "desc": "Acoustic and electric guitar group lessons learning chords and rock classics."}
        ]
      },
      {
        "partNumber": 3,
        "title": "Part 3: Questions 11 - 20 (The History of Video Games - Đúng / Sai)",
        "instruction": "Look at the sentences below about video games. Read the text to decide if each sentence is correct or incorrect. If it is correct, mark A. If it is not correct, mark B.",
        "passageTitle": "From Arcade Cabinets to 3D Virtual Worlds: The Evolution of Video Games",
        "passage": "Video games have evolved from humble electronic experiments in university physics laboratories into the world's most lucrative and pervasive entertainment industry, surpassing both Hollywood box office revenues and music sales combined.\n\nThe global phenomenon began in the early 1970s with the release of 'Pong', a simple two-dimensional table tennis simulator featuring two white rectangles and a bouncing square dot. Despite its primitive graphics, Pong proved immensely addictive, sparking the golden age of coin-operated arcade cabinets in shopping malls, bowling alleys, and pizza parlours.\n\nThe 1980s brought interactive entertainment directly into family living rooms with the revolutionary Nintendo Entertainment System and iconic characters like Super Mario and Pac-Man. In subsequent decades, the transition from pixelated 2D sprites to photorealistic 3D environments opened up vast cinematic storytelling possibilities. Today, esports tournaments fill Olympic-sized arenas with roaring spectators, while virtual reality headsets place players directly inside breathtaking, interactive alternate realities.",
        "questions": [
          {"number": 11, "statement": "Video games generate more global revenue than cinema box offices and music sales combined.", "correct": t9_k['11'], "explanation": "Đúng (A): 'surpassing both Hollywood box office revenues and music sales combined'."},
          {"number": 12, "statement": "Pong was an extremely complex virtual reality game with 3D graphics.", "correct": t9_k['12'], "explanation": "Sai (B): Pong là trò chơi mô phỏng bóng bàn 2D cực kỳ đơn giản với các vạch trắng và chấm vuông."},
          {"number": 13, "statement": "Arcade machines were popular in public locations like bowling alleys and malls.", "correct": t9_k['13'], "explanation": "Đúng (A): Máy chơi game thùng rất phổ biến tại các trung tâm thương mại và rạp bowling."},
          {"number": 14, "statement": "The Nintendo Entertainment System helped bring gaming into homes in the 1980s.", "correct": t9_k['14'], "explanation": "Đúng (A): 'The 1980s brought entertainment directly into family living rooms with Nintendo'."},
          {"number": 15, "statement": "Super Mario is mentioned as an iconic video game character.", "correct": t9_k['15'], "explanation": "Đúng (A): 'iconic characters like Super Mario and Pac-Man'."},
          {"number": 16, "statement": "3D graphics made cinematic storytelling in games impossible.", "correct": t9_k['16'], "explanation": "Sai (B): Đồ họa 3D mở ra khả năng kể chuyện điện ảnh vô tận ('opened up vast cinematic storytelling possibilities')."},
          {"number": 17, "statement": "Competitive esports tournaments can now fill large sports arenas with fans.", "correct": t9_k['17'], "explanation": "Đúng (A): Các giải đấu esports lấp đầy các nhà thi đấu thể thao cỡ Olympic."},
          {"number": 18, "statement": "Virtual reality headsets are banned for all video game players.", "correct": t9_k['18'], "explanation": "Sai (B): Kính thực tế ảo ngày càng phổ biến và đưa người chơi vào thế giới tương tác sống động."},
          {"number": 19, "statement": "Video games were originally invented on modern mobile smartphones.", "correct": t9_k['19'], "explanation": "Sai (B): Trò chơi điện tử bắt nguồn từ các thí nghiệm trong phòng lab vật lý trường đại học từ thập niên 1960."},
          {"number": 20, "statement": "The text demonstrates the massive cultural and technological growth of gaming.", "correct": t9_k['20'], "explanation": "Đúng (A): Bài đọc khái quát sự phát triển vượt bậc về công nghệ và văn hóa của ngành công nghiệp game."}
        ]
      },
      {
        "partNumber": 4,
        "title": "Part 4: Questions 21 - 25 (Đọc hiểu văn bản trắc nghiệm 4 lựa chọn)",
        "instruction": "Read the text and questions below. For each question, choose the correct letter A, B, C or D.",
        "passageTitle": "The National Youth Orchestra - Young Talents in Concert",
        "passage": "Every summer, one hundred and sixty of Britain's most gifted teenage musicians gather for an intensive residential rehearsal camp before embarking on a nationwide concert hall tour as the National Youth Orchestra (NYO). Ranging in age from thirteen to nineteen, these young instrumentalists represent the future of symphonic classical music.\n\nAdmission to the orchestra is famously competitive, with over a thousand aspiring musicians auditioning annually. Rather than examining exam certificates alone, adjudicators assess expressive musicality, passion, and ensemble adaptability. 'Individual technical virtuosity is important, but being able to listen intently and blend your instrument's tone with the section is what makes a great orchestral player,' notes musical director Sarah Connolly.\n\nThe rehearsal schedule is notoriously demanding, requiring up to eight hours of daily sectional practice. Yet the atmosphere is overwhelmingly supportive rather than cutthroat. For many members coming from small provincial towns where they were the sole classical musician in their school, joining the NYO offers a transformative community of like-minded peers who share their deepest artistic passion.",
        "questions": [
          {
            "number": 21,
            "question": "What is the primary theme of the article?",
            "options": [
              {"key": "A", "text": "The difficulty of manufacturing classical instruments."},
              {"key": "B", "text": "The inspirational experience and high standards of the National Youth Orchestra."},
              {"key": "C", "text": "Why young people should abandon classical music."},
              {"key": "D", "text": "The history of concert halls in London."}
            ],
            "correct": t9_k['21'],
            "explanation": "Chủ đề chính là trải nghiệm truyền cảm hứng và tiêu chuẩn nghệ thuật đỉnh cao của Dàn nhạc Giao hưởng Trẻ Quốc gia."
          },
          {
            "number": 22,
            "question": "How do adjudicators choose musicians during auditions?",
            "options": [
              {"key": "A", "text": "By looking solely at written certificates."},
              {"key": "B", "text": "By evaluating expressive musicality, passion, and ability to blend in an ensemble."},
              {"key": "C", "text": "By picking the loudest players only."},
              {"key": "D", "text": "By randomly drawing names from a hat."}
            ],
            "correct": t9_k['22'],
            "explanation": "Giám khảo đánh giá cảm thụ âm nhạc, niềm say mê và khả năng hòa âm cùng tập thể ('blend your tone with the section')."
          },
          {
            "number": 23,
            "question": "What does musical director Sarah Connolly emphasize as vital?",
            "options": [
              {"key": "A", "text": "Listening intently and blending your tone within the section."},
              {"key": "B", "text": "Playing faster than all the other musicians."},
              {"key": "C", "text": "Never practicing with others."},
              {"key": "D", "text": "Only performing solo pieces."}
            ],
            "correct": t9_k['23'],
            "explanation": "Khả năng lắng nghe chăm chú và hòa quyện âm sắc cùng bè nhạc cụ của mình."
          },
          {
            "number": 24,
            "question": "What characterizes the atmosphere at the summer rehearsal camp?",
            "options": [
              {"key": "A", "text": "Fierce hostility and jealousy among students."},
              {"key": "B", "text": "Demanding practice paired with warm, supportive peer camaraderie."},
              {"key": "C", "text": "Total silence with no interaction permitted."},
              {"key": "D", "text": "Students are forbidden from playing instruments."}
            ],
            "correct": t9_k['24'],
            "explanation": "Tập luyện cường độ cao nhưng bầu không khí gắn kết, hỗ trợ lẫn nhau ('overwhelmingly supportive')."
          },
          {
            "number": 25,
            "question": "Why is joining the orchestra especially transformative for provincial students?",
            "options": [
              {"key": "A", "text": "They can give up practicing permanently."},
              {"key": "B", "text": "They find a welcoming community of peers who share their musical passion."},
              {"key": "C", "text": "They never have to return home."},
              {"key": "D", "text": "They receive free cars."}
            ],
            "correct": t9_k['25'],
            "explanation": "Tìm thấy một cộng đồng những người bạn cùng chung niềm đam mê nghệ thuật sâu sắc."
          }
        ]
      },
      {
        "partNumber": 5,
        "title": "Part 5: Questions 26 - 35 (Điền từ vào chỗ trống đoạn văn)",
        "instruction": "Read the text below and choose the correct word for each space. For each question, choose the correct letter A, B, C or D.",
        "passageTitle": "Exploring the Mysteries of the Moon",
        "passage": "For thousands of years, humans have gazed up at the night sky in wonder at the Moon, Earth's only natural satellite. Because the Moon has no atmosphere or weather, its surface (26) ______ virtually unchanged for billions of years, preserving impact craters from ancient asteroid collisions.\n\nOn July 20, 1969, humanity achieved the impossible when Apollo 11 astronaut Neil Armstrong (27) ______ the first human foot on lunar soil, famously declaring it 'one small step for man, one giant leap for mankind'. Over the next three years, twelve astronauts walked on the Moon, (28) ______ scientific instruments and bringing back hundreds of kilograms of rock samples.\n\nThe Moon's gravitational pull exerts a profound effect on Earth, creating ocean (29) ______ that cycle daily. In recent years, renewed international interest has (30) ______ space agencies to plan permanent lunar research bases. Scientists have detected water ice in permanently shadowed polar craters, which could (31) ______ drinking water and rocket fuel for future missions to Mars. International agreements like the Artemis Accords aim to ensure that lunar exploration remains peaceful, sustainable, and (32) ______ for the benefit of all (33) ______. The Moon represents our gateway (34) ______ the wider cosmos, inspiring future generations of scientists to reach for the (35) ______.",
        "questions": [
          {"number": 26, "options": [{"key": "A", "text": "remains"}, {"key": "B", "text": "turns"}, {"key": "C", "text": "becomes"}, {"key": "D", "text": "stops"}], "correct": t9_k['26'], "explanation": "Động từ 'remains virtually unchanged' (gần như không hề thay đổi qua hàng tỷ năm)."},
          {"number": 27, "options": [{"key": "A", "text": "set"}, {"key": "B", "text": "put"}, {"key": "C", "text": "held"}, {"key": "D", "text": "dropped"}], "correct": t9_k['27'], "explanation": "Cụm 'set foot on' (đặt chân lên bề mặt Mặt trăng)."},
          {"number": 28, "options": [{"key": "A", "text": "installing"}, {"key": "B", "text": "breaking"}, {"key": "C", "text": "hiding"}, {"key": "D", "text": "stealing"}], "correct": t9_k['28'], "explanation": "'installing scientific instruments' (lắp đặt các thiết bị khoa học)."},
          {"number": 29, "options": [{"key": "A", "text": "tides"}, {"key": "B", "text": "winds"}, {"key": "C", "text": "clouds"}, {"key": "D", "text": "rains"}], "correct": t9_k['29'], "explanation": "Hiện tượng thủy triều đại dương ('ocean tides')."},
          {"number": 30, "options": [{"key": "A", "text": "led"}, {"key": "B", "text": "avoided"}, {"key": "C", "text": "stopped"}, {"key": "D", "text": "delayed"}], "correct": t9_k['30'], "explanation": "Cấu trúc 'led space agencies to plan' (thúc đẩy các cơ quan vũ trụ lên kế hoạch)."},
          {"number": 31, "options": [{"key": "A", "text": "provide"}, {"key": "B", "text": "waste"}, {"key": "C", "text": "lose"}, {"key": "D", "text": "spoil"}], "correct": t9_k['31'], "explanation": "Động từ 'provide drinking water' (cung cấp nước uống và nhiên liệu tên lửa)."},
          {"number": 32, "options": [{"key": "A", "text": "beneficial"}, {"key": "B", "text": "harmful"}, {"key": "C", "text": "dangerous"}, {"key": "D", "text": "useless"}], "correct": t9_k['32'], "explanation": "Tính từ 'beneficial' (mang lại lợi ích)."},
          {"number": 33, "options": [{"key": "A", "text": "mankind"}, {"key": "B", "text": "animals"}, {"key": "C", "text": "plants"}, {"key": "D", "text": "robots"}], "correct": t9_k['33'], "explanation": "'benefit of all mankind' (lợi ích của toàn thể nhân loại)."},
          {"number": 34, "options": [{"key": "A", "text": "into"}, {"key": "B", "text": "to"}, {"key": "C", "text": "towards"}, {"key": "D", "text": "from"}], "correct": t9_k['34'], "explanation": "Cụm 'gateway to the wider cosmos' (cánh cổng dẫn tới vũ trụ bao la)."},
          {"number": 35, "options": [{"key": "A", "text": "stars"}, {"key": "B", "text": "trees"}, {"key": "C", "text": "clouds"}, {"key": "D", "text": "seas"}], "correct": t9_k['35'], "explanation": "Thành ngữ 'reach for the stars' (vươn tới những vì sao / ước mơ cao cả)."}
        ]
      }
    ]
  }
}
all_tests.append(test_9)
print("Test 9 ready.")

# ==================== TEST 10 ====================
t10_k = all_keys['10']
test_10 = {
  "id": "test_10",
  "title": "Practice Test 10",
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
            "context": "TEACHER NOTE\nMegan, you missed Tuesday's history revision test due to your doctor's appointment. Please see Mr. Davis today to arrange a make-up session.",
            "question": "What is the reason for this note to Megan?",
            "options": [
              {"key": "A", "text": "Megan missed class and needs to arrange a test make-up session."},
              {"key": "B", "text": "Megan is being punished for bad behaviour."},
              {"key": "C", "text": "Megan is a history teacher."}
            ],
            "correct": t10_k['1'],
            "explanation": "Megan nghỉ học do khám bệnh và cần gặp thầy Davis để làm bài thi bù ('missed test... arrange make-up session')."
          },
          {
            "number": 2,
            "context": "TOURIST SIGN\nGUIDED CASTLE WALKING TOURS COMMENCE HERE EVERY 30 MINUTES FROM 10:00 AM UNTIL 4:30 PM.",
            "question": "What information does this tourist sign give?",
            "options": [
              {"key": "A", "text": "Announces that the castle tour has been cancelled."},
              {"key": "B", "text": "Gives opening hours for the gift shop only."},
              {"key": "C", "text": "Marks the departure location and timetable for castle tours."}
            ],
            "correct": t10_k['2'],
            "explanation": "Biển báo thông báo điểm tập trung xuất phát và lịch trình các chuyến tham quan có hướng dẫn."
          },
          {
            "number": 3,
            "context": "EXAM NOTICE\nSILENCE IN CORRIDORS: EXAMINATIONS IN PROGRESS IN ROOMS 12 - 16. PLEASE RESPECT CANDIDATES.",
            "question": "What does this examination notice demand?",
            "options": [
              {"key": "A", "text": "Candidates must shout during the exam."},
              {"key": "B", "text": "People in the hallways must keep quiet so as not to disturb candidates taking exams."},
              {"key": "C", "text": "The hallway is closed to all teachers."}
            ],
            "correct": t10_k['3'],
            "explanation": "Yêu cầu giữ yên lặng ở hành lang khi phòng thi đang diễn ra ('Silence in corridors')."
          },
          {
            "number": 4,
            "context": "PHONE MESSAGE\nToby called regarding Saturday's birthday barbecue. Please call him back by Friday evening to confirm if you can come.",
            "question": "What must the recipient do in response to the phone message?",
            "options": [
              {"key": "A", "text": "Call Toby back to confirm attendance at the Saturday party."},
              {"key": "B", "text": "Go to Toby's house immediately."},
              {"key": "C", "text": "Cancel the barbecue party."}
            ],
            "correct": t10_k['4'],
            "explanation": "Cần gọi lại cho Toby trước tối thứ Sáu để xác nhận có tham gia tiệc sinh nhật hay không."
          },
          {
            "number": 5,
            "context": "BIRTHDAY CARD\nDear Charlie, Happy 16th Birthday! Hope you enjoy this MP3 player and headphones for your morning jogs. Love from Uncle Robert",
            "question": "What happened according to the birthday card?",
            "options": [
              {"key": "A", "text": "Charlie bought a new MP3 player for his uncle."},
              {"key": "B", "text": "Charlie is a music teacher."},
              {"key": "C", "text": "Charlie received an MP3 player as a birthday gift from his uncle."}
            ],
            "correct": t10_k['5'],
            "explanation": "Charlie nhận được máy nghe nhạc MP3 làm quà sinh nhật từ người chú Robert ('received a gift')."
          }
        ]
      },
      {
        "partNumber": 2,
        "title": "Part 2: Questions 6 - 10 (Ghép học sinh với khóa học định hướng nghề nghiệp phù hợp)",
        "instruction": "These students (6-10) are considering their future careers. Look at the eight vocational study courses (A-H). Decide which course would be most suitable.",
        "teenagers": [
          {
            "number": 6,
            "name": "Amber",
            "demand": "Amber loves animals and dreams of working in veterinary clinical care, caring for sick pets, administering medications, and helping in surgery.",
            "correct": t10_k['6'],
            "explanation": f"Khóa học {t10_k['6']} đào tạo điều dưỡng thú y và chăm sóc y tế động vật trong phòng khám."
          },
          {
            "number": 7,
            "name": "Jordan",
            "demand": "Jordan is practical and fascinated by architectural building construction, carpentry woodwork, and modern eco-friendly timber framing.",
            "correct": t10_k['7'],
            "explanation": f"Khóa đào tạo {t10_k['7']} trang bị kỹ năng mộc xây dựng và kỹ thuật khung nhà gỗ sinh thái."
          },
          {
            "number": 8,
            "name": "Chloe",
            "demand": "Chloe wants to enter the graphic design industry, creating digital branding logos, magazine typography layouts, and website user interfaces.",
            "correct": t10_k['8'],
            "explanation": f"Chương trình {t10_k['8']} chuyên về thiết kế đồ họa số, nhận diện thương hiệu và giao diện web hiện đại."
          },
          {
            "number": 9,
            "name": "Kyle",
            "demand": "Kyle wants a culinary career in fine pastry baking, crafting delicate French patisserie, multi-tiered wedding cakes, and artisanal chocolate confectionery.",
            "correct": t10_k['9'],
            "explanation": f"Khóa làm bánh cao cấp {t10_k['9']} dạy kỹ thuật làm bánh ngọt Pháp, sô-cô-la nghệ thuật và bánh kem cưới."
          },
          {
            "number": 10,
            "name": "Tara",
            "demand": "Tara is interested in aviation and travel management, aspiring to work as airport flight dispatcher, airline passenger services, and tourism logistics.",
            "correct": t10_k['10'],
            "explanation": f"Khóa học hàng không {t10_k['10']} đào tạo dịch vụ hành khách sân bay, điều độ chuyến bay và quản trị lữ hành quốc tế."
          }
        ],
        "places": [
          {"code": "A", "title": "Veterinary Nursing & Animal Care", "desc": "Hands-on training in animal anatomy, clinical nursing, pet surgery preparation, pathology lab tests, and animal rescue welfare in a working veterinary hospital."},
          {"code": "B", "title": "Eco-Carpentry & Timber Construction", "desc": "Practical woodworking apprenticeship mastering roof truss construction, sustainable timber framing, architectural blueprint reading, and joinery tools."},
          {"code": "C", "title": "Digital Graphic Design & UX Layout", "desc": "Comprehensive digital design curriculum covering vector typography, branding identity, packaging aesthetics, and responsive mobile app prototyping."},
          {"code": "D", "title": "Artisanal Patisserie & Confectionery", "desc": "Master the art of choux pastry, macaron creation, chocolate tempering, spun-sugar decor, and tiered wedding cake architecture in commercial kitchens."},
          {"code": "E", "title": "Aviation Operations & Airline Logistics", "desc": "Prepares students for airline flight dispatch, airport terminal operations, international customs protocol, and airline hospitality customer service."},
          {"code": "F", "title": "Maritime Marine Engineering", "desc": "Technical training in ship engine maintenance, diesel diagnostics, and coastal vessel navigation."},
          {"code": "G", "title": "Horticulture & Landscape Gardening", "desc": "Botanical garden maintenance, greenhouse soil science, and landscape design."},
          {"code": "H", "title": "Automotive Mechanics & Electric Vehicles", "desc": "Diagnostic mechanics for hybrid electric cars, engine overhauls, and brake safety systems."}
        ]
      },
      {
        "partNumber": 3,
        "title": "Part 3: Questions 11 - 20 (Managing Exam Stress & Smart Revision - Đúng / Sai)",
        "instruction": "Look at the sentences below about exams. Read the text to decide if each sentence is correct or incorrect. If it is correct, mark A. If it is not correct, mark B.",
        "passageTitle": "Exam Success: Science-Backed Strategies to Prepare and Reduce Stress",
        "passage": "Preparing for major academic examinations is one of the most demanding challenges students encounter, but cognitive psychology shows that adopting smart study techniques dramatically boosts both memory retention and emotional wellbeing.\n\nPassive revision, such as simply re-reading highlighted textbooks over and over, is scientifically proven to be inefficient. Instead, psychologists strongly advocate 'active recall' and 'spaced repetition'. Testing yourself with flashcards, attempting past exam papers under timed conditions, and explaining complex concepts out loud in your own words force the brain to retrieve information, strengthening neural pathways.\n\nEqually vital is maintaining physical health throughout the revision period. Pulling late-night cramming sessions with excessive energy drinks severely impairs memory consolidation, which primarily takes place during deep sleep. Students who prioritize eight hours of sleep, stay hydrated, take brisk outdoor walks, and schedule structured twenty-minute study breaks consistently score higher and experience less anxiety on exam day.",
        "questions": [
          {"number": 11, "statement": "Cognitive psychology has demonstrated effective ways to improve study habits.", "correct": t10_k['11'], "explanation": "Đúng (A): 'cognitive psychology shows that adopting smart study techniques dramatically boosts memory retention'."},
          {"number": 12, "statement": "Simply re-reading highlighted notes is the most effective revision method.", "correct": t10_k['12'], "explanation": "Sai (B): Việc đọc lại ghi chú thụ động đã được chứng minh là kém hiệu quả ('inefficient')."},
          {"number": 13, "statement": "Active recall and spaced repetition are highly recommended by psychologists.", "correct": t10_k['13'], "explanation": "Đúng (A): 'psychologists strongly advocate active recall and spaced repetition'."},
          {"number": 14, "statement": "Practicing with past exam papers helps strengthen memory retention.", "correct": t10_k['14'], "explanation": "Đúng (A): Luyện đề thi thử có bấm giờ buộc não bộ phải truy xuất thông tin, củng cố trí nhớ."},
          {"number": 15, "statement": "All-night study sessions are encouraged as the best way to consolidate memory.", "correct": t10_k['15'], "explanation": "Sai (B): Thức khuya học dồn ('pulling late-night cramming sessions') làm suy giảm nghiêm trọng quá trình ghi nhớ sâu."},
          {"number": 16, "statement": "Memory consolidation predominantly occurs during deep sleep.", "correct": t10_k['16'], "explanation": "Đúng (A): 'memory consolidation... primarily takes place during deep sleep'."},
          {"number": 17, "statement": "Getting eight hours of sleep impairs exam performance.", "correct": t10_k['17'], "explanation": "Sai (B): Ngủ đủ 8 tiếng giúp đạt điểm số cao hơn và giảm lo lắng khi thi."},
          {"number": 18, "statement": "Hydration and brisk physical walks help reduce exam stress.", "correct": t10_k['18'], "explanation": "Đúng (A): Uống đủ nước và đi dạo ngoài trời giúp giảm căng thẳng rõ rệt."},
          {"number": 19, "statement": "Students should never take any study breaks while revising.", "correct": t10_k['19'], "explanation": "Sai (B): Cần sắp xếp các quãng nghỉ ngắn 20 phút có cấu trúc ('structured 20-minute study breaks')."},
          {"number": 20, "statement": "Overall, the text emphasizes balance between smart study methods and physical wellbeing.", "correct": t10_k['20'], "explanation": "Đúng (A): Bài viết nhấn mạnh sự cân bằng giữa phương pháp học thông minh và chăm sóc sức khỏe thể chất."}
        ]
      },
      {
        "partNumber": 4,
        "title": "Part 4: Questions 21 - 25 (Đọc hiểu văn bản trắc nghiệm 4 lựa chọn)",
        "instruction": "Read the text and questions below. For each question, choose the correct letter A, B, C or D.",
        "passageTitle": "The Origin of Blue Jeans - From Workwear to Fashion Staple",
        "passage": "In 1853, during the height of the California Gold Rush, a young Bavarian immigrant named Levi Strauss arrived in San Francisco with bolts of tough canvas cloth intended for wagon covers and tents. Recognizing that gold prospectors desperately needed trousers durable enough to withstand rugged mining conditions, Strauss began manufacturing heavy-duty work pants.\n\nA few years later, a tailor named Jacob Davis teamed up with Strauss to solve a persistent problem: pocket seams kept tearing under the weight of gold ore samples. Davis conceived the brilliant idea of reinforcing pocket corners with copper metal rivets. In 1873, Strauss and Davis were granted a United States patent for copper-riveted work trousers, officially birthing modern blue jeans made from sturdy indigo-dyed denim fabric from Nîmes, France ('de Nîmes').\n\nFor nearly a century, jeans remained strictly utilitarian attire for cowboys, factory labourers, and railroad workers. However, in the 1950s, Hollywood film legends like James Dean and Marlon Brando transformed denim into a symbol of youthful rebellion and effortless cool. Today, blue jeans have transcended all social and generational boundaries, becoming a truly universal wardrobe essential.",
        "questions": [
          {
            "number": 21,
            "question": "What is the primary topic of this historical passage?",
            "options": [
              {"key": "A", "text": "The life of Gold Rush miners in California."},
              {"key": "B", "text": "The evolution of blue jeans from durable work clothes to global fashion."},
              {"key": "C", "text": "How copper rivets are manufactured."},
              {"key": "D", "text": "The decline of the denim industry in Europe."}
            ],
            "correct": t10_k['21'],
            "explanation": "Chủ đề chính là sự phát triển của quần jean xanh từ trang phục bảo hộ lao động thành biểu tượng thời trang toàn cầu."
          },
          {
            "number": 22,
            "question": "Why did Levi Strauss originally make heavy trousers for miners?",
            "options": [
              {"key": "A", "text": "Gold prospectors urgently needed tough trousers that would not wear out quickly."},
              {"key": "B", "text": "He wanted to start a Parisian fashion company."},
              {"key": "C", "text": "The government ordered all miners to wear uniforms."},
              {"key": "D", "text": "Cloth for wagons was banned in San Francisco."}
            ],
            "correct": t10_k['22'],
            "explanation": "Thợ đào vàng cần loại quần bền chắc chịu được điều kiện làm việc khắc nghiệt trong hầm mỏ."
          },
          {
            "number": 23,
            "question": "What innovation did Jacob Davis introduce to make trousers stronger?",
            "options": [
              {"key": "A", "text": "Adding metal copper rivets at the corners of pockets."},
              {"key": "B", "text": "Making trousers completely out of gold."},
              {"key": "C", "text": "Removing all pockets entirely."},
              {"key": "D", "text": "Using thin silk cloth."}
            ],
            "correct": t10_k['23'],
            "explanation": "Ý tưởng đinh tán bằng đồng (copper rivets) ở góc túi để chống rách khi đựng quặng vàng nặng."
          },
          {
            "number": 24,
            "question": "Who popularized blue jeans as a symbol of youth culture in the 1950s?",
            "options": [
              {"key": "A", "text": "Bavarian railway workers."},
              {"key": "B", "text": "Hollywood screen actors like James Dean."},
              {"key": "C", "text": "French fabric merchants from Nîmes."},
              {"key": "D", "text": "Gold miners in 1853."}
            ],
            "correct": t10_k['24'],
            "explanation": "Các tài tử điện ảnh Hollywood như James Dean và Marlon Brando đã đưa quần jean thành biểu tượng văn hóa giới trẻ."
          },
          {
            "number": 25,
            "question": "What is blue jeans' current status according to the author?",
            "options": [
              {"key": "A", "text": "They are only worn by cowboys on ranches."},
              {"key": "B", "text": "They have become a universal everyday wardrobe essential across the world."},
              {"key": "C", "text": "They are completely out of fashion."},
              {"key": "D", "text": "They are banned in most countries."}
            ],
            "correct": t10_k['25'],
            "explanation": "Quần jean đã vượt qua mọi ranh giới xã hội và thế hệ để trở thành trang phục thiết yếu phổ biến toàn cầu."
          }
        ]
      },
      {
        "partNumber": 5,
        "title": "Part 5: Questions 26 - 35 (Điền từ vào chỗ trống đoạn văn)",
        "instruction": "Read the text below and choose the correct word for each space. For each question, choose the correct letter A, B, C or D.",
        "passageTitle": "The Bicycle - The Eco-Friendly Urban Transport Revolution",
        "passage": "First invented in the early nineteenth century, the bicycle is widely considered one of the greatest and most efficient machines (26) ______ created. Unlike cars or aeroplanes that consume fossil fuels and emit greenhouse gases, the bicycle is completely powered by human energy, making it the most environmentally (27) ______ vehicle on Earth.\n\nIn recent years, forward-thinking cities across Europe and around the world have invested (28) ______ in dedicated cycling infrastructure. Cities like Amsterdam and Copenhagen have constructed separated bike lanes, secure parking garages, and priority traffic lights that (29) ______ cycling faster, safer, and more convenient than driving. Studies show that regular cycling improves cardiovascular fitness, lowers stress, and (30) ______ the risk of chronic diseases.\n\nFurthermore, the recent boom in electric bicycles (e-bikes) has (31) ______ cycling accessible to people of all ages and fitness levels, allowing riders to conquer steep hills (32) ______ ease. By replacing motor vehicles for short daily commutes, bicycles reduce city air pollution and traffic congestion (33) ______. As urban planners prioritize sustainability, the humble bicycle is leading the transition towards cleaner, healthier, and more liveable (34) ______ for future (35) ______.",
        "questions": [
          {"number": 26, "options": [{"key": "A", "text": "ever"}, {"key": "B", "text": "never"}, {"key": "C", "text": "seldom"}, {"key": "D", "text": "always"}], "correct": t10_k['26'], "explanation": "Cụm 'most efficient machines ever created' (cỗ máy hiệu quả nhất từng được tạo ra)."},
          {"number": 27, "options": [{"key": "A", "text": "friendly"}, {"key": "B", "text": "harmful"}, {"key": "C", "text": "dangerous"}, {"key": "D", "text": "hostile"}], "correct": t10_k['27'], "explanation": "Cụm 'environmentally friendly' (thân thiện với môi trường)."},
          {"number": 28, "options": [{"key": "A", "text": "heavily"}, {"key": "B", "text": "scarcely"}, {"key": "C", "text": "hardly"}, {"key": "D", "text": "rarely"}], "correct": t10_k['28'], "explanation": "Trạng từ 'invested heavily' (đầu tư mạnh mẽ vào cơ sở hạ tầng)."},
          {"number": 29, "options": [{"key": "A", "text": "make"}, {"key": "B", "text": "do"}, {"key": "C", "text": "take"}, {"key": "D", "text": "bring"}], "correct": t10_k['29'], "explanation": "Cấu trúc 'make + adj' ('make cycling faster, safer')."},
          {"number": 30, "options": [{"key": "A", "text": "reduces"}, {"key": "B", "text": "increases"}, {"key": "C", "text": "creates"}, {"key": "D", "text": "raises"}], "correct": t10_k['30'], "explanation": "Động từ 'reduces the risk' (làm giảm nguy cơ mắc bệnh mãn tính)."},
          {"number": 31, "options": [{"key": "A", "text": "made"}, {"key": "B", "text": "done"}, {"key": "C", "text": "seen"}, {"key": "D", "text": "given"}], "correct": t10_k['31'], "explanation": "Cấu trúc 'made cycling accessible' (khiến việc đạp xe trở nên dễ tiếp cận)."},
          {"number": 32, "options": [{"key": "A", "text": "with"}, {"key": "B", "text": "by"}, {"key": "C", "text": "at"}, {"key": "D", "text": "on"}], "correct": t10_k['32'], "explanation": "Thành ngữ 'with ease' (một cách dễ dàng)."},
          {"number": 33, "options": [{"key": "A", "text": "significantly"}, {"key": "B", "text": "barely"}, {"key": "C", "text": "slightly"}, {"key": "D", "text": "scarcely"}], "correct": t10_k['33'], "explanation": "Trạng từ 'significantly' (giảm ô nhiễm và tắc nghẽn giao thông một cách đáng kể)."},
          {"number": 34, "options": [{"key": "A", "text": "cities"}, {"key": "B", "text": "oceans"}, {"key": "C", "text": "deserts"}, {"key": "D", "text": "forests"}], "correct": t10_k['34'], "explanation": "'liveable cities' (các đô thị đáng sống hơn)."},
          {"number": 35, "options": [{"key": "A", "text": "generations"}, {"key": "B", "text": "past"}, {"key": "C", "text": "yesterdays"}, {"key": "D", "text": "minutes"}], "correct": t10_k['35'], "explanation": "Cụm 'future generations' (các thế hệ tương lai)."}
        ]
      }
    ]
  }
}
all_tests.append(test_10)
print("Test 10 ready.")

with open('digital_tests_all_3_to_10.json', 'w', encoding='utf-8') as f:
    json.dump(all_tests, f, ensure_ascii=False, indent=2)

print("Saved digital_tests_all_3_to_10.json with", len(all_tests), "tests!")
