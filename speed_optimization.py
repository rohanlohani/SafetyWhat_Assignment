import torch
import cv2
import time

model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

def process_video(video_path, model, output_path='output.avi', display=False):
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Error opening video file")
        return

    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))
    fps = cap.get(cv2.CAP_PROP_FPS)

    out = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc(*'XVID'), fps, (frame_width, frame_height))

    frame_count = 0
    total_time = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        start_time = time.time()
        results = model(frame)
        frame_with_detections = results.render()[0]
        end_time = time.time()
        total_time += end_time - start_time

        out.write(frame_with_detections)
        frame_count += 1

        if display:
            cv2.imshow('Frame', frame_with_detections)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    cap.release()
    out.release()
    cv2.destroyAllWindows()

    avg_fps = frame_count / total_time
    print(f"Processed {frame_count} frames in {total_time:.2f} seconds.")
    print(f"Average FPS: {avg_fps:.2f}")

video_path = 'video2.mp4'
process_video(video_path, model, display=True)
