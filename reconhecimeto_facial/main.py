# importa as bibliotecas
import cv2
import numpy as np
import os 

def captura(largura, altura):
    # classificadores
    classificador = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    classificador_olho = cv2.CascadeClassifier('haarcascade_eye.xml')

    # camera
    camera = cv2.VideoCapture(0) # 0 é câmera padrão, pode haver mais de uma câmera, veja qual irá utilizar

    # amostras do usuário, ideal de no mínimo de 25 imagens diferentes do mesmo usuário 
    amostra = 1 
    n_amostras = 25

    # recebe o id do usuário 
    id = input("Digite o ID do usuário: ")

    # mensagem indicando capturas de imagens
    print('Capturando as imagens...')

    # Loop 
    while True:
        conectado, imagem = camera.read()
        imagem_cinza = cv2.cvtColor(imagem,cv2.COLOR_BGR2GRAY)
        faces_detectadas = classificador.detectMultiScale (imagem_cinza, scaleFactor=1.5, minSize=(150,150))

        # identifica a geometria das faces
        for (x, y, l, a) in faces_detectadas:
            cv2.rectangle(imagem, (x, y), (x+l, y+a), (0, 0, 255), 2)
            regiao = imagem[y:y + a, x:x + 1]
            regiao_cinza_olhos = cv2.cvtColor(regiao, cv2.COLOR_BGR2GRAY)
            olhos_detectados = classificador_olho.detectMultiScale(regiao_cinza_olhos)

            # identificar a geometria dos olhos
            for (ox, oy, ol, oa) in olhos_detectados:
                cv2.rectangle(regiao, (ox, oy), (ox+ol, oy+oa), (0, 255,0), 2)

                if cv2.waitKey(1) and 0xFF == ord('c'):
                    if np.average(imagem_cinza) > 110:
                        while amostra <= n_amostras:
                            imagem_face = cv2.resize(imagem_cinza[y:y + a, x:x + 1], (largura, altura))
                            cv2.iwrite(f'fotos/pessoa.{str(id)}.{str(amostra)}.jpg', imagem_face)# caminho da imagem
                            print(f'[foto] {str(amostra)} capturada com sucesso.')
                            amostra += 1
        cv2.imshow('Detectar faces', imagem)
        cv2.waitKey(1)

        if (amostra >= n_amostras + 1):
            print('Faces capturadas com sucesso')
            break
        elif cv2.waitKey(1) == ord('q'):
            print('Captura encerrada.')
            break
    # encerra a captura 
    camera.realise()
    cv2.destroyAllWindows()
    # fim de função 

# programa principal
if __name__ == "__main__":
    # definir o tamanho da camera
    largura = 220
    altura = 220

    while True:
    # menu
        print('0 - Sair do programa.')
        print('1 - Capturar a imagem do usuário.')

        opcao = input('Opção desejada: ')

        match opcao:
            case '0':
                print('Programa encerrado')
                break
            case '1':
                captura(largura, altura)
                continue

# trecho de código para consertar é amtes do for (ox, oy) mesma identação, retirar o if cv2.waitKey
'''
if np.average(imagem_cinza) > 110 and amostra <= n_amostras: 
    imagem_face = cv2.resize(imagem_cinza[y:y + a, x:x + 1], (largura, altura))
    cv2.imwrite(f'fotos/pessoas. {str(amostra)}.jpg', imagem_face)
    print(f'[foto] {str(ampstra)} capturada com sucesso)
    amostra += 1
# NOTE: Funciona com "c"
'''



