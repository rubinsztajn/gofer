import csv, os
from django.core.management.base import BaseCommand, CommandError
from django.core.files import File
from metadata.models import Image, Record

class Command(BaseCommand):
    args = '<csv_filename>'
    help = 'All images in the CSV are imported into Gofer'

    def handle(self, args, **options):
        csv_file = open(args, 'Urt')
        reader = csv.DictReader(csv_file)
        for row in reader:
            try: 
                r = Record.objects.get(pk=row['id'])
                basename = os.path.splitext(row['title'])[0]
                path = '/Users/arubinst/buffy/TAR/images_small/' + basename + '.jpg'
                f = File(open(path, 'r'))
                i = Image(title=basename, image=f, record=r)
                i.image.save(f.name, f)
                i.save()
            except IOError:
                print basename
    
