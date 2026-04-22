import random 

user_email = str(input("Digite o seu Email: "))
user_password = int(input("Digite a sua Senha Numérica: "))

list_user_input_email = [
    "kaua@gmail.com",
    "vitoriagmail.com",
    "anita@gmailcom",
    "  MARIA@GMAIL.COM  ",
    "lucas@g mail com",
]

list_user_input_email.append(user_email)

list_user_valid_email = []
list_user_invalid_email = []

for email in list_user_input_email:
    valid_email = email.strip().lower().replace(" ", "")
    if "@" not in valid_email or "." not in valid_email or len(valid_email) > 25:
        list_user_invalid_email.append(email)
        is_email_valid = False
    else:
        list_user_valid_email.append(valid_email)
        is_email_valid = True

list_user_input_password = [
    1234,
    5678,
    123,
    123456789
]

list_user_input_password.append(user_password)

list_user_valid_password = []
list_user_invalid_password = []

for password in list_user_input_password:
    if len(str(password)) > 3 and len(str(password)) < 9:
        list_user_valid_password.append(password)
        is_password_valid = True
    else:
        list_user_invalid_password.append(password)
        is_password_valid = False

print(f"-" * 5, "EMAILS E SENHAS CORRETOS", "-" * 5)
for i in list_user_valid_email:
    print(i)
for i in list_user_valid_password:
    print(i)

print(f"-" * 5, "EMAILS E SENHAS INCORRETOS", "-" * 5)
for i in list_user_invalid_email:
    print(i)
for i in list_user_invalid_password:
    print(i)

if is_email_valid == True and is_password_valid == True:
    print("="*30)
    print(f"-" * 5, "INICIANDO O JOGO", "-" * 5,)
    print("="*30)
    
    forbidden_names = ["admin", "deus", "mestre"]

while True:
    character_user = input("Digite o nome do seu personagem: ")
    name = character_user.strip().replace(" ", "_").isalpha()
    if name in forbidden_names:
        print("Esse nome não é permitido! Escolha outro.")
        continue
    print(f"O nome {character_user} é válido!\nCONTINUE E ESCOLHA SEU TIPO DE PERSONAGEM!\n")
    
    itens = []
    number_choice = input('DIGITE O NÚMERO:\n1 - Guerreiro (tanque)\n2 - Assasino (DPS)\n3 - Mago (conjurador)\n4 - Clérico (curandeiro)\n5 - Arqueiro (suporte)\nQual número você escolhe: ')
    match number_choice:
        case "1":
            itens.extend(["Martelo","Canhão","Espada"])
            type_character = "Guerreiro"
            print(f'Você escolheu ser um Guerreiro!\nVocê recebeu os reguintes itens: {itens}')
        case "2":
            itens.extend(["Faca Dupla","Veneno","Corda"])
            type_character = "Assasino"
            print(f'Você escolheu ser um Assasino!\nVocê recebeu os reguintes itens: {itens}')
        case "3":
            itens.extend(["Vara","Kit Poçoes","Barsa"])
            type_character = "Mago"
            print(f'Você escolheu ser um Mago!\nVocê recebeu os reguintes itens: {itens}')
        case "4":
            itens.extend(["Ervas","Biblia","Cruz Grande"])
            type_character = "Clérico"
            print(f'Você escolheu ser um Clérico!\nVocê recebeu os reguintes itens: {itens}')
        case "5":
            itens.extend(["Arco e flecha","Querosene","Granadas"])
            type_character = "Arqueiro"
            print(f'Você escolheu ser um Arqueiro!\nVocê recebeu os reguintes itens: {itens}')
    break 

print("="*50)
print(f"-" * 5, " Você encontrou um baú misterioso!", "-" * 5,)
print("="*50)

rare_items = {
    "Guerreiro": "Espada Lendária",
    "Assasino": "Adaga Sombria",
    "Mago": "Grimório Proibido",
    "Clérico": "Relíquia Sagrada",
    "Arqueiro": "Arco Élfico"
}
while True:
    chest_choice = input('Você escolhe abrir o baú? (sim/não): ').strip().lower()
    if chest_choice not in ['sim','SIM','nao','não', 'NÃO']:
        print('Resposta inválida!   Tente novamente')
        continue
    break
if chest_choice == 'sim':
    rare_items = rare_items[type_character]
    itens.append(rare_items)
    print(f'Você encontrou: -- {rare_items} --')
    print(f'Inventário atual: {itens}')
else:
    print('Você ignorou o baú e seguiu em frente...')
    
    
#*evento do ladrão
    

print("*" * 40)
print("FICHA DO HERÓI".center(40))

print('*' * 40)
print(f'Nome:                {character_user}')
print(f'Classe:              {type_character.capitalize()}')
if len(itens) == 0:
    print('Inventário: vazio...')
else:
    print(f'Inventario: ')
    for item in itens:
        print(f'                     [ {item} ]')
print('*' * 40)