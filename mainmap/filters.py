import django_filters
from functools import reduce
from operator import or_
from django.db.models import Q

def Filter_photo(photos,params):
    if any(x for x in params.values()):
        if params.get('date_before'):
            photos = photos.filter(year__lte=params.get('date_before'))
        if params.get('date_after'):
            photos = photos.filter(year__gte=params.get('date_after'))
        if params.get('description'):
            keywords = params.get('description').split()
            photos = photos.filter(reduce(or_, [Q(description__icontains=keyword) for keyword in keywords]))
        if params.get('source'):
            photos = photos.filter(source__iexact=params.get('source'))
    return photos
