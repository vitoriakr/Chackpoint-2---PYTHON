# Ela será usada para escolher um item aleatório depois
from random import choice

# Entrada de email e senha do usuário
user_email = str(input("Digite o seu Email: "))
user_password = int(input("Digite a sua Senha Numérica: "))

# Lista com alguns emails para teste de validação
list_user_input_email = [
    "kaua@gmail.com",
    "vitoriagmail.com",
    "anita@gmailcom",
    "  MARIA@GMAIL.COM  ",
    "lucas@g mail com",
]

# Adiciona o email digitado pelo usuário na lista
list_user_input_email.append(user_email)

# Listas para separar emails válidos e inválidos
list_user_valid_email = []
list_user_invalid_email = []

# Percorre todos os emails da lista
for email in list_user_input_email:
    # Remove espaços, deixa tudo minúsculo
    valid_email = email.strip().lower().replace(" ", "") 
    # Verifica se o email possui @, . e tamanho máximo
    if "@" not in valid_email or "." not in valid_email or len(valid_email) > 25:
        # Se for inválido, adiciona na lista de inválidos
        list_user_invalid_email.append(email)
        is_email_valid = False
    else:
        # Se for válido, adiciona na lista de válidos
        list_user_valid_email.append(valid_email)
        is_email_valid = True

# Lista de senhas para teste
list_user_input_password = [
    1234,
    5678,
    123,
    123456789
]

# Adiciona a senha do usuário na lista
list_user_input_password.append(user_password)

# Listas para separar senhas válidas e inválidas
list_user_valid_password = []
list_user_invalid_password = []

# Percorre todas as senhas
for password in list_user_input_password:
    # Verifica se a senha possui entre 4 e 8 números
    if len(str(password)) > 3 and len(str(password)) < 9:
        list_user_valid_password.append(password)
        is_password_valid = True
    else:
        list_user_invalid_password.append(password)
        is_password_valid = False

# Mostra os emails e senhas corretos
print(f"-" * 5, "EMAILS E SENHAS CORRETOS", "-" * 5)
for i in list_user_valid_email:
    print(i)
for i in list_user_valid_password:
    print(i)

# Mostra os emails e senhas incorretos
print(f"-" * 5, "EMAILS E SENHAS INCORRETOS", "-" * 5)
for i in list_user_invalid_email:
    print(i)
for i in list_user_invalid_password:
    print(i)

# O jogo só inicia se email e senha forem válidos
if is_email_valid == True and is_password_valid == True:

    print("\n" + "=" * 40)
    print("INICIANDO O JOGO".center(40))
    print("=" * 40 + "\n")

    forbidden_names = ["admin", "deus", "mestre"] # Lista de nomes proibidos

    # Loop para validar o nome do personagem
    while True:
        character_user = input("\nDigite o Nome do Seu Personagem: ")
        # Remove espaços e transforma o nome em minúsculo
        name = character_user.strip().lower()
        # Verifica se o nome possui apenas letras
        if not name.isalpha():
            print("Digite apenas letras.")
            continue
        # Verifica se o nome está na lista proibida
        elif name in forbidden_names:
            print(f"-" * 5, "ESSE NOME NÃO É PERMITIDO. ESCOLHA OUTRO.", "-" * 5)
            continue
        print("-" * 5, f"O NOME {character_user} É VÁLIDO", "-" * 5)
        print(f"-" * 5, "ESCOLHA A SUA CLASSE", f"-" * 5)
        
        # Lista do inventário inicial
        itens = []
        
        # Escolha da classe do personagem
        number_choice = input('DIGITE O NÚMERO PARA ESCOLHER A SUA CLASSE:\n1 - Guerreiro\n2 - Assassino\n3 - Mago\n4 - Clérico\n5 - Arqueiro: ')
        # Define a classe e os itens iniciais
        match number_choice:
            case "1":
                itens.extend(["Martelo","Canhão","Espada"])
                type_character = "Guerreiro"
                print(f'Você escolheu ser um Guerreiro!\nVocê recebeu os seguintes itens: {itens}')
            case "2":
                itens.extend(["Faca Dupla","Veneno","Corda"])
                type_character = "Assassino"
                print(f'Você escolheu ser um Assassino!\nVocê recebeu os seguintes itens: {itens}')
            case "3":
                itens.extend(["Vara","Kit Poçoes","Barsa"])
                type_character = "Mago"
                print(f'Você escolheu ser um Mago!\nVocê recebeu os seguintes itens: {itens}')
            case "4":
                itens.extend(["Ervas","Biblia","Cruz Grande"])
                type_character = "Clérico"
                print(f'Você escolheu ser um Clérico!\nVocê recebeu os seguintes itens: {itens}')
            case "5":
                itens.extend(["Arco e flecha","Querosene","Granadas"])
                type_character = "Arqueiro"
                print(f'Você escolheu ser um Arqueiro!\nVocê recebeu os seguintes itens: {itens}')
            # Caso o jogador digite uma opção inválida
            case _:
                print("Classe inválida.")
                continue
        break 

        # Evento do baú
    print('='*50)
    print(f'-' * 5, ' Você encontrou um baú misterioso! ', '-' * 5,)
    print('='*50)

        # Dicionário com itens raros de cada classe
    rare_items = {
        'Guerreiro': 'Espada Lendária',
        'Assassino': 'Adaga Sombria',
        'Mago': 'Grimório Proibido',
        'Clérico': 'Relíquia Sagrada',
        'Arqueiro': 'Arco Élfico'
        }
    while True:
        chest_choice = input('\nVocê escolhe abrir o baú? (sim/não): ').strip().lower()
        # Validação da resposta
        if chest_choice not in ["sim", "não", "nao"]:
            print('Resposta inválida!   Tente novamente')
            continue
        break

    # Adiciona item raro caso o jogador abra o baú
    if chest_choice == 'sim':
        rare_items = rare_items[type_character]
        itens.append(rare_items)
        print(f'\nVocê encontrou: -- {rare_items} --')
        print(f'\nInventário atual: {itens}')
    else:
        print('Você ignorou o baú e seguiu em frente...')


    # Evento do ladrão
    if len(itens) > 0:
        print("-" * 5, "LADRÃO APARECE", "-" * 5)
            # Escolhe um item aleatório para ser roubado
        stolen_item = choice(itens)
        itens.remove(stolen_item)
        print("-" * 5, f"INFELIZMENTE, O ITEM {stolen_item} FOI ROUBADO.", "-" * 5)

        # Exibição da ficha final do herói
    print('*' * 40)
    print('FICHA DO HERÓI'.center(40))
    print('*' * 40)
    print(f'\nNome:               {character_user}')
    print(f'\nClasse:             {type_character}')
    if len(itens) == 0:
        print('\nInventário: vazio...')
    else:
        print(f'\nInventario: ')
        for item in itens:
            print(f'                    [ {item} ]')
    print('*' * 40)

# Mensagem exibida caso email ou senha sejam inválidos
else:
    print("\nERRO: Email ou senha inválidos.")
    print("Não foi possível iniciar o jogo.")