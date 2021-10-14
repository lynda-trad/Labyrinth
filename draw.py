from PIL import Image, ImageDraw


def rectangle(output_path, lab, path):
    imageSize = len(lab) * 2
    rectSize = int(len(lab) / 2)
    #imageSize = 100
    #rectSize = 20

    image = Image.new("RGB", (imageSize, imageSize), "#F5F5DC")
    draw = ImageDraw.Draw(image)

    for i in range(len(lab)):
        for j in range(len(lab)):
            if i == j == 0:
                draw.rectangle([(0, 0), (rectSize, rectSize)], fill="black")
            elif lab[i][j] == '#':
                draw.rectangle([(j * rectSize, i * rectSize), (j + 1 * rectSize, i + 1 * rectSize)], fill="black")
            elif (i, j) in path:
                draw.rectangle([(j * rectSize, i * rectSize), (j + 1 * rectSize, i + 1 * rectSize)], fill="blue")
            else:
                draw.rectangle([(j * rectSize, i * rectSize), (j + 1 * rectSize, i + 1 * rectSize)], fill="white")

    image.save(output_path)
    image.show()

####################################
# MEMO
# draw.rectangle([(0, 0), (19, 19)], fill="black")    # 0 ; 0
# draw.rectangle([(20, 0), (40, 20)], fill="red")     # 0 ; 1
# draw.rectangle([(40, 0), (60, 20)], fill="green")   # 0 ; 2
# draw.rectangle([(0, 20), (20, 40)], fill="yellow")  # 1 ; 0
# draw.rectangle([(0, 40), (20, 60)], fill="purple")  # 2 ; 0
# (j * 20, i * 20), (j + 1 * 20, i + 1 * 20)
