import cv2
import os
import numpy as np


videopath = "D:/Uni/Semester 5/Cultural Analytics/Videos/"
image_folders_path = "D:/Uni/Semester 5/Cultural Analytics/Daten/frames/"
filenames = [f for f in os.listdir(videopath) if os.path.isfile(os.path.join(videopath, f))]

# loop over every file
for filename in filenames:
    # list of ever frame of a given video
    images = [f for f in os.listdir(image_folders_path + filename.split(".")[0]) if os.path.isfile(os.path.join(image_folders_path + filename.split(".")[0], f))]


    all_centers = []

    # loop over every image in the folder
    for image in images:
        img = cv2.imread(image_folders_path+ filename.split(".")[0]+"/"+image)

        # get image shape and reshape it to work with the data
        height, width, _ = np.shape(img)
        data = np.reshape(img, (height * width, 3))
        data = np.float32(data)


        cluster_number = 5
        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER,10,1.0) # initialize criteria for the clustering
        flags = cv2.KMEANS_RANDOM_CENTERS # we want to cluster with random center initialization
        compactness, labels, centers = cv2.kmeans(data, cluster_number, None, criteria, 10, flags) # k-means-clustering
        for rgb in centers:
            all_centers.append([rgb[0],rgb[1],rgb[2]]) #save everyy center as an rgb value array in the center list

    # write computed centers into a text file for every video, which is later read to compute the cluster centers for every video
    file = open("D:/Uni/Semester 5/Cultural Analytics/Daten/centers/"+ filename.split(".")[0] +".txt", "w+")
    content = str(all_centers)
    file.write(content)
    file.close()