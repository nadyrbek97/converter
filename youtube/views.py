from django.shortcuts import render, redirect
from .forms import YoutubeFileForm
from .forms import YoutubeFile
from .services import download


def home_view(request):

    if request.method == "POST":
        form = YoutubeFileForm(request.POST)

        if form.is_valid():
            # get link from cleaned data
            link = form.cleaned_data.get('link')
            # save object for getting it in admin panel
            YoutubeFile.objects.create(link=link)
            # passing our link to download function from services.py
            video_link = download(link)

            return redirect(video_link)

        return render(request, 'youtube/home.html', {'form': form})
    else:

        form = YoutubeFileForm()

        return render(request, 'youtube/home.html', {'form': form})
