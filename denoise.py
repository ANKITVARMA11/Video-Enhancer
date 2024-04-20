import cv2
# Read the noisy image
def denoise(image_path):
    noisy_image = cv2.imread(image_path)
    # Apply Gaussian blur
    denoised_image = cv2.GaussianBlur(noisy_image, (5, 5), 0)  # Adjust the kernel size (e.g., (5, 5)) as needed
    return denoised_image
