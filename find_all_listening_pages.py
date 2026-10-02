import fitz

doc = fitz.open('Sach_B1_clean.pdf')
print("Total pages:", len(doc))

# Let's search each page or inspect where 'PAPER 2 - LISTENING' appears.
# Because it's scanned, we can inspect using OCR or by checking test headers.
# Let's see: each test has approx 11-13 pages.
# Let's inspect test start pages:
# In Cambridge PET (12 tests):
# Test 1: p. 18-28 (Listening p. 25-26 in PDF indices 24-25)
# Test 2: p. 29-39 (Listening p. 36-37 in PDF indices 35-36)
# Let's verify each test!
