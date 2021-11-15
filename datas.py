from datetime import date

dia_nascimento = int(input("Digite o dia do nascimento: "))
mes_nascimento = int(input("Digite o mês do nascimento: "))
ano_nasciemnto = int(input("DIgite o ano de nascimento; "))

data_nascimento = date(ano_nasciemnto,mes_nascimento,dia_nascimento)
data_atual = date.today()
idade = data_atual.year - data_nascimento.year
meses_de_idade = data_atual.month - data_nascimento.month
dias_de_idade = data_atual.day - data_nascimento.day
total_de_dias = date.today() - data_nascimento
total_de_semanas = (idade * 52) + (meses_de_idade * 4) + (dias_de_idade / 7)
total_de_meses = meses_de_idade + (idade * 12)
print(f"O total de  meses é {total_de_meses}")
print(f"O total de semanas é %.d2" % (total_de_semanas))
print(f"O total de dias é {total_de_dias}")
print(f"A idade é {idade} anos {meses_de_idade} meses e {dias_de_idade} dias")

