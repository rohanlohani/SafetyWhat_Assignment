# Object Detection and Sub-object Cropping System

This system uses the YOLOv5 model to detect objects in an image, crop specific sub-objects (e.g., helmet and tire), and save them as separate images.

## Requirements

- Python 3.6 or higher
- pip (Python package installer)
- OpenCV
- PyTorch
- Ultralytics YOLOv5

## Installation

1. **Clone the YOLOv5 repository**:
    ```bash
    git clone https://github.com/ultralytics/yolov5.git
    cd yolov5
    ```

2. **Install the required Python packages**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Install OpenCV**:
    ```bash
    pip install opencv-python-headless
    ```

## Running the System

1. **Place the input image**:
    - Ensure your input image is named `pic2.jpg` and placed in the project directory.

2. **Run the Python script**:
    ```bash
    python script.py
    ```

    The script performs the following:
    - Loads the YOLOv5 model.
    - Detects objects and sub-objects in the image.
    - Crops the sub-objects (helmet and tire).
    - Saves the cropped images in the `sub_objects/` directory.

3. **Check the output**:
    - The cropped images of the detected sub-objects will be saved as `Helmet_1.jpg` and `Tire_2.jpg` in the `sub_objects/` directory.

## Example Usage

After running the script, the following output files should be generated:
- `sub_objects/Helmet_1.jpg`
- `sub_objects/Tire_2.jpg`

These files contain the cropped images of the helmet and tire detected in the input image.

## Troubleshooting

- **Error opening video file**: Ensure the input image `pic2.jpg` exists in the correct directory.
- **Incorrect bounding boxes**: You may need to adjust the bounding box coordinates in the `sub_object_detections` list in `script.py`.

