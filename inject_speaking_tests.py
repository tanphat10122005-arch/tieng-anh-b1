# -*- coding: utf-8 -*-
"""
Generate complete 12 Speaking Tests for Cambridge B1 Preliminary
Matching the exact topics and images in the book.
"""
import json

new_speaking_tests = [
    # Test 3: Journey in a car
    {
        "id": "spk_3",
        "title": "Speaking Test 3",
        "topic": "Journey in a Car & Public Transport",
        "part1": {
            "questions": [
                "How do you usually travel to school or work every day?",
                "Do you prefer travelling by car or by train?",
                "Tell me about a memorable journey you have been on.",
                "Have you ever experienced a traffic jam?"
            ],
            "sampleAnswers": [
                "I usually travel to school by electric bicycle because it is convenient, affordable, and helps avoid morning traffic.",
                "I definitely prefer travelling by train because you can sit comfortably, read a book, and admire panoramic countryside scenery through large windows.",
                "Last summer, my family took a memorable six-hour coastal road trip to Nha Trang. The coastal scenery with limestone cliffs and sparkling blue sea was stunning.",
                "Yes, quite frequently during rush hour in big cities. It can be frustrating, but I usually pass the time by listening to English podcasts or upbeat music."
            ]
        },
        "part2": {
            "title": "Part 2: Simulated Situation (Journey in a Car)",
            "image": "assets/speaking/test3_part2.png",
            "scenario": "A family is planning a long five-hour car trip with two young children. Talk together about the different things they could bring to keep the children entertained (audiobooks, handheld games, travel pillow, snacks, map, drawing kit) and decide which two are most useful.",
            "usefulPhrases": [
                "Why don't we consider bringing...",
                "Children easily get bored, so handheld games are very practical.",
                "On the other hand, looking at screens for too long might cause car sickness.",
                "Healthy snacks and water are essential for keeping their energy and mood up.",
                "I think the drawing kit and healthy snacks are the two best choices."
            ],
            "sampleDialogue": "Candidate A: A five-hour journey is quite long for young kids. What should the parents bring?\nCandidate B: Handheld video games will keep them completely occupied, but staring at a screen in a moving vehicle often causes nausea.\nCandidate A: That's a valid point. What about audiobooks or an engaging story CD that the whole family can listen to together?\nCandidate B: Excellent idea! It encourages their imagination. And of course, having plenty of fresh fruit, juice, and healthy snacks is indispensable.\nCandidate A: Exactly. Children get cranky when hungry. So shall we select the family audiobooks and the snack basket as the two top essentials?\nCandidate B: I totally agree with that decision!"
        },
        "part3": {
            "title": "Part 3: Photograph Description",
            "image": "assets/speaking/test3_part3.png",
            "photoA": {
                "title": "Photo A: Commuters waiting on a modern railway platform",
                "description": "In this photograph, I can see several commuters standing on a clean, modern railway station platform on a brisk morning. A high-speed electric train is pulling into the station. Some passengers are looking at the digital departure boards, while others are checking their mobile smartphones or carrying briefcases and backpacks. In the background, there are large glass architectural structures letting in natural daylight. The overall atmosphere feels organized, punctual, and typical of an urban morning commute."
            },
            "photoB": {
                "title": "Photo B: Traffic congestion in a crowded city street",
                "description": "In contrast to the railway station, this image depicts a heavily congested city boulevard during evening peak hours. Yellow taxis, red double-decker buses, and private cars are stuck in a standstill queue. Pedestrians on the sidewalks are walking briskly with umbrellas under misty rain. Bright red taillights and shopfront neon signs reflect on the wet asphalt pavement, conveying a busy, vibrant yet chaotic urban evening."
            }
        },
        "part4": {
            "title": "Part 4: Extended Discussion",
            "questions": [
                "What can governments do to encourage people to use public transport?",
                "Do you think electric vehicles will completely replace petrol cars in the future?",
                "Is it better to travel alone or with friends and family?"
            ],
            "sampleAnswers": [
                "Governments should modernize bus and metro networks, ensure affordable ticket prices, and expand dedicated bus lanes so public transit is faster and more reliable than driving.",
                "Yes, I believe so. As battery technology improves and charging stations become ubiquitous, zero-emission electric vehicles are essential to combat air pollution and climate change.",
                "Travelling with close friends or family is much more enjoyable because sharing memorable experiences, delicious meals, and funny moments creates deeper bonds."
            ]
        }
    },
    # Test 4: School trip
    {
        "id": "spk_4",
        "title": "Speaking Test 4",
        "topic": "School Trip & Historical Sites",
        "part1": {
            "questions": [
                "Have you ever been on a school excursion?",
                "What kind of museums or exhibitions do you find most fascinating?",
                "Do you prefer learning history from textbooks or by visiting historic sites?",
                "What is your favourite subject at school?"
            ],
            "sampleAnswers": [
                "Yes, last semester my school arranged a field trip to the National History Museum, which was both educational and enjoyable.",
                "I find interactive science and technology exhibitions most captivating because visitors can conduct hands-on experiments rather than just looking at artifacts behind glass.",
                "Visiting authentic historic monuments is far more inspiring because standing inside century-old castles or ancient temples makes historical events come alive vividly.",
                "My favourite subject is geography because it allows me to explore diverse cultures, climates, and natural wonders across the world."
            ]
        },
        "part2": {
            "title": "Part 2: Simulated Situation (School Trip)",
            "image": "assets/speaking/test4_part2.png",
            "scenario": "A secondary school class is planning an end-of-term educational day trip. Talk together about the various destinations they could visit (theme park, science centre, ancient castle, art gallery, wildlife reserve, botanical garden) and choose the best one for all students.",
            "usefulPhrases": [
                "Let's look at the science centre first.",
                "A theme park is fun, but it lacks educational value for a school trip.",
                "An ancient castle offers rich historical insights and scenic outdoor grounds.",
                "A wildlife nature reserve combines environmental education with outdoor walking.",
                "I believe the science discovery centre offers the ideal blend of learning and fun."
            ],
            "sampleDialogue": "Candidate A: We need to choose the best destination for the class day trip. What do you think about the amusement theme park?\nCandidate B: Well, it's very entertaining, but our teachers will certainly prefer somewhere with educational value.\nCandidate A: You're right. How about the ancient castle or the interactive science centre?\nCandidate B: The science centre is fantastic because it has 3D planetarium shows and hands-on experiments that cater to everyone's curiosity.\nCandidate A: That sounds brilliant! It's both educational and engaging for teenagers. Shall we agree on the science centre?\nCandidate B: Absolutely, that's an ideal choice."
        },
        "part3": {
            "title": "Part 3: Photograph Description",
            "image": "assets/speaking/test4_part3.png",
            "photoA": {
                "title": "Photo A: Students examining exhibits in a natural history museum",
                "description": "In this photograph, a group of teenage students and their teacher are gathered in a spacious museum hall around a towering prehistoric dinosaur skeleton. Several students are taking notes on clipboards, while the guide is gesturing upwards and explaining fascinating facts. The gallery is well-lit with spotlights illuminating ancient fossils and informative placards. The students appear genuinely fascinated and engaged in the lesson."
            },
            "photoB": {
                "title": "Photo B: Schoolchildren doing outdoor science fieldwork near a pond",
                "description": "This photograph shows an energetic outdoor learning session in a lush green countryside park. A group of primary school children wearing waterproof boots are kneeling near the edge of a freshwater pond. They are holding small nets and magnifying glasses to examine aquatic plants and insects in plastic trays. Their teacher is smiling and assisting a student. The sunny, nature-filled environment conveys curiosity, teamwork, and healthy outdoor exploration."
            }
        },
        "part4": {
            "title": "Part 4: Extended Discussion",
            "questions": [
                "Why are school field trips important for students' development?",
                "Should museums and art galleries offer free admission to students?",
                "How can technology enhance learning in modern classrooms?"
            ],
            "sampleAnswers": [
                "Field trips bridge the gap between classroom theory and real-world practice, fostering practical curiosity, social teamwork, and memorable bonding with peers.",
                "Definitely. Free access encourages young people from all socioeconomic backgrounds to appreciate culture, history, and scientific progress without financial barriers.",
                "Digital interactive whiteboards, VR virtual field trips, and educational apps make complex concepts intuitive, engaging visual learners and keeping students motivated."
            ]
        }
    },
    # Test 6: Camping holiday
    {
        "id": "spk_6",
        "title": "Speaking Test 6",
        "topic": "Camping Holiday & Outdoor Adventure",
        "part1": {
            "questions": [
                "Have you ever slept in a tent outdoors?",
                "Do you enjoy spending time in nature and forests?",
                "What items do you always take when going on a picnic?",
                "Do you prefer staying in luxury hotels or outdoor campsites?"
            ],
            "sampleAnswers": [
                "Yes, I went on a two-day camping trip to Ba Vi National Park with my scouts group last year, and sleeping under canvas was an amazing experience.",
                "I truly love nature because the tranquil atmosphere, chirping birds, and fresh pine-scented air completely refresh my mind after busy study weeks.",
                "I always bring a waterproof mat, homemade sandwiches, fresh fruit, a portable speaker, and insect repellent.",
                "While hotels are comfortable, camping provides a genuine sense of adventure, outdoor campfire cooking, and stargazing that hotels cannot match."
            ]
        },
        "part2": {
            "title": "Part 2: Simulated Situation (Camping Trip)",
            "image": "assets/speaking/test6_part2.png",
            "scenario": "A group of teenage friends are going on their first weekend camping expedition in the countryside. Discuss the essential gear they should bring (waterproof tent, warm sleeping bag, gas stove, first aid kit, sturdy boots, solar torch) and agree on the two most crucial items.",
            "usefulPhrases": [
                "Without a sturdy waterproof tent, bad weather will ruin the trip.",
                "Night temperatures in the mountains drop sharply, so a warm sleeping bag is vital.",
                "Safety comes first, so a basic first-aid kit is non-negotiable.",
                "Cooking over a portable gas stove is very convenient.",
                "Let's agree that the tent and the first-aid kit are the two most essential items."
            ],
            "sampleDialogue": "Candidate A: Our friends are preparing for their first wild camping weekend. What gear is top priority?\nCandidate B: A durable, waterproof tent is definitely mandatory. If it rains at night, having dry shelter protects everything.\nCandidate A: Very true. And what about cooking equipment versus safety items?\nCandidate B: While a gas stove is convenient, a comprehensive first-aid kit is much more critical in case of cuts, insect bites, or minor sprains miles from town.\nCandidate A: I agree completely. Safety and shelter must always come first. So the tent and the first-aid kit are our top two choices.\nCandidate B: Perfect, we have reached an agreement!"
        },
        "part3": {
            "title": "Part 3: Photograph Description",
            "image": "assets/speaking/test6_part3.png",
            "photoA": {
                "title": "Photo A: Setting up a campsite beside a serene lake",
                "description": "In this photograph, two young backpackers are pitching a modern orange dome tent on a grassy lakeside campsite in late afternoon. Behind them, a calm lake mirrors majestic mountain peaks bathed in golden sunset light. They have unpacked their large trekking rucksacks and rolled out insulating sleeping pads. The scene conveys peaceful camaraderie, self-reliance, and deep harmony with the great outdoors."
            },
            "photoB": {
                "title": "Photo B: Friends gathered around an evening campfire",
                "description": "In contrast, this photograph captures a lively night-time campfire scene. Four cheerful friends wearing wool sweaters are sitting on wooden logs around crackling yellow flames. One young man is strumming an acoustic guitar while the others toast marshmallows on wooden skewers and sing along. Sparks drift into the dark starry night sky, radiating warmth, laughter, and youthful friendship."
            }
        },
        "part4": {
            "title": "Part 4: Extended Discussion",
            "questions": [
                "What skills can young people learn from outdoor camping?",
                "What rules should campers follow to protect the natural environment?",
                "Would you like to try extreme survival camping on a deserted island?"
            ],
            "sampleAnswers": [
                "Camping teaches resourcefulness, fire safety, map reading, teamwork, and resilience when overcoming unexpected weather challenges.",
                "Campers must strictly follow 'Leave No Trace' principles: pack out all plastic rubbish, extinguish campfires completely, and respect native wildlife habitats.",
                "It sounds thrilling, but I would need thorough survival training first because finding clean drinking water and foraging food requires serious preparation!"
            ]
        }
    },
    # Test 7: Mother's Day present
    {
        "id": "spk_7",
        "title": "Speaking Test 7",
        "topic": "Mother's Day & Gift Giving",
        "part1": {
            "questions": [
                "How do you usually celebrate special family occasions in your country?",
                "What was the best present you have ever received?",
                "Do you prefer buying gifts or making homemade presents?",
                "Who in your family are you closest to?"
            ],
            "sampleAnswers": [
                "We usually celebrate special family occasions by cooking a large traditional feast together, sharing stories, and presenting thoughtful gifts or flowers.",
                "The best present I ever received was a classical acoustic guitar from my parents on my fifteenth birthday, which inspired my passion for music.",
                "I prefer handmade gifts like photo scrapbooks or baked cakes because they carry personal effort, love, and emotional significance.",
                "I am closest to my mother because she is an empathetic listener and always offers wise, gentle guidance whenever I face difficult decisions."
            ]
        },
        "part2": {
            "title": "Part 2: Simulated Situation (Mother's Day Present)",
            "image": "assets/speaking/test7_part2.png",
            "scenario": "Two siblings want to buy a thoughtful Mother's Day gift for their hard-working mother. Talk together about the various gift options (spa treatment voucher, bouquet of roses, perfume, kitchen appliance, weekend family dinner, smart watch) and decide which gift she will appreciate most.",
            "usefulPhrases": [
                "Our mother works very hard, so she deserves relaxation.",
                "A kitchen appliance feels too much like daily work rather than a treat.",
                "A full-day luxury spa and wellness voucher would allow her to totally unwind.",
                "Alternatively, cooking her a special family dinner creates meaningful memories together.",
                "I believe combining flowers with a spa massage voucher is the sweetest gesture."
            ],
            "sampleDialogue": "Candidate A: Mother's Day is next Sunday. What present should we prepare for mum?\nCandidate B: Some people buy kitchen appliances, but I feel that just reminds her of daily cooking duties. She deserves pampering!\nCandidate A: That's so true. What about a bottle of designer perfume or a relaxing spa wellness package?\nCandidate B: The spa voucher is fantastic! She's been complaining of neck stiffness from office work. A soothing massage and aromatherapy will relieve all her stress.\nCandidate A: And we can pair it with a fresh bouquet of her favourite sunflowers. Shall we go with that idea?\nCandidate B: Yes, she will absolutely cherish that thoughtful surprise!"
        },
        "part3": {
            "title": "Part 3: Photograph Description",
            "image": "assets/speaking/test7_part3.png",
            "photoA": {
                "title": "Photo A: A family presenting gifts and a cake on Mother's Day",
                "description": "In this photograph, a smiling mother is sitting at a brightly decorated dining table surrounded by her husband and two young children. Her daughter is handing her a beautifully wrapped gift box with a silk ribbon, while her son holds up a colourful hand-drawn greeting card. In the center of the table is a lovely strawberry sponge cake with lit candles. The warm living room lighting creates an intimate, heartwarming atmosphere filled with gratitude and family love."
            },
            "photoB": {
                "title": "Photo B: A mother and daughter enjoying a sunny picnic in a botanical garden",
                "description": "This photograph shows a mother and her teenage daughter spending quality leisure time outdoors on a checkered picnic blanket in a blossoming park. They are laughing happily while sharing homemade cupcakes and sparkling fruit juice. Around them, pink cherry blossoms and lush green lawns stretch under clear blue skies. It represents deep mutual affection, companionship, and genuine relaxation."
            }
        },
        "part4": {
            "title": "Part 4: Extended Discussion",
            "questions": [
                "Why is it important to show appreciation to parents regularly, not just on holidays?",
                "Do you think commercial festivals encourage people to spend too much money?",
                "What is the most meaningful way to express gratitude to someone who helped you?"
            ],
            "sampleAnswers": [
                "Parents dedicate immense love and sacrifice to nurture us every day, so small daily gestures—like preparing tea or saying thank you—mean much more than once-a-year gifts.",
                "Yes, commercial advertising often pressures people to buy expensive items, whereas heartfelt handwritten notes and spent time together carry far deeper value.",
                "A sincere handwritten letter detailing how their guidance made a tangible difference in your life is the most touching and memorable expression of gratitude."
            ]
        }
    },
    # Test 8: Visit from a friend
    {
        "id": "spk_8",
        "title": "Speaking Test 8",
        "topic": "Visit from a Friend & City Tour",
        "part1": {
            "questions": [
                "How do you feel when friends come to stay at your home?",
                "What is the most interesting attraction in your local area?",
                "Where do you usually take foreign visitors to eat?",
                "What kind of entertainment is popular in your neighborhood?"
            ],
            "sampleAnswers": [
                "I always feel delighted and enthusiastic because hosting friends allows us to share our local culture and enjoy long conversations late into the night.",
                "The most historic attraction in my city is the old citadel, featuring imperial architecture, ancient stone gates, and serene lotus ponds.",
                "I always take them to bustling street food quarters to taste genuine local delicacies like sizzling pancakes, fresh spring rolls, and iced milk coffee.",
                "Going to modern cinema complexes, singing in karaoke lounges, and strolling along weekend pedestrian walking streets are extremely popular."
            ]
        },
        "part2": {
            "title": "Part 2: Simulated Situation (Visit from an English Friend)",
            "image": "assets/speaking/test8_part2.png",
            "scenario": "An English friend is visiting your city for just one single weekend. Discuss the various activities you could organize (open-top sightseeing bus tour, street food night market, modern art gallery, traditional puppet theatre, riverside boat cruise, shopping mall) and pick the best itinerary for Saturday evening.",
            "usefulPhrases": [
                "Since our friend has only one weekend, we should choose uniquely local experiences.",
                "A modern shopping mall can be found anywhere in the world.",
                "The street food night market offers authentic flavours, lively sounds, and cultural immersion.",
                "A sunset riverside boat cruise gives a magnificent view of the illuminated bridges.",
                "Let's combine the riverside cruise with exploring the night food market."
            ],
            "sampleDialogue": "Candidate A: Our English friend has only 48 hours in our city. What should we plan for Saturday evening?\nCandidate B: We could visit the contemporary art museum, but it closes early at 6 pm.\nCandidate A: How about a sunset cruise along the river, followed by dinner at the vibrant night food market?\nCandidate B: That sounds fantastic! From the riverboat, he can view the city skyline sparkling with colorful lights. Then at the food market, he can taste authentic street dishes.\nCandidate A: Exactly, it showcases both the picturesque scenery and the culinary vibrancy of our city. Shall we finalize that schedule?\nCandidate B: Yes, he is going to have an unforgettable evening!"
        },
        "part3": {
            "title": "Part 3: Photograph Description",
            "image": "assets/speaking/test8_part3.png",
            "photoA": {
                "title": "Photo A: Tourists on an open-top double decker tour bus",
                "description": "In this photograph, a diverse group of cheerful tourists are seated on the upper deck of a bright red open-top tour bus driving past historic gothic buildings. A young woman in sunglasses is taking photos with her DSLR camera, while a guide in a headset points towards a famous clock tower in the distance. The weather is clear and breezy, conveying excitement, curiosity, and pleasant urban sightseeing."
            },
            "photoB": {
                "title": "Photo B: Friends browsing colorful souvenir stalls at a night market",
                "description": "In contrast, this photograph displays a bustling outdoor night market lit by glowing hanging lanterns. Two friends are browsing colorful handicraft stalls filled with hand-woven silk scarves, lacquerware, and ceramic bowls. In the blurred background, steam rises from nearby sizzling food carts where cooks are preparing local skewers. The atmosphere feels lively, authentic, and bursting with cultural charm."
            }
        },
        "part4": {
            "title": "Part 4: Extended Discussion",
            "questions": [
                "What qualities make someone an outstanding host when guests visit?",
                "What can tourists do to respect local customs when visiting another country?",
                "Do you think tourism benefits or harms traditional local communities?"
            ],
            "sampleAnswers": [
                "A great host is attentive, thoughtful about dietary preferences, flexible with scheduling, and eager to make guests feel relaxed like at home.",
                "Tourists should dress modestly when visiting religious sites, learn a few polite phrases in the native language, and avoid speaking overly loudly in public spaces.",
                "Tourism brings vital economic income and cultural pride, but excessive mass tourism can cause overcrowding and environmental damage if not managed responsibly."
            ]
        }
    },
    # Test 9: Interesting class
    {
        "id": "spk_9",
        "title": "Speaking Test 9",
        "topic": "Interesting Class & Lifelong Learning",
        "part1": {
            "questions": [
                "What extra classes or workshops have you attended outside school?",
                "If you could learn any new skill tomorrow, what would it be?",
                "Do you prefer learning in small groups or one-on-one with a tutor?",
                "How do you stay focused when studying difficult subjects?"
            ],
            "sampleAnswers": [
                "I attended a three-month graphic design workshop last summer, which taught me photo editing and digital illustration techniques.",
                "I would love to learn culinary pastry arts because baking French croissants and decorated cakes has always been a dream of mine.",
                "I prefer small interactive groups of four to six learners because peer discussions generate diverse ideas and encourage friendly motivation.",
                "I break my study time into 25-minute Pomodoro sessions, keep my phone in another room, and listen to instrumental background music."
            ]
        },
        "part2": {
            "title": "Part 2: Simulated Situation (Interesting Class)",
            "image": "assets/speaking/test9_part2.png",
            "scenario": "A community youth centre is introducing free weekend evening workshops for teenagers. Discuss the different courses they could offer (photography, public speaking, coding & robotics, cooking, martial arts, foreign languages) and decide which two would attract the highest number of teenagers.",
            "usefulPhrases": [
                "Coding and robotics are in high demand for future careers.",
                "On the other hand, cooking is an essential practical life skill.",
                "Photography appeals to almost everyone who uses social media.",
                "Public speaking builds confidence, but some shy students might hesitate.",
                "I think photography and coding are the two most attractive and modern options."
            ],
            "sampleDialogue": "Candidate A: The community centre wants to attract lots of local teenagers. Which workshops should they offer?\nCandidate B: Digital photography and video editing would be extremely popular because all teenagers want to create stunning content for Instagram and TikTok.\nCandidate A: That's very true! And for the second workshop, what about coding and app development?\nCandidate B: Excellent recommendation. Tech skills are exciting, highly valued by parents, and open up great future career opportunities.\nCandidate A: So we agree on Photography & Content Creation, and Coding & App Development as the two most engaging choices?\nCandidate B: Absolutely, those two are sure to be fully booked!"
        },
        "part3": {
            "title": "Part 3: Photograph Description",
            "image": "assets/speaking/test9_part3.png",
            "photoA": {
                "title": "Photo A: An interactive high-tech robotics workshop",
                "description": "In this photograph, a group of teenage students in a brightly lit modern computer laboratory are collaborating around a small wheeled robotic vehicle. A young girl with safety glasses is adjusting wires with a screwdriver, while her teammate is typing Python code into a laptop monitor. Their instructor is leaning in to offer constructive feedback. The atmosphere reflects intense concentration, scientific curiosity, and high-tech teamwork."
            },
            "photoB": {
                "title": "Photo B: Students learning pottery and sculpting in an art studio",
                "description": "In contrast to the computer lab, this photograph portrays an artistic, creative environment in a sunlit pottery studio. A student is working at a spinning pottery wheel, shaping wet clay into a smooth ceramic vase with focused hands. Splatters of clay cover her apron, and wooden shelves behind her hold finished glazed bowls and cups. The scene conveys patience, mindfulness, and artistic craftsmanship."
            }
        },
        "part4": {
            "title": "Part 4: Extended Discussion",
            "questions": [
                "Should practical life skills like cooking and budgeting be mandatory in high schools?",
                "Can online video tutorials fully replace learning from human teachers?",
                "How important is it for adults to continue learning new skills throughout life?"
            ],
            "sampleAnswers": [
                "Yes, definitely. Many graduates excel academically but struggle with basic meal preparation, tax filing, or household maintenance when living independently.",
                "Online tutorials are great for self-paced review, but real human mentors provide instant feedback, personalized empathy, and emotional encouragement that videos lack.",
                "Lifelong learning keeps our brains active and adaptable in an era of rapid technological change, while expanding personal horizons and social connections."
            ]
        }
    },
    # Test 10: Your favourite pet
    {
        "id": "spk_10",
        "title": "Speaking Test 10",
        "topic": "Pets & Animal Welfare",
        "part1": {
            "questions": [
                "Do you have a pet at home, or did you have one when you were younger?",
                "What are the benefits of having pets for children?",
                "Which animal do you think makes the ideal companion in an apartment?",
                "What responsibilities come with adopting a rescue dog?"
            ],
            "sampleAnswers": [
                "Yes, our family has a playful ginger cat named Miu who loves curling up on my lap while I study.",
                "Pets teach children empathy, gentleness, and daily responsibility through feeding, grooming, and walking them.",
                "A domestic cat or a small rabbit is ideal for apartment living because they are quiet, clean, and do not require large open gardens.",
                "Adopting a dog requires commitment: regular vet check-ups, daily exercise walks regardless of weather, proper training, and endless patience."
            ]
        },
        "part2": {
            "title": "Part 2: Simulated Situation (Choosing a Pet for an Elderly Relative)",
            "image": "assets/speaking/test10_part2.png",
            "scenario": "An elderly grandmother who lives alone in a quiet suburban cottage wants to get a pet for companionship. Talk together about the various animals she could consider (energetic puppy, calm adult cat, singing canary bird, aquarium fish, small tortoise) and decide which one is most suitable for her.",
            "usefulPhrases": [
                "An energetic puppy requires too much physical walking and strenuous exercise.",
                "Goldfish are peaceful to watch, but you cannot hug or cuddle them.",
                "A calm adult cat is affectionate, independent, and easy to care for indoors.",
                "A canary bird sings sweetly and needs minimal physical maintenance.",
                "I believe a calm adult rescue cat is the ideal companion for warmth and affection."
            ],
            "sampleDialogue": "Candidate A: Our grandmother wants a companion animal. An energetic puppy might be too demanding for her knees, right?\nCandidate B: Definitely. Puppies jump around and need two long walks every day. What about a gentle, mature adult cat?\nCandidate A: That's a wonderful suggestion! Adult cats are already house-trained, peaceful, and love sleeping beside someone on the sofa while purring.\nCandidate B: Exactly. And unlike fish or tortoises, a cat interacts warmly with its owner. What about a canary bird?\nCandidate A: A bird is sweet, but cleaning the cage can be fiddly, and she can't pet it. A mature cat offers genuine emotional affection and companionship.\nCandidate B: I agree wholeheartedly. A gentle adult cat is the perfect choice for grandma!"
        },
        "part3": {
            "title": "Part 3: Photograph Description",
            "image": "assets/speaking/test10_part3.png",
            "photoA": {
                "title": "Photo A: A veterinary nurse examining a golden retriever puppy",
                "description": "In this photograph, a friendly female veterinary nurse in teal medical scrubs is examining an adorable golden retriever puppy on a stainless steel examination table. She is using a stethoscope to listen to the puppy's heartbeat while gently stroking its head to keep it calm. The clinic appears spotlessly clean and modern, equipped with diagnostic charts on the wall. The nurse's warm smile reflects professionalism and deep compassion for animals."
            },
            "photoB": {
                "title": "Photo B: Volunteers walking rescue dogs in a sunny meadow",
                "description": "In contrast, this photograph shows an outdoor scene at an animal rescue sanctuary on a sunny morning. Two smiling young volunteers in branded charity t-shirts are walking several joyful rescue dogs on leashes across a wide wildflower meadow. The dogs are happily sniffing grass and wagging their tails. The bright blue sky and lush greenery emphasize freedom, care, and the heartwarming work of animal rescue shelters."
            }
        },
        "part4": {
            "title": "Part 4: Extended Discussion",
            "questions": [
                "Why should prospective pet owners adopt from rescue shelters rather than buying from pet shops?",
                "Do you think zoos play a positive or negative role in modern wildlife conservation?",
                "How can city authorities create more pet-friendly public environments?"
            ],
            "sampleAnswers": [
                "Adopting from shelters saves vulnerable animals from euthanasia, combats unethical puppy breeding mills, and gives abandoned pets a deserving second chance at happiness.",
                "Modern accredited conservation zoos help preserve endangered species through breeding programmes and educational awareness, though keeping large animals in confined enclosures remains controversial.",
                "Cities should designate fenced dog agility parks, install free waste disposal bag dispensers, and permit well-behaved leashed pets on public transport during off-peak hours."
            ]
        }
    }
]

# Load existing data.js
with open('data.js', 'r', encoding='utf-8') as f:
    raw = f.read()

prefix = 'window.PET_DATA = '
suffix = ';\n'
if raw.startswith(prefix):
    json_str = raw[len(prefix):].rstrip(';\n')
else:
    json_str = raw

pet_data = json.loads(json_str)

existing_spk = pet_data.get('speakingTests', [])
print(f"Current speaking tests: {len(existing_spk)}")

# Merge new speaking tests, keeping existing ones if any
existing_ids = {s['id'] for s in existing_spk}
for new_s in new_speaking_tests:
    if new_s['id'] not in existing_ids:
        existing_spk.append(new_s)
        print(f"Added {new_s['id']} - {new_s['title']}")

# Sort speaking tests by ID
def get_spk_num(item):
    try:
        return int(item['id'].replace('spk_', ''))
    except:
        return 999

existing_spk.sort(key=get_spk_num)
pet_data['speakingTests'] = existing_spk

# Write back
with open('data.js', 'w', encoding='utf-8') as f:
    f.write(prefix + json.dumps(pet_data, ensure_ascii=False, indent=2) + suffix)

print(f"Total speaking tests in data.js now: {len(pet_data['speakingTests'])}")
for s in pet_data['speakingTests']:
    print(f"  {s['id']}: {s['title']} - {s['topic']}")
