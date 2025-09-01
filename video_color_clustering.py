import cv2 
import os
import numpy as np

# creates a bar which is later stacked to form the color palettes
def create_bar(height, width, color):
    bar = np.zeros((height, width, 3), np.uint8)
    bar[:] = color
    red, green, blue = int(color[2]), int(color[1]), int(color[0])
    return bar, (red, green, blue)

centers_path = "D:/Uni/Semester 5/Cultural Analytics/Daten/centers/"
filenames = [f for f in os.listdir(centers_path) if os.path.isfile(os.path.join(centers_path, f))]

for filename in filenames:
    
    # read the cluster center list which was produced by frame_color_extraction.py
    f = open(centers_path+filename, "r")
    content = f.read()
    f.close()

    # split unnecessary chars from the text file data to extract the color values
    initial = content.split('], [')
    initial[0] = initial[0].split('[[')[1]
    initial[len(initial)-1] = initial[len(initial)-1].split(']]')[0]
    
    # save all values as float values in a new list
    rgb_result = [[np.float32(x) for x in y.split(', ')] for y in initial]
    rgb_result = np.float32(rgb_result)
    
    # k means clustering on that list to extract dominant colors for every video
    # parameters are the same as in frame_color_extraction.py
    cluster_number = 5
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER,10,1.0)
    flags = cv2.KMEANS_RANDOM_CENTERS
    compactness, labels, centers = cv2.kmeans(rgb_result, cluster_number, None, criteria, 10, flags)
    
    # create bars for every resulting color
    bars=[]
    for index, row in enumerate(centers):
        bar, rgb = create_bar(200,200,row)
        bars.append(bar)

    # stack bars into a single palette
    img_bar = np.hstack(bars)

    # return images of the color palettes and save them to the drive
    cv2.imshow(filename, img_bar)
    cv2.imwrite("D:/Uni/Semester 5/Cultural Analytics/Daten/dominant_colors/"+filename.split(".")[0]+".png",img_bar)

cv2.waitKey(0)

