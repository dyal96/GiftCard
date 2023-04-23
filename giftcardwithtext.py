import random
import string

def generate_gift_card_code():
    # Define the characters to use for the gift card code
    characters = string.ascii_uppercase + string.digits
    
    # Generate a random gift card code
    code = '-'.join([
        ''.join(random.choice(characters) for i in range(4)),
        ''.join(random.choice(characters) for i in range(6)),
        ''.join(random.choice(characters) for i in range(4))
    ])
    
    return code

# Generate 10 random gift card codes
gift_card_codes = []
for i in range(10):
    gift_card_codes.append(generate_gift_card_code())

# Export gift card codes to a text file
with open('gift_card_codes.txt', 'w') as f:
    for code in gift_card_codes:
        f.write(f'{code}\n')
