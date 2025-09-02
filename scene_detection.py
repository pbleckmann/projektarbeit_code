from scenedetect import detect, HashDetector
import matplotlib.pyplot as plt
import cv2
import os


videos = "D:/Uni/Semester 5/Cultural Analytics/Videos/"
video_files = [f for f in os.listdir(videos) if os.path.isfile(os.path.join(videos, f))]

# calculate the video length by capturing it, extracting frame count and fps and returning the result
def duration(video):
    vid = cv2.VideoCapture(video)

    frame_count = vid.get(cv2.CAP_PROP_FRAME_COUNT)
    fps = vid.get(cv2.CAP_PROP_FPS)

    return frame_count/fps


val = []
j = 0

# looping over every video file
for video in video_files:
    dur= duration(videos+video) # calculating the duration

    scenes = detect(videos+video, HashDetector()) # detect the scenes via HashDetector

    val.append(len(scenes)/dur) # calculating average amount of cuts per second

    # for every genre append the 5 videos into a bar chart
    x = [1,2,3,4,5] 
    if j%5 == 4:
        plt.bar(x, val)
        plt.xlabel("Videos")
        plt.ylabel("scenes per second")
        plt.ylim([0,1.5])
        plt.show()

        val = []
    
    j += 1
    

