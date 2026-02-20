import numpy as np
import matplotlib.pyplot as plt
import imageio.v2 as imageio

img = imageio.imread('imageio:chelsea.png')

print("========== IMAGE INFO ==========")
print("Data type:", img.dtype)
print("Shape:", img.shape)
print("Number of dimensions:", img.ndim)

height, width, channels = img.shape
print("Resolution:", width, "x", height)
print("Channels:", channels)

plt.figure()
plt.imshow(img)
plt.title("Original Image")
plt.axis('off')
plt.show()

sRGB_array = img / 255
grey_vals = np.array([0.2126, 0.7152, 0.0722])
img_gray = sRGB_array @ grey_vals
plt.figure()
plt.imshow(img_gray, cmap='gray')
plt.title("Grayscale Image")
plt.axis('off')
plt.show()

# Flip Grayscale Image
img_flipped = np.flip(img_gray)
plt.figure()
plt.imshow(img_flipped, cmap='gray')
plt.title("Flipped Grayscale Image")
plt.axis('off')
plt.show()


# Rotate Colour Image
img_rotated = np.rot90(img)
plt.figure()
plt.imshow(img_rotated)
plt.title("Rotated Colour Image")
plt.axis('off')
plt.show()

# Invert (Solarize) Colour Image

solar_img = 255 - img
plt.figure()
plt.imshow(solar_img)
plt.title("Solarized Image")
plt.axis('off')
plt.show()