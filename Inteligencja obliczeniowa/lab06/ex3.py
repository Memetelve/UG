import cv2
import os

images = []


def count_blobs(img):
    pass


# open bird_minatures folder and read all images
for filename in os.listdir("bird_miniatures"):
    img = cv2.imread("./bird_miniatures/" + filename)
    images.append(img)

print("Number of images: ", len(images))

# convert images to grayscale
gray_images = []
for img in images:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray_images.append(gray)

# apply threshold to images
threshold_images = []
for img in gray_images:

    thres = cv2.adaptiveThreshold(
        img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 5
    )

    img = cv2.GaussianBlur(img, (7, 7), 0)
    cv2.imwrite("./ex3/image_" + str(len(threshold_images)) + ".jpg", thres)

    threshold_images.append(thres)


# count black blobs
for i, img in enumerate(threshold_images):

    contours, image = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    print("Number of blobs in image ", i, " : ", len(contours) - 1)
