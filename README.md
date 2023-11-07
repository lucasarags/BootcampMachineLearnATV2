# Processamento de Imagem com Filtros em Python

Neste script em Python, estamos realizando o processamento de imagem em um conjunto de dados chamado CIFAR-10 usando diversas técnicas de filtragem, como o filtro da média, o filtro da mediana e o filtro gaussiano. Vamos detalhar as tecnologias utilizadas, o que foi feito e o propósito deste código.

## Tecnologias Utilizadas:

-   Python: Linguagem de programação de alto nível.
-   OpenCV (cv2): Uma biblioteca amplamente usada para processamento de imagens.
-   NumPy: Biblioteca para computação numérica em Python.
-   Matplotlib: Uma biblioteca para criar visualizações e gráficos em Python.
-   Gzip: Usado para descompactar arquivos gzip.
-   Pickle: Usado para serializar e desserializar objetos Python.
-   Tarfile: Usado para descompactar arquivos tar.

## Detalhes do Código:

1.  A função `extract_data_from_gz(gz_file)` é definida para extrair os dados de um arquivo compactado no formato `.tar.gz`. O código verifica se o diretório já existe e, se não, descompacta o arquivo `.tar` e, em seguida, extrai o conteúdo.
    
2.  O exemplo de uso mostra como utilizar a função `extract_data_from_gz()` para extrair os dados do arquivo CIFAR-10. Devido aos limites de 100 MB pelo github, optou-se por deixar somente uma parte dos dados extraídos.
    
3.  Após a extração, o código carrega um arquivo de lote de dados (por exemplo, `data_batch_1`) e exibe informações sobre uma imagem específica, como altura, largura, canais de cor, tipo de dado e tons de cinza máximo, médio e mínimo.
    
4.  O código aplica três filtros diferentes à imagem:
    
    -   Filtro da Média: `cv2.blur(image, (5, 5))`
    -   Filtro da Mediana: `cv2.medianBlur(image, 5)`
    -   Filtro Gaussiano: `cv2.GaussianBlur(image, (5, 5), 0)`
5.  As imagens originais e as imagens filtradas são exibidas em um único gráfico usando o Matplotlib para permitir a comparação dos efeitos dos diferentes filtros.
    

## Propósito:

O propósito deste código é ilustrar o processo de processamento de imagem usando diferentes filtros em um exemplo prático. Os filtros da média, mediana e gaussiano são comumente usados para suavizar imagens, reduzir ruídos ou realçar certos recursos. Este código permite aos usuários ver o efeito desses filtros em uma imagem específica e entender como ajustar os parâmetros dos filtros para atender às necessidades de processamento de imagem em suas próprias aplicações. Além disso, demonstra a extração de dados de um arquivo compactado, o carregamento de imagens e o uso de bibliotecas populares de processamento de imagem em Python.
