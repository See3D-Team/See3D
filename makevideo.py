import os
# import os
# import cv2

# # Path to the folder containing the videos
# folder_path = '/Users/gaohuachen/MyResources/research/see3d.github.io/static/videos/data_shu'

# # Get a list of all video files in the folder
# video_files = [f for f in os.listdir(folder_path) if f.endswith('.mp4') or f.endswith('.avi')]

# # Loop through each video file
# for video_file in video_files:
#     # Construct the full path to the video file
#     video_path = os.path.join(folder_path, video_file)

#     # Open the video file
#     cap = cv2.VideoCapture(video_path)

#     # Get the original video's width and height
#     width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
#     height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

#     # Create a VideoWriter object to save the resized video
#     output_path = os.path.join(folder_path, 'resized_' + video_file)
#     fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Change codec as needed
#     out = cv2.VideoWriter(output_path, fourcc, 30.0, (960, 720))

#     # Read and resize each frame of the video
#     while True:
#         ret, frame = cap.read()
#         if not ret:
#             break

#         # Resize the frame to 720x960 pixels
#         resized_frame = cv2.resize(frame, (960, 720))

#         # Write the resized frame to the output video file
#         out.write(resized_frame)

#     # Release the video capture and writer objects
#     cap.release()
#     out.release()

#     print(f'Resized video saved to: {output_path}')
# Path to the folder containing the videos
# folder_path = '/Users/gaohuachen/MyResources/research/see3d.github.io/static/videos/openworld'

# # Get a list of all video files in the folder
# video_files = [f for f in os.listdir(folder_path) if f.endswith('.mp4') or f.endswith('.avi')]

# # Loop through each video file
# for video_file in video_files:
#     # Construct the full path to the video file
#     video_path = os.path.join(folder_path, video_file)

#     # Construct the output path for the compressed video
#     output_path = os.path.join(folder_path, 'compressed_' + video_file)

#     # Compress the video using ffmpeg
#     os.system(f'ffmpeg -i {video_path} -c:v libx264 -crf 23 -preset medium {output_path}')

#     print(f'Compressed video saved to: {output_path}')
# folder_path = '/Users/gaohuachen/MyResources/research/see3d.github.io/static/videos/openworld'

# # Get a list of all video files in the folder
# video_files = [f for f in os.listdir(folder_path) if f.endswith('.mp4') or f.endswith('.avi')]

# # Loop through each video file
# for video_file in video_files:
#     # Construct the full path to the video file
#     video_path = os.path.join(folder_path, video_file)

#     # Construct the output path for the compressed video
#     output_path = os.path.join(folder_path, 'compressed_' + video_file)

#     # Compress the video using ffmpeg
#     os.system(f'ffmpeg -i {video_path} -c:v libx264 -crf 23 -preset medium {output_path}')

#     print(f'Compressed video saved to: {output_path}')
import os
import subprocess
from pathlib import Path

def compress_videos(input_dir, output_dir, target_ratio=0.1):
    """
    Compress all videos in the input directory to the target size ratio
    and save them to the output directory.

    Args:
        input_dir (str): Path to the input directory containing videos.
        output_dir (str): Path to the output directory for compressed videos.
        target_ratio (float): Target size ratio (e.g., 0.4 for 40%).
    """
    # Ensure output directory exists
    Path(output_dir).mkdir(parents=True, exist_ok=True)

    for root, _, files in os.walk(input_dir):
        for file in files:
            if file.endswith(('.mp4', '.avi', '.mkv', '.mov', '.flv', '.wmv')):
                input_path = os.path.join(root, file)
                output_path = os.path.join(output_dir, file)

                # Get the original file size
                original_size = os.path.getsize(input_path)
                target_size = int(original_size * target_ratio)

                # Use ffmpeg to compress the video
                command = [
                    "ffmpeg", "-i", input_path, "-vcodec", "libx264", "-crf", "23",
                    "-fs", str(target_size), "-y", output_path
                ]

                print(f"Compressing: {input_path} -> {output_path}")
                try:
                    subprocess.run(command, check=True)
                except subprocess.CalledProcessError as e:
                    print(f"Error compressing {input_path}: {e}")

if __name__ == "__main__":
    input_folder = "/Users/gaohuachen/MyResources/research/see3d.github.io/static/videos/data_shu"
    output_folder = "/Users/gaohuachen/MyResources/research/see3d.github.io/static/videos/data_shu_compressed"
    compress_videos(input_folder, output_folder)