import hashlib
import json
import itertools
import string

def generate_emails():
    letters = string.ascii_lowercase
    numbers = [str(i).zfill(3) for i in range(1000)]
    return [f'{l1}{l2}{num}@snu.edu.in' for l1, l2, num in itertools.product(letters, letters, numbers)]

def hash_email(email: str):
    return hashlib.sha256(email.encode()).hexdigest()

def generate_hashed_emails():
    emails = generate_emails()
    hashed_emails = { email: hash_email(email) for email in emails }
    return hashed_emails

def main():
    hashed_emails = generate_hashed_emails()
    with open('hash_snu.json', 'w') as f:
        json.dump(hashed_emails, f, indent=4)

if __name__ == "__main__":
    main()