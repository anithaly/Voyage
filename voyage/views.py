from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

from .models import Place, Comment
from .forms import PlaceForm, CommentForm

# @login_required
def place_list(request):
    places = Place.objects.filter(published_date__isnull=False).order_by('-published_date')
    return render(request, 'place/list.html', {'places': places})

def place_detail(request, pk):
    place = get_object_or_404(Place, pk=pk)
    form = CommentForm(request.POST or None)
    # place = Place.objects.get(pk=pk)
    return render(request, 'place/detail.html', {'place': place, 'form': form})

@login_required
def place_new(request):
    if request.method == "POST":
        form = PlaceForm(request.POST)
        if form.is_valid():
            place = form.save(commit=False)
            place.author = request.user
            place.save()
            return redirect('voyage.views.place_detail', pk=place.pk)
    else:
        form = PlaceForm()
    return render(request, 'place/form.html', {'form': form})

@login_required
def place_edit(request, pk):
    place = get_object_or_404(Place, pk=pk)
    if request.method == "POST":
        form = PlaceForm(request.POST, instance=place)
        if form.is_valid():
            place = form.save(commit=False)
            place.author = request.user
            place.save()
            return redirect('voyage.views.place_detail', pk=place.pk)
    else:
        form = PlaceForm(instance=place)
    return render(request, 'place/form.html', {'form': form, 'place': place})

@login_required
def place_remove(request, pk):
    place = get_object_or_404(Place, pk=pk)
    place.delete()
    return redirect('voyage.views.place_list')

@login_required
def place_publish(request, pk):
    place = get_object_or_404(Place, pk=pk)
    place.publish()
    return redirect('voyage.views.place_detail', pk=pk)

@login_required
def place_drafts_list(request):
    places = Place.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'place/drafts_list.html', {'places': places})

@login_required
def place_comment_new(request, pk):
    place = get_object_or_404(Place, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.place = place
            comment.save()
            return redirect('voyage.views.place_detail', pk=place.pk)
    else:
        form = CommentForm()
    return render(request, 'place/detail.html', {'place': place, 'form': form})