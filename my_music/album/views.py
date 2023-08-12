from django.shortcuts import render, redirect
from .models import Album
from .forms import CreateAlbumForm, EditAlbumForm, DeleteAlbumForm
# Create your views here.

def add_album(request):
    form = CreateAlbumForm()

    if request.method == 'POST':
        form = CreateAlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home-page')

    context = {
        'form': form
    }

    return  render(request, 'album/add-album.html', context=context)

def album_details(request, album_id):
    album = Album.objects.filter(id=album_id).get()

    context = {
        'album': album
    }

    return render(request, 'album/album-details.html', context=context)

def album_edit(request, album_id):
    album = Album.objects.filter(id=album_id).get()
    form = EditAlbumForm(instance=album)

    if request.method == 'POST':
        form = EditAlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('home-page')

    context = {
        'form': form,
        'album': album
    }

    return render(request, 'album/edit-album.html', context=context)

def album_delete(request, album_id):
    album = Album.objects.filter(id=album_id).get()
    form = DeleteAlbumForm(instance=album)

    if request.method == 'POST':
        album.delete()
        return redirect('home-page')

    context = {
        'album': album,
        'form': form
    }

    return render(request, 'album/delete-album.html', context=context)
