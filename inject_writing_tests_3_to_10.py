# -*- coding: utf-8 -*-
"""
Generate authentic Writing data for Cambridge B1 Preliminary Tests 3 to 10
Extracted from Sach_B1_clean.pdf
"""
import json

tests_writing = {
    "test_3": {
        "title": "Paper 1 - Writing (Part 1 to Part 3)",
        "duration": 40,
        "parts": [
            {
                "partNumber": 1,
                "title": "Part 1: Questions 1 - 5 (Sentence Transformation)",
                "instruction": "Here are some sentences about playing football. For each question, complete the second sentence so that it means the same as the first, using no more than three words. Write only the missing words.",
                "questions": [
                    {
                        "number": 1,
                        "first": "It is three years since Mike and I went to the stadium for the last time.",
                        "second": "Mike and I [GAP] to the stadium for three years.",
                        "acceptedAnswers": ["haven't been", "have not been"],
                        "explanation": "Cấu trúc: It is + time + since... = have not been... for + time (Đã 3 năm rồi chúng tôi chưa đến sân vận động)."
                    },
                    {
                        "number": 2,
                        "first": "Buy a season ticket, and you can go to the match every week.",
                        "second": "If you had a season ticket, [GAP] to the match every week.",
                        "acceptedAnswers": ["you could go", "you'd be able to go"],
                        "explanation": "Câu điều kiện loại 2: If + quá khứ đơn, S + could/would + V nguyên mẫu."
                    },
                    {
                        "number": 3,
                        "first": "The manager bought three new players last year.",
                        "second": "Three new players [GAP] the manager last year.",
                        "acceptedAnswers": ["were bought by"],
                        "explanation": "Câu bị động quá khứ đơn: was/were + V3/ed + by O."
                    },
                    {
                        "number": 4,
                        "first": "The team scored too few goals and didn't win its last game.",
                        "second": "The team did not score [GAP] to win its last game.",
                        "acceptedAnswers": ["enough goals"],
                        "explanation": "Cấu trúc 'not... enough + danh từ' tương đương 'too few + danh từ'."
                    },
                    {
                        "number": 5,
                        "first": "The young defender performed well in his first match.",
                        "second": "The young defender gave a good [GAP] in his first match.",
                        "acceptedAnswers": ["performance"],
                        "explanation": "Chuyển đổi động từ sang cụm danh từ: perform well = give a good performance."
                    }
                ]
            },
            {
                "partNumber": 2,
                "title": "Part 2: Question 6 (Short Card to Jim)",
                "prompt": "Your English friend Jim has shown you around the famous sights of London.\nWrite a card to Jim. In your card you should:\n• Thank him for showing you the city\n• Say what you enjoyed seeing most\n• Invite Jim to visit you\nWrite 35-45 words.",
                "sampleAnswer": "Dear Jim,\nThank you so much for guiding me around London yesterday! I had a wonderful time, and seeing the view from the London Eye was definitely the best part. You must come and visit my hometown next month!\nBest regards,\nNam",
                "wordCount": 43,
                "keyPoints": [
                    "Cảm ơn Jim đã dẫn đi tham quan thành phố London",
                    "Nêu điểm tham quan thích nhất (the view from the London Eye)",
                    "Mời Jim đến thăm quê hương của bạn vào tháng sau"
                ]
            },
            {
                "partNumber": 3,
                "title": "Part 3: Questions 7 & 8 (Letter or Story)",
                "tasks": [
                    {
                        "number": 7,
                        "type": "Letter",
                        "prompt": "This is part of a letter you receive from an English pen friend:\n'In your next letter, tell me about your favourite meal. What ingredients is it made of? How often do you eat it?'\nNow write a letter answering your pen friend's questions. Write about 100 words.",
                        "sampleAnswer": "Dear Oliver,\n\nIt was lovely to hear from you! You asked about my favourite meal, so let me tell you about Pho, which is the most famous traditional noodle soup in Vietnam.\n\nIt is made with flat rice noodles, tender slices of beef, and fresh herbs like basil and coriander. The most important element is the rich broth, gently simmered with cinnamon, star anise, and beef bones for over eight hours.\n\nI usually eat Pho every weekend with my family for breakfast. The soothing aroma and hearty taste always give me energy for the whole day. You should definitely try it when you visit!\n\nBest wishes,\nLinh",
                        "wordCount": 105
                    },
                    {
                        "number": 8,
                        "type": "Story",
                        "prompt": "Your English teacher has asked you to write a story. Your story must begin with this sentence:\n'It started to rain heavily.'\nWrite your story in about 100 words.",
                        "sampleAnswer": "It started to rain heavily just as we reached the foot of the mountain. Dark thunderclouds quickly covered the sky, and cold winds whipped through our thin jackets. With no shelter nearby, my friend Liam pointed towards an old wooden hut half-hidden among the pine trees.\n\nWe dashed inside just before the storm unleashed its full fury. To our delight, the hut was dry and cozy, with an old stove and a stack of dry firewood. We lit a small fire and shared hot tea from our thermos flask, listening to the soothing sound of rain outside. It turned into an unforgettable adventure!",
                        "wordCount": 103
                    }
                ]
            }
        ]
    },
    "test_4": {
        "title": "Paper 1 - Writing (Part 1 to Part 3)",
        "duration": 40,
        "parts": [
            {
                "partNumber": 1,
                "title": "Part 1: Questions 1 - 5 (Sentence Transformation)",
                "instruction": "Here are some sentences about work and jobs. For each question, complete the second sentence so that it means the same as the first, using no more than three words. Write only the missing words.",
                "questions": [
                    {
                        "number": 1,
                        "first": "John will be at home on Saturday, if he doesn't have to work overtime.",
                        "second": "John will be at home on Saturday, [GAP] to work overtime.",
                        "acceptedAnswers": ["unless he has", "if he hasn't"],
                        "explanation": "Cấu trúc tương đương: if not = unless (John sẽ ở nhà vào thứ Bảy trừ khi anh ấy phải làm thêm giờ)."
                    },
                    {
                        "number": 2,
                        "first": "The secretary said, 'Andrew will leave early today'.",
                        "second": "The secretary said that Andrew [GAP] early that day.",
                        "acceptedAnswers": ["would leave"],
                        "explanation": "Câu gián tiếp: lùi thì từ 'will leave' thành 'would leave'."
                    },
                    {
                        "number": 3,
                        "first": "This city has very few good jobs.",
                        "second": "There are not [GAP] in this city.",
                        "acceptedAnswers": ["many good jobs", "many jobs"],
                        "explanation": "So sánh số lượng: very few = not many (không có nhiều công việc tốt)."
                    },
                    {
                        "number": 4,
                        "first": "You must not play games on your computer while at work.",
                        "second": "You are [GAP] to play games on your computer while at work.",
                        "acceptedAnswers": ["not allowed", "forbidden"],
                        "explanation": "Cấu trúc cấm đoán: must not = be not allowed to (không được phép chơi điện tử trong giờ làm)."
                    },
                    {
                        "number": 5,
                        "first": "Helen started working at the office two years ago.",
                        "second": "Helen [GAP] at the office for two years.",
                        "acceptedAnswers": ["has worked", "has been working"],
                        "explanation": "Thì hiện tại hoàn thành: started... ago = has worked... for + time."
                    }
                ]
            },
            {
                "partNumber": 2,
                "title": "Part 2: Question 6 (Email to a Friend)",
                "prompt": "You have recently moved to a new town. Write an email to your friend. In your email you should:\n• Tell your friend how happy you are\n• Say something good about your town\n• Suggest what you will do in the first week\nWrite 35-45 words.",
                "sampleAnswer": "Hi Lucas,\nI'm so thrilled with my new life here! The town is peaceful and has a gorgeous riverside park with cozy cafes. During my first week, I'm planning to join the local sports club and explore the historic market. Come visit soon!\nYours,\nAlex",
                "wordCount": 45,
                "keyPoints": [
                    "Bày tỏ sự hạnh phúc/hào hứng với nơi ở mới (so thrilled)",
                    "Khen ngợi điểm tốt của thị trấn (riverside park, cozy cafes)",
                    "Đề xuất hoạt động tuần đầu tiên (join sports club, explore market)"
                ]
            },
            {
                "partNumber": 3,
                "title": "Part 3: Questions 7 & 8 (Letter or Story)",
                "tasks": [
                    {
                        "number": 7,
                        "type": "Letter",
                        "prompt": "This is part of a letter you have received from an English pen friend:\n'That's everything about my house, I love it! What about your house? What do you like most about it?'\nNow write a letter to your pen friend, telling him/her about your house. Write about 100 words.",
                        "sampleAnswer": "Dear Emily,\n\nThanks for describing your lovely home! I am delighted to tell you about mine.\n\nI live in a comfortable two-story house located in a quiet suburb. It has three bedrooms, a sunny kitchen, and a small garden blooming with jasmine flowers. What I love most is my bedroom on the top floor. It has a large balcony overlooking the green hills, where I often sit in the afternoon with a book and hot chocolate.\n\nIt is the perfect place to relax after stressful school days. I would love for you to stay here one day!\n\nWarm wishes,\nHai",
                        "wordCount": 101
                    },
                    {
                        "number": 8,
                        "type": "Story",
                        "prompt": "Your English teacher has asked you to write a story. Your story must begin with this title:\n'My Favourite Person'\nWrite your story in about 100 words.",
                        "sampleAnswer": "My Favourite Person\n\nWhenever people ask who inspires me most, my grandfather immediately comes to mind. At seventy-five, he still wakes up at dawn every day with an infectious smile, ready to tend his vegetable garden or fix bicycles for local children.\n\nHe spent forty years as a passionate history teacher, and his captivating stories always taught me courage and kindness. Last year, when I failed my piano exam and felt like giving up, he sat beside me patiently, reminding me that true success requires perseverance. Thanks to his constant encouragement, I never lose confidence when facing life's toughest obstacles.",
                        "wordCount": 99
                    }
                ]
            }
        ]
    },
    "test_5": {
        "title": "Paper 1 - Writing (Part 1 to Part 3)",
        "duration": 40,
        "parts": [
            {
                "partNumber": 1,
                "title": "Part 1: Questions 1 - 5 (Sentence Transformation)",
                "instruction": "Here are some sentences about food and drink. For each question, complete the second sentence so that it means the same as the first, using no more than three words. Write only the missing words.",
                "questions": [
                    {
                        "number": 1,
                        "first": "I have never met such a clever man as the chef.",
                        "second": "The chef is the [GAP] man I've ever met.",
                        "acceptedAnswers": ["cleverest", "most clever"],
                        "explanation": "So sánh nhất: the cleverest / the most clever (đầu bếp thông minh nhất tôi từng gặp)."
                    },
                    {
                        "number": 2,
                        "first": "We could not sit down at the restaurant, as there were so many people.",
                        "second": "There were [GAP] people at the restaurant for us to sit down.",
                        "acceptedAnswers": ["too many"],
                        "explanation": "Cấu trúc quá mức: too many + danh từ số nhiều + for someone to do something."
                    },
                    {
                        "number": 3,
                        "first": "Only a small group of French monks make this wine.",
                        "second": "This wine [GAP] by a small group of French monks.",
                        "acceptedAnswers": ["is made", "is produced"],
                        "explanation": "Bị động thì hiện tại đơn: is/are + V3/ed + by."
                    },
                    {
                        "number": 4,
                        "first": "'Did you buy Italian food?' Jim asked Carol.",
                        "second": "Jim asked Carol if she [GAP] Italian food.",
                        "acceptedAnswers": ["had bought"],
                        "explanation": "Câu gián tiếp Yes/No: lùi thì từ quá khứ đơn 'did buy' thành quá khứ hoàn thành 'had bought'."
                    },
                    {
                        "number": 5,
                        "first": "My parents thought that we should eat healthier food.",
                        "second": "My parents wanted [GAP] healthier food.",
                        "acceptedAnswers": ["us to eat"],
                        "explanation": "Cấu trúc: want someone to do something (muốn ai đó làm gì)."
                    }
                ]
            },
            {
                "partNumber": 2,
                "title": "Part 2: Question 6 (Email to Penfriend about School)",
                "prompt": "An English friend of yours wants to know what school is like in your country.\nWrite an email to your friend. In your email you should:\n• Tell him how big your school is\n• Say something about your friends\n• Explain what subjects you like best\nWrite 35-45 words.",
                "sampleAnswer": "Hi Daniel,\nMy secondary school is quite large, with over one thousand enthusiastic students. My classmates are super friendly and helpful. I especially enjoy science and history because the experiments are fun and our teacher tells fascinating stories. What is your school like?\nWrite back,\nMinh",
                "wordCount": 44,
                "keyPoints": [
                    "Quy mô trường học (large, over 1000 students)",
                    "Mô tả về bạn bè (super friendly and helpful)",
                    "Môn học yêu thích nhất (science and history) và lý do"
                ]
            },
            {
                "partNumber": 3,
                "title": "Part 3: Questions 7 & 8 (Letter or Story)",
                "tasks": [
                    {
                        "number": 7,
                        "type": "Letter",
                        "prompt": "This is part of a letter you receive from an English pen friend:\n'I had a great time that summer. Have you ever had a great summer holiday? Tell me all about what you did.'\nNow write a letter answering your pen friend's questions. Write about 100 words.",
                        "sampleAnswer": "Dear Sophie,\n\nI was thrilled to read your letter about your summer! Let me tell you about my memorable holiday in Da Nang last July.\n\nI spent an unforgettable week there with my family. We stayed at a coastal hotel right opposite My Khe beach. Every morning, we woke up early to swim in the turquoise sea and admire the magnificent sunrise. In the afternoons, we rented bicycles to wander around the ancient town of Hoi An, sampling crispy pancakes and sweet herbal tea.\n\nIt was the most relaxing vacation I've ever experienced. Have you made plans for next year?\n\nLove,\nTrang",
                        "wordCount": 101
                    },
                    {
                        "number": 8,
                        "type": "Story",
                        "prompt": "Your English teacher has asked you to write a story. Your story must begin with this sentence:\n'I couldn't believe what my dad had just said.'\nWrite your story in about 100 words.",
                        "sampleAnswer": "I couldn't believe what my dad had just said. He calmly set down his evening newspaper and announced that our entire family had won two tickets to attend the FIFA World Cup final in London!\n\nFor seconds, stunned silence filled the living room. Then, my sister and I leaped off the sofa, cheering wildly at the top of our lungs. Football had been our greatest passion since childhood, and we had spent years watching big matches on an old television screen. Now, we were actually flying across the globe to see our heroes live on the pitch. Dreams really do come true!",
                        "wordCount": 103
                    }
                ]
            }
        ]
    },
    "test_6": {
        "title": "Paper 1 - Writing (Part 1 to Part 3)",
        "duration": 40,
        "parts": [
            {
                "partNumber": 1,
                "title": "Part 1: Questions 1 - 5 (Sentence Transformation)",
                "instruction": "Here are some sentences about travelling. For each question, complete the second sentence so that it means the same as the first, using no more than three words. Write only the missing words.",
                "questions": [
                    {
                        "number": 1,
                        "first": "You should go on a cruise.",
                        "second": "If I were you, [GAP] on a cruise.",
                        "acceptedAnswers": ["I would go", "I'd go"],
                        "explanation": "Câu khuyên nhủ điều kiện loại 2: If I were you, I would do something."
                    },
                    {
                        "number": 2,
                        "first": "It's too expensive to stay in that hotel.",
                        "second": "It isn't [GAP] to stay in that hotel.",
                        "acceptedAnswers": ["cheap enough"],
                        "explanation": "Cấu trúc tương đương: too expensive = not cheap enough."
                    },
                    {
                        "number": 3,
                        "first": "If you don't remember your passport, you won't be able to go on the plane.",
                        "second": "You won't be able to go on the plane unless [GAP] your passport.",
                        "acceptedAnswers": ["you remember"],
                        "explanation": "Cấu trúc điều kiện với 'unless': unless you remember = if you don't remember."
                    },
                    {
                        "number": 4,
                        "first": "You missed the plane because you checked in too late.",
                        "second": "If you hadn't checked in so late, you [GAP] missed the plane.",
                        "acceptedAnswers": ["would not have", "wouldn't have"],
                        "explanation": "Câu điều kiện loại 3 diễn tả giả định trái ngược quá khứ: wouldn't have + V3."
                    },
                    {
                        "number": 5,
                        "first": "There aren't many tourists in this area.",
                        "second": "There are very [GAP] in this area.",
                        "acceptedAnswers": ["few tourists", "few"],
                        "explanation": "Cấu trúc chỉ lượng: not many = very few."
                    }
                ]
            },
            {
                "partNumber": 2,
                "title": "Part 2: Question 6 (Card to Tom for Birthday CD)",
                "prompt": "An English friend of yours called Tom sent you a CD for your birthday, which you liked very much.\nWrite a card to Tom. In your card you should:\n• Thank him for the CD\n• Say which song you liked best\n• Suggest another singer that Tom might like\nWrite 35-45 words.",
                "sampleAnswer": "Dear Tom,\nThanks a million for the fantastic CD you gave me for my birthday! I absolutely love track four; the melody is catchy and uplifting. Since you like acoustic pop, you should definitely listen to Ed Sheeran. Let's hang out soon!\nCheers,\nKhoa",
                "wordCount": 44,
                "keyPoints": [
                    "Cảm ơn Tom về đĩa CD quà sinh nhật",
                    "Khen bài hát thích nhất (track four, melody is catchy)",
                    "Gợi ý ca sĩ khác Tom có thể thích (Ed Sheeran)"
                ]
            },
            {
                "partNumber": 3,
                "title": "Part 3: Questions 7 & 8 (Letter or Story)",
                "tasks": [
                    {
                        "number": 7,
                        "type": "Letter",
                        "prompt": "This is part of a letter you receive from an English pen friend:\n'What do you do at the weekend generally? Where do you like to spend time with your friends?'\nNow write a letter answering your pen friend's questions. Write about 100 words.",
                        "sampleAnswer": "Dear James,\n\nIt was great to hear from you again! Weekends are definitely my favourite time of the week.\n\nOn Saturday mornings, I usually sleep in and help my parents with light chores around the house. In the afternoon, I meet up with my closest friends at a cozy coffee shop downtown. We enjoy chatting about school, playing card games, and listening to indie music. On Sundays, if the weather is warm and sunny, we ride our bicycles to the municipal sports complex to play basketball.\n\nHow do you usually spend your weekend? Tell me in your next letter!\n\nBest wishes,\nTuan",
                        "wordCount": 102
                    },
                    {
                        "number": 8,
                        "type": "Story",
                        "prompt": "Your English teacher has asked you to write a story. Your story must begin with this sentence:\n'I couldn't believe my eyes.'\nWrite your story in about 100 words.",
                        "sampleAnswer": "I couldn't believe my eyes when I looked out of my bedroom window on Sunday morning. The familiar concrete street had vanished under a pristine blanket of glistening white snow! In our southern coastal city, snow had never fallen in recorded history.\n\nI threw on my thickest coat and rushed outside. Children from neighboring houses were already laughing, building snowmen and having cheerful snowball fights. Everything felt magical, like a fairy tale brought to life. My friends and I spent hours sculpting an enormous icy fort before heading inside for hot cocoa. It was truly a winter miracle I will never forget.",
                        "wordCount": 102
                    }
                ]
            }
        ]
    },
    "test_7": {
        "title": "Paper 1 - Writing (Part 1 to Part 3)",
        "duration": 40,
        "parts": [
            {
                "partNumber": 1,
                "title": "Part 1: Questions 1 - 5 (Sentence Transformation)",
                "instruction": "Here are some sentences about leisure and sport. For each question, complete the second sentence so that it means the same as the first, using no more than three words. Write only the missing words.",
                "questions": [
                    {
                        "number": 1,
                        "first": "The reporter described the game in detail.",
                        "second": "The reporter gave a [GAP] the game.",
                        "acceptedAnswers": ["detailed description of", "detailed account of"],
                        "explanation": "Chuyển từ động từ 'describe' sang cụm danh từ: give a detailed description of."
                    },
                    {
                        "number": 2,
                        "first": "You can borrow my racket, but you must be careful with it.",
                        "second": "You can borrow my racket as [GAP] are careful with it.",
                        "acceptedAnswers": ["long as you"],
                        "explanation": "Liên từ điều kiện: as long as you (miễn là bạn cẩn thận với nó)."
                    },
                    {
                        "number": 3,
                        "first": "She left early because she did not want to miss the start of the match.",
                        "second": "She left early [GAP] would not miss the start of the match.",
                        "acceptedAnswers": ["so that she", "in order that she"],
                        "explanation": "Mệnh đề chỉ mục đích: so that + S + modal verb (để cô ấy không bỏ lỡ trận đấu)."
                    },
                    {
                        "number": 4,
                        "first": "'I'm sorry but I don't want to play tennis', said Harry.",
                        "second": "Harry said that he [GAP] to play tennis.",
                        "acceptedAnswers": ["did not want", "didn't want", "refused"],
                        "explanation": "Câu gián tiếp: lùi thì hiện tại đơn 'don't want' thành quá khứ đơn 'didn't want'."
                    },
                    {
                        "number": 5,
                        "first": "All the players did their best apart from Alan.",
                        "second": "Alan was the only player [GAP] try his best.",
                        "acceptedAnswers": ["who did not", "who didn't"],
                        "explanation": "Mệnh đề quan hệ xác định: who didn't try his best = apart from Alan."
                    }
                ]
            },
            {
                "partNumber": 2,
                "title": "Part 2: Question 6 (Card to Sarah for Dinner Party)",
                "prompt": "An English friend of yours, called Sarah, gave a dinner party last night, which you enjoyed! Write a card to Sarah. In your card, you should:\n• Thank her for dinner\n• Say how much you enjoyed the food\n• Invite her to dinner\nWrite 35-45 words.",
                "sampleAnswer": "Dear Sarah,\nThank you so much for the wonderful dinner party last night! The roast chicken and homemade apple tart were absolutely delicious. I would love to return the hospitality, so please come to my house for traditional Vietnamese noodles this Friday!\nWarmly,\nHoa",
                "wordCount": 43,
                "keyPoints": [
                    "Cảm ơn Sarah vì bữa tiệc tối ấm cúng",
                    "Khen ngợi thức ăn (roast chicken and apple tart were delicious)",
                    "Mời Sarah đến nhà ăn tối vào thứ Sáu"
                ]
            },
            {
                "partNumber": 3,
                "title": "Part 3: Questions 7 & 8 (Letter or Story)",
                "tasks": [
                    {
                        "number": 7,
                        "type": "Letter",
                        "prompt": "This is part of a letter you receive from an English pen friend:\n'In your next letter please tell me about traditional food in your country. What's your favourite meal? Do you eat fast food?'\nNow write a letter answering your pen friend's questions. Write about 100 words.",
                        "sampleAnswer": "Dear Chloe,\n\nIt is always a pleasure to receive your letters! You asked about food in Vietnam, where cuisine is famous worldwide for fresh ingredients and rich herbs.\n\nMy personal favourite is Banh Mi, a crispy French baguette stuffed with savory pate, grilled pork, pickled vegetables, and cilantro. It combines crunchy textures with bursting flavours. As for fast food like hamburgers or fried chicken, I rarely eat them—maybe once a month with friends—because traditional street food here is much healthier, cheaper, and far more delicious.\n\nWhat kind of traditional British meals do you enjoy eating?\n\nWrite back soon,\nBao",
                        "wordCount": 101
                    },
                    {
                        "number": 8,
                        "type": "Story",
                        "prompt": "Your English teacher has asked you to write a story. Your story must begin with this sentence:\n'Jackie didn't know whether to laugh or cry.'\nWrite your story in about 100 words.",
                        "sampleAnswer": "Jackie didn't know whether to laugh or cry. Standing in the middle of his newly painted kitchen, he looked down at his golden retriever, Barney. Barney had somehow knocked over an open bucket of bright purple paint and was now joyfully wagging his colourful tail, leaving vibrant paw prints all across the polished wooden floor.\n\nJackie had spent the whole Saturday painstakingly painting the walls. Yet seeing the dog's innocent, goofy expression made it impossible to stay angry. Shaking his head in amusement, Jackie took out his phone, snapped a hilarious photo, and grabbed the mop with a chuckle.",
                        "wordCount": 99
                    }
                ]
            }
        ]
    },
    "test_8": {
        "title": "Paper 1 - Writing (Part 1 to Part 3)",
        "duration": 40,
        "parts": [
            {
                "partNumber": 1,
                "title": "Part 1: Questions 1 - 5 (Sentence Transformation)",
                "instruction": "Here are some sentences about smoking and health. For each question, complete the second sentence so that it means the same as the first, using no more than three words. Write only the missing words.",
                "questions": [
                    {
                        "number": 1,
                        "first": "Fewer people smoke than they used to.",
                        "second": "Not [GAP] people smoke as they used to.",
                        "acceptedAnswers": ["as many", "so many"],
                        "explanation": "So sánh bằng thể phủ định: not as/so many people... as (Không nhiều người hút thuốc như trước đây)."
                    },
                    {
                        "number": 2,
                        "first": "I tried to stop smoking but it was very difficult to do.",
                        "second": "Although I tried to stop smoking, [GAP] up easily.",
                        "acceptedAnswers": ["I couldn't give", "I could not give"],
                        "explanation": "Cụm động từ: give up = stop doing something."
                    },
                    {
                        "number": 3,
                        "first": "We left the bar because it was too smoky.",
                        "second": "It was [GAP] that we left the bar.",
                        "acceptedAnswers": ["so smoky"],
                        "explanation": "Cấu trúc kết quả: so + tính từ + that clause (Quá ngột ngạt khói thuốc đến nỗi chúng tôi phải rời đi)."
                    },
                    {
                        "number": 4,
                        "first": "George suggested asking the doctor to help me stop smoking.",
                        "second": "George said, 'Why don't you [GAP] to help you stop smoking?'",
                        "acceptedAnswers": ["ask the doctor"],
                        "explanation": "Lời gợi ý trực tiếp: suggest doing sth = Why don't you do sth?"
                    },
                    {
                        "number": 5,
                        "first": "I don't have the strength to stop smoking.",
                        "second": "I'm not [GAP] to stop smoking.",
                        "acceptedAnswers": ["strong enough"],
                        "explanation": "Cấu trúc: not strong enough to do something = don't have the strength."
                    }
                ]
            },
            {
                "partNumber": 2,
                "title": "Part 2: Question 6 (Email to Paul about New Restaurant)",
                "prompt": "You have just been to a new restaurant for the first time and you think your friend Paul would like it.\nWrite an email to Paul. In your email you should:\n• Explain where the restaurant is\n• Tell him what you ate\n• Say why you think he'd like it\nWrite 35-45 words.",
                "sampleAnswer": "Hi Paul,\nI discovered a fantastic Italian eatery located right next to the town hall. I tasted their wood-fired Margherita pizza and homemade gelato. Because you are crazy about authentic cheese and crispy pasta, you'll love it! Shall we dine there on Friday?\nBest,\nDavid",
                "wordCount": 44,
                "keyPoints": [
                    "Vị trí nhà hàng (next to the town hall)",
                    "Món đã ăn (wood-fired Margherita pizza, homemade gelato)",
                    "Lý do Paul sẽ thích (crazy about authentic cheese and crispy pasta)"
                ]
            },
            {
                "partNumber": 3,
                "title": "Part 3: Questions 7 & 8 (Letter or Story)",
                "tasks": [
                    {
                        "number": 7,
                        "type": "Letter",
                        "prompt": "This is part of a letter you receive from a pen friend in another country:\n'So, I have decided that it's time for me to visit your country! Where would you recommend I go? What is the weather like in August? Can I find cheap accommodation? Write and tell me what you think.'\nNow write a letter answering your pen friend's questions. Write about 100 words.",
                        "sampleAnswer": "Dear Lucas,\n\nI am thrilled to hear that you are visiting Vietnam this summer! It will be an extraordinary journey.\n\nI strongly suggest spending time in Da Nang and Hoi An. In August, the weather is warm and sunny, which is perfect for swimming and outdoor sightseeing, though short afternoon showers might occur. As for accommodation, finding budget options is very straightforward. There are abundant cozy homestays and backpacker hostels offering clean air-conditioned rooms for around fifteen dollars per night.\n\nDon't hesitate to ask if you need assistance booking tickets. I can't wait to welcome you!\n\nBest wishes,\nLong",
                        "wordCount": 99
                    },
                    {
                        "number": 8,
                        "type": "Story",
                        "prompt": "Your English teacher has asked you to write a story. Your story must have this title:\n'One of the most important days of my life'\nWrite your story in about 100 words.",
                        "sampleAnswer": "One of the most important days of my life\n\nIt was a freezing Friday morning in December when the scholarship committee published their final admission list. For months, I had spent every evening preparing essays and practicing interview questions, sacrificing social gatherings with friends. When my mother and I opened the portal, my name was displayed right at the very top.\n\nMy mother burst into tears of happiness, hugging me tightly. That pivotal moment taught me that genuine discipline and perseverance always triumph over self-doubt. It opened up a brand new chapter of educational opportunities that completely transformed my future.",
                        "wordCount": 98
                    }
                ]
            }
        ]
    },
    "test_9": {
        "title": "Paper 1 - Writing (Part 1 to Part 3)",
        "duration": 40,
        "parts": [
            {
                "partNumber": 1,
                "title": "Part 1: Questions 1 - 5 (Sentence Transformation)",
                "instruction": "Here are some sentences about my friend, Keith. For each question, complete the second sentence so that it means the same as the first, using no more than three words. Write only the missing words.",
                "questions": [
                    {
                        "number": 1,
                        "first": "I asked Keith what he had done on Saturday.",
                        "second": "I asked Keith, 'What did [GAP] on Saturday?'",
                        "acceptedAnswers": ["you do"],
                        "explanation": "Chuyển câu gián tiếp sang trực tiếp: What did you do on Saturday?"
                    },
                    {
                        "number": 2,
                        "first": "He told me that he had seen an action film.",
                        "second": "'[GAP] an action film', he told me.",
                        "acceptedAnswers": ["I saw", "I have seen", "I've seen"],
                        "explanation": "Câu trực tiếp ở thì quá khứ đơn hoặc hiện tại hoàn thành: 'I saw / I have seen'."
                    },
                    {
                        "number": 3,
                        "first": "Keith prefers action films to dramas.",
                        "second": "Keith likes action films [GAP] he likes dramas.",
                        "acceptedAnswers": ["better than", "more than"],
                        "explanation": "Cấu trúc so sánh: like something better/more than."
                    },
                    {
                        "number": 4,
                        "first": "The film was so good that they couldn't stop talking about it.",
                        "second": "It was [GAP] film that they couldn't stop talking about it.",
                        "acceptedAnswers": ["such a good"],
                        "explanation": "Cấu trúc: such + a/an + adj + noun + that..."
                    },
                    {
                        "number": 5,
                        "first": "Keith's parents let him stay out until midnight.",
                        "second": "Keith was [GAP] out until midnight.",
                        "acceptedAnswers": ["allowed to stay", "permitted to stay"],
                        "explanation": "Cấu trúc bị động: let someone do sth = be allowed to do sth."
                    }
                ]
            },
            {
                "partNumber": 2,
                "title": "Part 2: Question 6 (Card to Elizabeth about Lost MP3 Player)",
                "prompt": "You just came home from visiting your friend Elizabeth in England. Now, you can't find your MP3 player. Write a card to Elizabeth. In your card you should:\n• Thank her for hosting you and tell her you had a good time\n• Ask if you have left your MP3 player at her house\n• Describe it, and suggest where she should look for it\nWrite 35-45 words.",
                "sampleAnswer": "Dear Elizabeth,\nThanks so much for having me; I had an incredible holiday with your family! However, I can't find my silver Sony MP3 player anywhere. Could it be on the bedside table in the guest room? Please check for me!\nBest regards,\nGiang",
                "wordCount": 44,
                "keyPoints": [
                    "Cảm ơn Elizabeth vì sự đón tiếp chu đáo",
                    "Hỏi xem có để quên máy MP3 tại nhà bạn không",
                    "Mô tả máy (silver Sony MP3 player) và vị trí gợi ý tìm (bedside table in guest room)"
                ]
            },
            {
                "partNumber": 3,
                "title": "Part 3: Questions 7 & 8 (Letter or Story)",
                "tasks": [
                    {
                        "number": 7,
                        "type": "Letter",
                        "prompt": "This is part of a letter you receive from an English pen friend:\n'I'm going to Spain in June! I'm so excited, but I want to lose a bit of weight and get fit in the next few months, so that I feel comfortable at the beach. How can I do it?'\nNow write a letter giving your pen friend some advice. Write about 100 words.",
                        "sampleAnswer": "Dear Ryan,\n\nHow exciting that you are going to Spain in June! You will have an amazing holiday there.\n\nGetting in shape over the next few months is totally achievable with small daily habits. Firstly, try jogging for thirty minutes every morning or cycling to school; cardio exercises burn calories effectively and boost stamina. Secondly, cut down on sugary soft drinks and processed snacks. Instead, drink plenty of water and eat fresh fruit, lean chicken, and green vegetables. Consistency is key, so don't push yourself too hard initially.\n\nYou'll look and feel fantastic on the beach! Keep me updated on your progress.\n\nAll the best,\nQuan",
                        "wordCount": 105
                    },
                    {
                        "number": 8,
                        "type": "Story",
                        "prompt": "Your English teacher has asked you to write a story. This is the title for your story:\n'A Wonderful Surprise'\nWrite your story in about 100 words.",
                        "sampleAnswer": "A Wonderful Surprise\n\nComing home from a tiring badminton practice on my sixteenth birthday, I found our front porch in total darkness. Thinking my family had forgotten the date, I pushed the heavy oak door open with a quiet sigh.\n\nSuddenly, the lights flashed on and twenty of my closest classmates shouted 'Surprise!' Confetti fluttered through the air, and on the dining table sat a two-tier chocolate cake decorated with mini shuttlecocks. My best friend had secretly organized the entire event with my parents. Seeing everyone smiling and celebrating made it the happiest and most unforgettable birthday of my life.",
                        "wordCount": 99
                    }
                ]
            }
        ]
    },
    "test_10": {
        "title": "Paper 1 - Writing (Part 1 to Part 3)",
        "duration": 40,
        "parts": [
            {
                "partNumber": 1,
                "title": "Part 1: Questions 1 - 5 (Sentence Transformation)",
                "instruction": "Here are some sentences about me and my family. For each question, complete the second sentence so that it means the same as the first, using no more than three words. Write only the missing words.",
                "questions": [
                    {
                        "number": 1,
                        "first": "My brother started playing the violin 5 years ago.",
                        "second": "My brother [GAP] the violin for 5 years.",
                        "acceptedAnswers": ["has played", "has been playing"],
                        "explanation": "Hiện tại hoàn thành / tiếp diễn: started playing... ago = has played / has been playing... for + time."
                    },
                    {
                        "number": 2,
                        "first": "My father is a musician. He is the best guitar player I have ever seen!",
                        "second": "My father [GAP] all the other guitar players I have seen so far!",
                        "acceptedAnswers": ["plays better than", "is better than"],
                        "explanation": "So sánh hơn: plays better than all the other guitar players."
                    },
                    {
                        "number": 3,
                        "first": "My brother told me he wanted a scarf for his birthday.",
                        "second": "'[GAP] a scarf for my birthday,' said my brother.",
                        "acceptedAnswers": ["I want", "I would like", "I'd like"],
                        "explanation": "Chuyển câu gián tiếp sang trực tiếp: 'I want / I would like a scarf'."
                    },
                    {
                        "number": 4,
                        "first": "I very rarely go into the city centre, so I don't know where to shop.",
                        "second": "I am [GAP] shopping in the city centre.",
                        "acceptedAnswers": ["not used to"],
                        "explanation": "Cấu trúc quen thuộc: be not used to + V-ing (chưa quen với việc mua sắm ở trung tâm thành phố)."
                    },
                    {
                        "number": 5,
                        "first": "My mother told me the high street would be more affordable than the mall.",
                        "second": "My mother told me the mall would [GAP] affordable than the high street.",
                        "acceptedAnswers": ["be less"],
                        "explanation": "So sánh kém hơn: more affordable than = be less affordable than."
                    }
                ]
            },
            {
                "partNumber": 2,
                "title": "Part 2: Question 6 (Email Complaint to Online Clothing Store)",
                "prompt": "You recently bought a T-shirt from a company on the internet. You are not at all happy with the purchase.\nWrite an email to the company to complain. Include the following points:\n• took too long to arrive\n• fits well, but is not good quality\n• would like a refund\nWrite 35-45 words.",
                "sampleAnswer": "Dear Customer Support,\nI am writing regarding order #4829. The T-shirt took over four weeks to arrive. Although the size fits nicely, the fabric is extremely thin and frayed. Therefore, I request a full refund to my bank card.\nSincerely,\nEmma",
                "wordCount": 42,
                "keyPoints": [
                    "Giao hàng quá chậm (took over four weeks to arrive)",
                    "Vừa vặn nhưng chất lượng kém (fits nicely, but fabric is thin and frayed)",
                    "Yêu cầu hoàn tiền (request a full refund)"
                ]
            },
            {
                "partNumber": 3,
                "title": "Part 3: Questions 7 & 8 (Letter or Story)",
                "tasks": [
                    {
                        "number": 7,
                        "type": "Letter",
                        "prompt": "This is part of a letter you received from an English pen friend:\n'I'm so excited to be coming to visit you this summer! What do I need to bring with me?'\nNow write a letter, telling your pen friend what he or she needs to bring. Write about 100 words.",
                        "sampleAnswer": "Dear Jack,\n\nI can't wait to see you this summer! It is going to be a blast.\n\nSince our summer climate is hot and humid, make sure to pack lightweight cotton T-shirts, comfortable shorts, and a sturdy pair of sandals. Don't forget your swimming trunks, as we'll spend several days lounging by the beach. You should also bring strong sunscreen and sunglasses to protect against intense sunshine. Finally, bring a light waterproof jacket or compact umbrella for sudden tropical downpours.\n\nLet me know your flight details as soon as you book them so I can meet you!\n\nBest,\nThang",
                        "wordCount": 99
                    },
                    {
                        "number": 8,
                        "type": "Story",
                        "prompt": "Your English teacher has asked you to write a story. This is the title for your story:\n'A Frightening Experience'\nWrite your story in about 100 words.",
                        "sampleAnswer": "A Frightening Experience\n\nWhile camping in Cuc Phuong National Park last autumn, my cousin and I decided to take a short evening hike before dusk. However, mist rolled in swiftly, obscuring the trail markers. Within an hour, darkness had engulfed the dense forest, and our flashlight batteries suddenly died.\n\nStrange rustling sounds echoed in the bamboo groves around us, making our hearts pound violently against our chests. Clinging to each other, we blew our emergency whistles repeatedly. Fortunately, twenty nerve-wracking minutes later, park rangers with powerful searchlights found us. Sitting safely by their ranger station fire, I breathed the greatest sigh of relief.",
                        "wordCount": 102
                    }
                ]
            }
        ]
    }
}

# Now inject these writing tests into data.js
with open('data.js', 'r', encoding='utf-8') as f:
    raw = f.read()

prefix = 'window.PET_DATA = '
suffix = ';\n'
if raw.startswith(prefix):
    json_str = raw[len(prefix):].rstrip(';\n')
else:
    json_str = raw

pet_data = json.loads(json_str)

for test_id, w_data in tests_writing.items():
    test_obj = next((t for t in pet_data['practiceTests'] if t['id'] == test_id), None)
    if test_obj:
        test_obj['writing'] = w_data
        print(f"Updated writing for {test_id}")
    else:
        print(f"Warning: {test_id} not found!")

# Save back to data.js
new_content = prefix + json.dumps(pet_data, ensure_ascii=False, indent=2) + suffix
with open('data.js', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Successfully injected all authentic writing data for Tests 3 to 10 into data.js!")
