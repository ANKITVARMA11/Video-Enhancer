import preprocess
import denoise
import os
import cv2
import imageio


input_path = str(input("Path of the input video:")) #Giving the input video's path
output_path = str(input("Path of the output video:")) #The resultant video's desired path
output_video = str(input("Name of the output video:"))

fps = preprocess.fps(input_path)

if preprocess.resolution(input_path) != (640,480): # If incase the resolution of input data is not 640x480 we will convert it to SD first.
    preprocess.frame_extractor(input_path,frame_folder='media/temp')
    preprocess.frame_resizer(640,480,path='media/temp',resized_path='media/resized_temp')
else:
    preprocess.frame_extractor(input_path,frame_folder="media/resized_temp")


preprocess.frame_resizer(1280,720,path="media/resized_temp",resized_path='media/target_output_temp')
for img in os.listdir("media/resized_temp"):
    deletable_frame = os.path.join("media/resized_temp", img)
    os.remove(deletable_frame)


# denoise loop
for path in range(preprocess.frame_count('media/target_output_temp')):
    denoised_frame = denoise.denoise(os.path.join('media/target_output_temp', "frame%d.jpg" % path))
    image = cv2.cvtColor(denoised_frame, cv2.COLOR_RGB2BGR)
    cv2.imwrite(os.path.join("media/denoised_frames_temp","frame%d.jpg" % path),image)

# folder = os.listdir('media/target_output_temp')
# counter = 0
# for item in folder:
#     striii = os.path.join('media/target_output_temp', item)
#     denoised_frame = denoise.denoise(striii)
#     image = cv2.cvtColor(denoised_frame, cv2.COLOR_RGB2BGR)
#     cv2.imwrite(os.path.join("media/denoised_frames_temp","frame%d.jpg" % counter),image)
#     counter += 1


for img in os.listdir('media/target_output_temp'):
    deletable_frame = os.path.join('media/target_output_temp',img)
    os.remove(deletable_frame)



image_folder = 'media/denoised_frames_temp'
video_name = output_video+".mp4"

images = []
# img for img in os.listdir(image_folder) if img.endswith(".jpg")
for img in os.listdir(image_folder):
    images.append(img)

frame = cv2.imread(os.path.join(image_folder, images[0]))
height, width, layers = frame.shape
print("Generating your video!!")

video_path = os.path.join(output_path, video_name) 
video = cv2.VideoWriter(video_path, 0, fps, (width,height))

# for image in images:
#     video.write(cv2.imread(os.path.join(image_folder, image)))
    # cv2.imwrite(os.path.join("media/denoised_frames_temp","frame%d.jpg" % path),image)
for image in range(preprocess.frame_count(image_folder)):
    video.write(cv2.imread(os.path.join("media/denoised_frames_temp","frame%d.jpg" % image)))


print("Video generated and upscaled to 1280x720 and saved in {}".format(output_path))

cv2.destroyAllWindows()
# video.release()

for img in os.listdir('media/denoised_frames_temp'):
    deletable_frame = os.path.join('media/denoised_frames_temp',img)
    os.remove(deletable_frame)