from django.shortcuts import render,redirect,HttpResponse
from .models import VideoModel

# Create your views here.
# full_path="C:\\Users\\Sooraj\\OneDrive\\Apps\\mp3_conveter\\converter\\media\\video"+name


from moviepy.editor import VideoFileClip
def index(request):
    output_audio_path = "C:\\Users\\Sooraj\\OneDrive\\Apps\\mp3_conveter\\converter\\media\\video\\"
    mp3_ready = False
    if request.method == 'POST':
        vdio = request.FILES.get('vdio')
        # vname=vdio.name
        # if vname.endswith('.mp3'):
        #     return HttpResponse(" unsupported File Type")
        vedio = VideoModel()
        
        vedio.video_name = vdio
        vedio.save()
        vedio_path = vedio.video_name.path
        
        videoclip = VideoFileClip(vedio_path)
        audio = videoclip.audio
        audio.write_audiofile(output_audio_path + 'output.mp3', codec='mp3')
        mp3_ready = True
        
    return render(request, 'index.html', {'mp3_ready': mp3_ready})

def download_mp3(request):
    file_path = "C:\\Users\\Sooraj\\OneDrive\\Apps\\mp3_conveter\\converter\\media\\video\\output.mp3"
    with open(file_path, 'rb') as f:
        response = HttpResponse(f.read(), content_type="audio/mpeg")
        response['Content-Disposition'] = 'attachment; filename=output.mp3'
        return response


