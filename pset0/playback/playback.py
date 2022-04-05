import re

# Ask for text input from the user
text = input('Text: ').strip()

# Replace each space with 3 dots
text = re.sub(r' ', '...', text)

# Print the text
print(text)