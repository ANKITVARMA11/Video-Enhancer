from PIL import Image
import os
import cv2

def fps(input_video):
    vid = cv2.VideoCapture(input_video)
    Fps = vid.get(cv2.CAP_PROP_FPS)
    return float(Fps)


def resolution(video_path):
    '''Results out the resolution of input video'''
    global resolution
    vid = cv2.VideoCapture(video_path)
    width = vid.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = vid.get(cv2.CAP_PROP_XI_HEIGHT)
    resolution = (width,height)
    return resolution

def frame_count(dir_path):
    '''Counts the total number of frames extracted. This will be used for further while giving range to the loop while denosing'''
    global count
    count = 0
    for path in os.listdir(dir_path):
        if os.path.isfile(os.path.join(dir_path, path)):
            count += 1
    return count

def frame_extractor(input_video,frame_folder):
    '''Extract the frames and stores them in a temp folder'''

    print("Extracting the frames from the {} and saving them to {}.....".format(input_video,frame_folder))

    input = cv2.VideoCapture(input_video)
    count = 0
    success = 1
    while success:
        success, frame = input.read()
        if success:
            temp_extracted_path = frame_folder
            cv2.imwrite(os.path.join(temp_extracted_path, "frame%d.jpg" % count), frame)
            count += 1
    print("Extraction done!!")



def frame_resizer(w,h, path, resized_path, temp = True):
    '''Resizes the images at a "path" to (wxh) and save them to "resized_path". Since the requirement from the TENSORGO is to use the SD (640X480), instead of finding the online samples, I converted my videos to the SD'''
    print("Resizing the frames at {} to {}x{} and saving it to {}".format(path,w,h,resized_path))
    size = (w,h)
    count = frame_count(path)
    for frame in range(count):
        image = Image.open(os.path.join(path, "frame%d.jpg" % frame))
        resized_image = image.resize(size)
        resized_image.save(os.path.join(resized_path, "frame%d.jpg" % frame))
    
    if temp==True:
        print("Deleting the frames from {}...".format(path))
        for img in os.listdir(path):
            deletable_frame = os.path.join(path,img)
            os.remove(deletable_frame)
        print("Deletion done!!")

