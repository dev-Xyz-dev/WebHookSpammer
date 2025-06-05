# Made By Xyz
from dhooks import Webhook
import colorama
from colorama import Fore
colorama.init(autoreset=True)

print(f"""{Fore.RED}
██╗  ██╗██╗   ██╗███████╗
╚██╗██╔╝╚██╗ ██╔╝╚══███╔╝
 ╚███╔╝  ╚████╔╝   ███╔╝ 
 ██╔██╗   ╚██╔╝   ███╔╝  
██╔╝ ██╗   ██║   ███████╗
╚═╝  ╚═╝   ╚═╝   ╚══════╝                     {Fore.GREEN}
▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼
""")

print(Fore.GREEN + "Enter webhook URLs (separated by commas): ", end='')
webhooks_raw = input()
webhooks_list = [Webhook(url.strip()) for url in webhooks_raw.split(",") if url.strip()]

print(" ")

print(Fore.GREEN + "Enter the message to spam: ", end='')
message_to_spam = input()

print(f"""
{Fore.GREEN}Spamming started using rotating webhooks...
""")

print(f"""{Fore.GREEN}Close this window to stop.

{Fore.GREEN}▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼
""")

index = 0
while True:
    try:
        current_hook = webhooks_list[index % len(webhooks_list)]
        current_hook.send(message_to_spam)
        print(Fore.CYAN + f"[{index}] Sent via webhook #{(index % len(webhooks_list)) + 1}")
        index += 1
    except Exception as e:
        print(Fore.RED + f"[{index}] Error: {e}")
        index += 1
        continue
