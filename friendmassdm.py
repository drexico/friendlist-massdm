import discord, colorama, os
from colorama import Fore
from discord.ext import commands

class nigger:
    def rename(name)
        os.system(f'title Friend DMER - {name}')

token = input("Enter Token : ")
os.system('cls')


class bruh:
    drex = discord.Client()
    drex = commands.Bot(command_prefix='.', self_bot=True)
    drex.remove_command('help')
    nigger.rename(f"Connected To Account, Waiting For Input...")
    def banner():
        print(f"""{Fore.MAGENTA}
                        ╔═╗╦═╗╦╔═╗╔╗╔╔╦╗╔═╗╦  ╦╔═╗╔╦╗  ╔╦╗╔╦╗╔═╗╦═╗
                        ╠╣ ╠╦╝║║╣ ║║║ ║║╚═╗║  ║╚═╗ ║    ║║║║║║╣ ╠╦╝
                        ╚  ╩╚═╩╚═╝╝╚╝═╩╝╚═╝╩═╝╩╚═╝ ╩   ═╩╝╩ ╩╚═╝╩╚═
                                                  Drexico Made This 
                   {Fore.RESET}                                                             
           """)

    @drex.event
    async def on_connect():
        friends = []
        for i in kek.client.user.friends:
            friends.append(i)
        kek.banner()
        input(f"{Fore.LIGHTGREEN_EX}Press Any Button To Continue...")
        messagewesending = input(f"{Fore.LIGHTGREEN_EX}Enter Message To Send : ")
        print("Starting...")
        utils.rename(f"Sending Message To {len(friends)} Friends...")
        for i in friends:
            try:
                await i.send(messagewesending)
          w      print(f"{Fore.LIGHTCYAN_EX}Message Successfully Sent To : {i.name}{Fore.RESET}")
            except Exception as err:
                print(f"{Fore.RED} Error Sending DM To {i.name}: {err}{Fore.RESET}")
        input(f"{Fore.GREEN}Message Has Been Dmed To {len(friends)} Friends, Press Any Button To Exit.")
        utils.rename("Done sending messages")

    def run(token):
        kek.drex.run(token, bot=False)

kek.run(token)









