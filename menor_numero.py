numero_1 = int(input("Digite o primeiro número: "))
numero_2 = int(input("Digite o segundo número: "))
numero_3 = int(input('Digite o terceiro número: '))

if numero_2 and numero_3 > numero_1:
    print("O menor número é o primeiro")
elif numero_1 and numero_2 > numero_3:
    print("O menor número é o terceiro")
elif numero_1 and numero_3 > numero_2:
    print("O menor número é o segundo")
elif numero_1 == numero_2 == numero_3:
    print("Todos os números são iguais")