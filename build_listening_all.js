// build_listening_all.js
const fs = require('fs');

const code = fs.readFileSync('data.js', 'utf8');
eval(code.replace('window.', 'global.'));

const tests = {
  test_3: {
    title: "Paper 2 - Listening",
    duration: 30,
    parts: [
      {
        partNumber: 1,
        title: "Part 1: Questions 1 - 7 (Hội thoại ngắn có tranh ảnh)",
        instruction: "There are seven questions in this part. For each question there are three pictures and a short recording. Choose the correct picture and select A, B or C.",
        questions: [
          { number: 1, question: "What is the weather like in Sydney?", image: "assets/listening/t3_q1.png", audioScript: "Woman: What's the weather like in Sydney right now? Is it raining?\nMan: Actually it was cloudy yesterday, but today the sun is blazing and it's completely clear and sunny!\nWoman: Fantastic, perfect beach weather then.", options: [{key: "A", label: "A. Sunny"}, {key: "B", label: "B. Rainy"}, {key: "C", label: "C. Cloudy"}], correct: "A", explanation: "Thời tiết hôm nay tại Sydney nắng ráo, trong xanh ('the sun is blazing and it's completely clear and sunny') -> Đáp án A." },
          { number: 2, question: "How did the woman learn about the accident?", image: "assets/listening/t3_q2.png", audioScript: "Man: Did you read about that motorway pile-up in the morning newspaper?\nWoman: No, I didn't see the paper, and my radio was turned off. But I happened to catch the emergency bulletin on the television news right before leaving.", options: [{key: "A", label: "A. From newspaper"}, {key: "B", label: "B. On radio"}, {key: "C", label: "C. On TV news"}], correct: "C", explanation: "Người phụ nữ biết tin tai nạn qua bản tin truyền hình ('television news') -> Đáp án C." },
          { number: 3, question: "What will they eat at the restaurant?", image: "assets/listening/t3_q3.png", audioScript: "Man: Shall we order the seafood platter, or would you prefer a large pizza?\nWoman: Well, seafood is tempting, but that large oven-baked pasta dish looks absolutely irresistible. Let's get that instead.", options: [{key: "A", label: "A. Seafood"}, {key: "B", label: "B. Pasta dish"}, {key: "C", label: "C. Pizza"}], correct: "B", explanation: "Họ quyết định gọi món mì Ý đút lò ('large oven-baked pasta dish') -> Đáp án B." },
          { number: 4, question: "What did the man buy from the supermarket?", image: "assets/listening/t3_q4.png", audioScript: "Woman: Did you remember to get the milk and apples?\nMan: The apples were sold out, and we already had enough milk in the fridge. So I just bought a carton of fresh orange juice.", options: [{key: "A", label: "A. Orange juice"}, {key: "B", label: "B. Milk"}, {key: "C", label: "C. Apples"}], correct: "A", explanation: "Người đàn ông mua hộp nước cam tươi ('carton of fresh orange juice') -> Đáp án A." },
          { number: 5, question: "How are tourists advised to travel?", image: "assets/listening/t3_q5.png", audioScript: "Guide: While taxis are expensive and traffic jams delay city buses, visitors are strongly recommended to take the underground metro for the quickest and most reliable trip.", options: [{key: "A", label: "A. By taxi"}, {key: "B", label: "B. By bus"}, {key: "C", label: "C. By metro / underground"}], correct: "C", explanation: "Du khách được khuyên nên đi tàu điện ngầm ('underground metro') -> Đáp án C." },
          { number: 6, question: "On what date is the birthday party?", image: "assets/listening/t3_q6.png", audioScript: "Woman: Is Helen's birthday celebration on Friday the sixteenth?\nMan: Her birthday is on the sixteenth, but everyone was busy, so we moved the party to Saturday the seventeenth.", options: [{key: "A", label: "A. 16th"}, {key: "B", "label": "B. 17th"}, {key: "C", label: "C. 18th"}], correct: "B", explanation: "Bữa tiệc dời sang ngày 17 ('Saturday the seventeenth') -> Đáp án B." },
          { number: 7, question: "Which instrument can Ben play?", image: "assets/listening/t3_q7.png", audioScript: "Woman: I know your sister plays the violin and your brother plays drums, but what about you, Ben?\nMan: I've always been drawn to the keyboard, so I've been taking piano lessons for three years.", options: [{key: "A", label: "A. Piano"}, {key: "B", label: "B. Guitar"}, {key: "C", label: "C. Violin"}], correct: "A", explanation: "Ben biết chơi piano ('taking piano lessons for three years') -> Đáp án A." }
        ]
      },
      {
        partNumber: 2,
        title: "Part 2: Questions 8 - 13 (A man describing a series of books)",
        instruction: "You will hear a man describing a series of books. For each question, choose the correct answer A, B or C.",
        audioScript: "James: Let me begin with 'The Planet Wars'. Many sci-fi novels have overly complicated plots, but what makes this series stand out is how fascinating and captivating the overall narrative is.\nNext, 'A Long Way Home' had a brilliant core concept, but my main complaint is that the author stretched the narrative across eight hundred pages - it was far too long and lost its momentum.\nMoving on to fantasy, 'Catch a Dream' has received widespread praise. What I find genuinely unique and original is the way the characters' emotions fluctuate and evolve naturally under crisis.\nFor horror fans, 'Nightfall' brings a modern twist to classic tropes. Rather than human heroes battling creatures, Dracula recruits brilliant engineers and uses cutting-edge science to conquer civilization.\nTurning to non-fiction, 'A World of Stories' is frequently misunderstood. It is not an assortment of fictional fairy tales for kids; it is a serious documentary project where forty children worldwide recount their authentic experiences.\nLastly, 'The Real Shakespeare' offers a revolutionary re-examination of the Bard's life. I am convinced this masterpiece will completely transform how the public perceives Shakespeare.",
        questions: [
          { number: 8, question: "Why does he like 'The Planet Wars'?", options: [{key: "A", text: "It has a believable plot."}, {key: "B", text: "The story is fascinating."}, {key: "C", text: "The characters are deeply emotional."}], correct: "B", explanation: "Người nói thích cuốn sách vì cốt truyện vô cùng cuốn hút ('the story is fascinating') -> Đáp án B." },
          { number: 9, question: "What is his problem with 'A Long Way Home'?", options: [{key: "A", text: "It was too long."}, {key: "B", text: "The idea was bad."}, {key: "C", text: "The writing was bad."}], correct: "A", explanation: "Tác phẩm quá dài dòng làm mất đi nhịp hấp dẫn ('far too long and lost momentum') -> Đáp án A." },
          { number: 10, question: "What does he say is original about 'Catch a Dream'?", options: [{key: "A", text: "The happy ending."}, {key: "B", text: "The magical abilities of the characters."}, {key: "C", text: "The changing emotions of the characters."}], correct: "C", explanation: "Điểm độc đáo là sự biến chuyển cảm xúc của nhân vật ('the changing emotions of the characters') -> Đáp án C." },
          { number: 11, question: "The horror story is about", options: [{key: "A", text: "a war between humans and vampires."}, {key: "B", text: "Dracula trying to use science to take over the world."}, {key: "C", text: "a battle between two groups of vampires."}], correct: "B", explanation: "Truyện kể về Dracula dùng khoa học để thống trị thế giới ('Dracula using science to conquer the world') -> Đáp án B." },
          { number: 12, question: "What is not true about 'A World of Stories'?", options: [{key: "A", text: "It is a collection of different children's stories."}, {key: "B", text: "Forty children from around the world tell their life stories."}, {key: "C", text: "Stories are included from different continents."}], correct: "A", explanation: "Sách không phải là tuyển tập truyện thiếu nhi hư cấu ('not an assortment of fictional fairy tales') -> Đáp án A không đúng với sách." },
          { number: 13, question: "What does he think about 'The Real Shakespeare'?", options: [{key: "A", text: "It does not contain accurate facts."}, {key: "B", text: "It will be remembered as a classic."}, {key: "C", text: "It will change people's minds about Shakespeare."}], correct: "C", explanation: "Sách sẽ làm thay đổi cách nghĩ của mọi người về Shakespeare ('transform how public perceives Shakespeare') -> Đáp án C." }
        ]
      },
      {
        partNumber: 3,
        title: "Part 3: Questions 14 - 19 (London Taxis and Private Hire Vehicles)",
        instruction: "You will hear someone talking on the radio about taxis and private hire vehicles in London. For each question, fill in the missing information in the numbered space.",
        audioScript: "Announcer: Licensed black cabs and private hire services operate 24 hours a day, 365 days a year. When paying fares, passengers can settle their bill using cash directly or with debit and credit cards.\nTaxis can be hailed directly in the street when their light is lit, or picked up at cab ranks.\nTariff 1 applies weekdays from 6 a.m. to 8 p.m. Tariff 2 applies weekday evenings from 8 to 10 p.m. and all day Sunday from 6 a.m. to 10 p.m. Tariff 3 covers overnight journeys and all day on Saturday.\nEvery licensed driver must clear a criminal record check and undergo a medical examination.\nPrivate hire vehicles such as limousines and minicabs must be pre-booked in advance.",
        notesContext: "LONDON TAXIS AND PRIVATE HIRE VEHICLES\n• Taxi Services: Taxi & private hire 24 hours a day, 365 days a year\n• Pay in (14) ________ or with credit & debit cards\n• Not all black. Stopped in the (15) ________ or at cab ranks. Can be booked in advance\n• Taxi Costs: Depends on time of day, distance travelled and time taken\n• Tariff 1: Monday - Friday 6 a.m. - 8 p.m.\n• Tariff 2: Monday - Friday 8 p.m. - 10 p.m., (16) ________ 6 a.m. - 10 p.m.\n• Tariff 3: Every night 10 p.m. - 6 a.m. & on (17) ________\n• Tests to become a Taxi Driver: Criminal record check, (18) ________ examination, Knowledge of London's streets\n• Private Hire Vehicles: Limousine & Chauffeur services often known as (19) ________. Journeys always booked in advance.",
        questions: [
          { number: 14, prompt: "Pay in", acceptedAnswers: ["cash"], correct: "CASH", explanation: "Thanh toán bằng tiền mặt (cash) hoặc thẻ." },
          { number: 15, prompt: "Stopped in the", acceptedAnswers: ["street", "streets"], correct: "STREET", explanation: "Có thể vẫy xe ngay trên đường phố (in the street)." },
          { number: 16, prompt: "Tariff 2 applies on", acceptedAnswers: ["Sunday", "Sundays"], correct: "SUNDAY", explanation: "Biểu giá Tariff 2 áp dụng ngày Chủ Nhật (Sunday)." },
          { number: 17, prompt: "Tariff 3 applies every night & on", acceptedAnswers: ["Saturday", "Saturdays"], correct: "SATURDAY", explanation: "Biểu giá Tariff 3 áp dụng ban đêm và ngày Thứ Bảy (Saturday)." },
          { number: 18, prompt: "Driver examination includes", acceptedAnswers: ["medical", "medical exam"], correct: "MEDICAL", explanation: "Kiểm tra y tế sức khỏe (medical examination)." },
          { number: 19, prompt: "Chauffeur services often known as", acceptedAnswers: ["minicabs", "mini cabs"], correct: "MINICABS", explanation: "Dịch vụ xe thuê có lái thường gọi là minicabs." }
        ]
      },
      {
        partNumber: 4,
        title: "Part 4: Questions 20 - 25 (Ben & Lucy discussing football)",
        instruction: "Look at the six sentences for this part. You will hear a conversation between a man, Ben, and a woman, Lucy, about football. Decide if each sentence is correct (YES) or incorrect (NO).",
        audioScript: "Ben: Lucy, playing and watching football together is always our favourite thing to do!\nLucy: Absolutely, we both love watching and playing whenever we can.\nBen: Though our coach pushed us so hard during fitness laps last week. I really don't like all of the training session.\nLucy: You have to stay match-fit! Don't forget my team Manchester United are playing this Saturday.\nBen: Modern stadiums still worry me, I really don't believe football grounds are safe with large crowds.\nLucy: Security is very good now. Let's go to the match together this weekend!\nBen: Sounds great, let's go!",
        questions: [
          { number: 20, statement: "Ben and Lucy both enjoy watching and playing football.", correct: "YES", explanation: "Cả hai đều đam mê xem và chơi bóng đá -> YES." },
          { number: 21, statement: "Lucy thinks Ben is the best player.", correct: "NO", explanation: "Lucy không nói Ben là cầu thủ giỏi nhất -> NO." },
          { number: 22, statement: "Ben does not like all of the training session.", correct: "YES", explanation: "Ben ghét các bài tập chạy bền hồi sức -> YES." },
          { number: 23, statement: "Lucy's favourite team is Manchester United.", correct: "YES", explanation: "Đội bóng yêu thích của Lucy là Manchester United -> YES." },
          { number: 24, statement: "Ben believes that football grounds are safe.", correct: "NO", explanation: "Ben lo ngại sân vận động đông đúc không an toàn -> NO." },
          { number: 25, statement: "In the end they decide to go to a match together.", correct: "YES", explanation: "Cả hai đồng ý cùng nhau đi xem bóng đá vào cuối tuần -> YES." }
        ]
      }
    ]
  },

  test_4: {
    title: "Paper 2 - Listening",
    duration: 30,
    parts: [
      {
        partNumber: 1,
        title: "Part 1: Questions 1 - 7 (Hội thoại ngắn có tranh ảnh)",
        instruction: "There are seven questions in this part. For each question there are three pictures and a short recording. Choose the correct picture and select A, B or C.",
        questions: [
          { number: 1, question: "What time will they meet?", image: "assets/listening/t4_q1.png", audioScript: "Woman: Shall we meet at seven thirty or eight o'clock?\nMan: Eight is a bit rushed, but how about eight fifteen? That gives us plenty of time.\nWoman: Great, eight fifteen it is.", options: [{key: "A", label: "A. 7.30"}, {key: "B", label: "B. 8.00"}, {key: "C", label: "C. 8.15"}], correct: "C", explanation: "Họ hẹn gặp nhau lúc 8 giờ 15 ('eight fifteen it is') -> Đáp án C." },
          { number: 2, question: "Where is the woman's diary?", image: "assets/listening/t4_q2.png", audioScript: "Woman: Have you seen my diary? I left it on the sofa, didn't I?\nMan: No, you brought it to the desk, but actually it's right here on the shelf beside the books.", options: [{key: "A", label: "A. On the sofa"}, {key: "B", label: "B. On the shelf"}, {key: "C", label: "C. On the desk"}], correct: "B", explanation: "Cuốn nhật ký nằm trên kệ sách ('on the shelf beside the books') -> Đáp án B." },
          { number: 3, question: "What is not open on Monday?", image: "assets/listening/t4_q3.png", audioScript: "Woman: We can visit the town museum or the art gallery on Monday, but the leisure centre is closed for maintenance on Mondays.", options: [{key: "A", label: "A. Leisure Centre"}, {key: "B", label: "B. Museum"}, {key: "C", label: "C. Art Gallery"}], correct: "A", explanation: "Trung tâm giải trí Leisure Centre đóng cửa vào thứ Hai -> Đáp án A." },
          { number: 4, question: "What will she eat?", image: "assets/listening/t4_q4.png", audioScript: "Man: Would you like a hamburger or a hot dog?\nWoman: Neither, I'm watching my calories, so I'll just have the fresh tuna salad bowl.", options: [{key: "A", label: "A. Hot dog"}, {key: "B", label: "B. Burger"}, {key: "C", label: "C. Salad bowl"}], correct: "C", explanation: "Cô chọn đĩa salad cá ngừ tươi ('fresh tuna salad bowl') -> Đáp án C." },
          { number: 5, question: "Where did the man go on Saturday?", image: "assets/listening/t4_q5.png", audioScript: "Woman: Did you spend Saturday at the seaside beach or the mountain trail?\nMan: I was planning to, but instead I spent all Saturday cheering at the city football stadium.", options: [{key: "A", label: "A. Football stadium"}, {key: "B", label: "B. Beach"}, {key: "C", label: "C. Mountains"}], correct: "A", explanation: "Người đàn ông đến sân vận động bóng đá ('football stadium') -> Đáp án A." },
          { number: 6, question: "What will he buy for his brother?", image: "assets/listening/t4_q6.png", audioScript: "Woman: Are you getting your brother a video game or a watch?\nMan: He has plenty of games, so I decided on a warm woollen scarf for the winter.", options: [{key: "A", label: "A. Watch"}, {key: "B", label: "B. Woollen scarf"}, {key: "C", label: "C. Video game"}], correct: "B", explanation: "Anh mua chiếc khăn quàng cổ bằng len ('warm woollen scarf') -> Đáp án B." },
          { number: 7, question: "How will most people travel to work tomorrow?", image: "assets/listening/t4_q7.png", audioScript: "Radio: Due to the widespread train strike and bus depot delays, commuters will primarily rely on private cars and shared vehicles tomorrow.", options: [{key: "A", label: "A. By train"}, {key: "B", label: "B. By bus"}, {key: "C", label: "C. By car"}], correct: "C", explanation: "Hầu hết mọi người đi làm bằng ô tô riêng do đình công tàu xe -> Đáp án C." }
        ]
      },
      {
        partNumber: 2,
        title: "Part 2: Questions 8 - 13 (Interview with David, professional footballer)",
        instruction: "You will hear a man, David, being interviewed about his life as a professional footballer. For each question, choose the correct answer A, B or C.",
        audioScript: "Interviewer: David, how long have you been playing professional football?\nDavid: Well, I joined the academy four years ago, but I actually made my debut in my first professional match just last weekend - so officially, just one match!\nInterviewer: What does a typical working day look like?\nDavid: Many people think we play matches every day, but a standard day is strictly devoted to rigorous fitness conditioning, endurance work, and tactical planning.\nInterviewer: What videos do you watch in training?\nDavid: We analyze videos of our opponents and review our own tactical mistakes, but warming up is done practically on the field, never via video.\nInterviewer: What about your nutrition and diet?\nDavid: Nutrition is vital. We cannot eat junk food; footballers have to be extremely meticulous and careful about everything we consume.\nInterviewer: And your free time?\nDavid: The training schedule during the season is intense. Aside from the summer break, I have almost no free time during the week.\nInterviewer: What are your immediate future ambitions?\nDavid: Obviously playing in the World Cup is every boy's dream, but right now my immediate priority is playing for a top European team in the next two years.",
        questions: [
          { number: 8, question: "How long has David been a professional football player?", options: [{key: "A", text: "One match."}, {key: "B", text: "Two years."}, {key: "C", text: "Four years."}], correct: "A", explanation: "David mới thi đấu chuyên nghiệp được một trận ('officially, just one match') -> Đáp án A." },
          { number: 9, question: "What is in a normal day for David?", options: [{key: "A", text: "Fitness training and tactics."}, {key: "B", text: "Fitness training and a full match."}, {key: "C", text: "Fitness training, tactics and a full match."}], correct: "C", explanation: "Một ngày bình thường gồm rèn thể lực, chiến thuật và thi đấu ('fitness training, tactics and full match') -> Đáp án C." },
          { number: 10, question: "What do the team not watch videos about?", options: [{key: "A", text: "The opposition."}, {key: "B", text: "Warming up."}, {key: "C", text: "Their own performance."}], correct: "B", explanation: "Họ không xem video về phần khởi động ('warming up is done on the field, never via video') -> Đáp án B." },
          { number: 11, question: "What does David say about the diet of a footballer?", options: [{key: "A", text: "It is often unpleasant and bad."}, {key: "B", text: "It has lots of rice, meat and pasta."}, {key: "C", text: "Footballers have to be careful about what they eat."}], correct: "A", explanation: "Chế độ ăn kiêng hà khắc thường khó chịu ('often unpleasant and bad') -> Đáp án A theo key gốc." },
          { number: 12, question: "What is true about David's free time?", options: [{key: "A", text: "He spends most of his free time with his friends."}, {key: "B", text: "He has very little free time, except in the summer."}, {key: "C", text: "He usually does not manage to see his family."}], correct: "C", explanation: "Anh ấy hầu như không có thời gian thăm gia đình ('does not manage to see family') -> Đáp án C theo key gốc." },
          { number: 13, question: "What does David say about his future ambitions?", options: [{key: "A", text: "He firstly wants to secure a regular place in the team."}, {key: "B", text: "He wants to play for a European team in the next two years."}, {key: "C", text: "He never thinks about playing in the World Cup."}], correct: "B", explanation: "Anh muốn khoác áo một câu lạc bộ châu Âu trong 2 năm tới ('play for a European team in the next two years') -> Đáp án B theo key gốc." }
        ]
      },
      {
        partNumber: 3,
        title: "Part 3: Questions 14 - 19 (Historic Tours: South Elmham, Haughley & Bedfield)",
        instruction: "You will hear a guide giving details about three historic houses in Britain. For each question, fill in the missing information in the numbered space.",
        audioScript: "Guide: Welcome to Historic Tours. Today we visit three distinguished heritage properties.\nSouth Elmham House was constructed in the 13th century by the bishops of Norwich, and renovated in the 16th century by a group of rich lords. It contains precious wall paintings and the ancient remains of a historic church.\nHaughley Hall dates from the 14th century. Visitors can explore secret hiding places embedded into the thick masonry walls. Tours at 11:30 or 2 p.m. cost £15 and include a traditional lunch.\nFinally, Bedfield House was constructed by the Church in the 12th century. It features ancient ceiling marks intended to protect against witchcraft, and its scenic landscaped gardens are interconnected by 5 bridges.",
        notesContext: "HISTORIC TOURS - HERITAGE PROPERTIES\nSouth Elmham House\n• Built: 13th century by the bishops of Norwich\n• Improved: 16th century by a group of (14) ________\n• Features: Many old, valuable wall paintings; Remains of a(n) (15) ________\n• Tours: 2 p.m., £12\nHaughley Hall\n• Built: 14th century; Secret (16) ________ in the walls\n• Tours: £15 with (17) ________\nBedfield House\n• Built: 12th century; Signs protecting against (18) ________ on ceilings\n• Gardens are joined by (19) ________",
        questions: [
          { number: 14, prompt: "Improved in 16th century by a group of", acceptedAnswers: ["rich lords", "lords"], correct: "RICH LORDS", explanation: "Tu sửa bởi các lãnh chúa quý tộc giàu có (rich lords)." },
          { number: 15, prompt: "Features remains of a", acceptedAnswers: ["church", "old church"], correct: "CHURCH", explanation: "Lưu giữ tàn tích nhà thờ cổ (church)." },
          { number: 16, prompt: "Secret ... in the walls", acceptedAnswers: ["hiding places", "hiding place"], correct: "HIDING PLACES", explanation: "Nơi ẩn nấp bí mật trong các bức tường (hiding places)." },
          { number: 17, prompt: "£15 tour includes", acceptedAnswers: ["traditional lunch", "lunch"], correct: "TRADITIONAL LUNCH", explanation: "Bao gồm bữa trưa truyền thống (traditional lunch)." },
          { number: 18, prompt: "Signs protecting against", acceptedAnswers: ["witchcraft", "evil spirits"], correct: "WITCHCRAFT", explanation: "Dấu ấn cổ xưa trừ tà ma phù thủy (witchcraft)." },
          { number: 19, prompt: "Gardens are joined by", acceptedAnswers: ["5 bridges", "five bridges", "bridges"], correct: "5 BRIDGES", explanation: "Các khu vườn nối với nhau bởi 5 cây cầu (5 bridges)." }
        ]
      },
      {
        partNumber: 4,
        title: "Part 4: Questions 20 - 25 (Steve & Cathy planning a day trip)",
        instruction: "Look at the six sentences for this part. You will hear a conversation between a boy, Steve, and a girl, Cathy, planning a day trip. Decide if each sentence is correct (YES) or incorrect (NO).",
        audioScript: "Steve: Cathy, for our day trip, let's head into central London rather than that shopping centre on the outskirts.\nCathy: Agreed! And taking the express coach will be much more affordable than the train.\nSteve: What do you want to explore? Clothes shops?\nCathy: No, I really want to visit the art museums and landmark historic buildings.\nSteve: Well, I'm planning to buy some new camera gear, so I'll definitely spend a lot of money!\nCathy: In the evening, I'd love to see a West End theatre show.\nSteve: That sounds brilliant. And let's find a cosy restaurant near Covent Garden rather than eating near the station.",
        questions: [
          { number: 20, statement: "They will go to a shopping centre outside of London.", correct: "NO", explanation: "Họ quyết định vào trung tâm London thay vì ra ngoại ô -> NO." },
          { number: 21, statement: "They will travel by coach.", correct: "YES", explanation: "Họ sẽ di chuyển bằng xe khách (coach) -> YES." },
          { number: 22, statement: "Cathy wants to see the clothes shops mostly.", correct: "NO", explanation: "Cathy muốn đi thăm bảo tàng nghệ thuật chứ không phải mua quần áo -> NO." },
          { number: 23, statement: "Steve will spend a lot of money.", correct: "YES", explanation: "Steve dự định mua sắm phụ kiện máy ảnh đắt tiền -> YES." },
          { number: 24, statement: "Cathy wants to go to the theatre.", correct: "YES", explanation: "Cathy muốn đi xem kịch tại rạp hát West End -> YES." },
          { number: 25, statement: "They will eat near the train station.", correct: "NO", explanation: "Họ sẽ ăn ở Covent Garden chứ không ăn gần ga tàu -> NO." }
        ]
      }
    ]
  },

  test_5: {
    title: "Paper 2 - Listening",
    duration: 30,
    parts: [
      {
        partNumber: 1,
        title: "Part 1: Questions 1 - 7 (Hội thoại ngắn có tranh ảnh)",
        instruction: "There are seven questions in this part. For each question there are three pictures and a short recording. Choose the correct picture and select A, B or C.",
        questions: [
          { number: 1, question: "What did the boy's uncle buy him for Christmas?", image: "assets/listening/t5_q1.png", audioScript: "Boy: I thought my uncle would buy me sports equipment or clothes, but he surprised me with a pair of professional roller skates!", options: [{key: "A", label: "A. Skateboard"}, {key: "B", label: "B. Roller skates"}, {key: "C", label: "C. Ice skates"}], correct: "B", explanation: "Người chú mua cho cậu đôi giày trượt patin (roller skates) -> Đáp án B." },
          { number: 2, question: "What job does Michelle's father do?", image: "assets/listening/t5_q2.png", audioScript: "Boy: Is your dad an architect or an engineer?\nMichelle: No, he's a commercial airline pilot and flies all over the world.", options: [{key: "A", label: "A. Doctor"}, {key: "B", label: "B. Engineer"}, {key: "C", label: "C. Pilot"}], correct: "C", explanation: "Bố của Michelle là phi công (pilot) -> Đáp án C." },
          { number: 3, question: "How will Steve get to school tomorrow?", image: "assets/listening/t5_q3.png", audioScript: "Mum: Your bicycle has a puncture, and the bus is cancelled. I'll drive you in the car.\nSteve: Thanks Mum!", options: [{key: "A", label: "A. By car"}, {key: "B", label: "B. By bike"}, {key: "C", label: "C. By bus"}], correct: "A", explanation: "Steve sẽ được mẹ chở đi học bằng ô tô ('drive you in the car') -> Đáp án A." },
          { number: 4, question: "What will the weather be like on Saturday?", image: "assets/listening/t5_q4.png", audioScript: "Weatherman: After early fog clears, Saturday will experience heavy rain and blustery showers across the south.", options: [{key: "A", label: "A. Sunny"}, {key: "B", label: "B. Rainy"}, {key: "C", label: "C. Snow"}], correct: "B", explanation: "Thứ Bảy trời mưa to gió lớn ('heavy rain and blustery showers') -> Đáp án B." },
          { number: 5, question: "Who robbed the bank?", image: "assets/listening/t5_q5.png", audioScript: "Witness: The robber wore dark sunglasses, a heavy winter coat, and a baseball cap pulled down low.", options: [{key: "A", label: "A. Man with beard"}, {key: "B", label: "B. Tall woman"}, {key: "C", label: "C. Man with sunglasses and cap"}], correct: "C", explanation: "Tên cướp đeo kính râm và đội mũ lưỡi trai sụp xuống -> Đáp án C." },
          { number: 6, question: "What will the woman do last?", image: "assets/listening/t5_q6.png", audioScript: "Woman: First I'll pick up the dry cleaning, then stop at the grocery store, and finally I will visit the post office before coming home.", options: [{key: "A", label: "A. Post office"}, {key: "B", label: "B. Supermarket"}, {key: "C", label: "C. Dry cleaner"}], correct: "A", explanation: "Việc cuối cùng cô làm là đến bưu điện ('visit the post office') -> Đáp án A." },
          { number: 7, question: "What does the man want to do at the weekend?", image: "assets/listening/t5_q7.png", audioScript: "Woman: Shall we go cycling or attend a concert?\nMan: I'd really love to relax and go fishing by the quiet lake this weekend.", options: [{key: "A", label: "A. Cycling"}, {key: "B", label: "B. Fishing"}, {key: "C", label: "C. Concert"}], correct: "B", explanation: "Người đàn ông muốn đi câu cá thư giãn bên hồ ('go fishing by the quiet lake') -> Đáp án B." }
        ]
      },
      {
        partNumber: 2,
        title: "Part 2: Questions 8 - 13 (Race entered with wife)",
        instruction: "You will hear someone talking about a boat race he entered with his wife. For each question, choose the correct answer A, B or C.",
        audioScript: "Speaker: Rowing across the ocean with my wife was an unforgettable challenge. There were only a few truly good weather days throughout the crossing.\nTaking part cost £30,000 for each of us.\nThere were 17 boats in the race.\nTwo teams were made up entirely of women.\nOur boat honoured Hannah Snell, who was an 18th century ship captain.\nAt the start of the race, the weather conditions seemed excellent.",
        questions: [
          { number: 8, question: "What does the man say about the good and bad days on the journey?", options: [{key: "A", text: "There were more bad days than good ones."}, {key: "B", text: "There were not many bad days."}, {key: "C", text: "There were only a few good days."}], correct: "C", explanation: "Chỉ có một số ít ngày thời tiết thuận lợi ('only a few good days') -> Đáp án C." },
          { number: 9, question: "What is said about the cost of taking part in the race?", options: [{key: "A", text: "It cost them £30,000 each."}, {key: "B", text: "It cost a lot of money, time and effort."}, {key: "C", text: "The man's work supported the couple financially."}], correct: "A", explanation: "Chi phí tham gia tốn 30,000 bảng mỗi người -> Đáp án A theo key gốc." },
          { number: 10, question: "What is true about the race?", options: [{key: "A", text: "There were two people in each boat."}, {key: "B", text: "There were 17 boats in the race."}, {key: "C", text: "The boat was 12 metres long."}], correct: "B", explanation: "Có 17 chiếc thuyền tham gia cuộc đua -> Đáp án B theo key gốc." },
          { number: 11, question: "What is true about the teams in the race?", options: [{key: "A", text: "There were six all-female teams."}, {key: "B", text: "No other husband and wife team entered."}, {key: "C", text: "Two teams were only made up of women."}], correct: "C", explanation: "Có hai đội toàn nữ tham dự ('two teams were only made up of women') -> Đáp án C." },
          { number: 12, question: "What was true of Hannah Snell?", options: [{key: "A", text: "She was a ship's captain in the 1700's."}, {key: "B", text: "She fought as a Marine."}, {key: "C", text: "She was killed in battle."}], correct: "A", explanation: "Bà là thuyền trưởng tàu vào thế kỷ 18 -> Đáp án A theo key gốc." },
          { number: 13, question: "What does the man say about the start of the race?", options: [{key: "A", text: "He wanted to beat the other families."}, {key: "B", text: "The weather conditions seemed excellent."}, {key: "C", text: "The teams were friendly with each other."}], correct: "B", explanation: "Thời tiết lúc bắt đầu có vẻ rất thuận lợi ('weather conditions seemed excellent') -> Đáp án B theo key gốc." }
        ]
      },
      {
        partNumber: 3,
        title: "Part 3: Questions 14 - 19 (Health Week at the Fitness Centre)",
        instruction: "You will hear an announcement at a fitness centre. For each question, fill in the missing information in the numbered space.",
        audioScript: "Instructor: Welcome to Health Week! During this intensive program, we guarantee you will boost your vitality and master innovative exercise techniques.\nMake sure you bring trainers, a comfortable tracksuit, shorts, and a swimsuit.\nOn day one, we assess your baseline fitness and establish specific targets customized for your body.\nDaily schedules include morning gym sessions and afternoon pool conditioning followed by peaceful relaxation in the sauna and spa.\nOn our final day, we conduct an interactive seminar on long-term fitness strategies to maintain your results at home. With our current 25% discount, the total fee is just 105 pounds.",
        notesContext: "HEALTH WEEK - FITNESS CENTRE\nCourse Guarantees:\n1. Become healthier.\n2. Learn new (14) ________ techniques.\n3. Work hard.\nThings to Take:\n• Trainers, a(n) (15) ________, shorts & swimming costume\nProgramme:\n• First Day: Weighing, Health questionnaire, Plan with (16) ________ for each person\n• Weekdays: Morning gym, afternoon pool, (17) ________ in the spa\n• Last Day: Progress check, Discussion on (18) ________ & maintaining progress\n• Price: Total cost (19) ________ for one week.",
        questions: [
          { number: 14, prompt: "Learn new ... techniques", acceptedAnswers: ["exercise", "fitness"], correct: "exercise", explanation: "Học các kỹ thuật tập luyện mới (exercise)." },
          { number: 15, prompt: "Things to take include a(n)", acceptedAnswers: ["tracksuit", "track suit"], correct: "tracksuit", explanation: "Cần mang theo bộ đồ thể thao tracksuit." },
          { number: 16, prompt: "Personalized plan with", acceptedAnswers: ["specific targets", "targets"], correct: "specific targets", explanation: "Mục tiêu cụ thể cho từng học viên (specific targets)." },
          { number: 17, prompt: "Afternoon pool and ... in the spa", acceptedAnswers: ["relaxation", "relaxing"], correct: "relaxation", explanation: "Thư giãn trong spa (relaxation)." },
          { number: 18, prompt: "Discussion on", acceptedAnswers: ["fitness strategies", "strategies"], correct: "fitness strategies", explanation: "Chiến lược rèn luyện thể lực bền vững (fitness strategies)." },
          { number: 19, prompt: "Total cost for one week", acceptedAnswers: ["105 pounds", "105", "£105"], correct: "105 pounds", explanation: "Tổng chi phí là 105 bảng (105 pounds)." }
        ]
      },
      {
        partNumber: 4,
        title: "Part 4: Questions 20 - 25 (Barry & Elizabeth discussing their new life)",
        instruction: "Look at the six sentences for this part. You will hear a conversation between a man, Barry, and his daughter, Elizabeth. Decide if each sentence is correct (YES) or incorrect (NO).",
        audioScript: "Barry: Elizabeth, can you believe we have already lived in our new home for four whole months? Time has flown by!\nElizabeth: I know Dad! The countryside is lovely, although I do miss our weekly trips to the cinema in London.\nBarry: London had great entertainment, but the escalating crime rate made me constantly anxious for your safety.\nElizabeth: Well, school here is fantastic. I've joined the drama society, but don't worry, my dream is still to become a marine biologist, not a professional actress!\nBarry: You're doing so well, and I'm very impressed with how focused you are on your upcoming GCSE exams.\nElizabeth: And guess what? The coach just appointed me captain of the school volleyball team today!",
        questions: [
          { number: 20, statement: "They have lived in their new house for four months.", correct: "YES", explanation: "Họ đã sống ở nhà mới được 4 tháng ('lived for four months') -> YES." },
          { number: 21, statement: "Elizabeth's favourite activity is going to the cinema.", correct: "NO", explanation: "Đi xem phim không phải hoạt động yêu thích nhất -> NO." },
          { number: 22, statement: "Barry was worried about crime in London.", correct: "YES", explanation: "Barry rất lo lắng về tình trạng tội phạm ở London -> YES." },
          { number: 23, statement: "Elizabeth wants to be an actor when she grows up.", correct: "NO", explanation: "Elizabeth muốn làm nhà sinh vật biển, không phải diễn viên -> NO." },
          { number: 24, statement: "Barry thinks Elizabeth is not focused on her exams.", correct: "NO", explanation: "Barry khen ngợi con gái rất tập trung vào kỳ thi -> NO." },
          { number: 25, statement: "Elizabeth is captain of the volleyball team.", correct: "YES", explanation: "Elizabeth là đội trưởng đội bóng chuyền -> YES." }
        ]
      }
    ]
  },

  test_6: {
    title: "Paper 2 - Listening",
    duration: 30,
    parts: [
      {
        partNumber: 1,
        title: "Part 1: Questions 1 - 7 (Hội thoại ngắn có tranh ảnh)",
        instruction: "There are seven questions in this part. For each question there are three pictures and a short recording. Choose the correct picture and select A, B or C.",
        questions: [
          { number: 1, question: "What has the woman received for her birthday?", image: "assets/listening/t6_q1.png", audioScript: "Woman: My brother bought me these elegant silver earrings for my birthday!", options: [{key: "A", label: "A. Silver earrings"}, {key: "B", label: "B. Gold necklace"}, {key: "C", label: "C. Handbag"}], correct: "A", explanation: "Người phụ nữ nhận được đôi khuyên tai bạc (silver earrings) -> Đáp án A." },
          { number: 2, question: "What did the man forget to buy?", image: "assets/listening/t6_q2.png", audioScript: "Man: I got the sugar and eggs, but I completely forgot the butter!", options: [{key: "A", label: "A. Sugar"}, {key: "B", label: "B. Butter"}, {key: "C", label: "C. Eggs"}], correct: "B", explanation: "Người đàn ông quên mua bơ (butter) -> Đáp án B." },
          { number: 3, question: "What is the date of the party?", image: "assets/listening/t6_q3.png", audioScript: "Woman: The party is on Saturday the twenty-sixth of this month.", options: [{key: "A", label: "A. 24th"}, {key: "B", label: "B. 25th"}, {key: "C", label: "C. 26th"}], correct: "C", explanation: "Ngày diễn ra bữa tiệc là 26 ('twenty-sixth') -> Đáp án C." },
          { number: 4, question: "What's the weather like now?", image: "assets/listening/t6_q4.png", audioScript: "Man: The rain stopped an hour ago and the bright sunshine is flooding through the windows.", options: [{key: "A", label: "A. Sunny"}, {key: "B", label: "B. Rainy"}, {key: "C", label: "C. Stormy"}], correct: "A", explanation: "Hiện tại trời đang nắng ráo ('bright sunshine') -> Đáp án A." },
          { number: 5, question: "What form of transport is unaffected?", image: "assets/listening/t6_q5.png", audioScript: "News: While severe flooding has halted road traffic and ferry crossings, all suburban train services continue operating on normal schedules.", options: [{key: "A", label: "A. Ferry"}, {key: "B", label: "B. Train"}, {key: "C", label: "C. Bus"}], correct: "B", explanation: "Tàu hỏa (train) không bị ảnh hưởng và hoạt động bình thường -> Đáp án B." },
          { number: 6, question: "What is Julie studying?", image: "assets/listening/t6_q6.png", audioScript: "Woman: Julie chose chemistry because she loves working in laboratory research.", options: [{key: "A", label: "A. Medicine"}, {key: "B", label: "B. Engineering"}, {key: "C", label: "C. Chemistry"}], correct: "C", explanation: "Julie đang theo học ngành hóa học (chemistry) -> Đáp án C." },
          { number: 7, question: "Where is Billy now?", image: "assets/listening/t6_q7.png", audioScript: "Man: He's sitting in the pizza restaurant with his friends having lunch.", options: [{key: "A", label: "A. Pizza restaurant"}, {key: "B", label: "B. Library"}, {key: "C", label: "C. Park"}], correct: "A", explanation: "Billy đang ở quán pizza ăn trưa ('pizza restaurant') -> Đáp án A." }
        ]
      },
      {
        partNumber: 2,
        title: "Part 2: Questions 8 - 13 (Local arts and entertainment events)",
        instruction: "You will hear someone reviewing some local arts and entertainment events. For each question, choose the correct answer A, B or C.",
        audioScript: "Presenter: Good evening! The contemporary art exhibition at Mill Street is quite shocking.\nAt the Civic Theatre, 'A Raisin in the Sun' deals with poignant themes about family life decisions.\nThe new animated film will be enjoyed by the whole family.\nFriday night at the Med Food Restaurant features free food for attendees.\nThe government aims to reduce competitive pressure on young children.\nSupermarkets don't sell healthy food compared to the local farmers market.",
        questions: [
          { number: 8, question: "The art exhibition", options: [{key: "A", text: "is boring."}, {key: "B", text: "is shocking."}, {key: "C", text: "has a mixture of amateur and professional artists."}], correct: "B", explanation: "Triển lãm nghệ thuật gây kinh ngạc mạnh ('is shocking') -> Đáp án B." },
          { number: 9, question: "'Raisin in the Sun' is", options: [{key: "A", text: "a comedy."}, {key: "B", text: "about religion."}, {key: "C", text: "about life decisions."}], correct: "C", explanation: "Vở kịch nói về những quyết định trong cuộc đời ('about life decisions') -> Đáp án C." },
          { number: 10, question: "What is said about the film?", options: [{key: "A", text: "The whole family may enjoy it."}, {key: "B", text: "Parents will be bored."}, {key: "C", text: "It would only appeal to Americans."}], correct: "A", explanation: "Cả gia đình đều có thể thưởng thức bộ phim ('the whole family may enjoy it') -> Đáp án A." },
          { number: 11, question: "What is special about Friday night at the 'Med Food Restaurant'?", options: [{key: "A", text: "The chefs are related."}, {key: "B", text: "The food will be free."}, {key: "C", text: "Customers can have a free drink."}], correct: "B", explanation: "Đồ ăn được phục vụ miễn phí -> Đáp án B theo key gốc." },
          { number: 12, question: "The government is trying to", options: [{key: "A", text: "encourage people to be healthier."}, {key: "B", text: "force children to do sport."}, {key: "C", text: "stop children from being too competitive."}], correct: "C", explanation: "Chính phủ nỗ lực giảm bớt áp lực cạnh tranh ở trẻ em -> Đáp án C theo key gốc." },
          { number: 13, question: "The speaker suggests that", options: [{key: "A", text: "Supermarkets don't sell healthy food."}, {key: "B", text: "The market is fun for all the family."}, {key: "C", text: "The market is good for a night out."}], correct: "A", explanation: "Siêu thị không bán nhiều thực phẩm lành mạnh bằng chợ nông sản -> Đáp án A." }
        ]
      },
      {
        partNumber: 3,
        title: "Part 3: Questions 14 - 19 (The Oasis Hotel - Guest Briefing)",
        instruction: "You will hear a holiday rep welcoming a new group of guests to a hotel. For each question, fill in the missing information in the numbered space.",
        audioScript: "Rep: Welcome to the Oasis Hotel! Steven is in his desk office between 10 and 11 a.m. or between 6 and 7 p.m.\nThe excursion costs cover everything except lunch.\nChildren under the age of 7 are not permitted on the full-day tour.\nThe hotel creche facility closes at 12 o'clock midday.\nOur aerobics classes cost £11.30 per hour, and Sunday features a water aerobics pool class.",
        notesContext: "THE OASIS HOTEL - GUEST INFORMATION\n• Steven's office hours: 10 - 11 a.m. or (14) ________ and 7 p.m.\n• Excursion includes all costs except (15) ________\n• Age limit: Children under (16) ________ not allowed on excursion\n• Creche closes at (17) ________ in the morning\n• Fitness aerobics class: £(18) ________ an hour\n• Sunday 10 a.m. pool session: (19) ________ class",
        questions: [
          { number: 14, prompt: "Office hours: 10 - 11 a.m. or ... and 7 p.m.", acceptedAnswers: ["6", "6 p.m.", "6.00"], correct: "6", explanation: "Văn phòng mở cửa lúc 6 giờ tối (6)." },
          { number: 15, prompt: "Excursion includes everything except", acceptedAnswers: ["lunch", "7"], correct: "7", explanation: "Đáp án theo key gốc là 7." },
          { number: 16, prompt: "Children under ... not allowed", acceptedAnswers: ["LUNCH", "lunch", "7"], correct: "LUNCH", explanation: "Không bao gồm bữa trưa (LUNCH)." },
          { number: 17, prompt: "Creche closes at", acceptedAnswers: ["12", "12 o'clock"], correct: "12", explanation: "Đóng cửa lúc 12 giờ trưa (12)." },
          { number: 18, prompt: "Aerobics cost per hour: £...", acceptedAnswers: ["11:30", "11.30", "11.50"], correct: "11:30", explanation: "Chi phí 11.30 bảng một giờ (11:30)." },
          { number: 19, prompt: "Sunday pool class is", acceptedAnswers: ["water aerobics", "aerobics"], correct: "water aerobics", explanation: "Thể dục nhịp điệu dưới nước (water aerobics)." }
        ]
      },
      {
        partNumber: 4,
        title: "Part 4: Questions 20 - 25 (John & Anna discussing their jobs)",
        instruction: "Look at the six sentences for this part. You will hear a conversation between a man, John, and a woman, Anna, about their jobs. Decide if each sentence is correct (YES) or incorrect (NO).",
        audioScript: "Anna: I have daytime meetings, but luckily I don't drive through the night.\nJohn: Do you still have sleep troubles?\nAnna: Yes, I generally have real problems getting to sleep.\nJohn: Were you expecting your promotion?\nAnna: No, it was a complete surprise, I hadn't been expecting it.\nJohn: Handling financial accounts makes me very nervous.\nAnna: Are you looking for a girlfriend?\nJohn: No, I deny that I am looking for a girlfriend right now.\nAnna: I'm so tired I probably won't go to Cactus Club tonight.",
        questions: [
          { number: 20, statement: "Anna has to drive throughout the night from meeting to meeting.", correct: "NO", explanation: "Anna không phải lái xe suốt đêm -> NO." },
          { number: 21, statement: "Anna generally has a problem getting to sleep.", correct: "YES", explanation: "Anna thường bị khó ngủ do căng thẳng -> YES." },
          { number: 22, statement: "John had been expecting his promotion.", correct: "NO", explanation: "John không hề ngờ trước việc được thăng chức -> NO." },
          { number: 23, statement: "John is nervous about doing the accounts.", correct: "YES", explanation: "John rất lo lắng khi làm sổ sách kế toán -> YES." },
          { number: 24, statement: "John denies he is looking for a girlfriend.", correct: "YES", explanation: "John khẳng định anh không tìm bạn gái vào lúc này -> YES." },
          { number: 25, statement: "Anna will probably go to the Cactus Club.", correct: "NO", explanation: "Anna quá mệt nên có lẽ sẽ không đi -> NO." }
        ]
      }
    ]
  },

  test_7: {
    title: "Paper 2 - Listening",
    duration: 30,
    parts: [
      {
        partNumber: 1,
        title: "Part 1: Questions 1 - 7 (Hội thoại ngắn có tranh ảnh)",
        instruction: "There are seven questions in this part. For each question there are three pictures and a short recording. Choose the correct picture and select A, B or C.",
        questions: [
          { number: 1, question: "What is the woman talking about?", image: "assets/listening/t7_q1.png", audioScript: "Woman: Look at this magnificent antique wooden desk with carved legs and brass drawers; it dates back to Victorian times.", options: [{key: "A", label: "A. Chair"}, {key: "B", label: "B. Wardrobe"}, {key: "C", label: "C. Antique desk"}], correct: "C", explanation: "Người phụ nữ miêu tả chiếc bàn làm việc cổ ('antique wooden desk') -> Đáp án C." },
          { number: 2, question: "What is the man's job?", image: "assets/listening/t7_q2.png", audioScript: "Man: I work as a head chef creating gourmet menus and supervising our kitchen cooks every evening.", options: [{key: "A", label: "A. Chef / Cook"}, {key: "B", label: "B. Waiter"}, {key: "C", label: "C. Manager"}], correct: "A", explanation: "Công việc là đầu bếp (chef) -> Đáp án A." },
          { number: 3, question: "Where are they?", image: "assets/listening/t7_q3.png", audioScript: "Woman: Please fasten your seatbelts and store your luggage securely in the overhead lockers before take-off.", options: [{key: "A", label: "A. Train"}, {key: "B", label: "B. Airplane"}, {key: "C", label: "C. Ferry"}], correct: "B", explanation: "Họ đang ở trên máy bay trước giờ cất cánh -> Đáp án B." },
          { number: 4, question: "What is the woman going to do on Sunday?", image: "assets/listening/t7_q4.png", audioScript: "Woman: I've booked tickets for the botanical garden flower festival on Sunday.", options: [{key: "A", label: "A. Shopping"}, {key: "B", label: "B. Zoo"}, {key: "C", label: "C. Botanical garden"}], correct: "C", explanation: "Cô sẽ đi thăm vườn bách thảo ('botanical garden') -> Đáp án C." },
          { number: 5, question: "What are the people talking about?", image: "assets/listening/t7_q5.png", audioScript: "Woman: Look at the size of that cruise ship docked in the harbor; it carries over three thousand passengers.", options: [{key: "A", label: "A. Cruise ship"}, {key: "B", label: "B. Submarine"}, {key: "C", label: "C. Cargo vessel"}], correct: "A", explanation: "Họ đang nói về tàu du lịch lớn ('cruise ship') -> Đáp án A." },
          { number: 6, question: "Where do the people work?", image: "assets/listening/t7_q6.png", audioScript: "Man: We handle bookings for international flights and holiday packages at our travel agency.", options: [{key: "A", label: "A. Hospital"}, {key: "B", label: "B. Travel agency"}, {key: "C", label: "C. Hotel"}], correct: "B", explanation: "Họ làm việc tại công ty du lịch ('travel agency') -> Đáp án B." },
          { number: 7, question: "What is dangerous about the weather tonight?", image: "assets/listening/t7_q7.png", audioScript: "Weather: Drivers should take extreme care tonight as temperatures plunge, creating hazardous black ice across all roads.", options: [{key: "A", label: "A. Fog"}, {key: "B", label: "B. Heavy snow"}, {key: "C", label: "C. Black ice on roads"}], correct: "C", explanation: "Băng đen trơn trượt trên mặt đường ('hazardous black ice') -> Đáp án C." }
        ]
      },
      {
        partNumber: 2,
        title: "Part 2: Questions 8 - 13 (New Community Centre opening)",
        instruction: "You will hear a man talking about a new community centre that is about to open. For each question, choose the correct answer A, B or C.",
        audioScript: "Speaker: Good evening everyone. My primary objective is to raise finances for the centre.\nThe building is a historic building that has been meticulously adapted.\nSally specializes in helping people who want to avoid athletic injuries.\nDancing is not provided regularly for our older visitors.\nJohn provides extensive guidance mostly for pensioners.\nRegarding the playgroup, mothers will be paid if they assist.",
        questions: [
          { number: 8, question: "What is the man's main aim in this report?", options: [{key: "A", text: "to raise finances for the centre"}, {key: "B", text: "to ask people to help run the centre"}, {key: "C", text: "to encourage different generations to use the centre"}], correct: "A", explanation: "Mục đích chính là gây quỹ tài chính cho trung tâm ('raise finances for the centre') -> Đáp án A." },
          { number: 9, question: "What is said about the building?", options: [{key: "A", text: "It is brand new."}, {key: "B", text: "It's a historic building that's been changed."}, {key: "C", text: "It needs a lot of work done on it."}], correct: "B", explanation: "Tòa nhà là công trình lịch sử được tu sửa cải tạo lại -> Đáp án B." },
          { number: 10, question: "Who will Sally be able to help?", options: [{key: "A", text: "People recovering from a leg operation."}, {key: "B", text: "People trying to improve as athletes."}, {key: "C", text: "People who want to avoid getting injured."}], correct: "C", explanation: "Sally hỗ trợ phòng tránh chấn thương ('avoid getting injured') -> Đáp án C." },
          { number: 11, question: "What is not provided regularly for older people?", options: [{key: "A", text: "dancing"}, {key: "B", text: "lectures"}, {key: "C", text: "Bingo"}], correct: "A", explanation: "Hoạt động khiêu vũ không được tổ chức thường xuyên -> Đáp án A theo key gốc." },
          { number: 12, question: "Who can John help?", options: [{key: "A", text: "only teenagers"}, {key: "B", text: "mostly pensioners"}, {key: "C", text: "people of all ages"}], correct: "B", explanation: "John chủ yếu hỗ trợ người cao tuổi nghỉ hưu -> Đáp án B theo key gốc." },
          { number: 13, question: "What is said about the playgroup?", options: [{key: "A", text: "Mums are expected to supervise their children."}, {key: "B", text: "Mums can go to work and leave their children there all morning."}, {key: "C", text: "Mums will be paid if they want to help out with the playgroup."}], correct: "C", explanation: "Các bà mẹ được trả phụ cấp nếu tham gia hỗ trợ nhóm trẻ -> Đáp án C theo key gốc." }
        ]
      },
      {
        partNumber: 3,
        title: "Part 3: Questions 14 - 19 (Spanish Art Holidays - Daily Programme)",
        instruction: "You will hear a woman talking about an art holiday. For each question, fill in the missing information in the numbered space.",
        audioScript: "Coordinator: Each morning starts with a delicious self-service buffet breakfast on the patio.\nAt 10 o'clock our resident master painter delivers a live demonstration using watercolours or charcoal.\nAt midday we enjoy a leisurely picnic lunch provided by the hotel. Please collect your lunch box from reception.\nIn the late afternoon at 3.30, we gather for a constructive tutorial session.",
        notesContext: "SPANISH ART HOLIDAYS - DAILY PROGRAMME\n• 8.30: Breakfast on patio. (14) ________ buffet-style breakfast\n• 10.00: Live (15) ________ of painting by teacher using acrylics or (16) ________\n• 12.30: (17) ________ lunch provided by hotel. Collect lunch from (18) ________\n• 15.30: Group (19) ________ to review artwork",
        questions: [
          { number: 14, prompt: "Patio breakfast is a ... buffet", acceptedAnswers: ["self-service", "self service"], correct: "self-service", explanation: "Bữa sáng buffet tự phục vụ (self-service)." },
          { number: 15, prompt: "10 o'clock feature is a", acceptedAnswers: ["Demonstration", "demonstration"], correct: "Demonstration", explanation: "Buổi vẽ biểu diễn thị phạm của thầy cô (Demonstration)." },
          { number: 16, prompt: "Drawing with pencil or", acceptedAnswers: ["charcoal"], correct: "charcoal", explanation: "Vẽ bằng chì than (charcoal)." },
          { number: 17, prompt: "12.30 is a ... lunch", acceptedAnswers: ["picnic", "packed lunch"], correct: "picnic", explanation: "Bữa trưa dã ngoại picnic (picnic)." },
          { number: 18, prompt: "Collect packed lunch from", acceptedAnswers: ["reception", "hotel reception"], correct: "reception", explanation: "Lấy phần cơm trưa tại quầy lễ tân (reception)." },
          { number: 19, prompt: "15.30 is a group", acceptedAnswers: ["tutorial", "discussion"], correct: "tutorial", explanation: "Buổi học nhóm nhận xét tranh (tutorial)." }
        ]
      },
      {
        partNumber: 4,
        title: "Part 4: Questions 20 - 25 (Amanda & George talking about travelling)",
        instruction: "Look at the six sentences for this part. You will hear a conversation between a man, George, and a woman, Amanda, about travelling. Decide if each sentence is correct (YES) or incorrect (NO).",
        audioScript: "Amanda: I love traveling with companions, it makes trips so vibrant.\nGeorge: Traveling alone in Europe never makes me nervous, I always feel calm.\nAmanda: I always take hundreds of photographs during vacations.\nGeorge: I never miss having company when wandering alone.\nGeorge: In the evenings I write memoirs and travel stories.\nGeorge: Originally I traveled for enjoyment, never because I had to.",
        questions: [
          { number: 20, statement: "Amanda likes to travel with other people.", correct: "YES", explanation: "Amanda thích đi du lịch cùng người khác -> YES." },
          { number: 21, statement: "George always feels a bit nervous in Europe.", correct: "NO", explanation: "George luôn cảm thấy thoải mái, không lo lắng -> NO." },
          { number: 22, statement: "Amanda always takes lots of photographs when she's on holiday.", correct: "YES", explanation: "Amanda luôn chụp rất nhiều ảnh kỷ niệm -> YES." },
          { number: 23, statement: "George sometimes misses having company when he's travelling.", correct: "NO", explanation: "George không hề nhớ việc có bạn đồng hành -> NO." },
          { number: 24, statement: "George writes when he's travelling.", correct: "YES", explanation: "George viết sách du ký khi đi du lịch -> YES." },
          { number: 25, statement: "George initially travelled a lot because he had to.", correct: "NO", explanation: "George đi du lịch vì đam mê chứ không bị bắt buộc -> NO." }
        ]
      }
    ]
  },

  test_8: {
    title: "Paper 2 - Listening",
    duration: 30,
    parts: [
      {
        partNumber: 1,
        title: "Part 1: Questions 1 - 7 (Hội thoại ngắn có tranh ảnh)",
        instruction: "There are seven questions in this part. For each question there are three pictures and a short recording. Choose the correct picture and select A, B or C.",
        questions: [
          { number: 1, question: "What will they have for dinner?", image: "assets/listening/t8_q1.png", audioScript: "Woman: I bought fresh sirloin steaks, so we're having steak and roasted potatoes tonight!", options: [{key: "A", label: "A. Fish"}, {key: "B", label: "B. Steak"}, {key: "C", label: "C. Chicken"}], correct: "B", explanation: "Họ sẽ ăn bít tết bò ('steak and roasted potatoes') -> Đáp án B." },
          { number: 2, question: "What's the time?", image: "assets/listening/t8_q2.png", audioScript: "Man: It's a quarter to eight - exactly seven forty-five.", options: [{key: "A", label: "A. 19:35"}, {key: "B", label: "B. 19:40"}, {key: "C", label: "C. 19:45 (7:45 PM)"}], correct: "C", explanation: "Đồng hồ chỉ 7 giờ 45 tối ('seven forty-five') -> Đáp án C." },
          { number: 3, question: "Which dress does Jenny buy?", image: "assets/listening/t8_q3.png", audioScript: "Jenny: I bought the elegant knee-length striped dress with short sleeves.", options: [{key: "A", label: "A. Knee-length striped dress"}, {key: "B", label: "B. Long dress"}, {key: "C", label: "C. Plain dress"}], correct: "A", explanation: "Jenny mua chiếc váy kẻ sọc dài ngang gối ('knee-length striped dress') -> Đáp án A." },
          { number: 4, question: "Where will the man go first after work?", image: "assets/listening/t8_q4.png", audioScript: "Man: Before going home or shopping, I must go straight to the petrol station because the fuel tank is empty.", options: [{key: "A", label: "A. Supermarket"}, {key: "B", label: "B. Petrol station"}, {key: "C", label: "C. Bank"}], correct: "B", explanation: "Nơi đầu tiên anh ghé là trạm đổ xăng ('petrol station') -> Đáp án B." },
          { number: 5, question: "How did the woman break her arm?", image: "assets/listening/t8_q5.png", audioScript: "Woman: I tripped over our puppy's toys on the staircase at home and fell.", options: [{key: "A", label: "A. Horse riding"}, {key: "B", label: "B. Slipping on ice"}, {key: "C", label: "C. Falling on stairs"}], correct: "C", explanation: "Cô vấp đồ chơi ngã ở cầu thang ('tripped on the staircase') -> Đáp án C." },
          { number: 6, question: "Where is the remote control?", image: "assets/listening/t8_q6.png", audioScript: "Man: Look, it's sitting right on top of the television set.", options: [{key: "A", label: "A. On top of the TV"}, {key: "B", label: "B. Under cushion"}, {key: "C", label: "C. On coffee table"}], correct: "A", explanation: "Chiếc điều khiển nằm trên nóc TV ('on top of television') -> Đáp án A." },
          { number: 7, question: "Where did they stay on holiday this year?", image: "assets/listening/t8_q7.png", audioScript: "Woman: We rented a tranquil country cottage by a babbling stream.", options: [{key: "A", label: "A. Hotel"}, {key: "B", label: "B. Country cottage"}, {key: "C", label: "C. Tent"}], correct: "B", explanation: "Họ thuê ngôi nhà nhỏ thôn quê ('country cottage') -> Đáp án B." }
        ]
      },
      {
        partNumber: 2,
        title: "Part 2: Questions 8 - 13 (Interview with Margaret about panic attacks)",
        instruction: "You will hear an interview with a woman who suffers from panic attacks. For each question, choose the correct answer A, B or C.",
        audioScript: "Presenter: Margaret, can you describe your first experience with panic disorder?\nMargaret: Nobody knows what triggered that initial attack.\nPanic attacks feel even worse than having a heart attack.\nI was completely shocked when it happened.\nMy husband bought me a camera because I'd always wanted one.\nWhile at the lake, I had a sudden panic attack.\nSoon, leaving the camera at home will prevent me becoming addicted to photography.",
        questions: [
          { number: 8, question: "What caused Margaret's first panic attack?", options: [{key: "A", text: "She was overstressed at work."}, {key: "B", text: "She was very tired."}, {key: "C", text: "Nobody knows."}], correct: "C", explanation: "Không ai rõ nguyên nhân gây ra cơn hoảng loạn đầu tiên ('nobody knows') -> Đáp án C." },
          { number: 9, question: "What does Margaret say about panic attacks?", options: [{key: "A", text: "They are worse than a heart attack."}, {key: "B", text: "They are as frightening as a heart attack."}, {key: "C", text: "You usually only ever have one in your life."}], correct: "A", explanation: "Cơn hoảng loạn còn đáng sợ hơn cả cơn đau tim -> Đáp án A theo key gốc." },
          { number: 10, question: "How did Margaret feel about her first panic attack?", options: [{key: "A", text: "angry"}, {key: "B", text: "shocked"}, {key: "C", text: "frustrated"}], correct: "B", explanation: "Cô cảm thấy bàng hoàng sửng sốt ('shocked') -> Đáp án B." },
          { number: 11, question: "Why did Margaret's husband buy her a camera?", options: [{key: "A", text: "to keep her mind off her fear"}, {key: "B", text: "to give her a new career"}, {key: "C", text: "because she'd always wanted one"}], correct: "C", explanation: "Vì cô đã luôn mong ước sở hữu một chiếc máy ảnh -> Đáp án C theo key gốc." },
          { number: 12, question: "Why did Margaret forget where she was at the lake?", options: [{key: "A", text: "She had a panic attack."}, {key: "B", text: "She became confused."}, {key: "C", text: "She was concentrating on the bird."}], correct: "A", explanation: "Do cô bất ngờ lên cơn hoảng sợ ('had a panic attack') -> Đáp án A theo key gốc." },
          { number: 13, question: "Why is it important that Margaret leaves her camera at home soon?", options: [{key: "A", text: "It will show that she is better."}, {key: "B", text: "She has become addicted to photography."}, {key: "C", text: "Her husband thinks she is being unsociable."}], correct: "B", explanation: "Để tránh bị quá phụ thuộc/nghiện nhiếp ảnh -> Đáp án B theo key gốc." }
        ]
      },
      {
        partNumber: 3,
        title: "Part 3: Questions 14 - 19 (Win a Dream Night at the Theatre)",
        instruction: "You will hear a radio announcement about a competition. For each question, fill in the missing information in the numbered space.",
        audioScript: "Announcer: Win a dream night at the theatre! In our prize draw, there are 4 pairs of tickets to be won.\nAfternoon matinees on Tuesday to Thursday start at 2:30PM.\nTicket prices range up to £24.50, and children's tickets are available at half price.\nYou can book online via the website. The competition closes on June 13th.",
        notesContext: "WIN A DREAM NIGHT AT THE THEATRE\n• Prize: (14) ________ pairs of tickets to be won\n• Matinees: Tuesday - Thursday afternoons at (15) ________\n• Ticket prices: From £11 to £(16) ________\n• Children's tickets available at (17) ________\n• Booking: Call by telephone or book (18) ________\n• Competition deadline: (19) ________ on June 13th",
        questions: [
          { number: 14, prompt: "Pairs of tickets to be won", acceptedAnswers: ["4", "four"], correct: "4", explanation: "Có 4 cặp vé xem kịch (4)." },
          { number: 15, prompt: "Tuesday - Thursday afternoon shows at", acceptedAnswers: ["2:30PM", "2.30pm", "2.30", "2:30"], correct: "2:30PM", explanation: "Suất diễn chiều lúc 2:30 chiều (2:30PM)." },
          { number: 16, prompt: "Ticket prices up to £...", acceptedAnswers: ["24.50 pounds", "24.50", "£24.50"], correct: "24.50 pounds", explanation: "Giá vé tối đa 24.50 bảng (24.50 pounds)." },
          { number: 17, prompt: "Children's tickets are", acceptedAnswers: ["half price", "half-price", "50%"], correct: "half price", explanation: "Vé trẻ em giảm nửa giá (half price)." },
          { number: 18, prompt: "Book by phone or", acceptedAnswers: ["online", "on the web"], correct: "online", explanation: "Đặt vé trực tuyến trên mạng (online)." },
          { number: 19, prompt: "Competition ... on June 13th", acceptedAnswers: ["closes", "ends"], correct: "closes", explanation: "Cuộc thi kết thúc đóng cổng ngày 13/6 (closes)." }
        ]
      },
      {
        partNumber: 4,
        title: "Part 4: Questions 20 - 25 (Alison & Bob talking about pets)",
        instruction: "Look at the six sentences for this part. You will hear a conversation between a girl, Alison, and a boy, Bob, about pets. Decide if each sentence is correct (YES) or incorrect (NO).",
        audioScript: "Alison: Would a dog be good company for Grandma?\nBob: No, walking a dog would be too exhausting for an elderly lady.\nBob: I really don't like dogs myself.\nAlison: Have you found homes for your kittens?\nBob: No, I haven't found homes for the kittens yet.\nAlison: I would happily volunteer at the animal rescue without getting paid.\nBob: That's very sweet, you're definitely not mad.\nBob: Let's visit the animal rescue centre together this Saturday!",
        questions: [
          { number: 20, statement: "Bob thinks a dog would be good company for Alison's grandma.", correct: "NO", explanation: "Bob cho rằng nuôi chó quá vất vả với bà -> NO." },
          { number: 21, statement: "Bob doesn't like dogs.", correct: "YES", explanation: "Bob thừa nhận anh không thích loài chó -> YES." },
          { number: 22, statement: "Bob has found homes for the kittens.", correct: "NO", explanation: "Bob chưa tìm được chủ cho đàn mèo con -> NO." },
          { number: 23, statement: "Alison would be happy to work at the dogs' home without getting paid.", correct: "YES", explanation: "Alison sẵn sàng làm việc tình nguyện không nhận lương -> YES." },
          { number: 24, statement: "Bob thinks Alison is mad.", correct: "NO", explanation: "Bob ủng hộ và không nghĩ cô điên rồ -> NO." },
          { number: 25, statement: "Bob and Alison will go to the dogs' home together.", correct: "YES", explanation: "Cả hai sẽ cùng nhau đến trại cứu hộ động vật -> YES." }
        ]
      }
    ]
  },

  test_9: {
    title: "Paper 2 - Listening",
    duration: 30,
    parts: [
      {
        partNumber: 1,
        title: "Part 1: Questions 1 - 7 (Hội thoại ngắn có tranh ảnh)",
        instruction: "There are seven questions in this part. For each question there are three pictures and a short recording. Choose the correct picture and select A, B or C.",
        questions: [
          { number: 1, question: "What pizza will the man get?", image: "assets/listening/t9_q1.png", audioScript: "Man: Please order the pepperoni pizza with mushrooms for me.", options: [{key: "A", label: "A. Pepperoni pizza"}, {key: "B", label: "B. Seafood pizza"}, {key: "C", label: "C. Vegetarian pizza"}], correct: "A", explanation: "Người đàn ông chọn pizza pepperoni xúc xích bò ('pepperoni pizza') -> Đáp án A." },
          { number: 2, question: "Who are they talking about?", image: "assets/listening/t9_q2.png", audioScript: "Man: Look at him over there - he has thick dark curls, glasses, and a full beard.", options: [{key: "A", label: "A. Man with hat"}, {key: "B", label: "B. Man with curly hair, beard & glasses"}, {key: "C", label: "C. Clean-shaven man"}], correct: "B", explanation: "Người đàn ông tóc xoăn, đeo kính và có râu ('curly hair, glasses & beard') -> Đáp án B." },
          { number: 3, question: "What is Jan doing now?", image: "assets/listening/t9_q3.png", audioScript: "Man: Right now she's riding her horse around the paddock.", options: [{key: "A", label: "A. Swimming"}, {key: "B", label: "B. Playing violin"}, {key: "C", label: "C. Horse riding"}], correct: "C", explanation: "Jan đang cưỡi ngựa ('riding her horse') -> Đáp án C." },
          { number: 4, question: "What is the museum near?", image: "assets/listening/t9_q4.png", audioScript: "Guide: The museum stands immediately opposite the central railway station.", options: [{key: "A", label: "A. Railway station"}, {key: "B", label: "B. Castle"}, {key: "C", label: "C. River bridge"}], correct: "A", explanation: "Bảo tàng nằm đối diện ga xe lửa ('opposite railway station') -> Đáp án A." },
          { number: 5, question: "What will the weather be like tomorrow night?", image: "assets/listening/t9_q5.png", audioScript: "Weatherman: Severe thunderstorms with vivid lightning will sweep across the area tomorrow night.", options: [{key: "A", label: "A. Sunny"}, {key: "B", label: "B. Thunderstorm / Lightning"}, {key: "C", label: "C. Snow"}], correct: "B", explanation: "Thời tiết đêm mai có giông bão sấm sét ('thunderstorms with lightning') -> Đáp án B." },
          { number: 6, question: "What kind of transportation is the man talking about?", image: "assets/listening/t9_q6.png", audioScript: "Man: I love gliding down the canal on an electric river barge.", options: [{key: "A", label: "A. Bus"}, {key: "B", label: "B. Train"}, {key: "C", label: "C. River boat / barge"}], correct: "C", explanation: "Đi thuyền sà lan trên sông ('river barge') -> Đáp án C." },
          { number: 7, question: "For how long was the man on the phone?", image: "assets/listening/t9_q7.png", audioScript: "Man: Customer support kept me on hold so long that my call lasted thirty minutes in total!", options: [{key: "A", label: "A. Thirty minutes (30 min)"}, {key: "B", label: "B. Fifteen minutes"}, {key: "C", label: "C. One hour"}], correct: "A", explanation: "Cuộc gọi kéo dài 30 phút ('thirty minutes in total') -> Đáp án A." }
        ]
      },
      {
        partNumber: 2,
        title: "Part 2: Questions 8 - 13 (Writers who were ambulance drivers in WWI)",
        instruction: "You will hear part of a radio programme about writers who worked as ambulance drivers in World War One. For each question, choose the correct answer A, B or C.",
        audioScript: "Presenter: During World War One, more than twenty-three famous American authors volunteered as ambulance drivers.\nThis connection between writers and ambulance driving is present throughout history.\nThe invention of the automobile dramatically revolutionized the image and speed of ambulances.\nMany volunteer drivers were university graduates or students eager to participate.\nMany joined out of a desire to avoid direct trench danger.\nUnlike frontline infantry, ambulance drivers were profoundly changed by their experiences.",
        questions: [
          { number: 8, question: "How many American authors were ambulance drivers?", options: [{key: "A", text: "not less than 23"}, {key: "B", text: "more than 23"}, {key: "C", text: "around 4"}], correct: "B", explanation: "Hơn 23 tác giả người Mỹ đã làm lái xe cứu thương ('more than 23') -> Đáp án B theo key gốc." },
          { number: 9, question: "The connection between ambulance driving and famous writers", options: [{key: "A", text: "is present throughout history."}, {key: "B", text: "is present in American Universities."}, {key: "C", text: "is present during World War I."}], correct: "A", explanation: "Mối liên hệ này xuất hiện xuyên suốt chiều dài lịch sử -> Đáp án A theo key gốc." },
          { number: 10, question: "What greatly changed the image of the ambulance?", options: [{key: "A", text: "that it became too difficult to drive"}, {key: "B", text: "World War I"}, {key: "C", text: "the invention of the automobile"}], correct: "C", explanation: "Sự phát minh ra xe ô tô ('invention of the automobile') -> Đáp án C." },
          { number: 11, question: "Many volunteer ambulance drivers were", options: [{key: "A", text: "race-car drivers."}, {key: "B", text: "university graduates or students."}, {key: "C", text: "very wealthy."}], correct: "B", explanation: "Nhiều tình nguyện viên là sinh viên hoặc cử nhân tốt nghiệp ('university graduates or students') -> Đáp án B." },
          { number: 12, question: "What is a reason that made people become ambulance drivers?", options: [{key: "A", text: "a desire to avoid danger"}, {key: "B", text: "a willingness to kill"}, {key: "C", text: "a wish to participate despite being unfit"}], correct: "A", explanation: "Mong muốn tránh những nguy hiểm trực tiếp nơi tuyến đầu -> Đáp án A theo key gốc." },
          { number: 13, question: "Ambulance drivers, but not soldiers", options: [{key: "A", text: "were face to face with the war."}, {key: "B", text: "had time to think"}, {key: "C", text: "were changed by their experiences."}], correct: "C", explanation: "Họ đã thay đổi sâu sắc qua những trải nghiệm thực tế ('changed by their experiences') -> Đáp án C theo key gốc." }
        ]
      },
      {
        partNumber: 3,
        title: "Part 3: Questions 14 - 19 (Fashion Photographs - Photographer Mike Jones)",
        instruction: "You will hear a radio announcer giving details about an event that is going to take place. For each question, fill in the missing information in the numbered space.",
        audioScript: "Announcer: Visiting photographer Mike Jones is hosting an open photoshoot for youngsters aged 14 to 18.\nPhotos will be featured on his popular blog.\nHe welcomes both girls and boys wearing any style of clothing.\nMeeting location is at the square in front of the museum at 10a.m. on Sunday.\nCall the project line on 394 944 9025.",
        notesContext: "FASHION PHOTOGRAPHS - MIKE JONES PROJECT\n• Visiting photographer: Mike Jones\n• Target ages: (14) ________\n• Photos featured on his: (15) ________\n• Looking for: all shapes, all styles of dress, and (16) ________\n• Meeting point: (17) ________ in front of the museum\n• Meeting time: (18) ________ on Sunday\n• Inquiry phone line: (19) ________",
        questions: [
          { number: 14, prompt: "Ages he wants to photograph", acceptedAnswers: ["14 to 18", "14-18"], correct: "14 to 18", explanation: "Độ tuổi tham gia từ 14 đến 18 (14 to 18)." },
          { number: 15, prompt: "He will feature his photos on his", acceptedAnswers: ["blog", "website"], correct: "blog", explanation: "Ảnh sẽ được đăng trên blog cá nhân (blog)." },
          { number: 16, prompt: "Looking for all styles, shapes, and", acceptedAnswers: ["girls and boys", "boys and girls"], correct: "girls and boys", explanation: "Tuyển cả nam và nữ (girls and boys)." },
          { number: 17, prompt: "Meeting place in front of museum", acceptedAnswers: ["the square", "square"], correct: "the square", explanation: "Gặp nhau ở quảng trường trước bảo tàng (the square)." },
          { number: 18, prompt: "Meeting time on Sunday", acceptedAnswers: ["10a.m", "10 a.m.", "10:00 AM"], correct: "10a.m", explanation: "Thời gian gặp là 10 giờ sáng Chủ Nhật (10a.m)." },
          { number: 19, prompt: "Inquiry line telephone number", acceptedAnswers: ["394 944 9025", "3949449025"], correct: "394 944 9025", explanation: "Số điện thoại liên hệ là 394 944 9025." }
        ]
      },
      {
        partNumber: 4,
        title: "Part 4: Questions 20 - 25 (William & Beth talking about after-school sports)",
        instruction: "Look at the six sentences for this part. You will hear a conversation between a boy, William, and a girl, Beth, about after-school sports. Decide if each sentence is correct (YES) or incorrect (NO).",
        audioScript: "William: Beth, you're so good at jumping rope!\nBeth: Thanks, but at the sports club yesterday we barely got any exercise because the courts were occupied.\nWilliam: There were only boys playing football.\nWilliam: You would be very welcome on the team!\nBeth: I'm not good at playing football at all.\nWilliam: Don't worry, the girls definitely won't tease you.",
        questions: [
          { number: 20, statement: "Beth is good at jumping rope.", correct: "YES", explanation: "Beth nhảy dây rất giỏi ('good at jumping rope') -> YES." },
          { number: 21, statement: "Beth got a lot of exercise when she went to the sports club.", correct: "NO", explanation: "Beth không tập được nhiều do sân bãi bị chiếm -> NO." },
          { number: 22, statement: "There were only boys playing football.", correct: "YES", explanation: "Chỉ có các bạn nam đá bóng trên sân -> YES." },
          { number: 23, statement: "William thinks Beth would be welcome on the team.", correct: "YES", explanation: "William tin rằng đội bóng sẽ chào đón Beth -> YES." },
          { number: 24, statement: "Beth is good at playing football.", correct: "NO", explanation: "Beth chơi bóng đá không tốt ('not good at playing football') -> NO." },
          { number: 25, statement: "William does not think the girls will tease Beth.", correct: "YES", explanation: "William khẳng định các bạn nữ sẽ không trêu chọc -> YES." }
        ]
      }
    ]
  },

  test_10: {
    title: "Paper 2 - Listening",
    duration: 30,
    parts: [
      {
        partNumber: 1,
        title: "Part 1: Questions 1 - 7 (Hội thoại ngắn có tranh ảnh)",
        instruction: "There are seven questions in this part. For each question there are three pictures and a short recording. Choose the correct picture and select A, B or C.",
        questions: [
          { number: 1, question: "Which jumper does the man like?", image: "assets/listening/t10_q1.png", audioScript: "Man: Actually, I like the V-neck sweater with horizontal stripes across the chest.", options: [{key: "A", label: "A. Plain jumper"}, {key: "B", label: "B. Diamond pattern"}, {key: "C", label: "C. Striped V-neck jumper"}], correct: "C", explanation: "Người đàn ông thích chiếc áo len kẻ sọc cổ chữ V ('striped V-neck jumper') -> Đáp án C." },
          { number: 2, question: "What is the current weather?", image: "assets/listening/t10_q2.png", audioScript: "Man: Thick fog has rolled in and you can hardly see across the street.", options: [{key: "A", label: "A. Thick fog"}, {key: "B", label: "B. Snow"}, {key: "C", label: "C. Sunny"}], correct: "A", explanation: "Thời tiết hiện tại sương mù dày đặc ('thick fog') -> Đáp án A." },
          { number: 3, question: "At which time is the plumber available?", image: "assets/listening/t10_q3.png", audioScript: "Man: He has an open appointment slot at five thirty.", options: [{key: "A", label: "A. 12 o'clock"}, {key: "B", label: "B. 5.30 o'clock"}, {key: "C", label: "C. 3 o'clock"}], correct: "B", explanation: "Thợ sửa ống nước rảnh lúc 5 giờ 30 ('five thirty') -> Đáp án B." },
          { number: 4, question: "Where was the book?", image: "assets/listening/t10_q4.png", audioScript: "Woman: Believe it or not, it was tucked away on the kitchen counter beside the toaster.", options: [{key: "A", label: "A. Under bed"}, {key: "B", label: "B. On coffee table"}, {key: "C", label: "C. On kitchen counter"}], correct: "C", explanation: "Cuốn sách ở trên bệ bếp ('kitchen counter') -> Đáp án C." },
          { number: 5, question: "What's the woman wearing?", image: "assets/listening/t10_q5.png", audioScript: "Woman: She's wearing a tailored blue jacket over a white blouse with dark trousers.", options: [{key: "A", label: "A. Jacket & trousers"}, {key: "B", label: "B. Dress"}, {key: "C", label: "C. Skirt"}], correct: "A", explanation: "Cô ấy mặc áo khoác jacket và quần âu dài -> Đáp án A." },
          { number: 6, question: "Which is the woman's handbag?", image: "assets/listening/t10_q6.png", audioScript: "Woman: My handbag is rectangular with a shoulder strap and buckle.", options: [{key: "A", label: "A. Round clutch"}, {key: "B", label: "B. Rectangular shoulder bag"}, {key: "C", label: "C. Backpack"}], correct: "B", explanation: "Túi xách hình chữ nhật có dây đeo vai ('rectangular shoulder bag') -> Đáp án B." },
          { number: 7, question: "Where are they going?", image: "assets/listening/t10_q7.png", audioScript: "Woman: We have tickets for the musical at the Theatre Royal.", options: [{key: "A", label: "A. Cinema"}, {key: "B", label: "B. Sports arena"}, {key: "C", label: "C. Theatre"}], correct: "C", explanation: "Họ đang đến nhà hát ('Theatre Royal') -> Đáp án C." }
        ]
      },
      {
        partNumber: 2,
        title: "Part 2: Questions 8 - 13 (Interview with Mr. Davies about Conkers)",
        instruction: "You will hear a radio interview with Mr. Davies about the game of conkers. For each question, choose the correct answer A, B or C.",
        audioScript: "Mr. Davies: Conkers is a classic school playground game.\nIt saddens me because the game has been completely forgotten by most youngsters.\nA conker is a children's game played in the autumn.\nChildren purchase their conkers from vendors.\nA player loses the game when his or her conker is destroyed.\nA winning conker is not used again in the next match.",
        questions: [
          { number: 8, question: "Conkers is", options: [{key: "A", text: "a playground game."}, {key: "B", text: "a seed from a tree."}, {key: "C", text: "a holiday in the autumn."}], correct: "A", explanation: "Conkers là trò chơi truyền thống trên sân trường ('playground game') -> Đáp án A." },
          { number: 9, question: "Mr. Davies is sad because", options: [{key: "A", text: "the game can only be played in the autumn."}, {key: "B", text: "fewer children now play the game."}, {key: "C", text: "the game has been completely forgotten."}], correct: "C", explanation: "Trò chơi gần như đã bị quên lãng hoàn toàn -> Đáp án C theo key gốc." },
          { number: 10, question: "A conker is", options: [{key: "A", text: "the winner of the game."}, {key: "B", text: "a children's game."}, {key: "C", text: "a seed from a tree."}], correct: "B", explanation: "Một trò chơi của trẻ em ('children's game') -> Đáp án B theo key gốc." },
          { number: 11, question: "The children", options: [{key: "A", text: "purchase their conkers."}, {key: "B", text: "find conkers if they are lucky."}, {key: "C", text: "make their own conkers."}], correct: "A", explanation: "Trẻ em mua hạt dẻ ngựa -> Đáp án A theo key gốc." },
          { number: 12, question: "Someone loses the game when", options: [{key: "A", text: "his or her conker is hit."}, {key: "B", text: "his or her conker is destroyed."}, {key: "C", text: "he or she has more than 10 points."}], correct: "B", explanation: "Người chơi bị thua khi quả conker bị đập vỡ nát ('conker is destroyed') -> Đáp án B." },
          { number: 13, question: "A winning conker", options: [{key: "A", text: "takes the score of its victim."}, {key: "B", text: "is replaced by another conker."}, {key: "C", text: "is not used again."}], correct: "C", explanation: "Quả conker thắng cuộc không được dùng lại -> Đáp án C theo key gốc." }
        ]
      },
      {
        partNumber: 3,
        title: "Part 3: Questions 14 - 19 (Photography Contest - North Counties)",
        instruction: "You will hear a radio announcer giving details about a contest that is being held. For each question, fill in the missing information in the numbered space.",
        audioScript: "Announcer: North Counties Animal Rescue is organizing their annual photography contest.\nSubmit charming photos of your pet.\nEmail entries to northcountiesrescue@gmail.com.\nEntries must be submitted by the 12th September.\nCategory winners will receive a £25 gift certificate.\nWinning photos will be printed in a special calendar!",
        notesContext: "PHOTOGRAPHY CONTEST - NORTH COUNTIES\n• Organised by: North Counties Animal (14) ________\n• Subject: Submit photos of (15) ________\n• Email submissions to: (16) ________\n• Deadline: Entries due by (17) ________\n• Prizes: Category winners receive a £25 (18) ________\n• Extra honor: Winning photos published in a charity (19) ________",
        questions: [
          { number: 14, prompt: "Contest held by North Counties Animal", acceptedAnswers: ["rescue", "Animal Rescue"], correct: "rescue", explanation: "Tổ chức cứu hộ động vật North Counties Animal Rescue (rescue)." },
          { number: 15, prompt: "Submit photos of", acceptedAnswers: ["your pet", "pets"], correct: "your pet", explanation: "Chụp ảnh thú cưng của bạn (your pet)." },
          { number: 16, prompt: "Email address for submissions", acceptedAnswers: ["northcountiesrescue@gmail.com"], correct: "northcountiesrescue@gmail.com", explanation: "Địa chỉ email nhận bài thi: northcountiesrescue@gmail.com." },
          { number: 17, prompt: "Photos must be sent by", acceptedAnswers: ["12th September", "September 12th", "12 September"], correct: "12th September", explanation: "Hạn gửi ảnh là ngày 12 tháng 9 (12th September)." },
          { number: 18, prompt: "Winners receive a £25", acceptedAnswers: ["gift certificate", "voucher"], correct: "gift certificate", explanation: "Phiếu quà tặng trị giá 25 bảng (gift certificate)." },
          { number: 19, prompt: "Winning photos published in a", acceptedAnswers: ["calendar"], correct: "calendar", explanation: "Các ảnh đẹp nhất được in trên cuốn lịch từ thiện (calendar)." }
        ]
      },
      {
        partNumber: 4,
        title: "Part 4: Questions 20 - 25 (Harry & Mum talking about test marks)",
        instruction: "Look at the six sentences for this part. You will hear a conversation between a boy, Harry, and his Mum, about the marks he got on a test. Decide if each sentence is correct (YES) or incorrect (NO).",
        audioScript: "Harry: It wasn't an exciting day Mum, but I actually really want to talk to you about it.\nMum: Let me guess, is it the maths test result? May I see your grade slip?\nHarry: It's in my bag.\nMum: I won't look in your bag unless you hand it to me yourself.\nHarry: Here it is Mum... I only got forty percent.\nMum: Forty percent?! Harry, I am furious and very angry about this exam result!\nHarry: I know, but I tried my best.\nMum: You stayed up gaming instead of revising, you definitely did not study hard enough!\nHarry: If you don't believe the exam was harsh, you can call my teacher, I don't mind at all.\nMum: I will certainly be phoning him tomorrow.",
        questions: [
          { number: 20, statement: "Harry had an exciting day.", correct: "NO", explanation: "Ngày của Harry không hề thú vị chút nào -> NO." },
          { number: 21, statement: "Harry wants to talk to his mum about his day.", correct: "YES", explanation: "Harry chủ động muốn tâm sự với mẹ về ngày của mình -> YES." },
          { number: 22, statement: "Harry's mum looks in his bag even though he doesn't want her to.", correct: "NO", explanation: "Mẹ tôn trọng và không tự ý lục cặp sách -> NO." },
          { number: 23, statement: "Harry's mum is very angry about the exam result.", correct: "YES", explanation: "Mẹ rất tức giận về điểm bài thi của Harry -> YES." },
          { number: 24, statement: "Harry's mum thinks he studied hard enough.", correct: "NO", explanation: "Mẹ cho rằng Harry chưa chịu học bài chăm chỉ -> NO." },
          { number: 25, statement: "Harry doesn't mind if his mum calls his teacher.", correct: "YES", explanation: "Harry không ngại việc mẹ gọi điện cho thầy giáo -> YES." }
        ]
      }
    ]
  }
};

// Attach to global.PET_DATA.practiceTests
for (const [testId, listenObj] of Object.entries(tests)) {
  const t = global.PET_DATA.practiceTests.find(item => item.id === testId);
  if (t) {
    t.listening = listenObj;
    console.log(`Attached listening to ${testId} (parts: ${listenObj.parts.length})`);
  } else {
    console.warn(`Could not find ${testId} in practiceTests`);
  }
}

// Write back to data.js
const newFileContent = 'window.PET_DATA = ' + JSON.stringify(global.PET_DATA, null, 2) + ';\n';
fs.writeFileSync('data.js', newFileContent, 'utf8');
console.log('Successfully updated data.js with all listening tests 3 to 10!');
