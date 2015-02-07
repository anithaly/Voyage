from django.shortcuts import render
from .models import Place

# Create your views here.
def voyage_list(request):
    places = Place.objects.filter(published_date__isnull=False).order_by('published_date')
    return render(request, 'voyage/voyage_list.html', {'places': places})