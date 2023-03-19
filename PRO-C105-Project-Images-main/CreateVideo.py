import os
import cv2

# set path for the Images folder
path = "C:\\Users\\User\\OneDrive\\Desktop\\New folder (2)\\New folder\\Project 117\\PRO-C105-Project-Images-main\\Images"

# create a list variable named Images
images = []

# use os.listdir(path) to check each file in the folder
for file in os.listdir(path):
    # separate name and extension using os.splitext(file)
    name, extension = os.path.splitext(file)
    # check if the extension matches the image extension
    if extension == ".jpg":
        # create file_name by concatenating path, "/", and filename
        file_name = os.path.join(path, file)
        # add each file in the images list using .append()
        images.append(file_name)
        # use print(file_name) to check filenames
        print(file_name)

# create a variable count to store len(images)
count = len(images)

# read the first image from the images list
frame = cv2.imread(images[0])

# use frame.shape to capture width, height & channels
height, width, channels = frame.shape

# create a tuple variable size using width, height
size = (width, height)

# use print(size) to check the result
print(size)

# create a variable out, assign with cv2.VideoWriter()
out = cv2.VideoWriter("Project.avi", cv2.VideoWriter_fourcc(*'DIVX'), 0.8, size)

# use a for loop to add images to a video writer
for i in range(0, count):
    # read each image using cv2.imread()
    img = cv2.imread(images[i])
    # add the image in the video using out.write()
    out.write(img)

# print a message to know the video is complete
print("Done")
