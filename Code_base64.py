import base64

# 1. Lee la imagen y conviértela en un string base64
with open("Images/Image_1.png", "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read()).decode()

# 2. Guarda el string base64 en un archivo de texto
with open("Images/Image_1_base64.txt", "w") as text_file:
    text_file.write(encoded_string)

print("Imagen guardada en base64 en Images/Image_1_base64.txt")
