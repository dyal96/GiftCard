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

# Generate and print 10 random gift card codes
for i in range(10):
    print(generate_gift_card_code())
