import cv2
import numpy as np
import os
import csv

DATASET_FOLDER = "dataset"
OUTPUT_CSV = "dental_features.csv"

def calculate_mandible_angle(image_path):
    img = cv2.imread(image_path)
    if img is None:
        return None

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50, 150)
    lines = cv2.HoughLines(edges, 1, np.pi / 180, 150)

    angles = []
    if lines is not None:
        for line in lines[:10]:
            rho, theta = line[0]
            angles.append(theta * 180 / np.pi)

    if len(angles) == 0:
        return None

    return round(sum(angles) / len(angles), 2)

with open(OUTPUT_CSV, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["image", "mandible_angle", "label"])

    for img_name in os.listdir(DATASET_FOLDER):
        img_path = os.path.join(DATASET_FOLDER, img_name)
        angle = calculate_mandible_angle(img_path)

        if angle is not None:
            label = img_name.split("_")[0]
            writer.writerow([img_name, angle, label])

print("Feature dataset created successfully!")
