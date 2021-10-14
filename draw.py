from PIL import Image, ImageDraw


def rectangle(output_path, lab):
    image = Image.new("RGB", (400, 400), "#F5F5DC")
    draw = ImageDraw.Draw(image)

    # draw.rectangle([(0, 0), (19, 19)], fill="black")   # 0 ; 0
    # draw.rectangle([(20, 0), (40, 20)], fill="red")    # 0 ; 1^   (j * 20, i * 20), (j + 1 * 20, i + 1 * 20)
    # draw.rectangle([(40, 0), (60, 20)], fill="green")  # 0 ; 2    (40, 0), (60, 20)
    # draw.rectangle([(0, 20), (20, 40)], fill="yellow")  # 1 ; 0   (0, 20), (20, 40)
    # draw.rectangle([(0, 40), (20, 60)], fill="purple")  # 2 ; 0
    # (j * 20, i * 20), (j + 1 * 20, i + 1 * 20)

    for i in range(len(lab)):
        for j in range(len(lab)):
            if i == j == 0:
                draw.rectangle([(0, 0), (19, 19)], fill="black")
            elif lab[i][j] == '#':
                draw.rectangle([(j * 20, i * 20), (j + 1 * 20, i + 1 * 20)], fill="black")
            else:
                draw.rectangle([(j * 20, i * 20), (j + 1 * 20, i + 1 * 20)], fill="white")

    image.save(output_path)
    image.show()
