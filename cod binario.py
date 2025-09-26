novoArrlll = []
for i in range (1,101):
    novoArrlll.append(i)
escolha = int(input("Escolha um número: "))
menor = 0 
maior = 99 
meio = (menor + maior) // 2 
while menor <= maior: 
    chute = novoArrlll[meio]
    if chute == escolha: 
        print(f"Achei o número escolhido! \nNúmero: {escolha}")
        break
    elif chute < escolha: 
        menor = chute 
        meio = (menor + maior) // 2 
    else: 
        maior = meio
        meio = (menor + maior) // 2