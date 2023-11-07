import gzip
import pickle
import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
import tarfile


#def extract_data_from_gz(gz_file):
    # Nome do arquivo descompactado
    #uncompressed_file = gz_file.replace('.gz', '')

    # Verificar se o diretório já existe
    #if not os.path.exists(uncompressed_file.replace('.tar', '-py')):
        # O diretório não existe, então descompacte o arquivo .tar
        #with gzip.open(gz_file, 'rb') as f_in:
            #with open(uncompressed_file, 'wb') as f_out:
                #f_out.write(f_in.read())

        # Agora, descompacte o arquivo .tar
        #with tarfile.open(uncompressed_file, 'r') as tar:
            #tar.extractall()

    #return uncompressed_file.replace('.tar', '-py')

# Exemplo de uso:
#gz_file = 'cifar-10-python.tar.gz'
#extracted_dir = extract_data_from_gz(gz_file)

# Caminho para o arquivo data_batch_1
data_batch_file = os.path.join('cifar-10-batches-py', 'data_batch_1')

# Verificar se o arquivo de dados existe
if os.path.exists(data_batch_file):
    # O arquivo existe, então prossiga com a leitura
    with open(data_batch_file, 'rb') as fo:
        data_batch = pickle.load(fo, encoding='bytes')

    # Escolha a imagem (ex: índice 100)
    image_data = data_batch[b'data'][100]
    image = image_data.reshape(3, 32, 32).transpose(1, 2, 0)

    # Exibir informações sobre a imagem
    altura, largura, canais = image.shape
    tipo_dado = image.dtype
    imagem_tons_de_cinza = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    tom_cinza_maximo = imagem_tons_de_cinza.max()
    tom_cinza_medio = imagem_tons_de_cinza.mean()
    tom_cinza_minimo = imagem_tons_de_cinza.min()

    print("Informações da Imagem:")
    print(f"Altura: {altura}")
    print(f"Largura: {largura}")
    print(f"Canais de Cor: {canais}")
    print(f"Tipo de Dado: {tipo_dado}")
    print(f"Tons de Cinza - Máximo: {tom_cinza_maximo}")
    print(f"Tons de Cinza - Médio: {tom_cinza_medio}")
    print(f"Tons de Cinza - Mínimo: {tom_cinza_minimo}")

    # Aplicar o filtro da média
    average_filtered = cv2.blur(image, (5, 5))  # O tamanho do kernel (5x5) pode ser ajustado

    # Aplicar o filtro da mediana
    median_filtered = cv2.medianBlur(image, 5)  # O tamanho do kernel (5) pode ser ajustado

    # Aplicar o filtro gaussiano
    gaussian_filtered = cv2.GaussianBlur(image, (5, 5), 0)  # O tamanho do kernel (5x5) pode ser ajustado

     # Configure a exibição das imagens
    plt.figure(figsize=(12, 4))

    plt.subplot(141)
    plt.title('Imagem Original')
    plt.imshow(image)
    plt.axis('off')

    plt.subplot(142)
    plt.title('Filtro da Média')
    plt.imshow(average_filtered)
    plt.axis('off')

    plt.subplot(143)
    plt.title('Filtro da Mediana')
    plt.imshow(median_filtered)
    plt.axis('off')

    plt.subplot(144)
    plt.title('Filtro Gaussiano')
    plt.imshow(gaussian_filtered)
    plt.axis('off')

    plt.tight_layout()
    plt.show()
else:
    print(f"Arquivo {data_batch_file} não encontrado.")