from time import sleep
nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
sleep(3)
print(f'Seu nome em maiúsculas é {nome.upper()}')
print(f'Seu nome em minúsculas é {nome.lower()}')
print(f'Seu nome tem {len(nome) - nome.count(" ")} letras.')
separa = nome.split()
print(f'O primeiro nome tem {nome.find(" ")} letras e é {separa[0]} .')

