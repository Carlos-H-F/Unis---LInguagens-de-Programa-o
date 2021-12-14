import datetime

import pymysql
from datetime import date

def cadastrar_paciente():
   nome_paciente = str(input("Nome Paciente"))
   sobrenome_paciente = str(input("Digite o sobrenome do paciente:"))
   idade_paciente = int(input("Digite a idade do paciente:"))
   endereco_paciente = str(input("Digite o endereco do paciente: "))
   controle = int(input("Digite 1 para gravar 2 para recomeçar: "))

   if controle == 1:

      conexao = pymysql.connect(host="localhost",database="imc",user="root",passwd="",autocommit=True,port=3306)
      cursor = conexao.cursor()
      data_cadastro = date.today()
      sql = "INSERT INTO paciente (nome_paciente,sobrenome_paciente,idade_paciente,endereco_paciente,data_cadastro) VALUES (%s,%s,%s,%s,%s)"
      cursor.execute(sql,(nome_paciente,sobrenome_paciente,idade_paciente,endereco_paciente,data_cadastro))
      conexao.close()
      principal()

   if controle ==2:
      cadastrar_paciente()

def consultar_paciente():


      conexao = pymysql.connect(host="localhost",database="imc",user="root",passwd="",autocommit=True,port=3306)
      cursor = conexao.cursor()
      teste = cursor.execute("SELECT * FROM paciente")
      teste = cursor.fetchall()

      for i in teste:
        id_paciente = i[0]
        nome_paciente = i[1]
        sobrenome_paciente =i[2]
        idade_paciente =i[3]
        endereco_paciente =i[4]
        data_cadastro = i[5]
        print(f"ID do paciente {id_paciente} - Nome do paciente {nome_paciente} - Sobrenome do paciente {sobrenome_paciente}")
      control = int(input("Digite 1 para ir ao menu e 2 para sair:"))

      if control == 1:
          principal()
      else:
          return
def calcular_imc():

    conexao = pymysql.connect(host="localhost", database="imc", user="root", passwd="", autocommit=True, port=3306)
    cursor = conexao.cursor()
    teste = cursor.execute("SELECT * FROM paciente")
    teste = cursor.fetchall()

    for i in teste:
        id_paciente = i[0]
        nome_paciente = i[1]
        sobrenome_paciente = i[2]
        idade_paciente = i[3]
        endereco_paciente = i[4]
        data_cadastro = i[5]
        print(f"ID do paciente {id_paciente} - Nome do paciente {nome_paciente} - Sobrenome do paciente {sobrenome_paciente}")

    paciente = int(input("Digite o ID do paciente"))
    altura = int(input("Digite a altura do paciente: "))
    peso = int(input("Digite o peso do paciente:"))
    imc = peso/(altura*altura)*10000
    print(f"SEU IMC É {imc}")
    print("GRAVANDO NO BANCO DE DADOS...")
    print("RETORNANDO AO MENU")
    data_calculado = date.today()

    conexao = pymysql.connect(host="localhost", database="imc", user="root", passwd="", autocommit=True, port=3306)
    cursor = conexao.cursor()
    sql = "INSERT INTO imc_calculado (id_paciente,altura,peso,imc,data_calculado) VALUES (%s,%s,%s,%s,%s)"
    cursor.execute(sql,(paciente,altura,peso,imc,data_calculado))
    principal()

def consultar_historico():
    conexao = pymysql.connect(host="localhost", database="imc", user="root", passwd="", autocommit=True, port=3306)
    cursor = conexao.cursor()
    teste = cursor.execute("SELECT * FROM paciente")
    teste = cursor.fetchall()

    for i in teste:
        id_paciente = i[0]
        nome_paciente = i[1]
        sobrenome_paciente = i[2]
        idade_paciente = i[3]
        endereco_paciente = i[4]
        data_cadastro = i[5]
        print(f"ID do paciente {id_paciente} - Nome do paciente {nome_paciente} - Sobrenome do paciente {sobrenome_paciente}")
    paciente = int(input("Digite o ID do cliente que deseja consultar o historico:"))

    conexao = pymysql.connect(host="localhost", database="imc", user="root", passwd="", autocommit=True, port=3306)
    cursor = conexao.cursor()
    sql = "SELECT nome_paciente, sobrenome_paciente, altura, peso, imc, idade_paciente, data_calculado FROM imc_calculado INNER JOIN paciente ON imc_calculado.id_paciente = paciente.id WHERE id_paciente = '%s' "
    historico = cursor.execute(sql,paciente)
    historico = cursor.fetchall()
    for i in historico:
        nome_paciente = i[0]
        sobrenome_paciente = i[1]
        altura_paciente = i[2]
        peso_paciente = i[3]
        imc_paciente = i[4]
        idade_paciente = i[5]
        data_calculado = i[6]
        print(f"RESULTADO DO HISTORICO DE IMC DO PACIENTE:")
        print(f"Nome do Paciente {nome_paciente}, Sobrenome: {sobrenome_paciente}, idade do paciente: {idade_paciente}")
        print(f"Altura do Paciente {altura_paciente}, Peso do paciente: {peso_paciente}")
        print(f"IMC {imc_paciente}")
        print(f"Calculado realizado em {data_calculado}")
        print("--------/----------///---------////---------//////--------///////-------//////")
    principal()


def principal():
    print("CALCULAR IMC")
    control = int(input("Digite 1 para cadastrar o paciente \n Digite 2 para consultar pacientes \n Digite 3 para calcular IMC \n digite 4 para ver historico"))

    if control == 1:
       cadastrar_paciente()
    if control == 2:
       consultar_paciente()
    if control == 3:
        calcular_imc()
    if control == 4:
        consultar_historico()


principal()
