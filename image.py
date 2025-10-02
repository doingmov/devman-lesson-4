from PIL import Image

image = Image.open("monro.jpg")
red, green, blue = image.split()

red_left = red.crop((50, 0, red.width, red.height))
red_middle = red.crop((25, 0, red.width - 25, red.height))
red_blend = Image.blend(red_left, red_middle, 0.5)

blue_right = blue.crop((0, 0, blue.width - 50, blue.height))
blue_middle = blue.crop((25, 0, blue.width - 25, blue.height))
blue_blend = Image.blend(blue_right, blue_middle, 0.5)

green_middle = green.crop((25, 0, green.width - 25, green.height))

min_width = min(red_blend.width, green_middle.width, blue_blend.width)
min_height = min(red_blend.height, green_middle.height, blue_blend.height)

red_final = red_blend.crop((0, 0, min_width, min_height))
green_final = green_middle.crop((0, 0, min_width, min_height))
blue_final = blue_blend.crop((0, 0, min_width, min_height))

final_image = Image.merge("RGB", (red_final, green_final, blue_final))
final_image.save("MONRO_FINAL.jpg")

image = Image.open("MONRO_FINAL.jpg")
image.thumbnail((80, 80))
image.save("MONRO_AVATAR.jpg")