from PIL import Image, ImageDraw


def rectangle(output_path, lab):
    image = Image.new("RGB", (400, 400), "#F5F5DC")
    draw = ImageDraw.Draw(image)

    #draw.rectangle((20, 0, 0, 20), fill="black")     # 0 ; 0
    #draw.rectangle((40, 0, 20, 20), fill="red")      # 0 ; 1
    #draw.rectangle((60, 0, 40, 20), fill="green")    # 0 ; 2

    #draw.rectangle((40, 20, 0, 40), fill="yellow")  # 1 ; 0
    # ( y , j , i * 20 , x )
    # x = j + 1 * 20
    # y = i + 1 * 20

    for i in range(len(lab)):
        for j in range(len(lab)):
            if i == j == 0:
                draw.rectangle((20, 0, 0, 20), fill="black")
            elif lab[i][j] == '#':
                y = (j + 1) * 20
                x = (i + 1) * 20
                jj = j * 20
                ii = i * 20
                draw.rectangle((y, jj, ii, x), fill="black")
            else:
                y = (j + 1) * 20
                x = (i + 1) * 20
                jj = j * 20
                ii = i * 20
                draw.rectangle((y, jj, ii, x), fill="red")

    image.save(output_path)
    image.show()
