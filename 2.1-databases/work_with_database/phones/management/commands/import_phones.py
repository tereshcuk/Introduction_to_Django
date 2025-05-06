import csv

from django.core.management.base import BaseCommand
from phones.models import Phone
from django.template.defaultfilters import slugify


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone in phones:
            # TODO: Добавьте сохранение модели
            new_phone = Phone()
            new_phone.id = int(phone['id'])
            new_phone.name = phone['name']
            new_phone.price = float(phone['price'])
            new_phone.image = phone['image']
            new_phone.release_date = phone['release_date']
            new_phone.lte_exists = phone['lte_exists']
            new_phone.slug = slugify(phone['name'])
            new_phone.save()
             
