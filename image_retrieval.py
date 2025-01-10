import cv2
import os

def retrieve_and_save_sub_objects(image, sub_object_detections, output_dir='sub_objects/'):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    for sub_obj in sub_object_detections:
        x1, y1, x2, y2 = sub_obj['bbox']
        cropped_image = image[y1:y2, x1:x2]
        filename = f"{output_dir}{sub_obj['object']}_{sub_obj['id']}.jpg"
        cv2.imwrite(filename, cropped_image)
        print(f"Saved: {filename}")

image_path = 'pic2.jpg'
image = cv2.imread(image_path)

sub_object_detections = [
    {"object": "Helmet", "id": 1, "bbox": [150, 80, 250, 180]},
    {"object": "Tire", "id": 2, "bbox": [270, 550, 570, 750]}
]

retrieve_and_save_sub_objects(image, sub_object_detections)
