from PIL import Image, ImageDraw


def rectangle(output_path, lab):
    image = Image.new("RGB", (400, 400), "#F5F5DC")
    draw = ImageDraw.Draw(image)

    draw.rectangle((20, 0, 0, 20), fill="black")  # 0 ; 0 0 i
    draw.rectangle((40, 0, 20, 20), fill="red")  # 0 ; 1 20 i * 20
    draw.rectangle((60, 0, 40, 20), fill="green")  # 0 ; 2 40

    draw.rectangle((60, 20, 40, 20), fill="yellow")  # 0 ; 2 40
    # ( x , i , j * 20 , taille 20)

    # image = Image.fromarray(lab, 'RGB')

    image.save(output_path)
    image.show()


def scrap(lab, draw):
    for i in range(len(lab)):
        for j in range(len(lab)):
            if i == j == 0:
                draw.rectangle((20, 0, 0, 20), fill="black")
            elif lab[i][j] == '#':
                x = i * 2 + 20
                draw.rectangle((x, i, j * 20, 20), fill="black")
            else:
                draw.rectangle((x, i, j * 20, 20), fill="white")
