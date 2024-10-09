from PIL import Image
import pytesseract
import cv2

def preprocess_image(image_path):
    """
    Pré-processa a imagem convertendo-a para escala de cinza e binarizando.
    :param image_path: Caminho para a imagem de entrada.
    :return: Imagem processada.
    """
    image = cv2.imread(image_path)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, binary_image = cv2.threshold(gray_image, 128, 255, cv2.THRESH_BINARY)
    return binary_image

def extract_text(image_path, lang='eng', preprocess=False):
    """
    Extrai texto de uma imagem usando Tesseract OCR.
    :param image_path: Caminho para a imagem de entrada.
    :param lang: Idioma para o OCR (ex: 'eng' para inglês, 'por' para português).
    :param preprocess: Se True, pré-processa a imagem antes de extrair o texto.
    :return: Texto extraído.
    """
    if preprocess:
        processed_image = preprocess_image(image_path)
        image = Image.fromarray(processed_image)
    else:
        image = Image.open(image_path)
    
    custom_config = f'--oem 3 --psm 6 -l {lang}'
    text = pytesseract.image_to_string(image, config=custom_config)
    return text
