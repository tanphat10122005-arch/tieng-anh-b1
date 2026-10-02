#!/usr/bin/env python3
"""
Rewrite all 10 Speaking Tests in data.js with:
1. B1-level vocabulary (simple, everyday English)
2. Photo descriptions that MATCH the actual images from the book
3. Sample answers using short, clear sentences a B1 student can produce
"""

import re, json

DATA_FILE = "data.js"

# Read the file
with open(DATA_FILE, "r", encoding="utf-8") as f:
    content = f.read()

# Find the speakingTests array
pattern = r'("speakingTests"\s*:\s*)\[[\s\S]*?\]\s*(?=,\s*"vocabulary")'
match = re.search(pattern, content)
if not match:
    print("ERROR: Could not find speakingTests array")
    exit(1)

print(f"Found speakingTests at position {match.start()}-{match.end()}")

# Build new B1-level speaking tests with ACCURATE photo descriptions
new_speaking_tests = [
    # ============ TEST 1 ============
    {
        "id": "spk_1",
        "title": "Speaking Test 1",
        "topic": "Starting a New Hobby & Landscapes",
        "part1": {
            "questions": [
                "What's your name and where do you come from?",
                "Do you work or are you a student?",
                "What do you enjoy doing in your free time?",
                "Do you prefer staying indoors or going outside?"
            ],
            "sampleAnswers": [
                "My name is Nam and I come from Hanoi, Vietnam.",
                "I am a student. I study at a university.",
                "In my free time, I like playing guitar, reading books, and riding my bicycle with friends.",
                "I prefer going outside because I like fresh air and sunshine."
            ]
        },
        "part2": {
            "title": "Part 2: Simulated Situation (Starting a Hobby)",
            "image": "assets/speaking/test1_part2.png",
            "scenario": "A young person wants to take up a new hobby to relax after work and meet people. Talk together about the different hobbies they could choose (sailing, playing piano, hiking, horse riding, ballet, tennis) and decide which one is best.",
            "usefulPhrases": [
                "Shall we start with...",
                "What do you think about tennis?",
                "Playing piano is nice, but you usually do it alone.",
                "Hiking is good for health and you can meet other people.",
                "I think tennis is the best choice because you play with other people."
            ],
            "sampleDialogue": "Candidate A: Let's talk about the hobbies. What about playing piano?\\nCandidate B: Piano is nice, but you usually play alone at home. Our friend wants to meet people.\\nCandidate A: You're right. What about sailing or horse riding?\\nCandidate B: They are exciting, but they are expensive. Hiking or tennis is easier to start.\\nCandidate A: I agree. I think tennis is the best because you can join a club and meet new people. What do you think?\\nCandidate B: Yes, let's choose tennis!"
        },
        "part3": {
            "title": "Part 3: Photograph Description",
            "image": "assets/speaking/test1_part3.png",
            "photoA": {
                "title": "Photo A: Walking in snowy mountains",
                "description": "In this photo, I can see a person standing on a snowy mountain. The person is wearing warm clothes - a hat, a jacket, and boots. They have a pink backpack and a walking stick. There is a lot of white snow on the ground. I can see tall trees with snow on them. Behind the person, there are mountains and a grey sky. It looks very cold and quiet. I think this person likes walking in the mountains in winter."
            },
            "photoB": {
                "title": "Photo B: A father and child on the beach",
                "description": "This photo is very different from the first one. I can see a man and a small child walking on a beach. The man is wearing a pink t-shirt and dark shorts. He is holding the child's hand. They are walking near the sea. The waves are big and the sand is brown. It looks like a warm day. I think they are a father and his child enjoying a holiday at the beach."
            }
        },
        "part4": {
            "title": "Part 4: Extended Discussion",
            "questions": [
                "Do you prefer winter holidays or beach holidays?",
                "What outdoor activities do people in your country enjoy?",
                "Do you think it's important for families to go on holiday together?"
            ],
            "sampleAnswers": [
                "I prefer beach holidays because I love swimming and it is warm. But some people like cold weather and snow.",
                "In my country, people enjoy playing football, going jogging in the park, and cycling. Some people also like camping at the weekend.",
                "Yes, I think family holidays are very important. Parents and children are often busy, so holidays help them spend time together."
            ]
        }
    },
    # ============ TEST 2 ============
    {
        "id": "spk_2",
        "title": "Speaking Test 2",
        "topic": "Keeping Healthy & Jobs",
        "part1": {
            "questions": [
                "Where do you live? Can you tell me about your area?",
                "How do you usually go to school or work?",
                "What is your favourite type of music?",
                "What did you do last weekend?"
            ],
            "sampleAnswers": [
                "I live in a quiet area of Hanoi. There are some shops, cafes, and a park near my house.",
                "I usually go by bus or motorbike. It takes about 20 minutes.",
                "I like pop music because the songs are happy and easy to listen to.",
                "Last weekend, I met my friends at a cafe on Saturday and helped my mum cook dinner on Sunday."
            ]
        },
        "part2": {
            "title": "Part 2: Simulated Situation (Weekend Activity)",
            "image": "assets/speaking/test2_part2.png",
            "scenario": "A group of friends want to celebrate finishing their exams by doing an exciting weekend activity together. Talk about the different options (cinema, bowling, theme park, picnic, museum) and decide on the best one.",
            "sampleDialogue": "Candidate A: We finished our exams! What should we do to celebrate?\\nCandidate B: How about going to the cinema?\\nCandidate A: That's nice, but we sit in a cinema all the time. I think we need something more exciting.\\nCandidate B: What about a theme park? We can go on rides and have fun together.\\nCandidate A: That's a great idea! It's more fun than a museum or a picnic.\\nCandidate B: I agree. Let's go to the theme park!"
        },
        "part3": {
            "title": "Part 3: Photograph Description",
            "image": "assets/speaking/test2_part3.png",
            "photoA": {
                "title": "Photo A: A person jogging",
                "description": "In this photo, I can see a person running outside. They are wearing a blue jacket and running shoes. It looks like they are jogging on grass. The weather looks a bit cloudy. I think this person is doing exercise to stay healthy. Running is a very popular sport because you don't need much equipment."
            },
            "photoB": {
                "title": "Photo B: A woman doctor writing",
                "description": "In this photo, I can see a woman who is a doctor. She is wearing a white coat and she has a stethoscope around her neck. She is writing something, maybe a prescription for a patient. She looks serious and focused. I think she is working in a hospital or a clinic. Being a doctor is an important job because you help people stay healthy."
            }
        },
        "part4": {
            "title": "Part 4: Extended Discussion",
            "questions": [
                "Do you prefer living in a city or in the countryside?",
                "What are the advantages of public transport?",
                "How can we encourage young people to do more exercise?"
            ],
            "sampleAnswers": [
                "I prefer living in a city because there are more shops, schools, and things to do. But the countryside is more peaceful.",
                "Public transport is cheaper than driving a car. It also helps reduce pollution and traffic jams.",
                "Schools can offer more sports clubs. Also, cities should build more parks and sports centres where young people can exercise for free."
            ]
        }
    },
    # ============ TEST 3 ============
    {
        "id": "spk_3",
        "title": "Speaking Test 3",
        "topic": "Journey in a Car & Free Time",
        "part1": {
            "questions": [
                "How do you usually travel to school or work?",
                "Do you prefer travelling by car or by train?",
                "Tell me about a journey you remember well.",
                "Have you ever been in a traffic jam?"
            ],
            "sampleAnswers": [
                "I usually go to school by bus. It takes about 30 minutes.",
                "I prefer the train because it's comfortable and I can read a book or look out the window.",
                "Last summer, my family drove to the beach. It took six hours but the view was beautiful.",
                "Yes, many times! In the morning, there is always a lot of traffic. I usually listen to music while I wait."
            ]
        },
        "part2": {
            "title": "Part 2: Simulated Situation (Journey in a Car)",
            "image": "assets/speaking/test3_part2.png",
            "scenario": "A family is planning a long five-hour car trip with two young children. Talk together about the different things they could bring to keep the children happy (audiobooks, handheld games, travel pillow, snacks, map, drawing kit) and decide which two are most useful.",
            "usefulPhrases": [
                "Why don't we think about...",
                "Children get bored easily, so games are useful.",
                "But looking at a screen in a car can make children feel sick.",
                "Snacks and water are important for long trips.",
                "I think the drawing kit and snacks are the best two choices."
            ],
            "sampleDialogue": "Candidate A: Five hours is a long time for children. What should the parents bring?\\nCandidate B: How about computer games? Children love games.\\nCandidate A: Yes, but looking at a screen in a car can make them feel sick.\\nCandidate B: That's true. What about a drawing kit? Children can draw pictures of things they see.\\nCandidate A: Good idea! And they also need snacks and water because children get hungry quickly.\\nCandidate B: I agree. Let's choose the drawing kit and snacks."
        },
        "part3": {
            "title": "Part 3: Photograph Description",
            "image": "assets/speaking/test3_part3.png",
            "photoA": {
                "title": "Photo A: Two boys relaxing on the grass",
                "description": "In this photo, I can see two young boys lying on the grass in a park. They are relaxing and looking up at the sky. One boy has his arms behind his head. There are some leaves on the grass and the sun is shining through the trees. They look very happy and relaxed. I think they are friends enjoying their free time outside."
            },
            "photoB": {
                "title": "Photo B: Two people playing tennis",
                "description": "In this photo, I can see two people playing tennis on a tennis court. One person is standing at one end of the court and the other person is at the other end. They are both wearing sports clothes. There are trees around the court. It looks like a nice day. I think they are enjoying playing tennis together."
            }
        },
        "part4": {
            "title": "Part 4: Extended Discussion",
            "questions": [
                "What can the government do to make public transport better?",
                "Do you think electric cars will replace normal cars in the future?",
                "Is it better to travel alone or with family?"
            ],
            "sampleAnswers": [
                "The government should make buses and trains cheaper and more comfortable. They should also make them come more often.",
                "Yes, I think so. Electric cars are better for the environment because they don't make pollution. More people will use them in the future.",
                "I prefer travelling with family because it's more fun. You can share happy moments together and help each other."
            ]
        }
    },
    # ============ TEST 4 ============
    {
        "id": "spk_4",
        "title": "Speaking Test 4",
        "topic": "Food & Healthy Eating",
        "part1": {
            "questions": [
                "What kind of food do you like best?",
                "Do you prefer eating at home or in a restaurant?",
                "Can you cook? What can you make?",
                "Do you think people eat more unhealthy food now than before?"
            ],
            "sampleAnswers": [
                "I like Vietnamese food best, especially pho and spring rolls. They are delicious and not too expensive.",
                "I prefer eating at home because my mum's cooking is the best! But I sometimes eat out with friends.",
                "Yes, I can cook some simple things like fried rice and noodle soup. I learned from watching my parents.",
                "Yes, I think so. Many people eat fast food now because it's quick and easy. But it's not very healthy."
            ]
        },
        "part2": {
            "title": "Part 2: Simulated Situation (School Trip)",
            "image": "assets/speaking/test4_part2.png",
            "scenario": "A school class is planning an end-of-term day trip. Talk together about the different places they could visit (theme park, science centre, castle, art gallery, wildlife reserve, garden) and choose the best one.",
            "usefulPhrases": [
                "Let's think about the science centre first.",
                "A theme park is fun, but it's not very educational.",
                "A castle has interesting history and nice gardens.",
                "A wildlife reserve is good because you learn about animals and walk outside.",
                "I think the science centre is the best because it's fun and educational."
            ],
            "sampleDialogue": "Candidate A: Where should our class go for the day trip? What about a theme park?\\nCandidate B: That's fun, but our teachers want us to learn something too.\\nCandidate A: OK, what about a castle or a science centre?\\nCandidate B: The science centre is great! You can do experiments and learn about space.\\nCandidate A: That sounds good. It's fun and we can learn at the same time.\\nCandidate B: I agree. Let's choose the science centre."
        },
        "part3": {
            "title": "Part 3: Photograph Description",
            "image": "assets/speaking/test4_part3.png",
            "photoA": {
                "title": "Photo A: A hot dog with chips",
                "description": "In this photo, I can see a plate of food. There is a hot dog with a sausage, ketchup, mustard, and some pickles. Next to it, there are a lot of chips. This is fast food. It looks tasty but it's not very healthy because there is a lot of fat and not many vegetables. Many people eat this kind of food when they are in a hurry."
            },
            "photoB": {
                "title": "Photo B: A fresh salad",
                "description": "This photo is very different from the first one. I can see a bowl of fresh salad. There are green leaves, tomatoes, cucumbers, onion rings, and some herbs on top. It looks very colourful and healthy. This is the kind of food that is good for your body because it has lots of vitamins. I think more people should eat salads like this."
            }
        },
        "part4": {
            "title": "Part 4: Extended Discussion",
            "questions": [
                "Why are school trips important for students?",
                "Should museums be free for students?",
                "Is fast food bad for you?"
            ],
            "sampleAnswers": [
                "School trips are important because students can learn outside the classroom. They can see real things, not just read about them in books.",
                "Yes, I think museums should be free for students. This way, all students can visit them, even if their family doesn't have much money.",
                "Yes, eating too much fast food is bad because it has a lot of fat, sugar, and salt. But eating it sometimes is OK if you also eat healthy food."
            ]
        }
    },
    # ============ TEST 5 ============
    {
        "id": "spk_5",
        "title": "Speaking Test 5",
        "topic": "Choosing a Job & Appearance",
        "part1": {
            "questions": [
                "What job would you like to do in the future?",
                "Do you prefer working alone or in a team?",
                "What skills are important for getting a good job?",
                "How do you relax when you are stressed?"
            ],
            "sampleAnswers": [
                "I want to be a teacher because I like helping people learn new things.",
                "I prefer working in a team because we can share ideas and help each other.",
                "I think speaking English well, using computers, and being able to work with other people are very important skills.",
                "When I am stressed, I listen to music, go for a walk, or talk to my friends."
            ]
        },
        "part2": {
            "title": "Part 2: Choosing the Best Job",
            "image": "assets/speaking/test5_part2.png",
            "scenario": "A student is deciding what kind of job to do (doctor, police officer, artist, truck driver, technician). Talk about the good and bad things about each job and choose the best one.",
            "sampleDialogue": "Candidate A: Being a doctor is a very good job because you help sick people. But you need to study for many years.\\nCandidate B: That's true. What about being an artist? You can be creative.\\nCandidate A: Yes, but it's hard to earn money as an artist sometimes.\\nCandidate B: A technician is good because there are lots of jobs in technology today.\\nCandidate A: I agree. But I think being a doctor is the best because you help people and it's a respected job.\\nCandidate B: OK, let's choose doctor."
        },
        "part3": {
            "title": "Part 3: Photograph Description",
            "image": "assets/speaking/test5_part3.png",
            "photoA": {
                "title": "Photo A: Two businessmen walking in a city",
                "description": "In this photo, I can see two men walking in a city street. They are wearing smart clothes - suits, shirts, and ties. They are talking to each other and they look serious. Behind them, there is a big building. I think they are businessmen going to a meeting. They look professional and confident."
            },
            "photoB": {
                "title": "Photo B: Two people with unusual clothes and hair",
                "description": "This photo is very different. I can see two people walking on a busy street. They have long blonde hair and they are wearing unusual clothes - a black leather jacket, pink trousers, a t-shirt with a logo, and sunglasses. Their style is very different from the businessmen in the first photo. I think they might be musicians or artists because their clothes are very creative and colourful."
            }
        },
        "part4": {
            "title": "Part 4: Extended Discussion",
            "questions": [
                "Do you think clothes are important for your job?",
                "Is it better to have a job with a high salary or a job you enjoy?",
                "How will technology change jobs in the future?"
            ],
            "sampleAnswers": [
                "Yes, I think your clothes can be important at work. If you look smart, people may trust you more. But what you know is more important than what you wear.",
                "I think it's better to have a job you enjoy. If you love your work, you will be happy every day. Money is important too, but it's not everything.",
                "Technology will change many jobs. Computers and robots will do some simple jobs. But people will still need to do creative work and help other people."
            ]
        }
    },
    # ============ TEST 6 ============
    {
        "id": "spk_6",
        "title": "Speaking Test 6",
        "topic": "Free Time & Outdoor Activities",
        "part1": {
            "questions": [
                "Have you ever slept in a tent outside?",
                "Do you enjoy spending time in nature?",
                "What do you always bring when you go on a picnic?",
                "Do you prefer hotels or camping?"
            ],
            "sampleAnswers": [
                "Yes, I went camping with my friends last summer. We slept in a tent near a river. It was really fun.",
                "Yes, I love nature. I like the fresh air, the trees, and the sound of birds singing.",
                "I always bring sandwiches, fruit, water, and a blanket to sit on.",
                "I like camping because it's more exciting than staying in a hotel. You can sit around a fire and look at the stars."
            ]
        },
        "part2": {
            "title": "Part 2: Simulated Situation (Camping Trip)",
            "image": "assets/speaking/test6_part2.png",
            "scenario": "A group of friends are going on their first camping trip in the countryside. Talk about what they should bring (tent, sleeping bag, stove, first aid kit, boots, torch) and agree on the two most important items.",
            "usefulPhrases": [
                "Without a tent, they will get wet if it rains.",
                "It can get very cold at night, so a sleeping bag is important.",
                "A first-aid kit is important in case someone gets hurt.",
                "A gas stove is useful for cooking food.",
                "I think the tent and first-aid kit are the two most important things."
            ],
            "sampleDialogue": "Candidate A: What should our friends bring for camping? A tent is very important, right?\\nCandidate B: Yes! If it rains, they need a dry place to sleep.\\nCandidate A: What else? A sleeping bag or a first-aid kit?\\nCandidate B: Both are important, but a first-aid kit is more important because if someone gets hurt, they need medicine.\\nCandidate A: I agree. So the tent and first-aid kit are the two most important things.\\nCandidate B: Yes, that's right!"
        },
        "part3": {
            "title": "Part 3: Photograph Description",
            "image": "assets/speaking/test6_part3.png",
            "photoA": {
                "title": "Photo A: A woman reading by the fireplace",
                "description": "In this photo, I can see a woman sitting on a sofa at home. She is reading a book. She is wearing a red dress. Behind her, there is a fireplace with a fire burning. There is also a bowl of apples on a shelf. The room looks warm and comfortable. I think she is relaxing at home on a cold evening. She looks peaceful and happy."
            },
            "photoB": {
                "title": "Photo B: Two people cycling in a park",
                "description": "This photo shows two people riding bicycles in a park. They are cycling on a path between tall trees. The grass around them is very green. It looks like a nice, sunny day. I think they are enjoying the fresh air and exercise. Cycling is a good way to stay healthy and enjoy nature at the same time."
            }
        },
        "part4": {
            "title": "Part 4: Extended Discussion",
            "questions": [
                "What can young people learn from camping?",
                "What rules should people follow when camping in nature?",
                "Would you like to try camping on a small island?"
            ],
            "sampleAnswers": [
                "Camping teaches young people to be independent. They learn to cook, make a fire, and work together as a team.",
                "People should always take their rubbish home. They should not make fires near trees. They should also be careful not to disturb animals.",
                "It sounds exciting but a bit scary! I would want to go with friends and bring lots of food and water."
            ]
        }
    },
    # ============ TEST 7 ============
    {
        "id": "spk_7",
        "title": "Speaking Test 7",
        "topic": "Animals & Pets",
        "part1": {
            "questions": [
                "How does your family celebrate special days?",
                "What was the best present you have ever got?",
                "Do you prefer buying presents or making them by hand?",
                "Who in your family are you closest to?"
            ],
            "sampleAnswers": [
                "We usually have a big meal together. Sometimes we give each other presents and take photos.",
                "The best present I got was a guitar from my parents for my birthday. I was so happy!",
                "I like making presents by hand because they are more special. For example, I made a photo album for my mum.",
                "I am closest to my mum because she always listens to me and helps me with my problems."
            ]
        },
        "part2": {
            "title": "Part 2: Simulated Situation (Mother's Day Present)",
            "image": "assets/speaking/test7_part2.png",
            "scenario": "Two brothers/sisters want to buy a nice Mother's Day present. Talk together about the different gifts (spa voucher, flowers, perfume, kitchen thing, family dinner, smart watch) and decide which gift is best.",
            "usefulPhrases": [
                "Our mum works very hard, so she needs to relax.",
                "A kitchen thing is not a nice present because it's like work.",
                "A spa day would help her relax and feel good.",
                "We could cook a special dinner for her at home.",
                "I think flowers and a spa day is the best present."
            ],
            "sampleDialogue": "Candidate A: Mother's Day is next week. What present should we get for mum?\\nCandidate B: What about a kitchen thing? No, that's like more work for her!\\nCandidate A: I agree. How about perfume or a spa day?\\nCandidate B: A spa day is great! Mum always says her back hurts from working.\\nCandidate A: And we can also buy her some nice flowers.\\nCandidate B: Yes! Flowers and a spa day. She will love it!"
        },
        "part3": {
            "title": "Part 3: Photograph Description",
            "image": "assets/speaking/test7_part3.png",
            "photoA": {
                "title": "Photo A: A boy playing with a big dog",
                "description": "In this photo, I can see a young boy playing with a very big dog outside. The boy is smiling and he looks happy. He is holding something up and the dog is jumping to get it. The dog is grey and very tall. The boy is wearing a jacket and jeans. I think the boy and the dog are good friends. The dog looks friendly and excited."
            },
            "photoB": {
                "title": "Photo B: A person holding a small kitten",
                "description": "In this photo, I can see someone's hands holding a small black and white kitten. The kitten is very young and cute. It has big eyes and white paws. There are more kittens behind it. I think this person is looking after the kittens. Kittens are very popular pets because they are small, soft, and easy to take care of."
            }
        },
        "part4": {
            "title": "Part 4: Extended Discussion",
            "questions": [
                "Why should we say thank you to our parents more often?",
                "Do you think shops make people spend too much money on presents?",
                "What is the best way to say thank you to someone who helped you?"
            ],
            "sampleAnswers": [
                "Our parents do many things for us every day, like cooking and helping with homework. We should say thank you more often, not just on special days.",
                "Yes, I think so. Shops have many advertisements that make people feel they need to buy expensive things. But a simple, personal gift can be just as nice.",
                "I think writing a nice letter or card is the best way. You can explain why you are thankful. It's more personal than just buying something."
            ]
        }
    },
    # ============ TEST 8 ============
    {
        "id": "spk_8",
        "title": "Speaking Test 8",
        "topic": "The Environment & Pollution",
        "part1": {
            "questions": [
                "How do you feel when friends visit your home?",
                "What is the most interesting place in your city?",
                "Where do you take visitors to eat?",
                "What entertainment is popular where you live?"
            ],
            "sampleAnswers": [
                "I feel very happy when friends come to my house. We can talk, play games, and have fun together.",
                "The most interesting place in my city is the old town. There are beautiful old buildings and nice lakes.",
                "I usually take visitors to a street food area. They can try many different local dishes.",
                "Going to the cinema, singing karaoke, and going to coffee shops are very popular where I live."
            ]
        },
        "part2": {
            "title": "Part 2: Simulated Situation (Visit from an English Friend)",
            "image": "assets/speaking/test8_part2.png",
            "scenario": "An English friend is visiting your city for just one weekend. Talk about what you could do together (bus tour, night market, art gallery, theatre, boat trip, shopping) and pick the best plan for Saturday evening.",
            "usefulPhrases": [
                "Our friend only has one weekend, so we should choose something special.",
                "A shopping mall is boring because you can find one in any city.",
                "The night market has great food and interesting things to buy.",
                "A boat trip on the river is a nice way to see the city.",
                "Let's do a boat trip and then go to the night market."
            ],
            "sampleDialogue": "Candidate A: Our friend is here for only two days. What should we do on Saturday evening?\\nCandidate B: We could go shopping, but that's not very special.\\nCandidate A: How about a boat trip on the river? He can see the city lights.\\nCandidate B: That's a great idea! And after that, we can go to the night food market.\\nCandidate A: Perfect! He can try local food and buy some small presents.\\nCandidate B: Yes, let's do the boat trip and the night market!"
        },
        "part3": {
            "title": "Part 3: Photograph Description",
            "image": "assets/speaking/test8_part3.png",
            "photoA": {
                "title": "Photo A: A wind turbine",
                "description": "In this photo, I can see a big wind turbine. It is very tall and it stands alone. The sky behind it is blue with some white clouds. Wind turbines use the wind to make electricity. This is good for the environment because it doesn't make pollution. I think more countries should use wind energy."
            },
            "photoB": {
                "title": "Photo B: A polluted river with rubbish",
                "description": "This photo is very different. I can see a river that is very dirty and full of rubbish. There are plastic bags, bottles, and other waste along the side of the river. Some people in a small boat are on the water. There are old houses near the river. This looks like a poor area. I think pollution is a big problem here. People should not throw rubbish into rivers."
            }
        },
        "part4": {
            "title": "Part 4: Extended Discussion",
            "questions": [
                "What makes a good host when people visit you?",
                "How should tourists behave when they visit another country?",
                "Does tourism help or hurt local communities?"
            ],
            "sampleAnswers": [
                "A good host makes their guests feel welcome. They should show them interesting places, recommend good food, and be friendly and helpful.",
                "Tourists should respect local customs and traditions. They should be polite, not too loud, and learn to say a few words in the local language.",
                "Tourism is mostly good because it brings money and jobs. But too many tourists can cause problems like pollution and higher prices for local people."
            ]
        }
    },
    # ============ TEST 9 ============
    {
        "id": "spk_9",
        "title": "Speaking Test 9",
        "topic": "Fashion & Appearance",
        "part1": {
            "questions": [
                "What extra classes have you done outside school?",
                "If you could learn a new skill, what would it be?",
                "Do you prefer learning in a group or one-to-one with a teacher?",
                "How do you stay focused when studying?"
            ],
            "sampleAnswers": [
                "I took an English class last summer. It helped me improve my speaking and listening.",
                "I would like to learn to cook because I want to make nice meals for my family.",
                "I prefer small groups because I can learn from other students and share ideas.",
                "I study for 25 minutes, then take a short break. I also put my phone in another room so I don't get distracted."
            ]
        },
        "part2": {
            "title": "Part 2: Simulated Situation (Interesting Class)",
            "image": "assets/speaking/test9_part2.png",
            "scenario": "A youth centre is starting free weekend classes for teenagers. Talk about the different courses (photography, public speaking, coding, cooking, martial arts, languages) and decide which two would be most popular.",
            "usefulPhrases": [
                "Coding is useful for getting a good job in the future.",
                "Cooking is a useful skill for everyday life.",
                "Photography is popular because teenagers love social media.",
                "Public speaking helps build confidence.",
                "I think photography and cooking are the two most popular choices."
            ],
            "sampleDialogue": "Candidate A: What classes should the youth centre offer?\\nCandidate B: Photography would be really popular! All teenagers want to take nice photos for social media.\\nCandidate A: Good idea! And what about the second class?\\nCandidate B: Cooking is useful because everyone needs to eat! Teenagers want to learn to cook for themselves.\\nCandidate A: I agree. Photography and cooking are the best choices.\\nCandidate B: Yes, I think lots of teenagers will come to those classes."
        },
        "part3": {
            "title": "Part 3: Photograph Description",
            "image": "assets/speaking/test9_part3.png",
            "photoA": {
                "title": "Photo A: A man in smart casual clothes",
                "description": "In this photo, I can see a young man standing and looking at the camera. He is wearing a dark sweater over a white shirt, blue jeans, and dark shoes. His hands are in his pockets. He looks relaxed and confident. His clothes are smart but also casual. I think this is a modern style that many young people like to wear."
            },
            "photoB": {
                "title": "Photo B: A man with a hat and dreadlocks",
                "description": "In this photo, I can see a young man looking up at the camera. He is wearing a brown hat and a brown sweater. He has short dreadlocks coming out of his hat. He is holding something in his hands. His style is very different from the first man - it's more artistic and creative. I think he likes to express himself through his clothes and hairstyle."
            }
        },
        "part4": {
            "title": "Part 4: Extended Discussion",
            "questions": [
                "Should schools teach practical skills like cooking?",
                "Can online videos replace real teachers?",
                "Is it important for adults to keep learning new things?"
            ],
            "sampleAnswers": [
                "Yes, I think schools should teach practical skills. Many students can pass exams but they can't cook a meal or manage their money.",
                "Online videos are useful for learning, but a real teacher can answer your questions and help you when you make mistakes. I think we need both.",
                "Yes, it's very important. The world is always changing, so we need to keep learning. It also keeps our minds active and helps us meet new people."
            ]
        }
    },
    # ============ TEST 10 ============
    {
        "id": "spk_10",
        "title": "Speaking Test 10",
        "topic": "Work & Education",
        "part1": {
            "questions": [
                "Do you have a pet at home?",
                "What are the good things about having a pet?",
                "What animal is the best pet for a flat?",
                "What do you need to do if you get a dog?"
            ],
            "sampleAnswers": [
                "Yes, we have a cat called Miu. She likes to sleep on my bed when I study.",
                "Pets teach children to be kind and responsible. Children learn to feed them, play with them, and take care of them.",
                "A cat or a small fish is good for a flat because they are quiet and don't need a garden.",
                "If you get a dog, you need to walk it every day, take it to the vet, feed it, and give it lots of love."
            ]
        },
        "part2": {
            "title": "Part 2: Simulated Situation (Choosing a Pet for Grandmother)",
            "image": "assets/speaking/test10_part2.png",
            "scenario": "A grandmother who lives alone wants to get a pet. Talk about the different animals (puppy, cat, bird, fish, tortoise) and decide which one is best for her.",
            "usefulPhrases": [
                "A puppy needs too much exercise for a grandmother.",
                "Fish are nice to look at, but you can't touch them.",
                "A cat is easy to look after and very friendly.",
                "A bird sings nicely but you need to clean the cage.",
                "I think a calm cat is the best pet for her."
            ],
            "sampleDialogue": "Candidate A: What pet should grandmother get? A puppy?\\nCandidate B: No, a puppy needs lots of walks every day. That's too tiring for grandmother.\\nCandidate A: What about a cat?\\nCandidate B: A cat is perfect! Cats are quiet, friendly, and they like sitting next to people.\\nCandidate A: Yes, and a cat is easy to look after. She just needs to feed it and give it water.\\nCandidate B: I agree. A cat is the best choice for grandmother."
        },
        "part3": {
            "title": "Part 3: Photograph Description",
            "image": "assets/speaking/test10_part3.png",
            "photoA": {
                "title": "Photo A: A man working with a laptop at a construction site",
                "description": "In this photo, I can see a man working outside. He is wearing a hard hat and a work jacket. He has a laptop computer in front of him. Behind him, I can see big machines. I think he is an engineer working at a building site. He is using his computer to check plans or write reports. This job needs both computer skills and practical knowledge."
            },
            "photoB": {
                "title": "Photo B: A woman with books, possibly a student or teacher",
                "description": "In this photo, I can see a young woman with curly red hair. She is wearing a green sweater and she is smiling. She is holding some books. Behind her, there seems to be a blackboard. I think she might be a student or a teacher at a school or university. She looks happy and friendly."
            }
        },
        "part4": {
            "title": "Part 4: Extended Discussion",
            "questions": [
                "Why should people get pets from animal shelters?",
                "Do you think zoos are good or bad?",
                "How can cities be better for pet owners?"
            ],
            "sampleAnswers": [
                "People should get pets from shelters because there are many animals that need a home. It's kinder than buying from a shop.",
                "Zoos can be good because they help protect animals that are in danger. But it's sad to see big animals in small spaces.",
                "Cities should have more parks where people can walk their dogs. They should also have more places where pets are allowed."
            ]
        }
    }
]

# Build the replacement JSON
new_json = json.dumps(new_speaking_tests, ensure_ascii=False, indent=6)
replacement = f'"speakingTests": {new_json}'

# Replace in content
new_content = content[:match.start()] + replacement + content[match.end():]

# Write back
with open(DATA_FILE, "w", encoding="utf-8") as f:
    f.write(new_content)

print(f"SUCCESS! Replaced speakingTests with {len(new_speaking_tests)} B1-level tests.")
print("All photo descriptions now match the actual images from the book.")
print("All sample answers use simple B1-level vocabulary.")
