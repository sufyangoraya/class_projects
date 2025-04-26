from hashlib import sha256

def login(email, stored_logins, password_to_check):
    """
    Returns True if the hash of the password we are checking matches the one in stored_logins
    for a specific email. Otherwise, returns False.
    """
    hashed_password = hash_password(password_to_check)
    
    # Check if email exists in stored_logins and compare the hashed password
    return stored_logins.get(email) == hashed_password

def hash_password(password):
    """
    Takes in a password and returns the SHA256 hashed value for that specific password.
    """
    return sha256(password.encode()).hexdigest()

def main():
    # stored_logins is a dictionary with emails as keys and hashed passwords as values
    stored_logins = {
        "example@gmail.com": "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8",
        "code_in_placer@cip.org": "973607a4ae7b4cf7d96a100b0fb07e8519cc4f70441d41214a9f811577bb06cc",
        "student@stanford.edu": "882c6df720fd99f5eebb1581a1cf975625cea8a160283011c0b9512bb56c95fb"
    }
    
    print(login("example@gmail.com", stored_logins, "word"))               # False
    print(login("example@gmail.com", stored_logins, "password"))           # True
    
    print(login("code_in_placer@cip.org", stored_logins, "Karel"))         # True
    print(login("code_in_placer@cip.org", stored_logins, "karel"))         # False
    
    print(login("student@stanford.edu", stored_logins, "password"))        # False
    print(login("student@stanford.edu", stored_logins, "123!456?789"))     # True

if __name__ == '__main__':
    main()
