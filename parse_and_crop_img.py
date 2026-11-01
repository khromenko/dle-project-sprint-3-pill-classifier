from PIL import Image
import numpy as np

def parse_and_crop_image(img: Image.Image, label_segment: str, margin = 100):   
    """
    Распарсивает контур объекта на изображении:
    - формирует обрезанное изображение только заданного объекта без лишней информации с исходного изображения
    - добавляет отступ (margin) от края изображения, чтобы захватить немного фона вокруг

    Returns:
        image_crop: Image - обрезанное изображение
        (points_x, points_y): tuple(float[], floatp[]) - точки (координат) контура
        (left, top, right, down): tuple(int, int, int, int) - границы (координаты) рамки вырезания объекта
    """
    
    # parse segment points
    coords = label_segment.split()[1:]
    points_x = [float(x) for x in coords[0::2]]
    points_y = [float(y) for y in coords[1::2]]

    # scale back to original sizes
    W, H = img.width, img.height
    points_x = np.array(points_x) * W
    points_y = np.array(points_y) * H

    # bounding box
    x_min, x_max = min(points_x), max(points_x)
    y_min, y_max = min(points_y), max(points_y)

    # add external margins for visual comfort
    margin = 100    
    left = max(0, x_min - margin)
    right = min(W, x_max + margin)
    top = max(0, y_min - margin)
    down = min(H, y_max + margin)
    image_crop = img.crop(box=(left, top, right, down))

    return image_crop, (points_x, points_y), (left, top, right, down)