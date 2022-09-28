#discord nitro generator code

import random
import string
import requests


def main():
    print("Discord Nitro Generator")
    print("Made by: SaumonDeLuxe#2960")
    print("")

    while True:
        code = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(16))
        r = requests.get("https://discordapp.com/api/v6/entitlements/gift-codes/" + code + "?with_application=false&with_subscription_plan=true")
        if r.status_code == 200:
            print("Valid Nitro Code: " + code)
            with open("Nitro Codes.txt", "a") as f:
                f.write("Valid Nitro Code: " + code + "")
        else:
            print("Invalid Nitro Code: " + code)

        # time.sleep(0.5)

if __name__ == "__main__":
    main()
