# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Photo
from .filters import Filter_photo
import json

def index(request):
	photos = Photo.objects.all()
	params = request.GET
	photos=Filter_photo(photos,params)

	feature_array =[]
	for photo in photos:
		feature ={ "type": "Feature",
			"properties": { "name": photo.name,
							"year": (photo.year).strftime('%Y-%m-%d'),
							"description": photo.description,
							"image": photo.image.url},
			"geometry": { "type": "Point", "coordinates": [ photo.coordinate_y, photo.coordinate_x ] } }
		feature_array.append(feature)

	json_v = {
		"type": "FeatureCollection",
		"crs": { "type": "name", "properties": { "name": "urn:ogc:def:crs:OGC:1.3:CRS84" } },
		"features": feature_array}

	ll = params.get('ll') or '52.59383, 34.49707'
	zoom = params.get('zoom') or 6
	return render(request,'mainmap/index.html',{"photos":json.dumps(json_v),"ll":ll,"zoom":zoom})
