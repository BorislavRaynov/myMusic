from django.shortcuts import render, redirect
from .models import User
from .forms import CreateProfileForm
from ..album.models import Album

# Create your views here.

def profile_details(request):
    profile = User.objects.first()
    albums = Album.objects.all()
    context = {
        'profile': profile,
        'albums': albums
    }

    return render(request, 'user/profile-details.html', context=context)


def profile_delete(request):
    profile = User.objects.first()
    albums = Album.objects.all()

    if request.method == 'POST':
        profile.delete()
        albums.delete()

        return redirect('home-page')

    return render(request, 'user/profile-delete.html')
