document.getElementById('generateBtn').addEventListener('click', async function() {
    const length = parseInt(document.getElementById('length').value);
    const includeUppercase = document.getElementById('uppercase').checked;
    const includeNumbers = document.getElementById('numbers').checked;
    const includeSpecialChars = document.getElementById('specialChars').checked;
    const userString = document.getElementById('userString').value;

    const response = await fetch('http://127.0.0.1:5000/generate-password', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ 
            length: length,
            include_uppercase: includeUppercase,
            include_numbers: includeNumbers,
            include_special_chars: includeSpecialChars,
            user_string: userString 
        }),
    });

    if (response.ok) {
        const data = await response.json();
        const password = data.password;

        document.getElementById('generatedPassword').innerText = password;
        document.getElementById('passwordContainer').style.display = 'block';
    } else {
        console.error('Error fetching password:', response.statusText);
    }
})