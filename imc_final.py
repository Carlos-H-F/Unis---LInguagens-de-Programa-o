from tkinter import *


def calcular_imc():
    peso_paciente = peso.get()
    altura_paciente = altura.get()
    peso_cv = float(peso_paciente)
    altura_cv = float(altura_paciente)
    imc = peso_cv/(altura_cv*altura_cv)

    caixa_de_resultado["text"] = imc


def reiniciar():
        endereco.delete(0)
        paciente.delete(0)
        peso.delete(0)
        altura.delete(0)
        return
def fechar():

    mainwindow.destroy()
    return

mainwindow = Tk()
mainwindow.geometry("650x450")
mainwindow.configure(background="#f00")
mainwindow.title("Cálculo do INC - índice de Massa Corporal")

txt = Label(mainwindow, text="Nome do Paciente", background="#f00", foreground="#000")
txt.place(x=10, y=30, height=30, width=150)
paciente = Entry(mainwindow)
paciente.place(x=160, y=35, height=20, width=450)

txt1 = Label(mainwindow, text="Endereço Completo", background="#f00", foreground="#000")
txt1.place(x=10, y=80, height=30, width=150)
endereco = Entry(mainwindow)
endereco.place(x=160, y=85, height=20, width=450)

txt2 = Label(mainwindow, text="Altura (cm)", background="#f00", foreground="#000")
txt2.place(x=10, y=130, height=30, width=150)
altura = Entry(mainwindow)
altura.place(x=160, y=135, height=20, width=150)

txt3 = Label(mainwindow, text="Peso (kg)", background="#f00", foreground="#000")
txt3.place(x=10, y=180, height=30, width=150)
peso = Entry(mainwindow)
peso.place(x=160, y=185, height=20, width=150)



caixa_de_resultado = Label(mainwindow, text="", background="#fff", foreground="#000")
caixa_de_resultado.place(x=350, y=130, height=75, width=260)

btn_calcular = Button(mainwindow, text="Calcular", background="#fff", foreground="#000",command=calcular_imc)
btn_calcular.place(x=50, y=245, width=100, height=30)

btn_reiniciar = Button(mainwindow, text="Reiniciar", background="#fff", foreground="#000",command=reiniciar)
btn_reiniciar.place(x=150, y=245, width=100, height=30)

btn_sair = Button(mainwindow, text="Sair", background="#fff", foreground="#000",command=fechar)
btn_sair.place(x=350, y=245, width=100, height=30)

mainwindow.mainloop()

