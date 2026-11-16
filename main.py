import cv2

def apply_color(image, filter_type):
    filtered_image = image.copy()

    if filter_type == "orignal":
        return filtered_image
    elif filter_type == "red_tint":
        filtered_image[:, :, 1] = 0
        filtered_image[:, :, 0] = 0
    elif filter_type == "blue_tint":
        filtered_image[:, :, 2] = 0
        filtered_image[:, :, 1] = 0
    elif filter_type == "green_tint":
        filtered_image[:, :, 0] = 0
        filtered_image[:, :, 2] = 0
    elif filter_type == "increase_red":
        filtered_image[:, :, 2] = cv2.add(filtered_image[:, :, 2], 50)
    elif filter_type == "decrease_blue":
        filtered_image[:, :, 0] = cv2.subtract(filtered_image[:, :, 0], 50)

    return filtered_image

image_path = "Me.jpeg"
image = cv2.imread(image_path)

if image is None:
    print("No image in path: ", image_path, "named Me.jpeg")
else:
    image = cv2.resize(image, (1200, 800))

    filter_type = "orignal"

    print("press the following keys for functions:")
    print("o - orignal")
    print("r - red tint")
    print("b - blue tint")
    print("g - green tint")
    print("i - increase red")
    print("d - decrease blue")
    print("q - quit")

    while True:
        filtered_image = apply_color(image, filter_type)

        cv2.imshow("Filtereded image", filtered_image)

        key = cv2.waitKey(0) & 0xFF

        if key == ord("o"):
            filter_type = "orignal"
        elif key == ord("r"):
            filter_type = "red_tint"
        elif key == ord("b"):
            filter_type = "blue_tint"
        elif key == ord("g"):
            filter_type = "green_tint"
        elif key == ord("i"):
            filter_type = "increase_red"
        elif key == ord("d"):
            filter_type = "decrease_blue"
        elif key == ord("q"):
            print("exiting....")
            break
        else:
            print("Invalid input please use o, r, g, b, i, d, q or click ctrl+c to force quit")

    cv2.destroyAllWindows()