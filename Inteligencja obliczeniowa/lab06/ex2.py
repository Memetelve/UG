import cv2

# Load the image
img = cv2.imread("image.jpg")

# convert the image to grayscale
gray = img[:, :, 0] * 0.114 + img[:, :, 1] * 0.587 + img[:, :, 2] * 0.299

# save the grayscale image
cv2.imwrite("gray_image.jpg", gray)

# show the grayscale image
cv2.imshow("Gray Image", gray)

# convert manually to grayscale
gray_manual = img[:, :, 0] * 0.333 + img[:, :, 1] * 0.333 + img[:, :, 2] * 0.333

# save the manually converted image
cv2.imwrite("gray_manual_image.jpg", gray_manual)
