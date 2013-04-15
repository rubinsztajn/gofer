import csv
from django.core.management.base import BaseCommand, CommandError
from django.core.files import File
from metadata.models import Image, Record

class Command(BaseCommand):
    args = '<csv_filename>'
    help = 'All images in the CSV are imported into Gofer'

    def handle(self, args, **options):
        csv_file = open(args, 'rt')
        reader = csv.DictReader(csv_file)
        for row in reader:
            r = Record.objects.get(pk=row['id'])

            path = '/Users/arubinst/y/scans/TAR/Photos/' + row['abstract']
            f = File(open(path, 'r'))
            i = Image(title=row['title'], image=f, record=r)
            i.image.save(row['title'], f)
            i.save()
    
