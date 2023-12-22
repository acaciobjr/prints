import os
import time

def criando_notepad(contador):
    nome_arquivo = f"Notepad_{contador}.txt"
    with open(nome_arquivo, "w") as arquivo:
        print(f'note {contador} criado.')

def apagando_notepad(contador):
    nome_arquivo = f"Notepad_{contador}.txt"
    if os.path.exists(nome_arquivo):
        os.remove(nome_arquivo)
        print(f"Notepad {nome_arquivo} foi apagado.")
    else:
        print(f"Notepad {nome_arquivo} não foi encontrado.")

contador = 1
text = input('deseja que comece? S/n')

if text == 'S' or text == 's':
    while contador < 30:
        criando_notepad(contador)
        time.sleep(3)
        apagando_notepad(contador)
        contador += 1
else:
    print('programa encerrado.')
