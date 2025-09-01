import cv2
import os
import numpy as np
from decord import VideoReader
from decord import cpu, gpu


def extract_frames(video_path, frames_dir, overwrite=False):
    video_dir, video_filename = os.path.split(video_path)  # get the video path and filename from the path

    assert os.path.exists(video_path)  # assert the video file exists

    # load the VideoReader
    vr = VideoReader(video_path, ctx=cpu(0))

    for index in range(0, len(vr)):
        frame = vr[index]  # read an image from the videoReader
            
        save_path = os.path.join(frames_dir, video_filename, "{:010d}.jpg".format(index))  # create the save path
        if not os.path.exists(save_path) or overwrite:  # if it doesn't exist or we want to overwrite anyways
            cv2.imwrite(save_path, cv2.cvtColor(frame.asnumpy(), cv2.COLOR_RGB2BGR))  # save the extracted image


def video_to_frames(video_path, frames_dir, overwrite=False):
    video_dir, video_filename = os.path.split(video_path)  # get the video path and filename from the path

    # make subdirectory in the frames directory with the video name
    os.makedirs(os.path.join(frames_dir, video_filename), exist_ok=True)
    
    extract_frames(video_path, frames_dir)

    return os.path.join(frames_dir, video_filename)


if __name__ == '__main__':

    videopath = "D:/Uni/Semester 5/Cultural Analytics/Videos/"
    destination = "D:/Uni/Semester 5/Cultural Analytics/Daten/frames/"
    onlyfiles = [f for f in os.listdir(videopath) if os.path.isfile(os.path.join(videopath, f))]

    for files in onlyfiles:
        video_to_frames(video_path= (videopath + files), frames_dir=destination, overwrite=False)