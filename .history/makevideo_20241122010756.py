from moviepy.editor import VideoFileClip
from moviepy.video.fx.resize import resize

def resize_videos(input_dir, output_dir, width, height):
    # Get a list of all video files in the input directory
    video_files = [f for f in os.listdir(input_dir) if f.endswith('.mp4')]

    for video_file in video_files:
        # Load the video clip
        clip = VideoFileClip(os.path.join(input_dir, video_file))

        # Check if the video needs to be resized
        if clip.size[0] > clip.size[1]:
            # Perform central cropping
            x_center = clip.size[0] / 2
            y_center = clip.size[1] / 2
            x_min = x_center - (clip.size[1] * width / height) / 2
            x_max = x_center + (clip.size[1] * width / height) / 2
            clip = clip.crop(x_min, 0, x_max, clip.size[1])

        # Resize the video to the desired dimensions
        clip = resize(clip, width=width, height=height)

        # Save the resized video to the output directory
        clip.write_videofile(os.path.join(output_dir, video_file))

# Usage example
input_dir = '/path/to/input/directory'
output_dir = '/path/to/output/directory'
width = 980
height = 720

resize_videos(input_dir, output_dir, width, height)
