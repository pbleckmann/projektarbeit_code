from PIL import Image, ImageStat
import os
import matplotlib.pyplot as plt
import matplotlib.image as im
import numpy as np
import statistics

videopath = "D:/Uni/Semester 5/Cultural Analytics/Videos/"
image_folders_path = "D:/Uni/Semester 5/Cultural Analytics/Daten/frames/"
folders = [f.split(".")[0]+"/" for f in os.listdir(videopath) if os.path.isfile(os.path.join(videopath, f))]

# calculate the brightness
def calculate_brightness(im):
    i1 = im.convert("L") # convert image to greyscale
    if np.max(i1) == np.min(i1): #if max and min value is the same (either 0 or 255)
        val = ImageStat.Stat(i1).mean[0]/255 # 0 stays 0, 255 is normed to 1
        return val
    else:
        brightval = ImageStat.Stat(i1).mean[0] # get mean brightess of the pixel values
        brightval = (brightval-np.min(i1))/(np.max(i1)-np.min(i1)) # min max normalization
        return brightval
    
# calculate the saturation
def calculate_saturation(im):
    i1 = im.convert("HSV") # convert image to hsv
    l = list(i1.getdata(1)) # get saturation value from hsv color tuple
    if np.max(l) == np.min(l): # if max and min value is the same (either greyscale or full saturation)
        saturation_value = statistics.mean(l)/255 # 0 stays 0, 255 is normed to 1
        return saturation_value
    else:
        saturation_value = statistics.mean(l) # get mean saturation of all pixel values
        saturation_value = (saturation_value - np.min(l))/(np.max(l)-np.min(l)) # min max normalization
        return saturation_value



if __name__ == '__main__':
    j = 0
    x = ["Mean Brightness", "Mean Saturation"]
    data = []
    for folder in folders:
        images = [f for f in os.listdir(image_folders_path + folder) if os.path.isfile(os.path.join(image_folders_path + folder, f))]
        brightness_values = []
        saturation_values = []

        # calculate brightness and saturation values for every frame of a video
        for image in images:
            img = Image.open(image_folders_path+folder+image)
            brightness_values.append(calculate_brightness(img))
            saturation_values.append(calculate_saturation(img))
            img.close()
        
        # calculate mean brightness and saturation for every video
        bright = statistics.mean(brightness_values)
        sat = statistics.mean(saturation_values)
        data.append([bright,sat])

        # make a bar chart for every video, all videos of a genre are appended to a single figure
        if( j > 0 and j%5 == 4):
            fig, axs = plt.subplots(1,5)
            axs[0].bar(x, data[0])
            axs[0].set_ylim([0,1])
            axs[1].bar(x, data[1])
            axs[1].set_ylim([0,1])
            axs[2].bar(x, data[2])
            axs[2].set_ylim([0,1])
            axs[3].bar(x, data[3])
            axs[3].set_ylim([0,1])
            axs[4].bar(x, data[4])
            axs[4].set_ylim([0,1])

            plt.show()
            data = []
        
        j += 1
        


