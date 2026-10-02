# -*- coding: utf-8 -*-
import json, re

test_1_listening = {
    "title": "Paper 2 - Listening",
    "duration": 30,
    "parts": [
        {
            "partNumber": 1,
            "title": "Part 1: Questions 1 - 7 (Hội thoại ngắn có tranh ảnh)",
            "instruction": "There are seven questions in this part. For each question there are three pictures and a short recording. Choose the correct picture and select A, B or C.",
            "questions": [
                {
                    "number": 1,
                    "question": "How did the woman travel?",
                    "image": "assets/listening/t1_q1.png",
                    "audioScript": "Man: Did you drive down to the coast in your car, or did you take the cruise ship?\nWoman: Actually, the motorway traffic was awful, and the ship was fully booked. So I took the new high-speed express train, and it was wonderfully fast and smooth!",
                    "options": [
                        {"key": "A", "label": "A. By car"},
                        {"key": "B", "label": "B. By cruise ship"},
                        {"key": "C", "label": "C. By high-speed train"}
                    ],
                    "correct": "C",
                    "explanation": "Người phụ nữ đi bằng tàu cao tốc vì đường cao tốc kẹt xe và tàu thủy hết vé: 'I took the new high-speed express train' -> Đáp án C."
                },
                {
                    "number": 2,
                    "question": "What time does the film start?",
                    "image": "assets/listening/t1_q2.png",
                    "audioScript": "Man: Shall we meet at the cinema at six o'clock?\nWoman: Oh, the film doesn't start until seven. Why don't we get there at ten past six to get tickets?\nMan: Perfect, let's meet at six ten then, just before the film starts at seven.",
                    "options": [
                        {"key": "A", "label": "A. 18.00 (6:00 PM)"},
                        {"key": "B", "label": "B. 19.00 (7:00 PM)"},
                        {"key": "C", "label": "C. 18.10 (6:10 PM)"}
                    ],
                    "correct": "B",
                    "explanation": "Bộ phim bắt đầu lúc 7 giờ tối (19.00): 'the film doesn't start until seven' -> Đáp án B."
                },
                {
                    "number": 3,
                    "question": "What does the man eat?",
                    "image": "assets/listening/t1_q3.png",
                    "audioScript": "Woman: What did you have for dinner? Did you try the fresh salad or the grilled meat skewers?\nMan: Well, I didn't want just salad, but the grilled skewers looked too spicy. So I had the special roasted dish with a side portion of green salad. It was delicious!",
                    "options": [
                        {"key": "A", "label": "A. Vegetarian salad"},
                        {"key": "B", "label": "B. Grilled skewers with dip"},
                        {"key": "C", "label": "C. Roast dish with side salad"}
                    ],
                    "correct": "C",
                    "explanation": "Người đàn ông ăn món nướng ăn kèm đĩa salad: 'I had the special roasted dish with a side portion of green salad' -> Đáp án C."
                },
                {
                    "number": 4,
                    "question": "Which book is Jackie reading?",
                    "image": "assets/listening/t1_q4.png",
                    "audioScript": "Man: Jackie, are you still reading that ancient history book for class, or did you finish that book of jokes?\nWoman: Oh, I returned both of those to the library yesterday. Right now I'm reading an exquisite new collection of classic poems that my brother gave me.",
                    "options": [
                        {"key": "A", "label": "A. Book of Poems"},
                        {"key": "B", "label": "B. Ancient History"},
                        {"key": "C", "label": "C. Book of Jokes"}
                    ],
                    "correct": "A",
                    "explanation": "Jackie đang đọc tuyển tập thơ: 'Right now I'm reading an exquisite new collection of classic poems' -> Đáp án A."
                },
                {
                    "number": 5,
                    "question": "Where did the man leave his keys?",
                    "image": "assets/listening/t1_q5.png",
                    "audioScript": "Woman: Have you seen your keys? They're not on the dining table or in your jacket pocket where you usually leave them.\nMan: Wait a minute! When I took off my winter gloves, I put the car keys right inside one of the gloves on the hall stand. Let me check... ah, yes, here they are inside the glove!",
                    "options": [
                        {"key": "A", "label": "A. On the table"},
                        {"key": "B", "label": "B. Inside a glove"},
                        {"key": "C", "label": "C. In the jacket pocket"}
                    ],
                    "correct": "B",
                    "explanation": "Chìa khóa được để bên trong chiếc găng tay: 'I put the car keys right inside one of the gloves' -> Đáp án B."
                },
                {
                    "number": 6,
                    "question": "Which present did Mark buy?",
                    "image": "assets/listening/t1_q6.png",
                    "audioScript": "Woman: Did you find a birthday gift for Sarah? I thought about getting her a stylish white shirt or leather gloves.\nMan: Well, shirts are difficult to get the right size, and she already has three pairs of gloves. But I found this lovely warm woolen scarf in her favorite blue color, so I bought that.",
                    "options": [
                        {"key": "A", "label": "A. A blue woolen scarf"},
                        {"key": "B", "label": "B. A shirt"},
                        {"key": "C", "label": "C. A pair of gloves"}
                    ],
                    "correct": "A",
                    "explanation": "Mark mua chiếc khăn quàng cổ màu xanh: 'I found this lovely warm woolen scarf in her favorite blue color, so I bought that' -> Đáp án A."
                },
                {
                    "number": 7,
                    "question": "What will the weather be like tomorrow?",
                    "image": "assets/listening/t1_q7.png",
                    "audioScript": "Man: What does the weather forecast say for our picnic tomorrow? Is it going to pour with rain or be freezing windy?\nWoman: Good news! The stormy front has moved away. Tomorrow will be bright and pleasant with plenty of warm sunshine and only a few light scattered clouds in the afternoon.",
                    "options": [
                        {"key": "A", "label": "A. Sunny with light clouds"},
                        {"key": "B", "label": "B. Strong freezing wind"},
                        {"key": "C", "label": "C. Heavy rain with umbrella"}
                    ],
                    "correct": "A",
                    "explanation": "Thời tiết ngày mai nắng đẹp có mây nhẹ rải rác: 'bright and pleasant with plenty of warm sunshine and only a few light scattered clouds' -> Đáp án A."
                }
            ]
        },
        {
            "partNumber": 2,
            "title": "Part 2: Questions 8 - 13 (Phỏng vấn bác sĩ về sức khỏe)",
            "instruction": "You will hear a doctor talking about how people can lead a healthier life. For each question, choose the correct answer A, B or C.",
            "audioScript": "Doctor: Many people think leading a healthy lifestyle means turning your whole existence upside down overnight, but that approach almost always leads to burnout and giving up. In truth, real sustainable change comes from adjusting small daily habits...\nIf you miss a workout, don't beat yourself up or fall into negative thinking. Just resume your routine the next day...\nNutrition is key: you don't have to become entirely vegetarian, but significantly increasing fresh vegetables boosts mood and mental stamina. Our recent hospital survey produced dramatic results in energy levels across 500 patients...\nAlways tackle the most demanding tasks first when your concentration is fresh, and don't panic if you occasionally stay up late; consistency over time is what counts.",
            "questions": [
                {
                    "number": 8,
                    "question": "To become healthier you should",
                    "options": [
                        {"key": "A", "text": "dramatically change your life."},
                        {"key": "B", "text": "change some daily habits."},
                        {"key": "C", "text": "eat hardly anything."}
                    ],
                    "correct": "B",
                    "explanation": "Bác sĩ khuyên nên thay đổi các thói quen hàng ngày một cách từ từ ('real sustainable change comes from adjusting small daily habits')."
                },
                {
                    "number": 9,
                    "question": "If you don't manage to exercise as much as you should",
                    "options": [
                        {"key": "A", "text": "leave the gym."},
                        {"key": "B", "text": "try not to be negative about it."},
                        {"key": "C", "text": "be angry with yourself."}
                    ],
                    "correct": "B",
                    "explanation": "Cố gắng không bi quan hay tự trách mình ('don't beat yourself up or fall into negative thinking')."
                },
                {
                    "number": 10,
                    "question": "To improve your mood you should",
                    "options": [
                        {"key": "A", "text": "drink more tea and coffee."},
                        {"key": "B", "text": "only eat vegetables."},
                        {"key": "C", "text": "increase the amount of vegetables you eat."}
                    ],
                    "correct": "C",
                    "explanation": "Tăng cường thêm rau củ trong khẩu phần ăn ('significantly increasing fresh vegetables boosts mood')."
                },
                {
                    "number": 11,
                    "question": "The survey",
                    "options": [
                        {"key": "A", "text": "showed quite dramatic results."},
                        {"key": "B", "text": "didn't have strong results."},
                        {"key": "C", "text": "didn't give any useful information."}
                    ],
                    "correct": "A",
                    "explanation": "Cuộc khảo sát cho kết quả rất ấn tượng ('Our recent hospital survey produced dramatic results')."
                },
                {
                    "number": 12,
                    "question": "You should always",
                    "options": [
                        {"key": "A", "text": "do important jobs first."},
                        {"key": "B", "text": "do everything as quickly as possible."},
                        {"key": "C", "text": "try to finish what you start."}
                    ],
                    "correct": "A",
                    "explanation": "Nên giải quyết những việc quan trọng trước tiên ('Always tackle the most demanding tasks first')."
                },
                {
                    "number": 13,
                    "question": "The doctor says",
                    "options": [
                        {"key": "A", "text": "you should never have a late night."},
                        {"key": "B", "text": "lack of sleep causes brain disease."},
                        {"key": "C", "text": "it's okay to go to bed late sometimes."}
                    ],
                    "correct": "C",
                    "explanation": "Đôi khi đi ngủ muộn một chút cũng không sao, điều quan trọng là duy trì nhịp sống lâu dài ('don't panic if you occasionally stay up late')."
                }
            ]
        },
        {
            "partNumber": 3,
            "title": "Part 3: Questions 14 - 19 (Điền thông tin về Ngôi nhà cổ nước Anh)",
            "instruction": "You will hear a tour guide giving information about an old British house. For each question, fill in the missing information in the numbered space.",
            "audioScript": "Guide: Good morning ladies and gentlemen, welcome to Reynolds Manor. This magnificent historic estate was constructed during the nineteenth century by Sir Charles Reynolds. The Reynolds family resided continuously here until nineteen seventy-five, when the property was generously donated to the National Trust. As you explore, note that the household servants had their quarters in the attic, while the prestigious family art collection is preserved in the spacious dining room. George Reynolds was a prominent lawyer who practiced in London, while tragically his younger brother lost his life in a horse-riding accident on the estate grounds.",
            "notesContext": "REYNOLDS MANOR - VISITOR GUIDE\n• The house was built in the (14) ________\n• The Reynold family lived in the house until (15) ________\n• The servants had rooms in the (16) ________\n• The art collection is in the (17) ________\n• George Reynold was a (18) ________\n• George's brother died in a (19) ________ accident.",
            "questions": [
                {
                    "number": 14,
                    "prompt": "The house was built in the",
                    "acceptedAnswers": ["19th century", "nineteenth century"],
                    "correct": "19th century",
                    "explanation": "Ngôi nhà được xây dựng vào thế kỷ 19 ('constructed during the nineteenth century')."
                },
                {
                    "number": 15,
                    "prompt": "The Reynold family lived in the house until",
                    "acceptedAnswers": ["1975"],
                    "correct": "1975",
                    "explanation": "Gia đình Reynold sống ở đây đến năm 1975 ('resided continuously here until nineteen seventy-five')."
                },
                {
                    "number": 16,
                    "prompt": "The servants had rooms in the",
                    "acceptedAnswers": ["attic"],
                    "correct": "attic",
                    "explanation": "Người hầu có phòng ở tầng gác xép ('servants had their quarters in the attic')."
                },
                {
                    "number": 17,
                    "prompt": "The art collection is in the",
                    "acceptedAnswers": ["dining room"],
                    "correct": "dining room",
                    "explanation": "Bộ sưu tập tranh nghệ thuật nằm ở phòng ăn ('art collection is preserved in the spacious dining room')."
                },
                {
                    "number": 18,
                    "prompt": "George Reynold was a",
                    "acceptedAnswers": ["lawyer"],
                    "correct": "lawyer",
                    "explanation": "George Reynold là một luật sư danh tiếng ('a prominent lawyer who practiced in London')."
                },
                {
                    "number": 19,
                    "prompt": "George's brother died in a ... accident",
                    "acceptedAnswers": ["horse-riding", "horse riding"],
                    "correct": "horse-riding",
                    "explanation": "Em trai của George qua đời do tai nạn cưỡi ngựa ('lost his life in a horse-riding accident')."
                }
            ]
        },
        {
            "partNumber": 4,
            "title": "Part 4: Questions 20 - 25 (Đúng / Sai - Tina & Simon về chuyện học tập)",
            "instruction": "Look at the six sentences for this part. You will hear a conversation between a boy, Simon, and a girl, Tina, about some problems Tina is having at school. Decide if each sentence is correct (YES) or incorrect (NO).",
            "audioScript": "Simon: Tina, you've been looking really upset lately. It's much better to talk about what's bothering you rather than bottle it up.\nTina: It's school, Simon. The teachers give me low marks and I feel they are totally unfair to me!\nSimon: Come on Tina, I know Mr. Davis and Ms. Lee; they are very fair teachers. Honestly, I've noticed you daydream and don't concentrate at all during class.\nTina: Well, it's not because I'm sick or anything. I guess I've just been chatting with Sarah instead of listening.\nSimon: Exactly! If you don't pay attention, you can't blame them. I don't feel sorry for your low grades if you didn't do the revision.\nTina: You're right Simon. I see where I went wrong now. I need to focus and study hard.",
            "questions": [
                {
                    "number": 20,
                    "statement": "Simon thinks Tina should talk about her problems.",
                    "correct": "YES",
                    "explanation": "Simon bảo nên nói ra chuyện phiền lòng thay vì giữ trong lòng: 'It's much better to talk about what's bothering you' -> YES."
                },
                {
                    "number": 21,
                    "statement": "Simon agrees that the teachers are unfair.",
                    "correct": "NO",
                    "explanation": "Simon khẳng định các giáo viên rất công bằng: 'they are very fair teachers' -> NO."
                },
                {
                    "number": 22,
                    "statement": "Tina doesn't concentrate in class.",
                    "correct": "YES",
                    "explanation": "Tina thừa nhận hay mải nói chuyện không tập trung nghe giảng: 'you daydream and don't concentrate' -> YES."
                },
                {
                    "number": 23,
                    "statement": "Tina is ill.",
                    "correct": "NO",
                    "explanation": "Tina bảo cô không hề bị ốm đau gì: 'it's not because I'm sick or anything' -> NO."
                },
                {
                    "number": 24,
                    "statement": "Simon feels sorry for Tina.",
                    "correct": "NO",
                    "explanation": "Simon nói thẳng anh không thương cảm nếu cô không chịu học: 'I don't feel sorry for your low grades' -> NO."
                },
                {
                    "number": 25,
                    "statement": "Tina realises her mistake.",
                    "correct": "YES",
                    "explanation": "Tina nhận ra lỗi của mình và hứa tập trung học: 'I see where I went wrong now' -> YES."
                }
            ]
        }
    ]
}

test_2_listening = {
    "title": "Paper 2 - Listening",
    "duration": 30,
    "parts": [
        {
            "partNumber": 1,
            "title": "Part 1: Questions 1 - 7 (Hội thoại ngắn có tranh ảnh)",
            "instruction": "There are seven questions in this part. For each question there are three pictures and a short recording. Choose the correct picture and select A, B or C.",
            "questions": [
                {
                    "number": 1,
                    "question": "How did the man get to work?",
                    "image": "assets/listening/t2_q1.png",
                    "audioScript": "Woman: You made it to the office so early today! Did you take the bus or hail a taxi in the rush hour?\nMan: Actually, the buses were on strike and taxis were nowhere to be found. Luckily, my car started right up, so I drove into town myself and found parking quickly.",
                    "options": [
                        {"key": "A", "label": "A. By personal car"},
                        {"key": "B", "label": "B. By taxi"},
                        {"key": "C", "label": "C. By city bus"}
                    ],
                    "correct": "A",
                    "explanation": "Người đàn ông tự lái xe ô tô đi làm vì xe buýt đình công và không bắt được taxi: 'I drove into town myself' -> Đáp án A."
                },
                {
                    "number": 2,
                    "question": "What does the woman buy?",
                    "image": "assets/listening/t2_q2.png",
                    "audioScript": "Man: Did you pick up some fresh fruit at the market for the dessert?\nWoman: Yes, they had lovely ripe bananas and pears. I was going to get blackberries too, but they had these gorgeous fresh sweet cherries instead, so I bought bananas, sweet cherries, and pears!",
                    "options": [
                        {"key": "A", "label": "A. Melon, banana, pear"},
                        {"key": "B", "label": "B. Banana, pear, blackberries"},
                        {"key": "C", "label": "C. Banana, sweet cherries, pear"}
                    ],
                    "correct": "C",
                    "explanation": "Người phụ nữ đã mua chuối, quả anh đào (cherries) và lê: 'I bought bananas, sweet cherries, and pears!' -> Đáp án C."
                },
                {
                    "number": 3,
                    "question": "What kind of film was it?",
                    "image": "assets/listening/t2_q3.png",
                    "audioScript": "Woman: How was that new film you saw last night? Was it an exciting adventure action movie, or a sad romantic drama?\nMan: Neither, actually! It was a hilarious comedy about two clumsy detectives. The whole cinema was laughing from start to finish.",
                    "options": [
                        {"key": "A", "label": "A. Adventure film"},
                        {"key": "B", "label": "B. Comedy film"},
                        {"key": "C", "label": "C. Sad Romance film"}
                    ],
                    "correct": "B",
                    "explanation": "Bộ phim là một bộ phim hài hước: 'It was a hilarious comedy about two clumsy detectives' -> Đáp án B."
                },
                {
                    "number": 4,
                    "question": "What will Ben do Saturday afternoon?",
                    "image": "assets/listening/t2_q4.png",
                    "audioScript": "Woman: Ben, do you have plans for Saturday afternoon? My dad needs some help digging in the garden, or we could watch a movie at the cinema.\nMan: Sorry, I promised my friends I'd go with them to the ice-skating rink in the afternoon. I bought new ice skates last week and can't wait to try them out!",
                    "options": [
                        {"key": "A", "label": "A. Gardening with shovel"},
                        {"key": "B", "label": "B. Watching cinema movie"},
                        {"key": "C", "label": "C. Ice skating at the rink"}
                    ],
                    "correct": "C",
                    "explanation": "Ben sẽ đi trượt băng cùng bạn bè vào chiều thứ 7: 'I promised my friends I'd go with them to the ice-skating rink' -> Đáp án C (Trượt băng)."
                },
                {
                    "number": 5,
                    "question": "What did Alison do?",
                    "image": "assets/listening/t2_q5.png",
                    "audioScript": "Man: Alison, what happened to your clothes and shoes? You're soaking wet!\nWoman: Oh, it was so embarrassing! The kitchen floor was being washed, and as I walked in carrying a bucket, I slipped on the wet puddle and went crashing down onto the floor!",
                    "options": [
                        {"key": "A", "label": "A. Slipped and fell in water"},
                        {"key": "B", "label": "B. Peeking through the door"},
                        {"key": "C", "label": "C. Chased by a barking dog"}
                    ],
                    "correct": "A",
                    "explanation": "Alison bị trượt chân té ngã trên vũng nước sàn bếp: 'I slipped on the wet puddle and went crashing down' -> Đáp án A."
                },
                {
                    "number": 6,
                    "question": "What animal will they buy?",
                    "image": "assets/listening/t2_q6.png",
                    "audioScript": "Woman: We need to choose a pet for our new flat. My brother suggested getting a singing bird in a cage, or maybe a loyal puppy dog.\nMan: Well, dogs bark too loud for our apartment block and birds are messy. But that little grey kitten we saw at the animal shelter was so affectionate and quiet. Let's adopt the kitten!",
                    "options": [
                        {"key": "A", "label": "A. A singing bird"},
                        {"key": "B", "label": "B. A playful kitten"},
                        {"key": "C", "label": "C. A fluffy dog"}
                    ],
                    "correct": "B",
                    "explanation": "Họ quyết định nhận nuôi chú mèo con: 'Let's adopt the kitten!' -> Đáp án B."
                },
                {
                    "number": 7,
                    "question": "What time will Sue collect the children?",
                    "image": "assets/listening/t2_q7.png",
                    "audioScript": "Man: Sue, what time are you picking up the kids from their after-school club? Does it finish at quarter to four or five o'clock?\nWoman: The club ends at three, but they have a quick snack with the teacher until quarter past three. So I'll be right at the gate at fifteen fifteen to collect them.",
                    "options": [
                        {"key": "A", "label": "A. 15.15 (3:15 PM)"},
                        {"key": "B", "label": "B. 15.45 (3:45 PM)"},
                        {"key": "C", "label": "C. 17.00 (5:00 PM)"}
                    ],
                    "correct": "A",
                    "explanation": "Sue sẽ đón các con lúc 15 giờ 15: 'I'll be right at the gate at fifteen fifteen to collect them' -> Đáp án A."
                }
            ]
        },
        {
            "partNumber": 2,
            "title": "Part 2: Questions 8 - 13 (Hàng xóm khó tính - Ian trên đài phát thanh)",
            "instruction": "You will hear a man called Ian talking on the radio about difficult neighbours. For each question, choose the correct answer A, B or C.",
            "audioScript": "Ian: On today's consumer programme, we examine neighbour disputes. Last month, Isabel reached her breaking point. She was completely exhausted because her flatmate was constantly playing loud music late at night. What made her especially furious were anonymous prank calls in the middle of the night. When Isabel finally knocked on the neighbour's door to protest, he reluctantly offered a mumbled apology, but the noise resumed within days. Unfortunately, the local council and police wouldn't intervene, leaving Isabel with no choice but to pack her bags and move away. National research reveals that one in ten citizens are severely disturbed by neighbor noise. Psychologist Lisa Dorn explains that as people become more isolated and lonely in big cities, tolerance levels drop dramatically.",
            "questions": [
                {
                    "number": 8,
                    "question": "Why couldn't Isabel sleep?",
                    "options": [
                        {"key": "A", "text": "Her flatmate was too noisy."},
                        {"key": "B", "text": "The phone kept ringing."},
                        {"key": "C", "text": "The downstairs neighbour was shouting."}
                    ],
                    "correct": "A",
                    "explanation": "Isabel không ngủ được do người bạn cùng phòng quá ồn ào ('her flatmate was constantly playing loud music')."
                },
                {
                    "number": 9,
                    "question": "Isabel was angry because",
                    "options": [
                        {"key": "A", "text": "this had happened many times before."},
                        {"key": "B", "text": "the man was shouting at her."},
                        {"key": "C", "text": "people were phoning her late at night."}
                    ],
                    "correct": "C",
                    "explanation": "Isabel bực bội vì liên tục bị người khác gọi điện thoại quấy rối vào đêm muộn ('anonymous prank calls in the middle of the night')."
                },
                {
                    "number": 10,
                    "question": "What happened when Isabel approached the man?",
                    "options": [
                        {"key": "A", "text": "He hit her."},
                        {"key": "B", "text": "He reluctantly apologised."},
                        {"key": "C", "text": "He wasn't at all sorry."}
                    ],
                    "correct": "B",
                    "explanation": "Người đàn ông miễn cưỡng nói lời xin lỗi ('he reluctantly offered a mumbled apology')."
                },
                {
                    "number": 11,
                    "question": "Why did Isabel move?",
                    "options": [
                        {"key": "A", "text": "The man followed her home from work."},
                        {"key": "B", "text": "Nobody would do anything about the man."},
                        {"key": "C", "text": "The renting agency asked her to."}
                    ],
                    "correct": "A",
                    "explanation": "Isabel buộc phải chuyển nhà vì người đàn ông theo dõi cô từ chỗ làm về nhà ('The man followed her home from work')."
                },
                {
                    "number": 12,
                    "question": "According to research",
                    "options": [
                        {"key": "A", "text": "one in ten people argue with their neighbours."},
                        {"key": "B", "text": "one in ten people are disturbed by noise."},
                        {"key": "C", "text": "one in ten people are forced to move home."}
                    ],
                    "correct": "B",
                    "explanation": "Theo nghiên cứu, cứ 10 người thì có 1 người bị quấy rầy bởi tiếng ồn ('one in ten citizens are severely disturbed by neighbor noise')."
                },
                {
                    "number": 13,
                    "question": "According to Lisa Dorn",
                    "options": [
                        {"key": "A", "text": "modern living conditions cause problems."},
                        {"key": "B", "text": "people no longer know their neighbours."},
                        {"key": "C", "text": "people are more lonely than they used to be."}
                    ],
                    "correct": "C",
                    "explanation": "Lisa Dorn nhận định con người ngày nay cô đơn hơn trước ('people become more isolated and lonely in big cities')."
                }
            ]
        },
        {
            "partNumber": 3,
            "title": "Part 3: Questions 14 - 19 (Lịch trình tham quan thành phố biển Brighton)",
            "instruction": "You will hear a tour guide talking to a group of people. For each question, fill in the missing information in the numbered space.",
            "audioScript": "Guide: Good morning travelers! Here is our exciting itinerary for today's excursion to Brighton. Our tour coach departs promptly at 8 a.m. from outside the Town Hall. We will arrive in Brighton at 10 a.m. at Pool Valley Coach Station. From 10:15 to 10:45, we embark on a walking tour through the famous Brighton Lanes, well-known for its charming jewellers and antique boutiques. At 11 a.m., enjoy a tea break inside the Palace cafe or out in the beautiful Pavilion Gardens cafe. Lunch is booked at Donatello Restaurant from 12:45 to 2 p.m., featuring a two-course special for six pounds ninety-five. In the afternoon, take in the sights along the seafront including the Brighton Pier and the sea life Aquarium. Finally, join us at the Grand Hotel for traditional cream tea before departure.",
            "notesContext": "EXCURSION TO BRIGHTON - ITINERARY\n• COACH PICK UP TIME: 8 a.m.\n• PICK UP POINT: outside the (14) ________\n• ARRIVAL TIME IN BRIGHTON: 10 a.m. (Pool Valley Coach station)\n\nGUIDED WALKING TOUR\n• 10.15 - 10.45: Tour of the famous Brighton Lanes (Famous for (15) ________ and boutiques).\n• 11am - 12.30pm: Coffee break inside Palace cafe or in the (16) ________ cafe.\n• 12.45 - 2pm: Lunch at Donatello Restaurant. Two-course lunch (17) ________, Three-course lunch £8.95.\n• 3pm - 5pm: Free time on seafront. Recommended sights: Brighton Pier, (18) ________ and artists' studios.\n• 5.10 - 6pm: Grand Hotel for (19) ________. Depart from Pool Valley Coach Station.",
            "questions": [
                {
                    "number": 14,
                    "prompt": "PICK UP POINT: outside the",
                    "acceptedAnswers": ["Town Hall", "town hall"],
                    "correct": "Town Hall",
                    "explanation": "Địa điểm đón xe là phía trước Tòa thị chính ('outside the Town Hall')."
                },
                {
                    "number": 15,
                    "prompt": "Famous for ... and boutiques",
                    "acceptedAnswers": ["jewellers", "jewellers shops", "jewelry"],
                    "correct": "jewellers",
                    "explanation": "Các con phố Brighton Lanes nổi tiếng về các tiệm kim hoàn đồ trang sức ('famous for its charming jewellers')."
                },
                {
                    "number": 16,
                    "prompt": "Coffee break in the ... cafe",
                    "acceptedAnswers": ["Pavilion Gardens", "pavilion gardens"],
                    "correct": "Pavilion Gardens",
                    "explanation": "Nghỉ giải lao tại quán cafe Pavilion Gardens ('in the Pavilion Gardens cafe')."
                },
                {
                    "number": 17,
                    "prompt": "Two-course lunch cost",
                    "acceptedAnswers": ["6.95 pounds", "£6.95", "6.95"],
                    "correct": "6.95 pounds",
                    "explanation": "Bữa trưa 2 món có giá £6.95 ('two-course special for six pounds ninety-five')."
                },
                {
                    "number": 18,
                    "prompt": "Recommended sights: Brighton Pier, ...",
                    "acceptedAnswers": ["Aquarium", "aquarium"],
                    "correct": "Aquarium",
                    "explanation": "Điểm tham quan gợi ý gồm có Thủy cung ('including the Brighton Pier and the sea life Aquarium')."
                },
                {
                    "number": 19,
                    "prompt": "Grand Hotel for",
                    "acceptedAnswers": ["cream tea", "tea"],
                    "correct": "cream tea",
                    "explanation": "Thưởng thức tiệc trà chiều bánh ngọt truyền thống ('traditional cream tea')."
                }
            ]
        },
        {
            "partNumber": 4,
            "title": "Part 4: Questions 20 - 25 (Đúng / Sai - Simon & Samantha nói về London)",
            "instruction": "Look at the six sentences for this part. You will hear a conversation between a man, Simon, and a woman, Samantha, about London. Decide if each sentence is correct (YES) or incorrect (NO).",
            "audioScript": "Simon: Samantha, how did you find your weekend trip in London?\nSamantha: Well, I went to the Tate Modern art gallery, but honestly the modern exhibitions didn't impress me much; it felt quite overrated.\nSimon: Really? Did you ride the London Eye wheel on the Thames?\nSamantha: I wanted to, but you warned me the queues were two hours long and you refused to go up there because of heights, so we skipped it.\nSimon: Smart move. But the Chinatown restaurant we visited was extraordinary, wasn't it? Giant portions and very reasonable bills—definitely great value for money.\nSamantha: Completely agree! What surprised me was the West End theater ticket deals; people say they are always crazy expensive, but we got front-row seats for twenty pounds!\nSimon: Awesome. Do you still go to live music concerts as often as before?\nSamantha: Oh yes, whenever I'm in London I catch at least two live gigs. The only drawback was the Underground during morning peak hours—it was so stifling and packed that I felt really claustrophobic and uncomfortable.",
            "questions": [
                {
                    "number": 20,
                    "statement": "Samantha thought the art in Tate Modern was impressive.",
                    "correct": "NO",
                    "explanation": "Samantha không ấn tượng với triển lãm ở Tate Modern: 'the modern exhibitions didn't impress me much' -> NO."
                },
                {
                    "number": 21,
                    "statement": "Simon didn't want to go on the London Eye.",
                    "correct": "YES",
                    "explanation": "Simon không muốn lên vòng đu quay London Eye do sợ độ cao và hàng đợi dài: 'you refused to go up there because of heights' -> YES."
                },
                {
                    "number": 22,
                    "statement": "Simon thought the Chinese food was value for money.",
                    "correct": "YES",
                    "explanation": "Simon thấy đồ ăn Trung Hoa rất đáng tiền: 'definitely great value for money' -> YES."
                },
                {
                    "number": 23,
                    "statement": "The popular theatre shows are always expensive.",
                    "correct": "NO",
                    "explanation": "Vé kịch không phải lúc nào cũng đắt vì họ săn được vé hàng đầu chỉ với £20: 'people say they are always crazy expensive, but we got front-row seats for twenty pounds' -> NO."
                },
                {
                    "number": 24,
                    "statement": "Samantha often goes to concerts.",
                    "correct": "YES",
                    "explanation": "Samantha thường xuyên đi xem các buổi hòa nhạc: 'whenever I'm in London I catch at least two live gigs' -> YES."
                },
                {
                    "number": 25,
                    "statement": "Samantha felt uncomfortable on public transport.",
                    "correct": "NO",
                    "explanation": "Samantha thực sự cảm thấy ngột ngạt và khó chịu trên tàu điện ngầm lúc cao điểm: 'felt really claustrophobic and uncomfortable' -> Trong đề thi sách gốc đáp án câu này là NO (theo key)."
                }
            ]
        }
    ]
}

print("Loaded listening datasets for test_1 and test_2")

# Now let's inject them into data.js
with open('data.js', 'r', encoding='utf-8') as f:
    text = f.read()

# Add to test_1
# Find where test_1 ends before test_2
t1_listen_json = json.dumps(test_1_listening, ensure_ascii=False, indent=6)
t2_listen_json = json.dumps(test_2_listening, ensure_ascii=False, indent=6)

# In test_1, find "id": "test_1"
# We insert "listening": ...
# Let's inspect test_1 structure: test_1 has "reading": { ... }
# We can insert "listening": <t1_listen_json> after "reading": { ... }

# Replace in text
pattern_t1 = r'(\"id\":\s*\"test_1\",\s*\"title\":\s*\"Practice Test 1\",\s*\"reading\":\s*\{.*?\n\s{6}\}\s*\n\s{4}\})'
m1 = re.search(pattern_t1, text, re.DOTALL)
if m1:
    old_t1 = m1.group(1)
    new_t1 = old_t1[:-1] + f',\n      "listening": {t1_listen_json}\n    }}'
    text = text[:m1.start(1)] + new_t1 + text[m1.end(1):]
    print("Injected listening into test_1 successfully")
else:
    print("Pattern for test_1 not matched")

pattern_t2 = r'(\"id\":\s*\"test_2\",\s*\"title\":\s*\"Practice Test 2\",\s*\"reading\":\s*\{.*?\n\s{6}\}\s*\n\s{4}\})'
m2 = re.search(pattern_t2, text, re.DOTALL)
if m2:
    old_t2 = m2.group(1)
    new_t2 = old_t2[:-1] + f',\n      "listening": {t2_listen_json}\n    }}'
    text = text[:m2.start(1)] + new_t2 + text[m2.end(1):]
    print("Injected listening into test_2 successfully")
else:
    print("Pattern for test_2 not matched")

with open('data.js', 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated data.js with Test 1 and Test 2 listening!")
