import numpy as np
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from tensorflow.keras.utils import img_to_array
from imutils import paths
import random
import numpy as np
import cv2
import os

# Load your image dataset and labels as you did before
dataset = 'E:/Hobby_Projects/MLOM/MobilenetV2/datasetlatest'  # Change this to your dataset path
# ... Load and preprocess your image data and labels ...
print("[INFO] loading images...")
data = []
labels = []
imagePaths = sorted(list(paths.list_images(dataset)))
random.seed(42)
random.shuffle(imagePaths)
# loop over the input images
for imagePath in imagePaths:
    # load the image, pre-process it, and store it in the data list
    image = cv2.imread(imagePath)
    image = cv2.resize(image,(32,24))
    cv2.imshow('resize', image)
    image = img_to_array(image)
    
    data.append(image)
    # extract the class label from the image path and update the labels list
    label = imagePath.split(os.path.sep)[-2]
    print(label)
    if label == 'forward/':
        label = 0
    elif label == 'right/':
        label = 1
    elif label == 'left/':
        label = 2
    elif label == 'stop/':
        label = 3
    labels.append(label)
# scale the raw pixel intensities to the range [0, 1]
data = np.array(data, dtype="float") / 255.0
labels = np.array(labels)
print(image.shape)
print(image)

# Reshape the images to feature vectors
num_samples, height, width, depth = data.shape
data_reshaped = data.reshape(num_samples, -1)

# Split the data into training, testing, and validation sets
X_train, X_temp, y_train, y_temp = train_test_split(data_reshaped, labels, test_size=0.4, random_state=42)
X_test, X_val, y_test, y_val = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42)

# Apply PCA to the training data
n_components = 100  # You can adjust this number
pca = PCA(n_components=n_components)
X_train_pca = pca.fit_transform(X_train)

# Transform the testing and validation data using the same PCA model
X_test_pca = pca.transform(X_test)
X_val_pca = pca.transform(X_val)

# Initialize a classifier (SVM in this example)
clf = SVC()

# Train the classifier on the transformed training data
clf.fit(X_train_pca, y_train)

# Make predictions on the transformed testing data
y_test_pred = clf.predict(X_test_pca)

# Calculate testing accuracy
test_accuracy = accuracy_score(y_test, y_test_pred)
print(f"Testing Accuracy: {test_accuracy}")

# Make predictions on the transformed validation data
y_val_pred = clf.predict(X_val_pca)

# Calculate validation accuracy
val_accuracy = accuracy_score(y_val, y_val_pred)
print(f"Validation Accuracy: {val_accuracy}")
