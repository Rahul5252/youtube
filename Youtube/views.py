# importing all the required modules
from django.shortcuts import render, redirect
from pytube import *
import os

# defining function
def youtube(request):
    if os.name == "nt":
        DOWNLOAD_FOLDER = f"{os.getenv('USERPROFILE')}\\Downloads"
        
    
	# checking whether request.method is post or not
        if request.method == 'POST':
            
            # getting link from frontend
            link = request.POST['link']
            video = YouTube(link)
        
            # setting video resolution
            stream = video.streams.filter(progressive=True)
            stream1 = video.streams.get_highest_resolution()
            filesize = video.streams.get_highest_resolution().filesize
            #stream.get_by_itag(139).download()
            # downloads video
            stream1.download(DOWNLOAD_FOLDER)
            data = {
                'streams' : stream,
                'title' : video.title,
                'thumbnail' : video.thumbnail_url,
                'you' : filesize
            }
            
            # returning HTML page
            return render(request, 'index.html', data)
        return render(request, 'index.html')
