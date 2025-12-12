from PIL import Image

def make_square_cover(input_path: str, output_path: str):
    img = Image.open(input_path).convert("RGB")
    width, height = img.size

    # Determinar el tamaño del cuadrado (lado = el menor de ancho/alto)
    size = min(width, height)

    # Calcular coordenadas para recorte centrado
    left = (width - size) // 2
    top = (height - size) // 2
    right = left + size
    bottom = top + size

    # Recortar y guardar
    cropped = img.crop((left, top, right, bottom))
    cropped.save(output_path, "JPEG")

    return output_path
