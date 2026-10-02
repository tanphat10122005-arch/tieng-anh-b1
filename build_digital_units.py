import json
import re

print("Building digital test 1 and test 2...")

test_1 = {
  "id": "test_1",
  "title": "Practice Test 1",
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
            "context": "Do not lean out of the train window",
            "question": "What does the sign say?",
            "options": [
              { "key": "A", "text": "You must not open the window." },
              { "key": "B", "text": "The windows do not open." },
              { "key": "C", "text": "You must not put your head out of the window." }
            ],
            "correct": "C",
            "explanation": "Biển báo 'Do not lean out of the train window' yêu cầu hành khách không được nhoài người hay thò đầu ra ngoài cửa sổ tàu hỏa."
          },
          {
            "number": 2,
            "context": "Smoking is only allowed in the smoking areas.",
            "question": "What does this notice tell you?",
            "options": [
              { "key": "A", "text": "You are not allowed to smoke anywhere in the building." },
              { "key": "B", "text": "There are certain places where you can smoke." },
              { "key": "C", "text": "You must smoke if you are in this area." }
            ],
            "correct": "B",
            "explanation": "'only allowed in the smoking areas' nghĩa là chỉ được phép hút thuốc tại một số khu vực nhất định được chỉ định."
          },
          {
            "number": 3,
            "context": "E-mail\nTo: Ben\nFrom: Mark\nThe tennis match will be cancelled if it is raining and we'll go to the cinema instead.",
            "question": "What does Mark tell Ben?",
            "options": [
              { "key": "A", "text": "They are not going to play tennis." },
              { "key": "B", "text": "They will go to the cinema." },
              { "key": "C", "text": "They may not play tennis." }
            ],
            "correct": "C",
            "explanation": "'will be cancelled if it is raining' -> Trận đấu quần vợt có thể sẽ không diễn ra nếu trời đổ mưa (may not play tennis)."
          },
          {
            "number": 4,
            "context": "Do not open the door until the red light has gone off and the green light comes on",
            "question": "What should people do?",
            "options": [
              { "key": "A", "text": "Wait for the green light before opening the door." },
              { "key": "B", "text": "Turn off the red light when you open the door." },
              { "key": "C", "text": "Do not open the door when the green light is on." }
            ],
            "correct": "A",
            "explanation": "Thông báo nhắc nhở phải đợi đèn đỏ tắt và đèn xanh bật lên mới được phép mở cửa."
          },
          {
            "number": 5,
            "context": "Message\nTo: Anne\nFrom: Julie\nAnne, your doctor's appointment is at two o'clock on Monday instead of three o'clock on Tuesday.",
            "question": "What does Julie say about the appointment?",
            "options": [
              { "key": "A", "text": "Anne's appointment will be a day later." },
              { "key": "B", "text": "Anne's appointment will no longer be on Tuesday." },
              { "key": "C", "text": "Anne's appointment will be an hour later." }
            ],
            "correct": "B",
            "explanation": "Cuộc hẹn đã được chuyển sang 2h chiều thứ Hai thay vì 3h chiều thứ Ba, do đó cuộc hẹn không còn diễn ra vào ngày thứ Ba nữa."
          }
        ]
      },
      {
        "partNumber": 2,
        "title": "Part 2: Questions 6 - 10 (Ghép người với chương trình truyền hình)",
        "instruction": "These people (6-10) want to stay home and watch TV tonight. Look at the eight TV programme reviews (A-H). Decide which programme would be the most suitable for each person. Write the correct letter (A-H).",
        "teenagers": [
          {
            "number": 6,
            "name": "Brian",
            "demand": "Brian likes watersports very much. He would like to go sailing next summer with his friends. He works in a shop and doesn't have much money.",
            "correct": "C",
            "explanation": "Brian thích thể thao dưới nước và muốn đi thuyền buồm giá rẻ -> Phù hợp với C: 'Summer Holidays' (cheap sailing holidays in the Mediterranean)."
          },
          {
            "number": 7,
            "name": "Sally",
            "demand": "Sally is a very romantic person. She likes watching programmes about real people who coped with problems in their life.",
            "correct": "H",
            "explanation": "Sally lãng mạn và thích xem câu chuyện người thật vượt qua khó khăn -> Phù hợp với H: 'Born to Run' (true story of a young man, happy ending will appeal to romantics)."
          },
          {
            "number": 8,
            "name": "Dave",
            "demand": "Dave is a geography teacher in a secondary school in Liverpool. He likes programmes about travel and the environment in general. He is also very interested in wildlife.",
            "correct": "A",
            "explanation": "Dave dạy địa lý, thích du lịch, môi trường và động vật hoang dã -> Phù hợp với A: 'The World Around Us' (phim tài liệu về kim tự tháp, sông Nile, sa mạc và động thực vật)."
          },
          {
            "number": 9,
            "name": "Jane",
            "demand": "Jane is a very artistic person. She enjoys making things and painting in her free time. She enjoys visiting art galleries and museums.",
            "correct": "F",
            "explanation": "Jane có năng khiếu nghệ thuật, thích vẽ tranh và đi bảo tàng -> Phù hợp với F: 'The Creative Mind' (khám phá nghệ thuật, phòng tranh, phỏng vấn nghệ sĩ)."
          },
          {
            "number": 10,
            "name": "Simon",
            "demand": "Simon works in a bank and is very interested in finance and politics. He likes to read the newspaper every day and to be aware of what is going on in the world.",
            "correct": "B",
            "explanation": "Simon làm ngân hàng, quan tâm tài chính và chính trị thế giới -> Phù hợp với B: 'Speak Up' (thảo luận các câu chuyện thời sự, chính phủ và chính đảng)."
          }
        ],
        "places": [
          {
            "code": "A",
            "title": "The World Around Us",
            "desc": "A fascinating study of the ancient Egyptian pyramids and the area around the River Nile in Egypt. The scenery is beautiful and the filming of this documentary is a work of art as it is so thoughtfully done. As well as the obvious camels, there are also many interesting images of other desert animals and plant life."
          },
          {
            "code": "B",
            "title": "Speak Up",
            "desc": "Well-known personalities discuss the main stories of the day. What is going on in the government and who is attacking who in the political parties. Always a lively programme as events, both at home and abroad, are debated with great enthusiasm."
          },
          {
            "code": "C",
            "title": "Summer Holidays",
            "desc": "A practical and honest account of some of the summer holidays that are on offer this year. Tonight's programme features a weekend in Disneyland in Paris, cheap sailing holidays in the Mediterranean and a shopping and sightseeing trip to New York."
          },
          {
            "code": "D",
            "title": "Cooking for special occasions",
            "desc": "The fun cookery programme that offers lots of exciting ideas from children's birthday parties to that frightening dinner for the boss and his wife. Easy to follow step-by-step instructions and many useful tips on how to make your dinner party a little bit special."
          },
          {
            "code": "E",
            "title": "The weather programme",
            "desc": "All your weather forecasts in one programme. Featuring local, national and international weather news this is a handy programme for anyone who is about to travel or go on holiday. So if you are off on a trip or have an outside event planned, don't miss this informative programme."
          },
          {
            "code": "F",
            "title": "The Creative Mind",
            "desc": "One of the most popular programmes on TV at the moment, The Creative Mind explores different artistic themes from exhibition reviews, information about major and smaller galleries and museums, and interviews with artists, writers, actors and musicians."
          },
          {
            "code": "G",
            "title": "Death in Paris",
            "desc": "A fast, violent film about the Mafia in Paris. Although there are some good actors in this film, the story isn't very exciting or interesting and it is often hard to understand what is going on. There are some beautiful Parisian scenes however and a few funny moments between the scenes of violence."
          },
          {
            "code": "H",
            "title": "Born to Run",
            "desc": "An interesting story of a young man with learning difficulties who overcame the problems in his life, through his great talent for athletics. This is a true story of how one person made the most of their life and also helped many other people with similar problems. The happy ending will appeal to all those romantics out there."
          }
        ]
      },
      {
        "partNumber": 3,
        "title": "Part 3: Questions 11 - 20 (Đúng / Sai - True or False)",
        "instruction": "Look at the statements below about holidays in and around the city of Norwich in England. Read the text to decide if each statement is correct or incorrect. If it is correct, mark A (TRUE). If it is incorrect, mark B (FALSE).",
        "passageTitle": "Holidays in Norwich",
        "passage": "Norwich is the capital of East Anglia, an area on the east coast of England which is famous for its natural beauty and impressive architecture. Norwich is a wonderful city to explore and is popular with tourists all year round.\n\nNorwich is not a city of luxurious hotels but it has a good selection of reasonably priced places to stay in, both in the city centre and further out. The Beeches Hotel, for example, next to the cathedral, has a beautiful Victorian garden and has just over twenty double rooms. Comfortable accommodation costs £65 for two nights' bed and breakfast per person; weekend breaks from October to May cost £59 per person.\n\nNorwich is famous for its magnificent cathedral. The cathedral has a summer programme of music and events which is open to the general public. One event, 'Fire from Heaven', is a drama and musical performance with fireworks, a laser light show and a carnival with local people dressed in colourful costumes.\n\nNorwich is also home to the Sainsbury Centre for the Visual Arts, a world-class collection of international art in a building at the University of East Anglia designed by Sir Norman Foster. This is well worth a visit and there is a lovely canteen with an excellent selection of hot and cold snacks. It also specializes in vegetarian food.\n\nThe city has a new professional theatre, the Playhouse, on the River Wensum. The city's annual international arts festival is from 10-20 October. Not on the classic tourist agenda but well worth a visit are the factory shoe shops in Norwich for men, women and children. Here you can buy shoes for less than half the shop price.\n\nFinally, if you fancy a complete break from the stresses of everyday life, you could hire a boat and spend a few days cruising along the rivers of the famous Norfolk Broads. The Broads have changed for the better in recent years. In our environmentally friendly age, the emphasis has moved towards the quiet enjoyment of nature and wildlife. You can hire a boat, big or small, for an hour or two or even up to a week or two. This makes a perfect day out or holiday for people of all ages.",
        "questions": [
          {
            "number": 11,
            "statement": "There are only a lot of tourists in Norwich in the summer.",
            "correct": "B",
            "explanation": "Trong bài nêu rõ: 'popular with tourists all year round' (thu hút khách du lịch quanh năm chứ không chỉ riêng mùa hè)."
          },
          {
            "number": 12,
            "statement": "You don't have to pay a lot of money to stay in Norwich.",
            "correct": "A",
            "explanation": "Thành phố có nhiều nơi ở giá cả rất hợp lý ('good selection of reasonably priced places to stay in')."
          },
          {
            "number": 13,
            "statement": "All your meals are included in the cost of a room at the Beeches Hotel.",
            "correct": "B",
            "explanation": "Chi phí chỉ bao gồm chỗ ở và bữa sáng ('bed and breakfast'), không bao gồm tất cả các bữa ăn."
          },
          {
            "number": 14,
            "statement": "It is cheaper to stay at the Beeches Hotel in the winter.",
            "correct": "A",
            "explanation": "Nghỉ cuối tuần từ tháng 10 đến tháng 5 (mùa đông) giá chỉ £59 so với giá thông thường £65."
          },
          {
            "number": 15,
            "statement": "'The Cathedral' is the name of a theatre in Norwich.",
            "correct": "B",
            "explanation": "The Cathedral là nhà thờ chính tòa lớn, còn tên của nhà hát thành phố là 'the Playhouse'."
          },
          {
            "number": 16,
            "statement": "Anyone can go to the 'Fire from Heaven' show.",
            "correct": "A",
            "explanation": "Chương trình này 'open to the general public' (mở cửa tự do cho mọi người trong công chúng)."
          },
          {
            "number": 17,
            "statement": "The Sainsbury Centre has art from all over the world.",
            "correct": "A",
            "explanation": "Nơi đây sở hữu 'world-class collection of international art' (bộ sưu tập nghệ thuật quốc tế đỉnh cao)."
          },
          {
            "number": 18,
            "statement": "If you don't eat meat, you shouldn't eat in the Sainsbury Centre canteen.",
            "correct": "B",
            "explanation": "Căn tin tại đây chuyên phục vụ món chay ('specializes in vegetarian food') nên người ăn chay rất nên tới."
          },
          {
            "number": 19,
            "statement": "You can save a lot of money at the factory shoe shops.",
            "correct": "A",
            "explanation": "Bạn có thể mua giày với giá chưa bằng một nửa giá ở các cửa hàng thông thường ('less than half the shop price')."
          },
          {
            "number": 20,
            "statement": "The Broads are not really suitable for a family holiday.",
            "correct": "B",
            "explanation": "Bài viết khẳng định nơi này tạo nên 'a perfect day out or holiday for people of all ages' (kỳ nghỉ hoàn hảo cho mọi lứa tuổi / gia đình)."
          }
        ]
      },
      {
        "partNumber": 4,
        "title": "Part 4: Questions 21 - 25 (Đọc hiểu văn bản trắc nghiệm)",
        "instruction": "Read the text and questions below. For each question, choose the correct letter A, B, C or D.",
        "passageTitle": "Mandy Jones - Holiday Company Manager",
        "passage": "I did a business administration degree at Bristol University and then worked for a credit card company for eight years. During this time, I was assistant marketing manager. I gained a lot of useful experience doing this job, but in 1997, I decided that I needed a change. I moved to Thomson Holidays where I have worked as a manager ever since. My main job is to think up new and interesting ideas for holidays.\n\nWhen I'm working from my office in the UK, I arrive at 9 a.m. First I answer my e-mails, then plan the day. My role is to investigate new projects for Thomson Holidays in our Mediterranean resorts. I am responsible for thinking up ideas, developing them and evaluating their success.\n\nWe have lots of meetings in the office which involve the marketing department, holiday reps and people that we bring in from outside such as entertainment organisers. The aim is to develop an exciting idea into a realistic and workable project.\n\nOnce a month I spend a few days overseas checking possible resorts, meeting with reps to develop their roles and working out how events should be sold to the customer. I work with resort supervisors, use their local knowledge of bars and clubs for venues, talk through new ideas and find out how existing ones are working. I also meet holidaymakers.\n\nI have to be very open-minded because ideas come from anywhere. I love my job because I get to travel and I am working on projects that really excite me.",
        "questions": [
          {
            "number": 21,
            "question": "What is the writer's main purpose in writing the text?",
            "options": [
              { "key": "A", "text": "To explain the best way to choose a holiday." },
              { "key": "B", "text": "To advise people on holiday resorts." },
              { "key": "C", "text": "To explain what her job involves." },
              { "key": "D", "text": "To show how stressful her job is." }
            ],
            "correct": "C",
            "explanation": "Mandy Jones miêu tả chi tiết công việc hàng ngày và vai trò của một người quản lý phát triển sản phẩm du lịch."
          },
          {
            "number": 22,
            "question": "What do we learn about the writer in the first paragraph?",
            "options": [
              { "key": "A", "text": "She learned a lot from her first job." },
              { "key": "B", "text": "She disliked her first job." },
              { "key": "C", "text": "She lost her first job." },
              { "key": "D", "text": "She worked in the administration department of Bristol University." }
            ],
            "correct": "A",
            "explanation": "Mandy chia sẻ: 'I gained a lot of useful experience doing this job' (tích lũy được rất nhiều kinh nghiệm quý báu)."
          },
          {
            "number": 23,
            "question": "The writer has to",
            "options": [
              { "key": "A", "text": "send e-mails all day." },
              { "key": "B", "text": "find out if new ideas could actually work." },
              { "key": "C", "text": "entertain the holiday reps." },
              { "key": "D", "text": "spend all of her time having meetings in the office." }
            ],
            "correct": "B",
            "explanation": "'The aim is to develop an exciting idea into a realistic and workable project' -> tìm hiểu xem ý tưởng có thực tế và khả thi hay không."
          },
          {
            "number": 24,
            "question": "What does she say about her job?",
            "options": [
              { "key": "A", "text": "She never knows where or how a new idea might come to her." },
              { "key": "B", "text": "It makes her very popular with lots of people." },
              { "key": "C", "text": "She spends too much time in bars and clubs." },
              { "key": "D", "text": "She has a few problems with local people at the resorts." }
            ],
            "correct": "A",
            "explanation": "'ideas come from anywhere' -> cô ấy không biết trước được ý tưởng mới sẽ xuất hiện từ đâu hay lúc nào."
          },
          {
            "number": 25,
            "question": "Which of the following is the best description of the writer?",
            "options": [
              { "key": "A", "text": "A working woman who very much enjoys what she does for a living." },
              { "key": "B", "text": "The travel agent who is trying to get a promotion." },
              { "key": "C", "text": "A woman who spends a lot of time on holiday and has an easy life." },
              { "key": "D", "text": "A woman who makes a lot of money by going to clubs and bars." }
            ],
            "correct": "A",
            "explanation": "'I love my job because I get to travel and I am working on projects that really excite me' -> một người phụ nữ làm việc đầy đam mê và yêu nghề."
          }
        ]
      },
      {
        "partNumber": 5,
        "title": "Part 5: Questions 26 - 35 (Điền từ vào đoạn văn)",
        "instruction": "Read the text below and choose the correct word for each space. For each question, choose the correct letter A, B, C or D.",
        "passageTitle": "Ask your pharmacist first",
        "passage": "Minor (0) illnesses have a nasty habit of striking (26) ________ the wrong time, don't they? (27) ________ you have a pile of things to do at work and even more on your plate at home, the last thing you want is a (28) ________ throat or a tension headache to drag you down. (29) ________ this summer, when you're feeling (30) ________ the weather, remember that a visit to your (31) ________ pharmacy (32) ________ be a real bonus in helping you get the right remedy to ease your symptoms. But it's not (33) ________ the medication that assists the cure - only at a pharmacy will you find expert (34) ________ from a highly trained health professional. Just try asking a supermarket shelf what it (35) ________ for family health problems!",
        "questions": [
          {
            "number": 26,
            "options": [
              { "key": "A", "text": "for" },
              { "key": "B", "text": "at" },
              { "key": "C", "text": "in" },
              { "key": "D", "text": "to" }
            ],
            "correct": "B",
            "explanation": "Cụm từ cố định 'at the wrong time' (vào thời điểm không thích hợp)."
          },
          {
            "number": 27,
            "options": [
              { "key": "A", "text": "However" },
              { "key": "B", "text": "Although" },
              { "key": "C", "text": "Despite" },
              { "key": "D", "text": "When" }
            ],
            "correct": "D",
            "explanation": "'When you have a pile of things to do...' (Khi bạn đang có cả núi việc cần giải quyết...)."
          },
          {
            "number": 28,
            "options": [
              { "key": "A", "text": "cut" },
              { "key": "B", "text": "sore" },
              { "key": "C", "text": "hurt" },
              { "key": "D", "text": "injured" }
            ],
            "correct": "B",
            "explanation": "Cụm từ y tế quen thuộc 'a sore throat' (viêm họng / đau rát họng)."
          },
          {
            "number": 29,
            "options": [
              { "key": "A", "text": "So" },
              { "key": "B", "text": "Then" },
              { "key": "C", "text": "As" },
              { "key": "D", "text": "On" }
            ],
            "correct": "A",
            "explanation": "'So this summer...' (Vì thế trong mùa hè này...)."
          },
          {
            "number": 30,
            "options": [
              { "key": "A", "text": "over" },
              { "key": "B", "text": "under" },
              { "key": "C", "text": "beneath" },
              { "key": "D", "text": "below" }
            ],
            "correct": "B",
            "explanation": "Thành ngữ tiếng Anh 'under the weather' (cảm thấy mệt mỏi, khó ở, ốm nhẹ)."
          },
          {
            "number": 31,
            "options": [
              { "key": "A", "text": "native" },
              { "key": "B", "text": "national" },
              { "key": "C", "text": "local" },
              { "key": "D", "text": "domestic" }
            ],
            "correct": "C",
            "explanation": "'local pharmacy' (hiệu thuốc địa phương / gần khu nhà bạn)."
          },
          {
            "number": 32,
            "options": [
              { "key": "A", "text": "must" },
              { "key": "B", "text": "ought" },
              { "key": "C", "text": "can" },
              { "key": "D", "text": "did" }
            ],
            "correct": "C",
            "explanation": "Động từ khuyết thiếu 'can be a real bonus' (có thể đem lại lợi ích rất lớn)."
          },
          {
            "number": 33,
            "options": [
              { "key": "A", "text": "just" },
              { "key": "B", "text": "then" },
              { "key": "C", "text": "since" },
              { "key": "D", "text": "as" }
            ],
            "correct": "A",
            "explanation": "'it's not just the medication...' (không chỉ đơn thuần là thuốc uống...)."
          },
          {
            "number": 34,
            "options": [
              { "key": "A", "text": "messages" },
              { "key": "B", "text": "preparation" },
              { "key": "C", "text": "therapy" },
              { "key": "D", "text": "advice" }
            ],
            "correct": "D",
            "explanation": "'expert advice' (lời khuyên chuyên môn từ dược sĩ)."
          },
          {
            "number": 35,
            "options": [
              { "key": "A", "text": "recommends" },
              { "key": "B", "text": "commands" },
              { "key": "C", "text": "orders" },
              { "key": "D", "text": "wants" }
            ],
            "correct": "A",
            "explanation": "'what it recommends' (kệ hàng siêu thị có thể khuyên dùng sản phẩm gì)."
          }
        ]
      }
    ]
  }
}

test_2 = {
  "id": "test_2",
  "title": "Practice Test 2",
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
            "context": "MESSAGE\nTony - the bookshop phoned to say they've got the book you ordered. They will keep it until Friday and then it will go out on the shelves.",
            "question": "What does the message say?",
            "options": [
              { "key": "A", "text": "The shop will have Tony's book by Friday." },
              { "key": "B", "text": "Tony needs to collect the book by Friday." },
              { "key": "C", "text": "The book is being delivered on Friday." }
            ],
            "correct": "B",
            "explanation": "Hiệu sách chỉ giữ cuốn sách cho Tony đến thứ Sáu, sau đó sẽ đem bán ra kệ, vì vậy Tony cần đến lấy trước thứ Sáu."
          },
          {
            "number": 2,
            "context": "CUSTOMER NOTICE\nTHE STORE WILL CLOSE AT 4 PM ON WEDNESDAY FOR A STOCK CHECK. NORMAL OPENING HOURS OF 9-5 WILL RESUME ON THURSDAY.",
            "question": "What does this notice tell customers?",
            "options": [
              { "key": "A", "text": "The store will open later than normal on Wednesday." },
              { "key": "B", "text": "The store usually closes at 4 pm." },
              { "key": "C", "text": "On Wednesday the store will close an hour earlier than usual." }
            ],
            "correct": "C",
            "explanation": "Giờ mở cửa bình thường là 9h sáng - 5h chiều, thứ Tư đóng cửa lúc 4h chiều để kiểm kê hàng -> Đóng sớm hơn 1 tiếng so với thường lệ."
          },
          {
            "number": 3,
            "context": "Please return all books by the due back date. There will be a fine for overdue books. Books may be renewed over the telephone on the condition that they have not been reserved by another borrower.",
            "question": "What does the notice explain?",
            "options": [
              { "key": "A", "text": "All books must be renewed by telephone." },
              { "key": "B", "text": "All books must be reserved by borrowers." },
              { "key": "C", "text": "Books must be returned on time." }
            ],
            "correct": "C",
            "explanation": "Sách phải được trả đúng hạn nếu không sẽ bị phạt tiền ('Books must be returned on time')."
          },
          {
            "number": 4,
            "context": "Please leave any parcels with number 24, Monday to Friday. No junk mail please.",
            "question": "What does the sign request?",
            "options": [
              { "key": "A", "text": "All post should be taken to number 24." },
              { "key": "B", "text": "Junk mail should not be posted here." },
              { "key": "C", "text": "No mail is accepted at weekends." }
            ],
            "correct": "B",
            "explanation": "'No junk mail please' -> Không được bỏ thư rác / thư quảng cáo vào đây."
          },
          {
            "number": 5,
            "context": "To: Mick\nFrom: Sharon\nRe: lecture notes\nHi Mick, can you e-mail me the history notes from Monday afternoon's lecture? I was under the weather and missed it. See you at the theatre Friday,\nSharon",
            "question": "Why did Sharon miss the lecture?",
            "options": [
              { "key": "A", "text": "Sharon was too ill to go to the lecture." },
              { "key": "B", "text": "Bad weather prevented Sharon from going to the lecture." },
              { "key": "C", "text": "Sharon went to the theatre instead of the lecture." }
            ],
            "correct": "A",
            "explanation": "'under the weather' là thành ngữ chỉ việc bị ốm/mệt mỏi, do đó Sharon bị ốm nên không thể đến lớp học."
          }
        ]
      },
      {
        "partNumber": 2,
        "title": "Part 2: Questions 6 - 10 (Ghép người với khóa học cao đẳng)",
        "instruction": "These people (6-10) all want to do a part-time course at college. Look at the eight reviews (A-H). Decide which course would be the most suitable for each person. For questions 6-10, choose the correct letter (A-H).",
        "teenagers": [
          {
            "number": 6,
            "name": "Jack",
            "demand": "Jack is eighteen. He works in a supermarket but he'd really like to get a job in a bank. He did well in his exams at school but he'd like to do a course that will help him get a better job.",
            "correct": "G",
            "explanation": "Jack muốn xin việc ở ngân hàng -> Cần khóa G: Basic Computing để thành thạo kỹ năng máy tính phục vụ công việc."
          },
          {
            "number": 7,
            "name": "Cathy",
            "demand": "Cathy is a police officer. She would like to do something relaxing that will take her mind off her work. She would enjoy doing something creative but without having to use her brain too much.",
            "correct": "D",
            "explanation": "Cathy muốn giải tỏa căng thẳng với môn học sáng tạo nhẹ nhàng -> D: Fine Art (hội họa, điêu khắc, làm gốm)."
          },
          {
            "number": 8,
            "name": "Daniel",
            "demand": "Daniel is 36 years old and works in Information Technology. He spends all day sitting at a computer and is putting on a lot of weight. He'd also like to do a course that is quite sociable in order to meet new people.",
            "correct": "B",
            "explanation": "Daniel làm IT ngồi máy tính nhiều, muốn vận động giảm cân và giao lưu bạn bè -> B: Basketball (bóng rổ, thể thao đồng đội)."
          },
          {
            "number": 9,
            "name": "Debbie",
            "demand": "Debbie is 29 years old. She is a housewife and has two young children who have just started school. She would like to work with children.",
            "correct": "E",
            "explanation": "Debbie là nội trợ có 2 con nhỏ, muốn học để đi làm việc với trẻ em -> E: Becoming a Teaching Assistant (trợ giảng trường tiểu học)."
          },
          {
            "number": 10,
            "name": "Rupert",
            "demand": "Rupert is 68 years old. He has retired but he used to be an architect. He has just bought a cottage in the countryside which he is slowly renovating because it is in bad condition. He enjoys walking and being outside in the fresh air.",
            "correct": "C",
            "explanation": "Rupert đã nghỉ hưu, có nhà ở vùng quê, thích làm việc ngoài trời thoáng mát -> C: Gardening (thiết kế và chăm sóc vườn tược)."
          }
        ],
        "places": [
          {
            "code": "A",
            "title": "Chess for beginners",
            "desc": "A great pastime for all ages. Come and exercise your mind and make new friends at the same time. Learn from an ex-British chess champion who has played against some of the great Russian players. Classes every Monday evening from 7-9 p.m. or Wednesday morning 9.30-11.30 a.m."
          },
          {
            "code": "B",
            "title": "Basketball (for men and women)",
            "desc": "Come and have a great workout as well as a lot of fun. We offer beginners and improvers classes. Experienced instructors. Join the college team and take part in weekend league competitions. Transport provided, free of charge, to games. Tues/Thurs Evening 7-9 p.m."
          },
          {
            "code": "C",
            "title": "Gardening",
            "desc": "Transform your garden into a paradise to be proud of. This course is run by two lecturers: one is a garden designer and the other is a horticulturist. Learn how to grow plants and landscape your surroundings. You will be the envy of all of your neighbours. Mon and Fri 9 a.m.-12 p.m."
          },
          {
            "code": "D",
            "title": "Fine Art",
            "desc": "This course will give you a taste of drawing, painting, sculpture and even pottery. You will be given basic guidance and then encouraged to develop your own ideas and creative skills. All materials are provided as part of the course. Tues and Friday mornings 10 a.m.-1 p.m."
          },
          {
            "code": "E",
            "title": "Becoming a Teaching Assistant",
            "desc": "Although this course doesn't lead to a formal qualification, it will prepare you for many aspects of life in the classroom. You will learn about teaching basic reading, writing and mathematics at primary level (ages 4 to 11). You will get to spend some mornings in a local primary school working alongside experienced teachers."
          },
          {
            "code": "F",
            "title": "Basic car maintenance",
            "desc": "Learn how to fix small problems on your car: checking the oil, changing a tyre, jump starting a flat battery and changing a blown bulb. You will also learn how to detect potential problems such as fan belt or brake pad issues. Make your car safer and save yourself money. Weds and Fri afternoons 3-6 p.m."
          },
          {
            "code": "G",
            "title": "Basic Computing",
            "desc": "This course starts at two levels: absolute beginners who have never used a computer, and those who want to develop their skills for home, study or work reasons. There will be a specific emphasis on using the Internet to its full potential and how to avoid problems. Monday and Wednesday evenings 7-10 p.m."
          },
          {
            "code": "H",
            "title": "Creative Writing",
            "desc": "Find the poet or novelist hidden deep inside you. You will be taught by a published poet and a published author who will offer guidelines on how to improve your writing skills and approach publishers or agents. Fairly intense course demanding home practice. Mon/Weds/Thurs afternoons 2-5 p.m."
          }
        ]
      },
      {
        "partNumber": 3,
        "title": "Part 3: Questions 11 - 20 (Đúng / Sai - True or False)",
        "instruction": "Look at the sentences below about a safety leaflet. Read the text to decide if each sentence is correct or incorrect. If it is correct, mark A (TRUE). If it is not correct, mark B (FALSE).",
        "passageTitle": "What to do if there's a fire",
        "passage": "What to do if there's a fire\n\nRaise the alarm:\n- If your smoke alarm goes off while you are asleep, don't investigate to see if there is a fire. Shout to wake everyone up, get everyone together, follow your plan and get out.\n- Check doors with the back of your hand - if they are warm, do not open them - the fire is on the other side.\n- If there is a lot of smoke, crawl along with your nose near the floor where the air will be cleaner.\n\nEscaping from a window:\n- If you are on the ground floor or first floor you may be able to escape from a window. If you have to break the window, cover the jagged glass with towels or thick bedding. Throw some more bedding out of the window to break your fall. Don't jump out of the window - lower yourself down to arm's length and drop to the ground.\n- If you have any children or elderly or disabled people with you, plan the order you will escape in so that you can help them down.\n\nDon't go back inside your home:\n- Call the Fire Brigade from a mobile phone, a neighbour's house or a phone box. Give the address of the fire. Don't stop or go back for anything.\n\nPractise your fire action plan:\n- Regularly take a few minutes to walk the escape route with everyone in your household and check that everyone can unlock and open windows and doors easily.\n- Review your plan regularly, especially if you make any changes in your home.\n- Protect yourself by fitting smoke alarms on each floor level and testing them each week.\n- Keep doors closed at night and switch off electrical appliances.\n\nWhat to do if your escape route is blocked:\n- Get everyone into one room and close the door. Put bedding or towels along the bottom of the door to seal the gap.\n- Open the window and stay near it for fresh air and to let the firefighters see you. Phone the Fire Brigade or shout for help.",
        "questions": [
          {
            "number": 11,
            "statement": "If there is a fire, leave the house and then shout.",
            "correct": "B",
            "explanation": "Hướng dẫn ghi: 'Shout to wake everyone up, get everyone together, follow your plan and get out' (Hô hoán báo động trước rồi mới cùng thoát ra ngoài)."
          },
          {
            "number": 12,
            "statement": "If the smoke alarm sounds, sit down and make an escape plan.",
            "correct": "B",
            "explanation": "Kế hoạch thoát hiểm phải được chuẩn bị từ trước, khi chuông báo cháy reo thì phải lập tức thực hiện ('follow your plan') chứ không phải ngồi lại lên kế hoạch."
          },
          {
            "number": 13,
            "statement": "You should decide what you would do before a fire starts.",
            "correct": "A",
            "explanation": "Cần chuẩn bị và diễn tập kế hoạch thoát hiểm trước khi sự cố xảy ra ('Practise your fire action plan')."
          },
          {
            "number": 14,
            "statement": "Smoke rises in a room.",
            "correct": "A",
            "explanation": "Khói bốc lên cao nên hướng dẫn khuyên 'crawl along with your nose near the floor where the air will be cleaner' (bò sát sàn nhà nơi không khí trong lành hơn)."
          },
          {
            "number": 15,
            "statement": "Jump out of a window arms first.",
            "correct": "B",
            "explanation": "Không được nhảy chúi đầu hay tay trước mà phải hạ người xuống hết sải tay rồi mới thả tiếp đất ('lower yourself down to arm's length and drop')."
          },
          {
            "number": 16,
            "statement": "You should have an alarm in each room.",
            "correct": "B",
            "explanation": "Hướng dẫn yêu cầu lắp chuông ở mỗi tầng ('on each floor level') chứ không bắt buộc mỗi phòng một cái."
          },
          {
            "number": 17,
            "statement": "Don't smoke at night in your house.",
            "correct": "B",
            "explanation": "Hướng dẫn chỉ nhắc 'Putting out cigarettes safely' (dập tắt tàn thuốc cẩn thận) chứ không cấm hút thuốc ban đêm."
          },
          {
            "number": 18,
            "statement": "Make sure that everyone is aware of the escape route.",
            "correct": "A",
            "explanation": "Cần phổ biến và diễn tập đường thoát hiểm cho tất cả thành viên trong nhà ('walk the escape route with everyone in your household')."
          },
          {
            "number": 19,
            "statement": "If you are trapped, stay by a window.",
            "correct": "A",
            "explanation": "Nếu bị kẹt trong phòng: 'Open the window and stay near it for fresh air and to let the firefighters see you'."
          },
          {
            "number": 20,
            "statement": "Never return to a burning building.",
            "correct": "A",
            "explanation": "Tuyệt đối không quay trở lại: 'Don't stop or go back for anything'."
          }
        ]
      },
      {
        "partNumber": 4,
        "title": "Part 4: Questions 21 - 25 (Đọc hiểu văn bản trắc nghiệm)",
        "instruction": "Read the text and questions below. For each question, choose the correct letter A, B, C or D.",
        "passageTitle": "Loisaba Wilderness Kenya",
        "passage": "There can be something brutal about emerging pale and tired from an overnight flight into the bright African sun. However, when you are met by a smiling, tanned pilot who whisks you through Customs and on to the runway to a waiting plane, life suddenly seems a whole lot better. When you are on a short break every hour matters so we were short-cutting the queues at Customs and heading off to the bush in time for breakfast.\n\nThe flight north from Nairobi lasts less than an hour but is a fascinating safari in itself. It took us out of the city and low over the patchwork fields and dark red roads of the Kenyan agricultural heartland until we reached Mount Kenya. Here suddenly the view changes. The pilot swooped breathtakingly low over the trees pointing out the elephants, giraffes, gazelles and even rhinos as they scattered beneath us. The tiny shadow of the plane followed us across the dry rugged land. We circled high above our final destination, Loisaba Lodge, before landing neatly on the dirt airstrip.\n\nLoisaba Wilderness is a 150 sq km, privately managed wildlife conservancy. It is larger than many of Kenya's game parks and a haven for more than 250 species of bird and 50 species of mammal - elephants, buffaloes. The wildlife here, unlike in the game parks, is still wild and so, far more exciting to see than bored lions sprawled in front of a crowd of tourists in jeeps.\n\nThe lodge perches high on a ridge. From each of the seven rooms guests can walk out onto their private terrace to marvel at the wildly dramatic view - 61,000 acres of acacia savannah and rocky outcrops lie beneath you. A thousand feet straight down the escarpment is a watering hole constantly drawing in animals for a drink; shimmering in the far distance swathed in cloud sit the darkly forested foothills of Mount Kenya. It's a view to knock you out, to savour, to return to again and again.",
        "questions": [
          {
            "number": 21,
            "question": "Why has the writer written this piece?",
            "options": [
              { "key": "A", "text": "to warn people about the dangers of a trip to Africa" },
              { "key": "B", "text": "to inform people about a short break in Africa" },
              { "key": "C", "text": "to discuss endangered species in Africa" },
              { "key": "D", "text": "to make people more aware of animal conservation" }
            ],
            "correct": "B",
            "explanation": "Tác giả chia sẻ trải nghiệm về chuyến du lịch ngắn ngày đầy ấn tượng tại Kenya."
          },
          {
            "number": 22,
            "question": "Why was the writer so pleased to be met by the pilot?",
            "options": [
              { "key": "A", "text": "Because he wanted to make the most of his time on holiday." },
              { "key": "B", "text": "Because he thought the pilot might not meet him." },
              { "key": "C", "text": "Because he expected the pilot to be unfriendly." },
              { "key": "D", "text": "Because the pilot showed him how to push up in the queue without being noticed." }
            ],
            "correct": "A",
            "explanation": "'When you are on a short break every hour matters' -> Tác giả muốn tận dụng tối đa thời gian của kỳ nghỉ ngắn ngày."
          },
          {
            "number": 23,
            "question": "What does the writer say about the flight from Nairobi?",
            "options": [
              { "key": "A", "text": "It is far too short." },
              { "key": "B", "text": "The pilot flew in a dangerous way." },
              { "key": "C", "text": "They were followed by a smaller plane." },
              { "key": "D", "text": "It offers many impressive views." }
            ],
            "correct": "D",
            "explanation": "Chuyến bay mang đến khung cảnh thiên nhiên hùng vĩ và bầy đàn động vật hoang dã nhìn từ trên cao ('fascinating safari in itself')."
          },
          {
            "number": 24,
            "question": "What does the writer suggest about Loisaba?",
            "options": [
              { "key": "A", "text": "It is still a safe and natural environment for animals." },
              { "key": "B", "text": "Tourists are spoiling it." },
              { "key": "C", "text": "Many of the animals are being hunted." },
              { "key": "D", "text": "The wild animals often attack people." }
            ],
            "correct": "A",
            "explanation": "Loisaba là khu bảo tồn thiên nhiên hoang dã lý tưởng cho hơn 250 loài chim và 50 loài động vật có vú sinh sống tự nhiên."
          },
          {
            "number": 25,
            "question": "Which of the following would be the best title for this text?",
            "options": [
              { "key": "A", "text": "Wild animals in danger" },
              { "key": "B", "text": "A taste of natural Africa" },
              { "key": "C", "text": "A day trip to the zoo" },
              { "key": "D", "text": "Tourists are taking over beautiful Africa" }
            ],
            "correct": "B",
            "explanation": "Tiêu đề phù hợp nhất là 'A taste of natural Africa' (Trải nghiệm vẻ đẹp hoang dã của châu Phi)."
          }
        ]
      },
      {
        "partNumber": 5,
        "title": "Part 5: Questions 26 - 35 (Điền từ vào đoạn văn)",
        "instruction": "Read the text below and choose the correct word for each space. For each question, choose the correct letter A, B, C or D.",
        "passageTitle": "Cabin Crew Career",
        "passage": "If you had asked Ann a few years (0) ago what she would be doing in five years' (26) ________, she wouldn't have believed you if you had suggested she would be cabin crew. Likewise, when she told her friends that she had (27) ________ for a job, most of them laughed. (28) ________, after successfully completing her four-week cabin crew training (29) ________ and embarking (30) ________ a new career, the only person laughing now is Ann! (31) ________ many cabin crew, Ann has had to make some changes in (32) ________ to meet the demands of her new career. She is expected to work at any time of the day on any day of the year, and sometimes operates up to six flights per day. The days can be long and the work tiring, but Ann is enjoying the unique and (33) ________ lifestyle that being cabin crew brings. In return for her hard work, Ann can enjoy a (34) ________ of up to £17,000. Cabin crew also have the privilege of working on some of the newest aircraft in Europe and can experience fast-track promotions. If you would like to (35) ________ in Ann's footsteps, and be considered as cabin crew at London Luton, London Gatwick or London Stansted, please visit our website for more information and to complete an online application form.",
        "questions": [
          {
            "number": 26,
            "options": [
              { "key": "A", "text": "time" },
              { "key": "B", "text": "later" },
              { "key": "C", "text": "next" },
              { "key": "D", "text": "future" }
            ],
            "correct": "A",
            "explanation": "Cụm từ 'in five years' time' (trong thời gian 5 năm tới)."
          },
          {
            "number": 27,
            "options": [
              { "key": "A", "text": "appealed" },
              { "key": "B", "text": "applied" },
              { "key": "C", "text": "assigned" },
              { "key": "D", "text": "requested" }
            ],
            "correct": "B",
            "explanation": "Cụm từ 'applied for a job' (nộp đơn xin việc làm)."
          },
          {
            "number": 28,
            "options": [
              { "key": "A", "text": "Moreover" },
              { "key": "B", "text": "Despite" },
              { "key": "C", "text": "However" },
              { "key": "D", "text": "Because" }
            ],
            "correct": "C",
            "explanation": "Từ nối thể hiện sự tương phản 'However' (Tuy nhiên)."
          },
          {
            "number": 29,
            "options": [
              { "key": "A", "text": "route" },
              { "key": "B", "text": "sequence" },
              { "key": "C", "text": "course" },
              { "key": "D", "text": "track" }
            ],
            "correct": "C",
            "explanation": "Cụm từ 'training course' (khóa học đào tạo huấn luyện)."
          },
          {
            "number": 30,
            "options": [
              { "key": "A", "text": "on" },
              { "key": "B", "text": "for" },
              { "key": "C", "text": "at" },
              { "key": "D", "text": "to" }
            ],
            "correct": "A",
            "explanation": "Cụm động từ 'embark on a new career' (bắt đầu một sự nghiệp mới)."
          },
          {
            "number": 31,
            "options": [
              { "key": "A", "text": "Like" },
              { "key": "B", "text": "With" },
              { "key": "C", "text": "Also" },
              { "key": "D", "text": "Plus" }
            ],
            "correct": "A",
            "explanation": "'Like many cabin crew...' (Cũng giống như nhiều tiếp viên hàng không khác...)."
          },
          {
            "number": 32,
            "options": [
              { "key": "A", "text": "deed" },
              { "key": "B", "text": "order" },
              { "key": "C", "text": "need" },
              { "key": "D", "text": "particular" }
            ],
            "correct": "B",
            "explanation": "Cụm từ 'in order to meet the demands' (để đáp ứng những yêu cầu)."
          },
          {
            "number": 33,
            "options": [
              { "key": "A", "text": "disturbing" },
              { "key": "B", "text": "challenging" },
              { "key": "C", "text": "reforming" },
              { "key": "D", "text": "unreliable" }
            ],
            "correct": "B",
            "explanation": "'challenging lifestyle' (lối sống đầy thử thách thú vị)."
          },
          {
            "number": 34,
            "options": [
              { "key": "A", "text": "fee" },
              { "key": "B", "text": "compensation" },
              { "key": "C", "text": "bill" },
              { "key": "D", "text": "salary" }
            ],
            "correct": "D",
            "explanation": "'salary of up to £17,000' (mức lương lên tới £17.000)."
          },
          {
            "number": 35,
            "options": [
              { "key": "A", "text": "step" },
              { "key": "B", "text": "accompany" },
              { "key": "C", "text": "chase" },
              { "key": "D", "text": "follow" }
            ],
            "correct": "D",
            "explanation": "Thành ngữ 'follow in someone's footsteps' (nối bước / theo chân ai đó)."
          }
        ]
      }
    ]
  }
}

# Now load data.js, parse window.PET_DATA, prepend test_1 and test_2 to practiceTests, and update unit_1 and unit_2
with open("data.js", "r", encoding="utf-8") as f:
    content = f.read()

# Strip "window.PET_DATA = " and parse JSON
match = re.search(r"^window\.PET_DATA\s*=\s*", content)
if not match:
    raise ValueError("Could not find window.PET_DATA assignment in data.js")

prefix = match.group(0)
json_str = content[match.end():].rstrip()
if json_str.endswith(";"):
    json_str = json_str[:-1].rstrip()

data = json.loads(json_str)

# Remove any existing test_1 or test_2 in practiceTests
data["practiceTests"] = [t for t in data["practiceTests"] if t["id"] not in ["test_1", "test_2"]]

# Prepend test_1 and test_2
data["practiceTests"].insert(0, test_2)
data["practiceTests"].insert(0, test_1)

# Update unit_1 and unit_2 in data["units"]
for u in data.get("units", []):
    if u["id"] == "unit_1":
        u["isFullDigital"] = True
        u["practiceTestId"] = "test_1"
    elif u["id"] == "unit_2":
        u["isFullDigital"] = True
        u["practiceTestId"] = "test_2"
    elif u["id"] == "unit_11":
        u["isFullDigital"] = True
        u["practiceTestId"] = "test_11"
    elif u["id"] == "unit_12":
        u["isFullDigital"] = True
        u["practiceTestId"] = "test_12"

# Write back to data.js
new_content = prefix + json.dumps(data, ensure_ascii=False, indent=2) + ";\n"

with open("data.js", "w", encoding="utf-8") as f:
    f.write(new_content)

print("SUCCESS: test_1 and test_2 successfully injected into data.js!")
