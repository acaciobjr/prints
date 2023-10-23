import os
#from PIL import ImageGrab

#Verificando se a pasta existe e criá-la se não existir.
decisao1 = input("qual nome deseja dar a pasta?")
nome_pasta = decisao1
caminho_pasta = os.path.join(os.getcwd(), nome_pasta)

if not os.path.exists(caminho_pasta):
    os.makedirs(caminho_pasta)
    print(f"a pasta '{decisao1}' foi criada")

#pergunta ao usuário se deseja criar um novo notepad para armazenamento dos novos dados.
while True:
    decisao = input("Deseja criar um novo Notepad (s/n)? ").lower()
    if decisao == 's' or 'S':
        nome_arquivo = input("Qual nome você deseja dar ao Notepad? ")
        caminho_arquivo = os.path.join(caminho_pasta, nome_arquivo + ".txt")
        with open(caminho_arquivo, "w") as arquivo:
            print(f"Notepad '{nome_arquivo}' criado com sucesso.")
        break
    elif decisao != 's' or 'S':
        notepad = input("Qual o nome do Notepad que você deseja abrir? ")
        caminhonote = os.path.join(os.getcwd(), notepad)
        if os.path.exists(caminhonote):
            print(f"Abrindo Notepad '{notepad}'...")
            #abaixo, linha que abre o notepad escolhido pelo nome
            os.system(f"notepad {caminhonote}")
            break
        else:
            print(f"O Notepad '{notepad}' não existe ou não foi encontrado.")


#Perguntando ao usuário o que ele deseja escrever e escrever isso no notepad.
texto = input("O que você deseja escrever no notepad? ")
with open(caminho_arquivo, "a") as arquivo:
    arquivo.write(texto + "\n")
print(f"Texto adicionado com sucesso no arquivo '{nome_arquivo}'.")

#Abrindo o arquivo com o aplicativo padrão
#os.system(f"start {caminho_arquivo}")

'''
contador = 1
nome_arquivoscreen = f"screenshot_{contador}.jpg"
caminho_screenshot = os.path.join(caminho_pasta, nome_arquivoscreen)

screenshot = ImageGrab.grab()
screenshot.save(caminho_screenshot)
print(f"Screenshot {nome_arquivoscreen} salvo em {caminho_screenshot}")
'''
