import re

text = 'my phone number is 408-555-1234'
phone_pattern = '\d{3}-\d{3}-\d{4}'
phone = re.search(phone_pattern, text)
# print(phone.group())
# print(phone.group(1))

print(re.search(r'man|women', 'This is a man'))
print(re.search(r'women', 'This is a women'))

print(re.findall(r'\S+at', 'the cat sat in the hat seat met'))