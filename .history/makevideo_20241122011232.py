from PIL import Image
import os

def resize_videos(input_dir, output_dir, width, height):
    # Get a list of all video files in the input directory
    video_files = [f for f in os.listdir(input_dir) if f.endswith('.mp4')]

    for video_file in video_files:
        # Load the video frame by frame
        frames = []
        video_path = os.path.join(input_dir, video_file)
        with open(video_path, 'rb') as f:
            while True:
                frame = f.read(width * height * 3)  # Assuming RGB frames
                if not frame:
                    break
                frames.append(frame)

        # Resize each frame
        resized_frames = []
        for frame in frames:
            image = Image.frombytes('RGB', (width, height), frame)
            resized_image = image.resize((width, height))
            resized_frames.append(resized_image.tobytes())

        # Save the resized frames as a new video file
        output_path = os.path.join(output_dir, video_file)
        with open(output_path, 'wb') as f:
            for frame in resized_frames:
                f.write(frame)

# Usage example
input_dir = '/Users/gaohuachen/Desktop/seesee'
output_dir = '/Users/gaohuachen/Desktop/seesee2'
width = 980
height = 720

resize_videos(input_dir, output_dir, width, height)
