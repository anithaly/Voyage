from django.shortcuts import render
from django.shortcuts import redirect
from .models import Place
from .forms import PlaceForm

from django.shortcuts import render, get_object_or_404

def voyage_list(request):
    places = Place.objects.filter(published_date__isnull=False).order_by('published_date')
    return render(request, 'voyage/voyage_list.html', {'places': places})

def voyage_detail(request, pk):
    place = get_object_or_404(Place, pk=pk)
    # place = Place.objects.get(pk=pk)
    return render(request, 'voyage/voyage_detail.html', {'place': place})

def voyage_new(request):
    if request.method == "POST":
        form = PlaceForm(request.POST)
        if form.is_valid():
            place = form.save(commit=False)
            place.author = request.user
            place.save()
            return redirect('voyage.views.voyage_detail', pk=place.pk)
    else:
        form = PlaceForm()
    return render(request, 'voyage/voyage_form.html', {'form': form})

def voyage_edit(request, pk):
    place = get_object_or_404(Place, pk=pk)
    if request.method == "POST":
        form = PlaceForm(request.POST, instance=place)
        if form.is_valid():
            place = form.save(commit=False)
            place.author = request.user
            place.save()
            return redirect('voyage.views.voyage_detail', pk=place.pk)
    else:
        form = PlaceForm(instance=place)
    return render(request, 'voyage/voyage_form.html', {'form': form, 'place': place})

def voyage_publish(request, pk):
    place = get_object_or_404(Place, pk=pk)
    place.publish()
    return redirect('voyage.views.voyage_detail', pk=pk)

def voyage_draft_list(request):
    place = Place.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'voyage/voyage_draft_list.html', {'places': places})