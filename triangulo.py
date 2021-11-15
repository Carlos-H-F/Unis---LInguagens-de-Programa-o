lado_um = int(input("Digite o valor do  1 lado: "))
lado_dois = int(input("Digite o valor do 2 lado:"))
lado_tres = int(input("Digite o valor do 3 lado: "))

if lado_um + lado_dois > lado_tres and lado_dois + lado_tres > lado_um and lado_tres + lado_um > lado_dois:
    print("Isso é um triangulo")
    base = int(input("Digite o valor da base do triangulo: "))
    altura = int(input('Digite o valor da altura do triangulo: '))
    area = ( base * altura )/ 2
    print(f"A area do triangulo é {area}")
else:
    print("Isso não é um triangulo")