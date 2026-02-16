import os
from utils import load_snack_images
import fiftyone as fo


# launch the app to visualize the dataset
data = load_snack_images()
session = fo.launch_app(data)