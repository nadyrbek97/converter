from django.shortcuts import render
from .forms import YoutubeFileForm


def home_view(request):

    if request.method == "POST":
        form = YoutubeFileForm(request.POST)

        if form.is_valid():

            print("form working correctly")
            return render(request, 'youtube/home.html', {'form': form})
    else:

        form = YoutubeFileForm()

        return render(request, 'youtube/home.html', {'form': form})
