import amino
import getpass
import os

# Feito por Luiz Eduardo
# Amino.py criada por Slimakoi™
# Slimakoi™ todos os direitos reservados ®.

# Abaixo uma proxy japonesa.
proxies = {'http': '43.224.8.125:6666'}
client = amino.Client(proxies=proxies)

# Sistema login amino:
os.system('clear')
print('\033[1;32m  ┏━━━━┳━━━┳━━━┓╋╋╋┏━━━┳━━━┓')
print('\033[1;32m  ┃┏┓┏┓┃┏━┓┃┏━┓┃╋╋╋┃┏━┓┃┏━┓┃')
print('\033[1;32m  ┗┛┃┃┗┫┃╋┃┃┃╋┗┛╋╋╋┃┗━┛┃┃┃┃┃')
print('\033[1;32m  ╋╋┃┃╋┃┗━┛┃┃┏━┓┏━━┫┏━┓┃┃┃┃┃')
print('\033[1;32m  ╋╋┃┃╋┃┏━┓┃┗┻━┃┗━━┫┗━┛┃┗━┛┃')
print('\033[1;32m  ╋╋┗┛╋┗┛╋┗┻━━━┛╋╋╋┗━━━┻━━━┛')
print('\033[1;32m  ┏━━━┳━━━┳━━━┳━━┳━━━┳━━━━┓')
print('\033[1;32m  ┃┏━┓┃┏━┓┃┏━┓┣┫┣┫┏━┓┃┏┓┏┓┃')
print('\033[1;32m  ┃┗━━┫┃╋┗┫┗━┛┃┃┃┃┗━┛┣┛┃┃┗┛')
print('\033[1;32m  ┗━━┓┃┃╋┏┫┏┓┏┛┃┃┃┏━━┛╋┃┃')
print('\033[1;32m  ┃┗━┛┃┗━┛┃┃┃┗┳┫┣┫┃╋╋╋╋┃┃')
print('\033[1;32m  ┗━━━┻━━━┻┛┗━┻━━┻┛╋╋╋╋┗┛')
print('\033[1;36mFeito por ~>\033[1;92m Luiz Eduardo')
print('\n\033[0m')
print('\033[1;36m Warning: You need a leader in the community to function, I am not responsible for the misuse of the script.')
mail = input('\033[1;32m Your Email:')
password = getpass.getpass('\033[1;32m Your Password:')

client.login(email=mail, password=password)

# Sistema de pegar id de comunidades:
os.system("clear")
print('\033[1;92m ┏━━━┓╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋┏┓')
print('\033[1;92m ┃┏━┓┃╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋┏┛┗┓')
print('\033[1;92m ┃┃╋┗╋━━┳┓┏┳┓┏┳┓┏┳━┓┏╋┓┏╋┓╋┏┓')
print('\033[1;92m ┃┃╋┏┫┏┓┃┗┛┃┗┛┃┃┃┃┏┓╋┫┃┃┃┃╋┃┃')
print('\033[1;92m ┃┗━┛┃┗┛┃┃┃┃┃┃┃┗┛┃┃┃┃┃┃┗┫┗━┛┃')
print('\033[1;92m ┗━━━┻━━┻┻┻┻┻┻┻━━┻┛┗┻┛┗━┻━┓┏┛')
print('\033[1;92m ╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋┏━┛┃')
print('\033[1;92m ╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋┗━━┛')
print('\033[1;92m ┏┓╋╋╋╋┏┓')
print('\033[1;92m ┃┃╋╋╋╋┃┃')
print('\033[1;92m ┃┃┏┳━┓┃┃┏┓┏┓')
print('\033[1;92m ┃┃┣┫┏┓┫┗┛┛┗┛')
print('\033[1;92m ┃┗┫┃┃┃┃┏┓┓┏┓')
print('\033[1;92m ┗━┻┻┛┗┻┛┗┛┗┛')
aminoId = input('\033[1;32m Amino ID Community: ')
sclient = amino.SubClient(aminoId=aminoId, profile=client.profile)

# Sistema de enviar as 80 tags:
os.system("clear")
print('033[1;92m ┏━━━┓╋╋┏┓╋┏┓')
print('033[1;92m ┃┏━┓┃╋┏┛┗┳┛┗┓')
print('033[1;92m ┃┗━┛┣┓┣┓┏┻┓┏╋┳━┓┏━━┓')
print('033[1;92m ┃┏━━┫┃┃┃┃╋┃┃┣┫┏┓┫┏┓┃')
print('033[1;92m ┃┃╋╋┃┗┛┃┗┓┃┗┫┃┃┃┃┗┛┃')
print('033[1;92m ┗┛╋╋┗━━┻━┛┗━┻┻┛┗┻━┓┃')
print('033[1;92m ╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋┏━┛┃')
print('033[1;92m ╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋┗━━┛')
print('033[1;92m ╋┏┓┏┓')
print('033[1;92m ┏┛┗┫┃')
print('033[1;92m ┗┓┏┫┗━┳━━┓')
print('033[1;92m ╋┃┃┃┏┓┃┃━┫')
print('033[1;92m ╋┃┗┫┃┃┃┃━┫')
print('033[1;92m ╋┗━┻┛┗┻━━┛')
print('033[1;92m ╋┏┓')
print('033[1;92m ┏┛┗┓')
print('033[1;92m ┗┓┏╋━━┳━━┳━━┓')
print('033[1;92m ╋┃┃┃┏┓┃┏┓┃━━┫')
print('033[1;92m ╋┃┗┫┏┓┃┗┛┣━━┃┏┓┏┓┏┓')
print('033[1;92m ╋┗━┻┛┗┻━┓┣━━┛┗┛┗┛┗┛')
print('033[1;92m ╋╋╋╋╋╋┏━┛┃')
print('033[1;92m ╋╋╋╋╋╋┗━━┛')
titles = []

for i in range(80):
    titles.append({"title": f"𝐿𝑢𝑓𝑓𝑦 ⛷ ★彡 {i}", "color":"#00EE95"})

# Sistema de finalização/Confirmação:
os.system("clear")
print('\033[1;92m ┏━━━┓╋╋╋╋╋╋╋┏┓╋╋╋╋╋╋┏┓')
print('\033[1;92m ┃┏━━┛╋╋╋╋╋╋╋┃┃╋╋╋╋╋╋┃┃')
print('\033[1;92m ┃┗━━┳┳━┓┏┳━━┫┗━┳━━┳━┛┃')
print('\033[1;92m ┃┏━━╋┫┏┓╋┫━━┫┏┓┃┃━┫┏┓┃')
print('\033[1;92m ┃┃╋╋┃┃┃┃┃┣━━┃┃┃┃┃━┫┗┛┃┏┓')
print('\033[1;92m ┗┛╋╋┗┻┛┗┻┻━━┻┛┗┻━━┻━━┛┗┛')

print(f"\033[1;32m Finished...")

sclient.edit_profile(titles=titles)