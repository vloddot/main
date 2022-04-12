import re

number = input('What is the answer to the Great Question of Life, the Universe, and everything? ').strip()

# If the number equals 42 or 'forty two' or 'forty-two' exactly, print 'Yes'
if re.match(r'^(42|forty[- ]two)$', number):
    
    print('Yes')
    
# Else, base case. Print 'No'
else:
  
    print('No')