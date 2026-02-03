from PIL import Image

image = Image.open("monro.jpg")
image_width = image.width
image_height = image.height
coordinates_middle_crop = (25, 0, image_width - 25, image_height)
coordinates_right_crop = (0, 0, image_width - 50, image_height)
coordinates_left_crop = (50, 0, image_width, image_height)
opacity = 0.3
		
red_image, green_image, blue_image = image.split()

red_image_left = red_image.crop(coordinates_left_crop)
red_image_middle = red_image.crop(coordinates_middle_crop)
red_image_blend = Image.blend(red_image_left, red_image_middle, opacity)

green_image_middle = green_image.crop(coordinates_middle_crop)

blue_image_right = blue_image.crop(coordinates_right_crop)
blue_image_middle = blue_image.crop(coordinates_middle_crop)
blue_image_blend = Image.blend(blue_image_right, blue_image_middle, opacity)

merge_image = Image.merge("RGB", (red_image_blend, green_image_middle, blue_image_blend))
merge_image.save("monro_offset.jpg")
merge_image.thumbnail((80, 80))
merge_image.save("monro_avatar.jpg")