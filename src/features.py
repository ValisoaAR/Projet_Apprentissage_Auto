# Import libraries
import matplotlib.pyplot as plt
from clustimage import Clustimage
from utils import load_snack_images

# Initialize
cl = Clustimage(method='pca', grayscale=False)

# Load data
data = load_snack_images()
img, labels = data

# Extract PCA features
img_pca = cl.extract_pca(img, pixels_per_cell=(8,8), orientations=8, flatten=False)

plt.figure()
fig,axs=plt.subplots(1,2, figsize=(15,10))
axs[0].imshow(img.reshape(128,128,3))
axs[0].axis('off')
axs[0].set_title('Preprocessed image', fontsize=12)
axs[1].imshow(img_pca, cmap='gray')
axs[1].axis('off')
axs[1].set_title('PCA', fontsize=12)