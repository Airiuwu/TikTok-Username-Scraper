import random, string, time, TikTokApi, os, config

api = TikTokApi.TikTokApi.get_instance(custom_verifyFp=config.verifyCode, use_test_endpoints=True)

if os.name != "nt":
    clear = os.system("clear")
else:
    clear = os.system("cls")

def randomUsername(size=8, chars=string.ascii_letters + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))

def checkUsers(count=0):
    clear
    print("NOTICE: Accounts with characters of 3/4 may have a chance of being not available though shown as not taken.")
    amount = int(input("Please enter the character amount of usernames you want to check. (Minimum is 3) "))
    if amount >= 3:
        clear
        while True:
            username = randomUsername(size=amount)
            try:
                tiktokUsers = api.get_user(username=username)
                count += 1
                print(f"\033[91mID -> {username}\n \033[0mAccounts Checked -> {count}")
                time.sleep(1)
            except TikTokApi.exceptions.TikTokNotFoundError as error:
                count += 1
                print(f"\033[92m{error}\n \033[0mAccounts Checked -> {count}")
                time.sleep(1)
                continue
    else:
        print("Minimum is 3.")

checkUsers()