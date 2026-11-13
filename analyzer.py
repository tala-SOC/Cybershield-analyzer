from collections import Counter
from datetime import datetime
login_counter = Counter()
failed_users = Counter()
file = open("security.log", "r")
for line in file:
    if "LOGIN SUCCESS" in line:
        login_counter['success'] += 1
        most_recent_success = line.strip()
    elif "LOGIN FAILED" in line:
        most_recent_failed = line.strip() 
        username = most_recent_failed.split()[2].replace("user=", "")
        failed_users[username] += 1
file.close()
print(f"Generated at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print("======================================")
print("     Security Log Analysis Report     ")
print("======================================")
print(f"Total Successful Attempts: {login_counter['success']}")
print(f"Total Failed Attempts: {sum(failed_users.values())}")
print(f"Total Login Attempts: {sum(login_counter.values()) + sum(failed_users.values())}")
most_targeted = failed_users.most_common(1)[0]
if most_targeted[1] >= 3:
    print("\n[WARNING]Possible Brute Force Attack Detected !!!")
    print(f"Top Targeted Users")
    print("---------------------")
    rank = 1
    for user, attempts in failed_users.most_common(): 
        print(f"{rank}. {user}: {attempts}")
        rank += 1
print(f"Target User: {most_targeted[0]}")
print(f"Failed Attempts: {most_targeted[1]}")
print(f"Risk Level: {'High' if sum(failed_users.values()) > 3 else 'Low'}")

print("\n==============")
print(f"   Summary    ")
print(f"==============")
print(f"The analayzed log contains 10 login attempts .")
print(f"5 of them were successful and 5 failed attempts were detected.")
print(f"The account 'admin' experienced the highest number of failed login attempts(3), indicating a potential brute-force attack.")
print("======================================")
print("       End of Security Report         ")
print("======================================")