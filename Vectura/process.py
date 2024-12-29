import cv2
import numpy as np

def process_image(image_path):
    """
    Обрабатывает изображение, извлекая контуры и создавая SVG-файл.
    :param image_path: Путь к изображению для обработки.
    :return: Путь к сгенерированному SVG-файлу.
    """
    # Загрузка изображения в оттенках серого
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if image is None:
        raise ValueError(f"Не удалось загрузить изображение: {image_path}")
    
    # Преобразование в бинарное изображение
    _, binary = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

    # Поиск контуров
    contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Создание SVG-контента
    height, width = image.shape
    svg_content = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" xmlns:xlink="http://www.w3.org/1999/xlink">\n'
    for contour in contours:
        points = " ".join([f"{point[0][0]},{point[0][1]}" for point in contour])
        svg_content += f'<polygon points="{points}" fill="black" stroke="black" stroke-width="1" />\n'
    svg_content += '</svg>'

    # Сохранение SVG-файла
    output_path = image_path.replace('.png', '_processed.svg').replace('.jpg', '_processed.svg')
    with open(output_path, 'w') as svg_file:
        svg_file.write(svg_content)

    return output_path