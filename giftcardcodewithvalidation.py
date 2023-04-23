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

def is_valid_gift_card_code(code):
    # Check if the code is in the correct format
    if len(code) != 15 or code[4] != '-' or code[11] != '-':
        return False
    
    # Check if the code contains only uppercase letters, digits, and hyphens
    for char in code:
        if char not in string.ascii_uppercase + string.digits + '-':
            return False
    
    return True

# Generate 10 random gift card codes
gift_card_codes = []
for i in range(10):
    gift_card_codes.append(generate_gift_card_code())

# Export gift card codes to a text file
with open('gift_card_codes.txt', 'w') as f:
    for code in gift_card_codes:
        f.write(f'{code}\n')

# Validate gift card codes
valid_gift_card_codes = []
invalid_gift_card_codes = []
with open('gift_card_codes.txt', 'r') as f:
    for line in f:
        code = line.strip()
        if is_valid_gift_card_code(code):
            valid_gift_card_codes.append(code)
        else:
            invalid_gift_card_codes.append(code)

# Export valid gift card codes to a text file
with open('valid_gift_card_codes.txt', 'w') as f:
    for code in valid_gift_card_codes:
        f.write(f'{code}\n')

# Export invalid gift card codes to a text file
with open('invalid_gift_card_codes.txt', 'w') as f:
    for code in invalid_gift_card_codes:
        f.write(f'{code}\n')

# Log valid gift card codes
with open('gift_card_code_log.txt', 'a') as f:
    for code in valid_gift_card_codes:
        f.write(f'{code}\n')

print(f'Generated {len(gift_card_codes)} gift card codes')
print(f'Validated {len(valid_gift_card_codes)} valid gift card codes')
print(f'Found {len(invalid_gift_card_codes)} invalid gift card codes')
