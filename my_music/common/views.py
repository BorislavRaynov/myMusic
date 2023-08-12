from django.shortcuts import render, redirect
from my_music.album.models import Album
from ..user.forms import CreateProfileForm
from ..album.forms import CreateAlbumForm

# Create your views here.

def home_page(request):
    albums = Album.objects.all()
    form = CreateProfileForm()

    if request.method == 'POST':
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()

    context = {
        'albums': albums,
        'form': form
    }

    return render(request, 'common/home-page.html', context=context)
