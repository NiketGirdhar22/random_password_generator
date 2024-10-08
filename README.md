# Password Generator API

This project is a simple API built using Flask that generates a random password based on user-defined criteria. The API also allows users to input a string and apply Caesar cipher encryption to it before using it as part of the generated password.

## Features

- Generate a random password with configurable length.
- Option to include/exclude uppercase letters, numbers, and special characters.
- Encrypt user-provided strings using Caesar cipher and incorporate them into the password.
- Randomly shuffle the characters in the password for additional security.

## Requirements

To run this project, you will need the following:

- Python 3.x
- Flask
- Flask-CORS

### Installation

1. Clone this repository:

    ```bash
    git clone https://github.com/your-username/password-generator-api.git
    ```

2. Navigate to the project directory:

    ```bash
    cd password-generator-api
    ```

3. Install the required dependencies:

    ```bash
    pip install Flask Flask-CORS
    ```

## Usage

1. Start the Flask development server:

    ```bash
    python app.py
    ```

    The app will run on `http://127.0.0.1:5000/` by default.

2. To generate a password, make a `POST` request to the `/generate-password` endpoint with the following JSON payload:

    ```json
    {
      "length": 19,
      "include_uppercase": true,
      "include_numbers": true,
      "include_special_chars": true,
      "user_string": "your-string"
    }
    ```

    - `length` (optional): The length of the generated password. Default is `19`.
    - `include_uppercase` (optional): Whether to include uppercase letters in the password. Default is `true`.
    - `include_numbers` (optional): Whether to include numbers in the password. Default is `true`.
    - `include_special_chars` (optional): Whether to include special characters in the password. Default is `true`.
    - `user_string` (optional): A custom string provided by the user, which will be encrypted using a Caesar cipher and included in the password.

3. Example response:

    ```json
    {
      "password": "J9#hPW!03bY$pa8"
    }
    ```

## API Endpoints

### `/generate-password` (POST)

This endpoint generates a random password based on the provided criteria.

- **Request Body**:
  - `length`: The desired length of the password.
  - `include_uppercase`: Boolean value to specify whether uppercase letters should be included.
  - `include_numbers`: Boolean value to specify whether numbers should be included.
  - `include_special_chars`: Boolean value to specify whether special characters should be included.
  - `user_string`: A string to be encrypted using Caesar cipher and included in the password.

- **Response**:
  - A JSON object with the generated password.

### Example:

```bash
curl -X POST http://127.0.0.1:5000/generate-password \
  -H "Content-Type: application/json" \
  -d '{
    "length": 12,
    "include_uppercase": true,
    "include_numbers": true,
    "include_special_chars": true,
    "user_string": "mypassword"
  }'
