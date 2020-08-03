# Helper functions
import cv2
import os
import glob # library for loading images from a directory
import matplotlib.image as mpimg
import numpy as np
import matplotlib.pyplot as plt



# This function loads in images and their labels and places them in a list
# The list contains all images and their associated labels
# For example, after data is loaded, im_list[0][:] will be the first image-label pair in the list
def load_dataset(image_dir):
    
    # Populate this empty image list
    #print("I am in the function load_dataset")
    im_list = []
    image_types = ["red", "yellow", "green"]
    
    # Iterate through each color folder
    for im_type in image_types:
        
        # Iterate through each image file in each image_type folder
        # glob reads in any image with the extension "image_dir/im_type/*"
        for file in glob.glob(os.path.join(image_dir, im_type, "*")):
            #print
            #print("I am in the loop for reading")
            # Read in the image
            im = mpimg.imread(file)
            
            # Check if the image exists/if it's been correctly read-in
            if not im is None:
                # Append the image, and it's type (red, green, yellow) to the image list
                im_list.append((im, im_type))

    return im_list

def mask_image(rgb_image, Min_H_Val, Max_H_Val, Min_S_Val, Max_S_Val, Min_V_Val, Max_V_Val):
    # Convert to HSV
    hsv = cv2.cvtColor(rgb_image, cv2.COLOR_RGB2HSV)
    
    hsv_lower = np.array([Min_H_Val, Min_S_Val, Min_V_Val]) 

    hsv_higher = np.array([Max_H_Val, Max_S_Val, Max_V_Val])
    
    ## TODO: Define the masked area and mask the image

    mask = cv2.inRange(hsv, hsv_lower, hsv_higher)
    
    masked_image = np.copy(rgb_image)

    masked_image[mask == 0] = [255]

    # Display it!
    plt.imshow(masked_image, cmap="gray")
    
def avg_brightness(hsv_image):
    # Convert image to HSV
    #hsv = cv2.cvtColor(rgb_image, cv2.COLOR_RGB2HSV)
    height, width = hsv_image.shape[:2]
    # Add up all the pixel values in the V channel
    sum_brightness = np.sum(hsv_image[:,:,2])
    #area = 32*32  # pixels
    area = height*width
    
    # find the avg
    avg = sum_brightness/area
    
    return avg

def max_brightness(rgb_image):
    # Return the image slice having the maxium avg brightness
    
    avgArray = []
    # Convert image to HSV
    hsv = cv2.cvtColor(rgb_image, cv2.COLOR_RGB2HSV)
    
    # Crop hsv image into 3 separate sub images
    top = hsv[2:11,5:25]
    
    middle = hsv[12:22,5:25]
    
    bottom = hsv[23:32,5:25]
    
    #Determine the HSV avg brightness
    
    top_avg = avg_brightness(top)
    
    #Print for double check
    print('Top part avg brightness = ' + str(top_avg))
    
    avgArray.append(top_avg)
    
    middle_avg = avg_brightness(middle)
    
    print('Middle part avg brightness = ' + str(middle_avg))
    
    avgArray.append(middle_avg)
    
    bottom_avg = avg_brightness(bottom)
    
    print('Bottom part avg brightness = ' + str(bottom_avg))
    
    avgArray.append(bottom_avg)
    
    #Find the max
    maxAvg = top_avg
    
    maxAvgIndex = 0;
    for i in range(0, len(avgArray)):
        if(avgArray[i] > maxAvg):
            maxAvg = avgArray[i]
            maxAvgIndex = i
            
    return maxAvgIndex
    
    
    
    
    




