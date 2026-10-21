import cv2

image = cv2.imread("OpenCV/Save and Grayscale Image/Me.jpeg")

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

resized_image = cv2.resize(gray_image, (512, 750))

cv2.imshow("Processed Image", resized_image)

key = cv2.waitKey(0)

if key == ord("s"):
    cv2.imwrite("OpenCV/Save and Grayscale Image/Me_grayscale.jpeg", resized_image)
    print("Image saved")
else:
    print("Not saved")

cv2.destroyAllWindows()

print(f"Image dimension : {resized_image.shape}")