from tkinter import *
from time import strftime

# Função para atualizar o relógio


def atualizar_relogio():
    horario_atual = strftime('%H:%M:%S %p')
    rotulo_relogio.config(text=horario_atual)
    rotulo_relogio.after(1000, atualizar_relogio)


# Criação da janela principal
janela = Tk()
janela.title('Relógio Digital')

# Criação do rótulo para exibir o relógio
rotulo_relogio = Label(
    janela,
    font=('Arial', 40, 'bold'),
    background=('light green'),
    foreground=('white')
)
# Posicionando o roótulo no centro da janela
rotulo_relogio.pack(anchor='center')

# Inicia a atualização do relógio
atualizar_relogio()

# Inicia o loop principal da interface gráfica
janela. mainloop()
