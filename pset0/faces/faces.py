import re

# Ask for text input from the user
text = input('Text: ').strip()

# Replace each :) with a 🙂 in the text 
text = re.sub(r':\)', '🙂', text)

# Replace each :( with a 🙁 in the text
text = re.sub(r':\(', '🙁', text)

# Print the text
print(text)