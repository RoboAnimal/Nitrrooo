import random, string
import webbrowser
import time
import requests

print("""    [̲̅N][̲̅i][̲̅t][̲̅r][̲̅o] [̲̅G][̲̅e][̲̅n]
""")
time.sleep(0.2)

num=input('How many nitros want?')

f=open("codes.txt","w", encoding='utf-8')

print("Okay lets generate....")
      
for n in range(int(num)):
   y = ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(16))
   f.write('https://discord.gift/')
   f.write(y)
   f.write("\n")

f.close()

with open("codes.txt") as f:
    for line in f:
        nitro = line.strip("\n")

        url = "https://discordapp.com/api/v6/entitlements/gift-codes/" + nitro + "?with_application=false&with_subscription_plan=true"

        r = requests.get(url)

        if r.status_code == 200:
            print(" Valid.txt: {} ".format(line.strip("\n")))
            break
        else:
        	print(" : {} ".format(line.strip("\n")))
input("Press enter 3 times to exit")
input("left 3")
input("left 2")
input("left 1")
print("--- Exit success")