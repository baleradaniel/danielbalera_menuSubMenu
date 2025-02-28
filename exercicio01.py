from tkinter import *
class janela:

    def __init__(self,instancia_de_Tk):
        principal = Menu(instancia_de_Tk)
        arquivo = Menu(principal)
        arquivo.add_command(label="Abrir",command=self.abrir)
        arquivo.add_command(label="Salvar",command=self.salvar)   
        principal.add_cascade(label="Arquivo",menu = arquivo)
        principal.add_command(label="Ajuda",command=self.ajuda)
        instancia_de_Tk.configure(menu=principal)

    def abrir(self):print,"Abrir"
    def salvar(self):print,"salvar"
    def ajuda(self):print,"Ajuda"

raiz = Tk()
janela(raiz)
raiz.mainloop()
