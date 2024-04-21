from django.test import TestCase
import os

from moviepy.editor import VideoFileClip
from pydub import AudioSegment
# from playsound import playsound
# Create your tests here.
video_path = "C:\\Users\\Sooraj\\OneDrive\\Pictures\\Voting_Website_full_Video.mp4"
output_audio_path = "out.mp3"

# Load the video
video = VideoFileClip(video_path)

# Extract audio
audio = video.audio

# Save audio as mp3
audio.write_audiofile(output_audio_path, codec='mp3')

# Play the exported audio
# playsound(output_audio_path)