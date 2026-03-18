from datetime import datetime

# Stored correct credentials
correct_username = "admin"
correct_password = "secure123"

# Track failed attempts for current run
failed_attempts = 0
max_attempts = 3


def write_log(message):
    with open("login_log.txt", "a") as file:
        file.write(message + "\n")


def analyze_log():
    failed_count = 0

    try:
        with open("login_log.txt", "r") as file:
            for line in file:
                if "FAILED LOGIN" in line:
                    failed_count += 1
    except FileNotFoundError:
        print("No log file found yet.")
        return

    print("\n--- Security Log Analysis ---")
    print(f"Total failed login attempts recorded: {failed_count}")

    if failed_count >= 3:
        print("ALERT: Suspicious activity detected - repeated failed logins.")
    else:
        print("No major security concern detected.")


while failed_attempts < max_attempts:
    username = input("Enter username: ")
    password = input("Enter password: ")

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if username == correct_username and password == correct_password:
        print("Login successful.")
        write_log(f"{timestamp} - SUCCESSFUL LOGIN - {username}")
        break
    else:
        failed_attempts += 1
        print("Invalid username or password.")
        write_log(f"{timestamp} - FAILED LOGIN - {username}")

        remaining = max_attempts - failed_attempts
        if remaining > 0:
            print(f"Attempts remaining: {remaining}")
        else:
            print("SECURITY ALERT: Too many failed login attempts.")
            write_log(f"{timestamp} - SECURITY ALERT - Too many failed login attempts for {username}")

analyze_log()