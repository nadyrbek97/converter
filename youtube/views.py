from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import YoutubeFileForm
from .forms import YoutubeFile
from .services import download
from youtube_dl.utils import DownloadError


def home_view(request):

    if request.method == "POST":
        form = YoutubeFileForm(request.POST)

        if form.is_valid():
            try:
                # get link from cleaned data
                link = form.cleaned_data.get('link')
                # save object for getting it in admin panel
                YoutubeFile.objects.create(link=link)
                # passing our link to download function from services.py
                video_link = download(link)
                return redirect(video_link)
            except DownloadError:
                messages.error(request, 'Unsupported URL, please put valid YOUTUBE url')
                return render(request, 'youtube/home.html', {'form': form})

        return render(request, 'youtube/home.html', {'form': form})
    else:

        form = YoutubeFileForm()

        return render(request, 'youtube/home.html', {'form': form})
