from PIL import Image


def split_image(image):

    # Get dimensions of the image
    width, height = image.size

    # Split the image into left and right halves
    left_half = image.crop((0, 0, width // 2, height))
    right_half = image.crop((width // 2, 0, width, height))

    return left_half, right_half


def split_images(image_list):

    split_images_list = []

    # Iterate through the list of images
    for img in image_list:
        left_half, right_half = split_image(img)
        split_images_list.append(left_half)
        split_images_list.append(right_half)

    return split_images_list

