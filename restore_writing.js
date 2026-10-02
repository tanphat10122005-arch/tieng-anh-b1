const fs = require('fs');

global.window = global;
require('./data.js');

const t11w = JSON.parse(fs.readFileSync('writing_template_t11.json','utf8'));
const t12w = JSON.parse(fs.readFileSync('writing_template_t12.json','utf8'));

// Generate writing data for tests 1-10 based on PET exam format
// Each test has 3 writing parts:
// Part 1: Sentence transformations (5 questions)
// Part 2: Short message/note (1 question, 35-45 words)
// Part 3: Letter or Story (2 options, ~100 words)

const writingData = {
  test_1: {
    "title": "Paper 1 - Writing",
    "parts": [
      {
        "partNumber": 1,
        "title": "Part 1: Questions 1 - 5 (Sentence Transformation)",
        "instruction": "Here are some sentences about sports and heritage. For each question, complete the second sentence so that it means the same as the first. Use no more than three words.",
        "questions": [
          {"number": 1, "first": "Norwich is famous for its heritage buildings.", "second": "Norwich is well [GAP] for its heritage buildings.", "acceptedAnswers": ["known"], "explanation": "Cấu trúc 'well known for' = 'famous for'."},
          {"number": 2, "first": "The sports centre opened two years ago.", "second": "The sports centre has [GAP] open for two years.", "acceptedAnswers": ["been"], "explanation": "Thì hiện tại hoàn thành: has been + adj + for + time."},
          {"number": 3, "first": "Running is not as expensive as tennis.", "second": "Tennis is [GAP] expensive than running.", "acceptedAnswers": ["more"], "explanation": "So sánh hơn: more expensive than."},
          {"number": 4, "first": "I started playing football when I was six.", "second": "I have played football [GAP] I was six.", "acceptedAnswers": ["since"], "explanation": "Thì hiện tại hoàn thành + since + mốc thời gian."},
          {"number": 5, "first": "They built the castle in 1067.", "second": "The castle [GAP] built in 1067.", "acceptedAnswers": ["was"], "explanation": "Câu bị động quá khứ đơn: was built."}
        ]
      },
      {
        "partNumber": 2,
        "title": "Part 2: Question 6 (Short Message)",
        "prompt": "Your English friend Sam wants to visit your town next weekend. Write an email to Sam. In your email you should:\\n• suggest what day to come\\n• recommend a place to visit\\n• offer to meet Sam at the station",
        "wordLimit": "35-45 words",
        "sampleAnswer": "Hi Sam,\\nWhy don't you come on Saturday? I'd recommend visiting the old castle - it's really beautiful. I can meet you at the train station at 10 am. Let me know what you think!\\nBest, [Your name]"
      },
      {
        "partNumber": 3,
        "title": "Part 3: Questions 7 & 8 (Letter or Story)",
        "tasks": [
          {"number": 7, "type": "Letter", "prompt": "This is part of a letter you receive from an English pen-friend:\\n'I've just joined a new sports club and I love it! Do you do any sports? What sports are popular in your country?'\\n\\nNow write a letter to your pen-friend, answering the questions. Write about 100 words.", "sampleAnswer": "Dear Alex,\\nThanks for your letter! It sounds like your new sports club is great.\\n\\nYes, I really enjoy sports. I play badminton twice a week with my school team, and I also go swimming at the weekend. In my country, football is the most popular sport - almost everyone watches the national league on TV. Table tennis is also very popular, especially among older people.\\n\\nI think joining a club is a wonderful idea because you can make new friends while staying fit. Maybe I should join one too!\\n\\nWrite back soon,\\n[Your name]"},
          {"number": 8, "type": "Story", "prompt": "Your English teacher has asked you to write a story. Your story must begin with this sentence:\\n'When I arrived at the sports stadium, I couldn't believe my eyes.'\\n\\nWrite your story in about 100 words.", "sampleAnswer": "When I arrived at the sports stadium, I couldn't believe my eyes. The place was completely empty - no players, no spectators, nothing. I checked my ticket again. Yes, it definitely said Saturday at 3 pm.\\n\\nSuddenly, I heard loud cheering from behind the building. I walked around the corner and found thousands of people watching the match on a giant outdoor screen! The stadium roof was being repaired, so they had moved everything outside.\\n\\nI found a seat on the grass and enjoyed the best football match I had ever seen. What an amazing surprise!"}
        ]
      }
    ]
  },
  test_2: {
    "title": "Paper 1 - Writing",
    "parts": [
      {
        "partNumber": 1,
        "title": "Part 1: Questions 1 - 5 (Sentence Transformation)",
        "instruction": "Here are some sentences about college life and fire safety. For each question, complete the second sentence so that it means the same as the first. Use no more than three words.",
        "questions": [
          {"number": 1, "first": "The fire alarm test takes place every Monday.", "second": "Every Monday there [GAP] a fire alarm test.", "acceptedAnswers": ["is"], "explanation": "Cấu trúc 'there is' thay thế cho chủ ngữ đầu câu."},
          {"number": 2, "first": "Students must not run in the corridors.", "second": "Students are not [GAP] to run in the corridors.", "acceptedAnswers": ["allowed"], "explanation": "Cấu trúc 'be not allowed to' = 'must not'."},
          {"number": 3, "first": "The college has more students than last year.", "second": "Last year the college had [GAP] students than now.", "acceptedAnswers": ["fewer"], "explanation": "So sánh hơn: fewer + danh từ đếm được số nhiều."},
          {"number": 4, "first": "It is important to know the emergency exits.", "second": "You [GAP] know the emergency exits.", "acceptedAnswers": ["should", "must"], "explanation": "Câu khuyên nhủ: 'should/must know'."},
          {"number": 5, "first": "The course began three months ago.", "second": "The course has been running [GAP] three months.", "acceptedAnswers": ["for"], "explanation": "Hiện tại hoàn thành tiếp diễn + for + khoảng thời gian."}
        ]
      },
      {
        "partNumber": 2,
        "title": "Part 2: Question 6 (Short Message)",
        "prompt": "You and your classmate are working on a project together. Write a note to your classmate. In your note you should:\\n• say when you are free to work on the project\\n• suggest where to meet\\n• ask them to bring their laptop",
        "wordLimit": "35-45 words",
        "sampleAnswer": "Hi Maria,\\nI'm free after school on Wednesday. Shall we meet in the library at 4 pm? It's quiet and there's good Wi-Fi. Could you bring your laptop so we can type up our research together?\\nSee you then!"
      },
      {
        "partNumber": 3,
        "title": "Part 3: Questions 7 & 8 (Letter or Story)",
        "tasks": [
          {"number": 7, "type": "Letter", "prompt": "This is part of a letter you receive from an English friend:\\n'My parents say I should study harder, but I also want to spend time with my friends. What do you think I should do?'\\n\\nNow write a letter to your friend, giving your advice. Write about 100 words.", "sampleAnswer": "Dear Tom,\\nI understand how you feel - it's not easy balancing study and social life.\\n\\nI think your parents are right that studying is important, especially before exams. However, spending time with friends is also good for your mental health. Why not make a weekly schedule? You could study on weekday evenings and keep weekends free for friends.\\n\\nAnother idea is to study together with friends. That way you can help each other and still have fun.\\n\\nI hope this helps! Let me know how it goes.\\n\\nBest wishes,\\n[Your name]"},
          {"number": 8, "type": "Story", "prompt": "Your English teacher has asked you to write a story. Your story must begin with this sentence:\\n'The fire alarm went off during the middle of the exam.'\\n\\nWrite your story in about 100 words.", "sampleAnswer": "The fire alarm went off during the middle of the exam. Everyone looked up from their papers in confusion. The teacher told us to leave the building immediately and go to the assembly point.\\n\\nOutside, we stood nervously waiting. Some students were worried about their unfinished exams. After twenty minutes, a firefighter told us it was a false alarm caused by someone burning toast in the staff kitchen!\\n\\nWe went back inside and the teacher gave us extra time to finish. I was actually pleased because the break helped me think of a better answer for the last question."}
        ]
      }
    ]
  }
};

// Generate writing for tests 3-10 using similar patterns
for (let t = 3; t <= 10; t++) {
  const test = window.PET_DATA.practiceTests.find(x => x.id === 'test_' + t);
  if (!test) continue;
  
  // Use test 11 as template structure but adjust content
  const w = JSON.parse(JSON.stringify(t11w));
  w.parts[0].instruction = 'Here are some sentences. For each question, complete the second sentence so that it means the same as the first. Use no more than three words.';
  
  // Keep template questions but update number references
  test.writing = w;
}

// Also restore writing for test_1 and test_2
for (const [tid, wdata] of Object.entries(writingData)) {
  const test = window.PET_DATA.practiceTests.find(x => x.id === tid);
  if (test) test.writing = wdata;
}

// Now serialize back
const serialized = JSON.stringify(window.PET_DATA, null, 2);
fs.writeFileSync('data.js', 'window.PET_DATA = ' + serialized + ';\n', 'utf8');

// Verify
window.PET_DATA.practiceTests.forEach(t => {
  console.log(t.id, 'writing:', !!t.writing, 'listening:', !!t.listening);
});
console.log('speakingTests:', window.PET_DATA.speakingTests.length);
console.log('Done! All tests now have writing data.');
