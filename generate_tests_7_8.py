import json
import re

print("Generating tests 7 and 8...")

with open('all_reading_keys.json', encoding='utf-8') as f:
    all_keys = json.load(f)

with open('digital_tests_3_6.json', encoding='utf-8') as f:
    all_tests = json.load(f)

# ==================== TEST 7 ====================
t7_k = all_keys['7']
test_7 = {
  "id": "test_7",
  "title": "Practice Test 7",
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
            "context": "FOOD LABEL\nKeep frozen at -18°C. Once defrosted, consume contents within 24 hours. Best before April 2027.",
            "question": "What instruction is given regarding the food container?",
            "options": [
              {"key": "A", "text": "You must eat the contents shortly after the container has thawed."},
              {"key": "B", "text": "The container must not be opened while frozen."},
              {"key": "C", "text": "The contents must be thrown away immediately."}
            ],
            "correct": t7_k['1'],
            "explanation": "Khi đã rã đông, phải sử dụng hết thức ăn trong vòng 24 giờ ('within 24 hours')."
          },
          {
            "number": 2,
            "context": "OFFICE MEMO\nPlease note: Today's budget committee meeting originally set for 4 pm on Wednesday has been moved to 5 pm this afternoon in Room 302.",
            "question": "When will the committee meeting take place?",
            "options": [
              {"key": "A", "text": "The meeting will be held at 5 o'clock today."},
              {"key": "B", "text": "The meeting will be held at 4 o'clock on Wednesday."},
              {"key": "C", "text": "The meeting has been cancelled."}
            ],
            "correct": t7_k['2'],
            "explanation": "Cuộc họp đã được chuyển sang 5 giờ chiều nay ('5 pm this afternoon')."
          },
          {
            "number": 3,
            "context": "SECURITY NOTICE\nNO ENTRY BEYOND THIS POINT WITHOUT AN AUTHORIZED VISITOR SECURITY PASS ISSUED BY RECEPTION.",
            "question": "What does this security notice mean?",
            "options": [
              {"key": "A", "text": "The receptionist will give everyone an unrestricted key."},
              {"key": "B", "text": "No one can enter under any circumstances."},
              {"key": "C", "text": "People without an authorized visitor pass will not be allowed past this point."}
            ],
            "correct": t7_k['3'],
            "explanation": "Người không có thẻ khách do lễ tân cấp sẽ không được phép qua khu vực này ('No entry without pass')."
          },
          {
            "number": 4,
            "context": "KITCHEN NOTE\nRoast chicken is in the top oven at 180°C. Please put the peeled carrots and potatoes in the roasting tray at 6:30 pm.",
            "question": "What is the situation regarding dinner preparation?",
            "options": [
              {"key": "A", "text": "The chicken is already cooking in the oven."},
              {"key": "B", "text": "The potatoes are already roasted."},
              {"key": "C", "text": "Dinner has already been served."}
            ],
            "correct": t7_k['4'],
            "explanation": "Gà nướng đã được cho vào lò nướng ('Roast chicken is in the top oven')."
          },
          {
            "number": 5,
            "context": "BAR NOTICE\nUNDER-18S ARE ONLY PERMITTED IN THE LOUNGE BAR WHEN ACCOMPANIED BY A RESPONSIBLE ADULT.",
            "question": "What are the rules regarding minors in the lounge bar?",
            "options": [
              {"key": "A", "text": "Under no circumstances are children allowed inside."},
              {"key": "B", "text": "Minors are allowed in the lounge if they are with an adult supervisor."},
              {"key": "C", "text": "Anyone can enter without supervision."}
            ],
            "correct": t7_k['5'],
            "explanation": "Trẻ vị thành niên dưới 18 tuổi chỉ được vào khi có người lớn đi cùng ('accompanied by an adult')."
          }
        ]
      },
      {
        "partNumber": 2,
        "title": "Part 2: Questions 6 - 10 (Ghép khán giả với chương trình truyền hình / phim tối nay)",
        "instruction": "These people (6-10) all want to watch something on TV tonight. Look at the eight TV reviews (A-H). Decide which would be the most suitable for each person.",
        "teenagers": [
          {
            "number": 6,
            "name": "Martin",
            "demand": "Martin wants to follow live professional football matches with expert tactical commentary and post-match player interviews.",
            "correct": t7_k['6'],
            "explanation": f"Chương trình {t7_k['6']} truyền hình trực tiếp các trận cầu đỉnh cao kèm bình luận chuyên sâu của các chuyên gia."
          },
          {
            "number": 7,
            "name": "Jessica & Tom",
            "demand": "Jessica and Tom enjoy fast-witted celebrity panel games and humorous quiz shows that test general knowledge with plenty of comedy.",
            "correct": t7_k['7'],
            "explanation": f"Gameshow {t7_k['7']} là chương trình đố vui hài hước với sự tham gia của các khách mời ngôi sao dí dỏm."
          },
          {
            "number": 8,
            "name": "Nadia",
            "demand": "Nadia is an enthusiastic home cook who wants practical culinary inspiration for authentic Italian pasta sauces and homemade crusty sourdough bread.",
            "correct": t7_k['8'],
            "explanation": f"Chương trình ẩm thực {t7_k['8']} hướng dẫn từng bước nấu các món mì Ý chuẩn vị và làm bánh mì thủ công tại nhà."
          },
          {
            "number": 9,
            "name": "Robert",
            "demand": "Robert is intrigued by deep investigative journalism, international political affairs, and award-winning documentary exposes on climate change.",
            "correct": t7_k['9'],
            "explanation": f"Kênh phóng sự {t7_k['9']} là loạt phim tài liệu điều tra thời sự uy tín về các vấn đề chính trị và môi trường toàn cầu."
          },
          {
            "number": 10,
            "name": "Grace",
            "demand": "Grace wants an immersive costume period drama set in Victorian London featuring opulent ballroom dances, romantic rivalries, and family secrets.",
            "correct": t7_k['10'],
            "explanation": f"Bộ phim truyền hình {t7_k['10']} tái hiện khung cảnh quý tộc thời Victoria lộng lẫy với những bí mật gia tộc hấp dẫn."
          }
        ],
        "places": [
          {"code": "A", "title": "Matchday Live Extra", "desc": "Live premier league football clash followed by in-depth statistical analysis, slow-motion replays, and dugout interviews with managers."},
          {"code": "B", "title": "The Wits' Circle", "desc": "A riotous primetime comedy panel quiz where comedians and guest celebrities compete in absurd trivia rounds. Non-stop laughter guaranteed."},
          {"code": "C", "title": "Cucina Rustica", "desc": "Acclaimed chef Antonio reveals the heritage of southern Italian cooking, demonstrating fresh handmade tagliatelle, slow-simmered sauces, and rustic loaves."},
          {"code": "D", "title": "Global Dispatches: Melting Horizons", "desc": "A hard-hitting investigative documentary investigating the melting glaciers of Greenland and international environmental climate treaties."},
          {"code": "E", "title": "Belgrave Square", "desc": "Lavish Victorian period drama chronicling the ambitions, scandals, and forbidden romances of an aristocratic London dynasty in 1885."},
          {"code": "F", "title": "Speed Kings", "desc": "Weekly motor racing magazine covering Formula 1 engineering breakthroughs and classic sports car restorations."},
          {"code": "G", "title": "Wild Serengeti", "desc": "Nature documentary following the annual wildebeest migration across African savannahs."},
          {"code": "H", "title": "Pop Anthems Rewind", "desc": "Music countdown show celebrating the top 100 hit songs and music videos of the 1990s."}
        ]
      },
      {
        "partNumber": 3,
        "title": "Part 3: Questions 11 - 20 (Discovering Berlin - Đúng / Sai)",
        "instruction": "Look at the sentences below about Berlin. Read the text to decide if each sentence is correct or incorrect. If it is correct, mark A. If it is not correct, mark B.",
        "passageTitle": "Berlin - A Modern City with Rich History and Vibrant Arts",
        "passage": "Germany's vibrant capital, Berlin, stands as one of the most culturally dynamic and historically compelling metropolises in Europe. Divided for nearly three decades during the Cold War by the infamous Berlin Wall, the city has undergone an extraordinary reunification, evolving into a thriving global centre for arts, design, and multicultural technology startups.\n\nVisitors can trace the city's complex history by cycling along the Wall Trail, where portions of the concrete barrier, such as the open-air East Side Gallery, are now decorated with colourful murals by international artists. In the historic Mitte district, the majestic neoclassical Brandenburg Gate symbolizes peace and unity, while Museum Island houses world-famous antiquities, including the bust of Egyptian Queen Nefertiti.\n\nBeyond its profound monuments, Berlin is celebrated for its relaxed urban lifestyle and sprawling green spaces. More than a third of the city's total area consists of public parks, woodlands, and scenic lakes. In the bohemian neighbourhoods of Kreuzberg and Friedrichshain, lively street food markets, canal-side cafes, and independent art galleries offer creative energy around the clock. With affordable and efficient public transit, exploring Berlin is both effortless and rewarding.",
        "questions": [
          {"number": 11, "statement": "Berlin was physically divided for almost thirty years during the Cold War.", "correct": t7_k['11'], "explanation": "Đúng (A): 'Divided for nearly three decades during the Cold War by the Berlin Wall'."},
          {"number": 12, "statement": "The Berlin Wall was never decorated with any artistic murals.", "correct": t7_k['12'], "explanation": "Sai (B): Bức tường East Side Gallery được trang trí bằng vô số tranh bích họa đầy màu sắc của các nghệ sĩ quốc tế."},
          {"number": 13, "statement": "The Brandenburg Gate is a well-known symbol of unity and peace.", "correct": t7_k['13'], "explanation": "Đúng (A): 'the Brandenburg Gate symbolizes peace and unity'."},
          {"number": 14, "statement": "Museum Island houses world-famous ancient historical treasures.", "correct": t7_k['14'], "explanation": "Đúng (A): Bảo tàng lưu giữ bức tượng bán thân Nữ hoàng Ai Cập Nefertiti và nhiều cổ vật quý giá."},
          {"number": 15, "statement": "Berlin contains very few public parks and green open spaces.", "correct": t7_k['15'], "explanation": "Sai (B): Hơn một phần ba diện tích thành phố là công viên, rừng cây và hồ nước ('more than a third of the city...')."},
          {"number": 16, "statement": "Cruising and relaxing by canals is popular in neighbourhoods like Kreuzberg.", "correct": t7_k['16'], "explanation": "Đúng (A): Các quán cà phê ven kênh và chợ ẩm thực đường phố rất nhộn nhịp ở Kreuzberg."},
          {"number": 17, "statement": "Public transport in Berlin is notoriously expensive and inefficient.", "correct": t7_k['17'], "explanation": "Sai (B): Giao thông công cộng tại Berlin giá cả phải chăng và rất hiệu quả ('affordable and efficient public transit')."},
          {"number": 18, "statement": "Berlin has attracted modern creative design and technology startups.", "correct": t7_k['18'], "explanation": "Đúng (A): Thành phố là trung tâm khởi nghiệp công nghệ và nghệ thuật thiết kế toàn cầu."},
          {"number": 19, "statement": "Cycling along the historic Wall Trail is impossible for tourists.", "correct": t7_k['19'], "explanation": "Sai (B): Du khách có thể dễ dàng đạp xe dọc theo cung đường di tích bức tường Berlin ('cycling along the Wall Trail')."},
          {"number": 20, "statement": "The text depicts Berlin as a culturally vibrant and rewarding destination.", "correct": t7_k['20'], "explanation": "Đúng (A): Tác giả ca ngợi Berlin là điểm đến sống động, giàu trải nghiệm văn hóa và nghệ thuật."},
        ]
      },
      {
        "partNumber": 4,
        "title": "Part 4: Questions 21 - 25 (Đọc hiểu văn bản trắc nghiệm 4 lựa chọn)",
        "instruction": "Read the text and questions below. For each question, choose the correct letter A, B, C or D.",
        "passageTitle": "Head Chef Marco - The Art of Running a Top Kitchen",
        "passage": "At five-thirty in the morning, while most of London is fast asleep, Chef Marco is already inspecting crates of freshly landed turbot and sea bass at Billingsgate Fish Market. For Marco, owner of the two-Michelin-starred restaurant 'L'Amiral', selecting seasonal ingredients at their absolute peak is non-negotiable.\n\n'People imagine cooking in a top kitchen is all about delicate sauces and artistic plating,' Marco remarks with a laugh. 'In reality, it's ninety percent discipline, teamwork, and stamina. During an evening dinner service, you're coordinating twenty chefs in an intense, high-temperature environment where dishes must leave the kitchen at precise intervals and exact temperatures.'\n\nMarco began his apprenticeship at sixteen, washing pots and peeling sacks of potatoes in a bustling seaside bistro. Rather than discouraging him, the intense pressure fueled his passion. He believes that true culinary excellence stems not from complicated tricks, but from respecting the natural flavours of honest produce and never settling for mediocrity.",
        "questions": [
          {
            "number": 21,
            "question": "What is the author trying to convey about Chef Marco?",
            "options": [
              {"key": "A", "text": "He dislikes buying seafood at early morning markets."},
              {"key": "B", "text": "His world-class restaurant success requires relentless dedication, discipline and passion."},
              {"key": "C", "text": "He prefers working completely alone in his kitchen."},
              {"key": "D", "text": "He plans to retire from cooking in London."}
            ],
            "correct": t7_k['21'],
            "explanation": "Tác giả muốn truyền tải sự tận tâm, kỷ luật và niềm đam mê không ngừng nghỉ của bếp trưởng Marco."
          },
          {
            "number": 22,
            "question": "Why does Marco wake up before dawn every morning?",
            "options": [
              {"key": "A", "text": "To personally choose the freshest wild fish at the wholesale market."},
              {"key": "B", "text": "To bake bread for nearby supermarket chains."},
              {"key": "C", "text": "To clean the restaurant dining room floors."},
              {"key": "D", "text": "To avoid morning traffic jams."}
            ],
            "correct": t7_k['22'],
            "explanation": "Marco đích thân dậy từ sáng sớm để chọn nguồn cá tươi ngon nhất tại chợ đầu mối Billingsgate."
          },
          {
            "number": 23,
            "question": "According to Marco, what is the reality of running a professional restaurant kitchen?",
            "options": [
              {"key": "A", "text": "It is effortless and relaxing all day."},
              {"key": "B", "text": "It requires immense discipline, endurance, and precise synchronization among the kitchen team."},
              {"key": "C", "text": "Chefs rarely talk to each other while cooking."},
              {"key": "D", "text": "Food temperature is unimportant."}
            ],
            "correct": t7_k['23'],
            "explanation": "Đòi hỏi kỷ luật cao, sức bền và sự phối hợp chuẩn xác từng giây giữa các đầu bếp trong ca phục vụ."
          },
          {
            "number": 24,
            "question": "How did Marco's early career begin at age sixteen?",
            "options": [
              {"key": "A", "text": "As head executive chef of a five-star hotel."},
              {"key": "B", "text": "Doing humble tasks like washing pots and peeling potatoes in a bistro."},
              {"key": "C", "text": "Writing restaurant reviews for food magazines."},
              {"key": "D", "text": "Managing a wine cellar in Paris."}
            ],
            "correct": t7_k['24'],
            "explanation": "Bắt đầu từ những việc giản dị nhất: rửa nồi và gọt khoai tây tại quán ăn ven biển."
          },
          {
            "number": 25,
            "question": "What is Marco's core cooking philosophy?",
            "options": [
              {"key": "A", "text": "Respect honest natural ingredients and never compromise on standards."},
              {"key": "B", "text": "Use as many artificial flavourings as possible."},
              {"key": "C", "text": "Focus only on visual plating rather than taste."},
              {"key": "D", "text": "Cook everything in microwaves for speed."}
            ],
            "correct": t7_k['25'],
            "explanation": "Tôn trọng hương vị tự nhiên nguyên bản của nguyên liệu và không bao giờ thỏa hiệp với sự tầm thường."
          }
        ]
      },
      {
        "partNumber": 5,
        "title": "Part 5: Questions 26 - 35 (Điền từ vào chỗ trống đoạn văn)",
        "instruction": "Read the text below and choose the correct word for each space. For each question, choose the correct letter A, B, C or D.",
        "passageTitle": "The Global Journey and Culture of Coffee",
        "passage": "Coffee is one of the most widely consumed beverages across the world today. Legend has it that coffee was first (26) ______ in the ancient Ethiopian highlands by a goat herder named Kaldi, who noticed that his goats became energetic after eating red berries from a certain bush.\n\nFrom Ethiopia, coffee cultivation spread across the Arabian Peninsula, where the first coffeehouses (27) ______ established in bustling trading ports. These venues became lively centres for intellectual discussion, debate, and music, earning the nickname 'schools of the wise'. In the seventeenth century, coffee made its (28) ______ to Europe, initially viewed with suspicion (29) ______ quickly embraced by intellectuals and merchants.\n\nToday, coffee is grown in tropical regions along the equator (30) ______ as the 'Bean Belt'. Millions of farmers (31) ______ on coffee crops for their livelihoods. From quick morning espresso shots in Rome to elaborate iced lattes in New York, coffee culture has (32) ______ into a global phenomenon. High-grade specialty coffee beans are now prized for subtle notes of fruit, chocolate, and floral aromas, and coffee tastings are conducted with the same precision (33) ______ fine wine tasting. Enjoyed in (34) ______, coffee provides a stimulating boost that powers modern (35) ______ life.",
        "questions": [
          {"number": 26, "options": [{"key": "A", "text": "discovered"}, {"key": "B", "text": "invented"}, {"key": "C", "text": "composed"}, {"key": "D", "text": "manufactured"}], "correct": t7_k['26'], "explanation": "Động từ 'discovered' (được phát hiện lần đầu tại Ethiopia)."},
          {"number": 27, "options": [{"key": "A", "text": "were"}, {"key": "B", "text": "are"}, {"key": "C", "text": "was"}, {"key": "D", "text": "is"}], "correct": t7_k['27'], "explanation": "Bị động quá khứ số nhiều 'coffeehouses were established'."},
          {"number": 28, "options": [{"key": "A", "text": "way"}, {"key": "B", "text": "trip"}, {"key": "C", "text": "walk"}, {"key": "D", "text": "path"}], "correct": t7_k['28'], "explanation": "Thành ngữ 'made its way to' (du nhập tới / tìm đường tới châu Âu)."},
          {"number": 29, "options": [{"key": "A", "text": "but"}, {"key": "B", "text": "and"}, {"key": "C", "text": "so"}, {"key": "D", "text": "or"}], "correct": t7_k['29'], "explanation": "Liên từ 'but' biểu thị sự tương phản ('initially viewed with suspicion but quickly embraced')."},
          {"number": 30, "options": [{"key": "A", "text": "known"}, {"key": "B", "text": "called"}, {"key": "C", "text": "said"}, {"key": "D", "text": "heard"}], "correct": t7_k['30'], "explanation": "Cụm 'known as' (được biết đến như là vành đai cà phê)."},
          {"number": 31, "options": [{"key": "A", "text": "rely"}, {"key": "B", "text": "wait"}, {"key": "C", "text": "stand"}, {"key": "D", "text": "look"}], "correct": t7_k['31'], "explanation": "Cụm động từ 'rely on' (phụ thuộc / sinh sống dựa vào vụ mùa)."},
          {"number": 32, "options": [{"key": "A", "text": "evolved"}, {"key": "B", "text": "decayed"}, {"key": "C", "text": "vanished"}, {"key": "D", "text": "stayed"}], "correct": t7_k['32'], "explanation": "Động từ 'evolved into' (phát triển / tiến hóa thành hiện tượng toàn cầu)."},
          {"number": 33, "options": [{"key": "A", "text": "as"}, {"key": "B", "text": "than"}, {"key": "C", "text": "like"}, {"key": "D", "text": "from"}], "correct": t7_k['33'], "explanation": "Cấu trúc so sánh bằng 'the same... as...' (cùng độ chuẩn xác như thử rượu vang)."},
          {"number": 34, "options": [{"key": "A", "text": "moderation"}, {"key": "B", "text": "extremes"}, {"key": "C", "text": "excess"}, {"key": "D", "text": "haste"}], "correct": t7_k['34'], "explanation": "Cụm 'enjoyed in moderation' (thưởng thức một cách điều độ)."},
          {"number": 35, "options": [{"key": "A", "text": "daily"}, {"key": "B", "text": "annual"}, {"key": "C", "text": "seldom"}, {"key": "D", "text": "never"}], "correct": t7_k['35'], "explanation": "Cụm 'daily life' (đời sống thường nhật)."}
        ]
      }
    ]
  }
}
all_tests.append(test_7)
print("Test 7 ready.")

# ==================== TEST 8 ====================
t8_k = all_keys['8']
test_8 = {
  "id": "test_8",
  "title": "Practice Test 8",
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
            "context": "OFFICE NOTICE\nAll quarterly sales reports must be submitted to departmental heads by 5 pm on Thursday, ahead of Friday's executive review meeting.",
            "question": "What is required regarding sales reports?",
            "options": [
              {"key": "A", "text": "Reports must be submitted during Friday's meeting."},
              {"key": "B", "text": "All reports are needed before Friday's meeting takes place."},
              {"key": "C", "text": "Staff do not need to prepare any reports this week."}
            ],
            "correct": t8_k['1'],
            "explanation": "Báo cáo phải nộp trước cuộc họp thứ Sáu ('ahead of Friday's meeting')."
          },
          {
            "number": 2,
            "context": "EMAIL\nDear Jane, Could I borrow your DSLR camera for my sister's wedding this weekend? I'll return it safely on Monday. Thanks a lot! George",
            "question": "Why did George email Jane?",
            "options": [
              {"key": "A", "text": "George is asking to borrow Jane's camera for a family event."},
              {"key": "B", "text": "George is inviting Jane to attend a wedding."},
              {"key": "C", "text": "George is offering to buy Jane's camera."}
            ],
            "correct": t8_k['2'],
            "explanation": "George mượn máy ảnh của Jane để chụp ảnh đám cưới của chị gái ('borrow your camera')."
          },
          {
            "number": 3,
            "context": "PHOTOCOPIER INSTRUCTION\nIf the red indicator light flashes continuously, paper has jammed in tray 2. Switch off power before attempting to remove paper.",
            "question": "What should you do if the red indicator flashes?",
            "options": [
              {"key": "A", "text": "Add more printing paper immediately."},
              {"key": "B", "text": "Turn off power before clearing the jammed paper."},
              {"key": "C", "text": "Keep copying until the light turns green."}
            ],
            "correct": t8_k['3'],
            "explanation": "Tắt nguồn trước khi rút giấy kẹt ('Switch off power before removing paper')."
          },
          {
            "number": 4,
            "context": "STREET SIGN\nLOADING BAY ONLY. STRICTLY NO PARKING MON - SAT 8 AM - 6 PM EXCEPT FOR AUTHORIZED COMMERCIAL VEHICLES.",
            "question": "What does this street sign mean?",
            "options": [
              {"key": "A", "text": "Anyone can park here on weekdays."},
              {"key": "B", "text": "Private vehicles are forbidden from parking here during business hours."},
              {"key": "C", "text": "Parking is completely free all day long."}
            ],
            "correct": t8_k['4'],
            "explanation": "Khu vực giao nhận hàng cấm xe cá nhân đỗ từ 8h sáng tới 6h chiều từ thứ Hai đến thứ Bảy."
          },
          {
            "number": 5,
            "context": "PARK NOTICE\nCYCLISTS MUST DISMOUNT AND WALK BICYCLES ACROSS THE PEDESTRIAN FOOTBRIDGE AT ALL TIMES.",
            "question": "What must cyclists do on the footbridge?",
            "options": [
              {"key": "A", "text": "Get off their bikes and walk across the footbridge."},
              {"key": "B", "text": "Ride at maximum speed across the footbridge."},
              {"key": "C", "text": "Leave bicycles at the park entrance."}
            ],
            "correct": t8_k['5'],
            "explanation": "'dismount and walk' nghĩa là xuống xe đạp và dắt bộ qua cầu người đi bộ."
          }
        ]
      },
      {
        "partNumber": 2,
        "title": "Part 2: Questions 6 - 10 (Ghép du khách với gói kỳ nghỉ phù hợp)",
        "instruction": "These people (6-10) are looking for a holiday. Look at the descriptions of eight holidays (A-H). Decide which holiday would be most suitable.",
        "teenagers": [
          {
            "number": 6,
            "name": "Arthur & Beatrice",
            "demand": "Arthur and Beatrice are retired lovers of classical architecture and Renaissance art. They prefer comfortable 4-star hotels with expert guided museum tours.",
            "correct": t8_k['6'],
            "explanation": f"Gói kỳ nghỉ {t8_k['6']} là tour nghệ thuật Phục hưng tại các thành phố lịch sử Ý với hướng dẫn viên chuyên gia."
          },
          {
            "number": 7,
            "name": "Gavin",
            "demand": "Gavin is an energetic mountaineer who wants strenuous guided hiking trails across alpine summits, staying in rustic mountain shelters.",
            "correct": t8_k['7'],
            "explanation": f"Hành trình {t8_k['7']} là cung đường leo núi vượt đỉnh An-pơ đầy thách thức với các trạm dừng nghỉ trên núi cao."
          },
          {
            "number": 8,
            "name": "The Chen Family",
            "demand": "The Chen family have two children under ten. They want an all-inclusive seaside resort with water slides, mini-golf, and organized evening entertainment.",
            "correct": t8_k['8'],
            "explanation": f"Khu nghỉ dưỡng {t8_k['8']} trọn gói với công viên nước, sân golf mini và các chương trình hoạt náo cho trẻ em."
          },
          {
            "number": 9,
            "name": "Claire",
            "demand": "Claire is stressed from her corporate job and desires a secluded luxury spa wellness break offering detox nutrition, yoga, and meditation.",
            "correct": t8_k['9'],
            "explanation": f"Khách sạn spa {t8_k['9']} biệt lập cung cấp các liệu trình thanh lọc cơ thể, thiền định và yoga thư giãn tuyệt đối."
          },
          {
            "number": 10,
            "name": "Simon and friends",
            "demand": "Simon and three friends want a budget coastal sailing holiday where they can learn basic skipper navigation and explore quiet island coves.",
            "correct": t8_k['10'],
            "explanation": f"Chuyến đi {t8_k['10']} dạy kỹ năng lái thuyền buồm giá rẻ quanh các vịnh đảo hoang sơ tuyệt đẹp."
          }
        ],
        "places": [
          {"code": "A", "title": "Italian Renaissance Treasures", "desc": "Immerse in the splendours of Florence, Venice, and Rome. Includes luxury boutique hotel stays and private curator-led access to the Uffizi Gallery and Vatican."},
          {"code": "B", "title": "Alpine Peak Trail Trek", "desc": "A demanding 7-day hiking trek across the Swiss and Austrian Alps. Steep summit climbs, pristine glaciers, and traditional hearty lodge stays."},
          {"code": "C", "title": "SunCoast Splash Family Park", "desc": "All-inclusive Mediterranean coastal village featuring giant water parks, children's mini-clubs, tennis courts, and nightly family stage musicals."},
          {"code": "D", "title": "Serenity Mountain Wellness Spa", "desc": "Nestled in pine-forested valleys, this retreat features holistic thermal baths, silent yoga pavilions, plant-based dining, and mindfulness coaches."},
          {"code": "E", "title": "Aegean Skipper Sailing Academy", "desc": "Learn navigation basics aboard modern 40-foot yachts cruising Greece's tranquil Cycladic islands with certified RYA sailing instructors."},
          {"code": "F", "title": "Sahara Dune Expedition", "desc": "4x4 desert safari across Moroccan dunes, camping in Bedouin tents beneath the star-filled desert sky."},
          {"code": "G", "title": "Nordic Fjord Cruise", "desc": "Relaxing luxury ship voyage through Norway's dramatic steep fjords with gourmet seafood dining."},
          {"code": "H", "title": "London Theatre Week", "desc": "City break featuring tickets to top West End musicals and historic backstage tours."}
        ]
      },
      {
        "partNumber": 3,
        "title": "Part 3: Questions 11 - 20 (Walking Through Ancient Rome - Đúng / Sai)",
        "instruction": "Look at the sentences below about Rome. Read the text to decide if each sentence is correct or incorrect. If it is correct, mark A. If it is not correct, mark B.",
        "passageTitle": "Rome - Exploring the Ancient Monuments and Street Life of the Eternal City",
        "passage": "Rome, famously known as the Eternal City, represents an extraordinary living museum where more than two millennia of history unfold around every corner. From the immense stone arches of the Colosseum to the soaring dome of the Pantheon, the architectural achievements of the Roman Empire continue to inspire awe.\n\nExploring Rome on foot is by far the most rewarding approach, though comfortable walking shoes are essential for navigating its ancient cobblestone streets, known locally as 'sampietrini'. A short walk from the Roman Forum brings visitors to the Trevi Fountain, where legend dictates that tossing a coin over your left shoulder ensures your return to Rome. Millions of euros gathered from the fountain each year are donated directly to charities supporting the city's homeless.\n\nAcross the Tiber River lies Vatican City, the world's smallest independent state. Here, St. Peter's Basilica and the Sistine Chapel, featuring Michelangelo's immortal ceiling frescoes, draw visitors from across the globe. Rome's lively piazzas, buzzing espresso bars, and open-air trattorias make it a feast for all the senses.",
        "questions": [
          {"number": 11, "statement": "Rome is often referred to as the Eternal City.", "correct": t8_k['11'], "explanation": "Đúng (A): 'Rome, famously known as the Eternal City'."},
          {"number": 12, "statement": "The Colosseum and Pantheon are examples of ancient Roman architecture.", "correct": t8_k['12'], "explanation": "Đúng (A): Hai công trình là minh chứng tiêu biểu cho kiến trúc La Mã cổ đại."},
          {"number": 13, "statement": "Walking is discouraged as a way to explore Rome.", "correct": t8_k['13'], "explanation": "Sai (B): Đi bộ là cách khám phá tuyệt vời nhất ('by far the most rewarding approach')."},
          {"number": 14, "statement": "The ancient cobblestone streets in Rome are called 'sampietrini'.", "correct": t8_k['14'], "explanation": "Đúng (A): 'ancient cobblestone streets, known locally as sampietrini'."},
          {"number": 15, "statement": "Tradition says throwing a coin into the Trevi Fountain guarantees you will return.", "correct": t8_k['15'], "explanation": "Đúng (A): Truyền thuyết ném đồng xu qua vai trái để đảm bảo ngày trở lại Roma."},
          {"number": 16, "statement": "Coins collected from the Trevi Fountain are kept by corrupt officials.", "correct": t8_k['16'], "explanation": "Sai (B): Tiền thu được từ đài phun nước được quyên góp từ thiện giúp người vô gia cư."},
          {"number": 17, "statement": "Vatican City is one of the largest countries in the world.", "correct": t8_k['17'], "explanation": "Sai (B): Vatican là quốc gia độc lập nhỏ nhất thế giới ('world's smallest independent state')."},
          {"number": 18, "statement": "Michelangelo painted the ceiling frescoes in the Sistine Chapel.", "correct": t8_k['18'], "explanation": "Đúng (A): 'Michelangelo's immortal ceiling frescoes'."},
          {"number": 19, "statement": "St. Peter's Basilica is located on the moon.", "correct": t8_k['19'], "explanation": "Sai (B): Vương cung thánh đường Thánh Peter nằm ở Vatican, Rome."},
          {"number": 20, "statement": "The author paints an enthusiastic picture of Rome's atmosphere and monuments.", "correct": t8_k['20'], "explanation": "Đúng (A): Tác giả ca ngợi Roma là bữa tiệc của mọi giác quan ('a feast for all the senses')."}
        ]
      },
      {
        "partNumber": 4,
        "title": "Part 4: Questions 21 - 25 (Đọc hiểu văn bản trắc nghiệm 4 lựa chọn)",
        "instruction": "Read the text and questions below. For each question, choose the correct letter A, B, C or D.",
        "passageTitle": "Getting Fit and Slim - Sustainable Health and Nutrition",
        "passage": "In a culture saturated with quick-fix miracle diets and celebrity fitness fads, nutritionists and sports scientists are increasingly urging people to embrace realistic, long-term lifestyle habits rather than rapid weight-loss gimmicks.\n\nExtreme crash diets that severely restrict calories almost always fail in the long run. When the body is deprived of essential fuel, its basal metabolism slows down defensively, and muscle tissue is broken down. Once normal eating resumes, lost weight is rapidly regained, often accompanied by feelings of demoralizing frustration.\n\nInstead, sustainable health is built on consistency and balance. Nutritionists advocate eating nutrient-dense whole foods, such as vibrant vegetables, lean proteins, legumes, and whole grains, while reducing ultra-processed snacks high in refined sugar. Combined with regular aerobic exercise and strength training that protects bone density, small daily changes compound over months into enduring vitality and lasting self-confidence.",
        "questions": [
          {
            "number": 21,
            "question": "What is the writer's primary message in this article?",
            "options": [
              {"key": "A", "text": "Rapid crash diets are the most effective way to stay healthy."},
              {"key": "B", "text": "Sustainable fitness requires balanced nutrition and consistent daily habits."},
              {"key": "C", "text": "Nobody should ever exercise outdoors."},
              {"key": "D", "text": "Sugary snacks are essential for good health."}
            ],
            "correct": t8_k['21'],
            "explanation": "Thông điệp chính là sức khỏe bền vững đến từ dinh dưỡng cân bằng và thói quen rèn luyện kiên trì."
          },
          {
            "number": 22,
            "question": "Why do severe crash diets typically fail over time?",
            "options": [
              {"key": "A", "text": "They cost too much money to purchase."},
              {"key": "B", "text": "The body slows its metabolism and regains weight once normal eating resumes."},
              {"key": "C", "text": "People lose all interest in food."},
              {"key": "D", "text": "They cause excessive muscle growth."}
            ],
            "correct": t8_k['22'],
            "explanation": "Ăn kiêng khắc nghiệt làm chậm trao đổi chất và dễ tăng cân trở lại khi ăn bình thường."
          },
          {
            "number": 23,
            "question": "What dietary approach do nutritionists recommend?",
            "options": [
              {"key": "A", "text": "Eating nutrient-dense whole foods like vegetables, lean protein, and whole grains."},
              {"key": "B", "text": "Living only on fruit juices."},
              {"key": "C", "text": "Eating only processed fried foods."},
              {"key": "D", "text": "Skipping all meals completely."}
            ],
            "correct": t8_k['23'],
            "explanation": "Khuyên dùng thực phẩm tự nhiên giàu dinh dưỡng: rau củ, đạm nạc, các loại đậu và ngũ cốc nguyên hạt."
          },
          {
            "number": 24,
            "question": "What benefit does strength training provide alongside aerobic exercise?",
            "options": [
              {"key": "A", "text": "It helps preserve bone density and maintain muscle tissue."},
              {"key": "B", "text": "It eliminates the need to sleep at night."},
              {"key": "C", "text": "It prevents people from drinking water."},
              {"key": "D", "text": "It makes running impossible."}
            ],
            "correct": t8_k['24'],
            "explanation": "Tập luyện sức mạnh giúp bảo vệ mật độ xương và duy trì khối cơ bắp dẻo dai."
          },
          {
            "number": 25,
            "question": "What conclusion does the author draw about healthy living?",
            "options": [
              {"key": "A", "text": "It is an impossible dream for working adults."},
              {"key": "B", "text": "Small daily positive choices compound over time into lasting vitality."},
              {"key": "C", "text": "Only Olympic athletes can achieve fitness."},
              {"key": "D", "text": "Fitness depends entirely on genetic luck."}
            ],
            "correct": t8_k['25'],
            "explanation": "Những thay đổi nhỏ tích cực hàng ngày sẽ tích lũy thành nguồn sinh lực và sự tự tin lâu dài."
          }
        ]
      },
      {
        "partNumber": 5,
        "title": "Part 5: Questions 26 - 35 (Điền từ vào chỗ trống đoạn văn)",
        "instruction": "Read the text below and choose the correct word for each space. For each question, choose the correct letter A, B, C or D.",
        "passageTitle": "How the Internet Connected the World",
        "passage": "It is difficult to imagine contemporary life (26) ______ the internet. From banking and shopping to streaming entertainment and staying in touch with distant relatives, computer networks (27) ______ transformed human society.\n\nThe earliest origins of the internet trace back to the late 1960s with ARPANET, a military research network (28) ______ by the United States government. However, the internet as we recognize it truly took off in 1989, when British computer scientist Tim Berners-Lee invented the World Wide Web, creating a system that (29) ______ ordinary users to navigate pages using hyperlinks.\n\nIn the decades since, the speed and availability of connections have increased (30) ______. Today, smartphones allow billions of people around the world to access the sum of human knowledge in the palm of their (31) ______. Digital communication allows international collaboration across continents in real time, accelerating scientific discoveries and economic (32) ______.\n\nAt the same time, this immense connectivity poses new challenges, including online privacy issues and misinformation. Developing digital literacy and critical thinking has therefore become (33) ______ essential skill for citizens of every age. As emerging technologies like artificial intelligence continue to evolve, the internet will undoubtedly (34) ______ to shape the future of our (35) ______ planet.",
        "questions": [
          {"number": 26, "options": [{"key": "A", "text": "without"}, {"key": "B", "text": "with"}, {"key": "C", "text": "within"}, {"key": "D", "text": "between"}], "correct": t8_k['26'], "explanation": "Giới từ 'without the internet' (nếu không có internet)."},
          {"number": 27, "options": [{"key": "A", "text": "have"}, {"key": "B", "text": "has"}, {"key": "C", "text": "had"}, {"key": "D", "text": "having"}], "correct": t8_k['27'], "explanation": "Thì hiện tại hoàn thành chủ ngữ số nhiều 'networks have transformed'."},
          {"number": 28, "options": [{"key": "A", "text": "developed"}, {"key": "B", "text": "forgotten"}, {"key": "C", "text": "wasted"}, {"key": "D", "text": "closed"}], "correct": t8_k['28'], "explanation": "Mệnh đề quan hệ rút gọn 'developed by the government' (được phát triển bởi chính phủ)."},
          {"number": 29, "options": [{"key": "A", "text": "enabled"}, {"key": "B", "text": "prevented"}, {"key": "C", "text": "stopped"}, {"key": "D", "text": "refused"}], "correct": t8_k['29'], "explanation": "Cấu trúc 'enabled ordinary users to navigate' (cho phép người dùng thông thường truy cập)."},
          {"number": 30, "options": [{"key": "A", "text": "dramatically"}, {"key": "B", "text": "slightly"}, {"key": "C", "text": "scarcely"}, {"key": "D", "text": "barely"}], "correct": t8_k['30'], "explanation": "Trạng từ 'dramatically' (tăng lên một cách ngoạn mục)."},
          {"number": 31, "options": [{"key": "A", "text": "hand"}, {"key": "B", "text": "foot"}, {"key": "C", "text": "head"}, {"key": "D", "text": "eye"}], "correct": t8_k['31'], "explanation": "Thành ngữ 'in the palm of their hand' (trong lòng bàn tay)."},
          {"number": 32, "options": [{"key": "A", "text": "growth"}, {"key": "B", "text": "loss"}, {"key": "C", "text": "fall"}, {"key": "D", "text": "drop"}], "correct": t8_k['32'], "explanation": "Cụm 'economic growth' (tăng trưởng kinh tế)."},
          {"number": 33, "options": [{"key": "A", "text": "an"}, {"key": "B", "text": "a"}, {"key": "C", "text": "the"}, {"key": "D", "text": "some"}], "correct": t8_k['33'], "explanation": "Mạo từ 'an essential skill' (kỹ năng thiết yếu bắt đầu bằng nguyên âm)."},
          {"number": 34, "options": [{"key": "A", "text": "continue"}, {"key": "B", "text": "stop"}, {"key": "C", "text": "refuse"}, {"key": "D", "text": "avoid"}], "correct": t8_k['34'], "explanation": "Động từ 'continue to shape' (tiếp tục định hình tương lai)."},
          {"number": 35, "options": [{"key": "A", "text": "shared"}, {"key": "B", "text": "empty"}, {"key": "C", "text": "silent"}, {"key": "D", "text": "cold"}], "correct": t8_k['35'], "explanation": "'our shared planet' (hành tinh chung của chúng ta)."}
        ]
      }
    ]
  }
}
all_tests.append(test_8)
print("Test 8 ready.")

with open('digital_tests_3_8.json', 'w', encoding='utf-8') as f:
    json.dump(all_tests, f, ensure_ascii=False, indent=2)

print("Saved digital_tests_3_8.json")
