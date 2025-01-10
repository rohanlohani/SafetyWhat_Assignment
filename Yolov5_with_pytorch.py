import torch
import cv2
import numpy as np

model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

def detect_objects(image, model, conf_threshold=0.5):
    results = model(image)
    results = results.pandas().xyxy[0]
    detections = []
    for _, row in results.iterrows():
        if row['confidence'] > conf_threshold:
            detections.append({
                'label': row['name'],
                'confidence': row['confidence'],
                'bbox': [int(row['xmin']), int(row['ymin']), int(row['xmax']), int(row['ymax'])]
            })
    return detections

def detect_sub_objects(image, detections, model, conf_threshold=0.5):
    sub_object_detections = []
    for i, det in enumerate(detections):
        x1, y1, x2, y2 = det['bbox']
        roi = image[y1:y2, x1:x2]
        sub_objects = detect_objects(roi, model, conf_threshold)
        for sub_obj in sub_objects:
            sub_obj['bbox'] = [sub_obj['bbox'][0] + x1, sub_obj['bbox'][1] + y1,
                               sub_obj['bbox'][2] + x1, sub_obj['bbox'][3] + y1]
            sub_obj['parent_id'] = i + 1
            sub_object_detections.append(sub_obj)
    return sub_object_detections

def draw_detections(image, detections):
    for det in detections:
        x1, y1, x2, y2 = det['bbox']
        label = f"{det['label']} ({det['confidence']:.2f})"
        cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(image, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

image_path = 'pic2.jpg'
image = cv2.imread(image_path)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

object_detections = detect_objects(image_rgb, model)
sub_object_detections = detect_sub_objects(image_rgb, object_detections, model)

draw_detections(image, object_detections)
draw_detections(image, sub_object_detections)

cv2.imshow('Detections', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
