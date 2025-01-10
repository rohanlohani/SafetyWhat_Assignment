import json

def format_detections_to_json(detections, sub_detections):
    json_output = []
    object_id = 1
    sub_object_id = 1
    
    for det in detections:
        obj_dict = {
            "object": det['label'],
            "id": object_id,
            "bbox": det['bbox'],
            "subobject": []
        }

        for sub_det in sub_detections:
            if sub_det['parent_id'] == object_id:
                sub_obj_dict = {
                    "object": sub_det['label'],
                    "id": sub_object_id,
                    "bbox": sub_det['bbox']
                }
                obj_dict["subobject"].append(sub_obj_dict)
                sub_object_id += 1
        
        json_output.append(obj_dict)
        object_id += 1
    
    return json.dumps(json_output, indent=4)

object_detections = [
    {"label": "Person", "bbox": [50, 100, 200, 400]},
    {"label": "Car", "bbox": [300, 400, 600, 800]}
]

sub_object_detections = [
    {"label": "Helmet", "bbox": [70, 150, 150, 250], "parent_id": 1},
    {"label": "Tire", "bbox": [320, 450, 500, 600], "parent_id": 2}
]

json_output = format_detections_to_json(object_detections, sub_object_detections)
print(json_output)
