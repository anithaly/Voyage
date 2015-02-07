from django.shortcuts import render
from .models import Place

from django.shortcuts import render, get_object_or_404

def voyage_list(request):
    places = Place.objects.filter(published_date__isnull=False).order_by('published_date')
    return render(request, 'voyage/voyage_list.html', {'places': places})

def voyage_detail(request, pk):
    # place = get_object_or_404(Place, pk=pk)
    place = Place.objects.get(pk=pk)
    return render(request, 'voyage/voyage_detail.html', {'place': place})
