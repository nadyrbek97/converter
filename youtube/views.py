from django.shortcuts import render
from .forms import YoutubeFileForm
from .forms import YoutubeFile


def home_view(request):

    if request.method == "POST":
        form = YoutubeFileForm(request.POST)

        if form.is_valid():

            link = form.cleaned_data.get('link')
            email = form.cleaned_data.get('email')

            YoutubeFile.objects.create(link=link, email=email)

            return render(request, 'youtube/home.html', {'form': form})
    else:

        form = YoutubeFileForm()

        return render(request, 'youtube/home.html', {'form': form})
