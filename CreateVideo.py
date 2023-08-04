import os
import cv2

caminho = "Images"

imagens = []

for arquivo in os.listdir(caminho):
    nome, extensao = os.path.splitext(arquivo)

    if extensao in ['.gif', '.png', '.jpg', '.jpeg', '.jfif']:
        nome_arquivo = os.path.join(caminho, arquivo)
        imagens.append(nome_arquivo)

quantidade = len(imagens)

quadro = cv2.imread(imagens[0])
altura, largura, canais = quadro.shape
tamanho = (largura, altura)

saida = cv2.VideoWriter('projeto.mp4', cv2.VideoWriter_fourcc(*'DIVX'), 5, tamanho)  # Mudar o codec para XVID

for i in range(quantidade - 1, 0, -1):
    quadro = cv2.imread(imagens[i])
    saida.write(quadro)

saida.release()
print("Concluído")
