import json
import re

print("Injecting all digital tests 3 to 10 into data.js...")

with open('digital_tests_all_3_to_10.json', encoding='utf-8') as f:
    new_tests = json.load(f)

print(f"Loaded {len(new_tests)} tests (IDs: {[t['id'] for t in new_tests]})")

# Read data.js
with open('data.js', 'r', encoding='utf-8') as f:
    content = f.read()

# We can use node to merge data.js safely!
merge_script = """
const fs = require('fs');

global.window = global;
require('./data.js');

const newTests = JSON.parse(fs.readFileSync('digital_tests_all_3_to_10.json', 'utf8'));

// Current practice tests
const currentTests = window.PET_DATA.practiceTests || [];

// Create a map by id
const testMap = new Map();
currentTests.forEach(t => testMap.set(t.id, t));

// Add / overwrite with new tests 3 to 10
newTests.forEach(t => testMap.set(t.id, t));

// Ensure ordered test_1 to test_12
const orderedTests = [];
for (let i = 1; i <= 12; i++) {
  const id = `test_${i}`;
  if (testMap.has(id)) {
    orderedTests.push(testMap.get(id));
  }
}

window.PET_DATA.practiceTests = orderedTests;

// Update units: set isFullDigital = true for all units 1 to 12
window.PET_DATA.units.forEach(u => {
  u.isFullDigital = true;
  u.practiceTestId = `test_${u.unitNumber}`;
});

// Serialize back to data.js
const newContent = 'window.PET_DATA = ' + JSON.stringify(window.PET_DATA, null, 2) + ';\n';
fs.writeFileSync('data.js', newContent, 'utf8');

console.log('Successfully updated data.js!');
console.log('Total practice tests in data.js:', orderedTests.length);
console.log('Test IDs:', orderedTests.map(t => t.id));
console.log('All units digital status:', window.PET_DATA.units.map(u => ({unit: u.unitNumber, isFullDigital: u.isFullDigital, practiceTestId: u.practiceTestId})));
"""

with open('merge_data.js', 'w', encoding='utf-8') as f:
    f.write(merge_script)

print("Created merge_data.js. Now running with Node...")
