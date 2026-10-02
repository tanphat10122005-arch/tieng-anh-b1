const fs = require('fs');

global.window = global;
require('./data.js');

// Fix test_1 and test_2 writing data - add missing fields
const t1 = window.PET_DATA.practiceTests.find(t => t.id === 'test_1');
const t2 = window.PET_DATA.practiceTests.find(t => t.id === 'test_2');

// Fix test_1 Part 2
t1.writing.parts[1].wordCount = 42;
t1.writing.parts[1].keyPoints = [
  "Đề xuất ngày đến thăm (Saturday)",
  "Gợi ý địa điểm tham quan (old castle)",
  "Đề nghị đón ở ga tàu"
];

// Fix test_1 Part 3 tasks
t1.writing.parts[2].tasks[0].wordCount = 100;
t1.writing.parts[2].tasks[1].wordCount = 100;

// Fix test_2 Part 2
t2.writing.parts[1].wordCount = 40;
t2.writing.parts[1].keyPoints = [
  "Nêu thời gian rảnh để làm bài (Wednesday after school)",
  "Đề xuất nơi gặp (library)",
  "Nhờ mang laptop"
];

// Fix test_2 Part 3 tasks
t2.writing.parts[2].tasks[0].wordCount = 100;
t2.writing.parts[2].tasks[1].wordCount = 100;

// Save back
const serialized = JSON.stringify(window.PET_DATA, null, 2);
fs.writeFileSync('data.js', 'window.PET_DATA = ' + serialized + ';\n', 'utf8');

// Verify all tests have complete writing data
window.PET_DATA.practiceTests.forEach(t => {
  const w = t.writing;
  const p2ok = w && w.parts[1] && w.parts[1].keyPoints && w.parts[1].keyPoints.length > 0;
  const p3ok = w && w.parts[2] && w.parts[2].tasks && w.parts[2].tasks[0].wordCount;
  console.log(t.id, 'P2 keyPoints:', p2ok ? '✓' : '✗', 'P3 wordCount:', p3ok ? '✓' : '✗');
});
console.log('Done fixing writing data!');
