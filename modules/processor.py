#(OpenCV - Göz) Bu kod, videoyu kare kare böler.
import cv2
import os

class VideoProcessor:
    def __init__(self, save_dir="temp_frames"):
        self.save_dir = save_dir
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)

    def process_video(self, video_path, interval=2):
        """
        Videoyu 'interval' saniyede bir kare olacak şekilde böler.
        """
        cap = cv2.VideoCapture(video_path)
        fps = int(cap.get(cv2.CAP_PROP_FPS))
        frame_interval = fps * interval 
        
        frames_data = []
        count = 0
        
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            
            if count % frame_interval == 0:
                timestamp = count / fps
                frame_filename = f"frame_{int(timestamp)}.jpg"
                frame_path = os.path.join(self.save_dir, frame_filename)
                
                # Kareyi kaydet
                cv2.imwrite(frame_path, frame)
                
                frames_data.append({
                    "path": frame_path,
                    "timestamp": timestamp,
                    "id": frame_filename
                })
            count += 1
            
        cap.release()
        return frames_data