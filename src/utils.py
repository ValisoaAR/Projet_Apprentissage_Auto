# Import libraries
from clustimage import Clustimage
import matplotlib.pyplot as plt
import os
import glob

# Initialize
cl = Clustimage()

def load_snack_images():
    # Load all images from data/test directory
    test_dir = "data/test"

    # Get all image files from subdirectories
    image_extensions = ['*.jpg']
    pathnames = []

    for ext in image_extensions:
        pathnames.extend(glob.glob(os.path.join(test_dir, '**', ext), recursive=True))

    print(f"Nombre d'images trouvées: {len(pathnames)}")

    # Load all images
    images = []
    labels = []

    for img_path in pathnames:
        # Preprocessing: resize to 128x128, color image (RGB)
        # 0: cv2.IMREAD_GRAYSCALE
        # 1: cv2.IMREAD_COLOR
        img = cl.imread(img_path, dim=(128,128), colorscale=1, flatten=True)
        images.append(img)
        
        # Extract label from folder name
        label = os.path.basename(os.path.dirname(img_path))
        labels.append(label)

    print(f"Images chargées: {len(images)}")

    return images, labels