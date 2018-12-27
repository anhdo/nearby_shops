import os
import json
from django.conf import settings
from django.core.management import BaseCommand
from django.contrib.gis.geos import fromstr
from shops.models import Shop

WGS84_SRID = 4326


class Command(BaseCommand):
    def _save_obj(self, obj):
        if obj['type'] == 'node':
            name = obj['tags'].get('name', 'no-name')
            longitude = obj.get('lon', 0)
            latitude = obj.get('lat', 0)
            location = fromstr(f'POINT({longitude} {latitude})', srid=WGS84_SRID)
            Shop(name=name, location=location).save()

    def _load_from_file(self, filepath):
        with open(filepath, encoding='utf-8') as f:
            objects = json.load(f)
            for obj in objects['elements']:
                try:
                    self._save_obj(obj)
                except:
                    pass     

    def handle(self, *args, **options):
        data_dir = os.path.join(settings.BASE_DIR, 'docker', 'data')
        for filename in os.listdir(data_dir):
            if filename.endswith('.json'):
                self._load_from_file(os.path.join(data_dir, filename))
