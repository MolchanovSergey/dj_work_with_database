import csv
from django.template.defaultfilters import slugify
from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = csv.reader(file, delimiter=';')
            # пропускаем заголовок
            next(phones)
            for line in phones:
                new_phone = Phone.objects.create(
                    id=int(line[0]),
                    name=line[1],
                    image=line[2],
                    price=int(line[3]),
                    release_date=line[4],
                    lte_exists=line[5],
                    slug=slugify(line[1]),
                )

            # TODO: Добавьте сохранение модели
        pass
