import sqlite3
import argon2

def _is_valid_password(password):
    
    if len(password) < 8:
        return False

    if not any(char.isupper() for char in password):
        return False

    if not any(char.isdigit() for char in password):
        return False
    
    return True


def _hash_password(password):
    # Generate a random salt
    salt = argon2.ffi.random_bytes(16)

    # Hash the password using Argon2
    hash_encoded = argon2.hash_password_raw(
        password.encode('utf-8'), salt,
        time_cost=2, memory_cost=65536, parallelism=1, hash_len=32, type=argon2.low_level.Type.ID,
    )

    return hash_encoded


def _verify_password(hashed_password, input_password):
    try:
        # Decode the hashed password
        decoded_hash = argon2.ffi.decode_base64(hashed_password)

        # Verify the password using Argon2
        return argon2.low_level.verify_password(
            decoded_hash, input_password.encode('utf-8'),
            type=argon2.low_level.Type.ID
        )
    except argon2.exceptions.VerificationError:
        return False


def login(con : sqlite3.Connection):
    while True:
        print("Please enter your login and password to continue or type 'REGISTER'.")
        answer = input()
        cur = con.cursor()
        if answer == "REGISTER":
            while True:
                print("Welcome to regestration. Type username and password to create a user (e.g. John123 safepassword) or 'b' to go back to login.")
                answer = input().split()
                if answer[0] == 'b':
                    break
                if len(answer) != 2:
                    print(f"Expected 2 arguments, got {len(answer)}.")
                    continue
                elif cur.execute("SELECT username FROM settings WHERE username=?", answer[0]).fetchall() is not None:
                    print(f"Username {answer[0]} is already taken, try another one.")
                    continue
                elif not _is_valid_password(answer[1]):
                    print("Password should be 8 symbols or longer, contain a digit and an upper case letter.")
                    continue
                else:
                    cur.execute("""INSERT INTO settings(username, password) VALUES
                                ('?,?')""", answer[0], _hash_password(answer[1]))
                    con.commit()
                    