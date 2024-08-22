from flask import Flask, request, jsonify
import random
import string
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def caesar_cipher(text, shift):
    encrypted_text = []
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            encrypted_text.append(chr((ord(char) - shift_base + shift) % 26 + shift_base))
        else:
            encrypted_text.append(char)
    return ''.join(encrypted_text)

def generate_password(length=8, include_uppercase=True, include_numbers=True, include_special_chars=True, user_string=None, shift=3):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase if include_uppercase else ''
    numbers = string.digits if include_numbers else ''
    special_chars = string.punctuation if include_special_chars else ''
    
    all_chars = lower + upper + numbers + special_chars
    
    if not all_chars:
        raise ValueError("No characters available to generate a password. Adjust your constraints.")
    
    if user_string:
        encrypted_string = caesar_cipher(user_string, shift)
        random_length = max(length - len(encrypted_string), 0)
        random_part = ''.join(random.choice(all_chars) for _ in range(random_length))
        password = random_part + encrypted_string
    else:
        password = ''.join(random.choice(all_chars) for _ in range(length))
    
    password = ''.join(random.sample(password, len(password)))
    
    return password

@app.route('/generate-password', methods=['POST'])
def generate_password_endpoint():
    data = request.json
    length = data.get('length', 19)
    include_uppercase = data.get('include_uppercase', True)
    include_numbers = data.get('include_numbers', True)
    include_special_chars = data.get('include_special_chars', True)
    user_string = data.get('user_string')
    
    password = generate_password(
        length=length, 
        include_uppercase=include_uppercase,
        include_numbers=include_numbers,
        include_special_chars=include_special_chars,
        user_string=user_string
    )
    return jsonify({"password": password})

if __name__ == '__main__':
    app.run(debug=True)