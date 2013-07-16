import csv
from django.core.management.base import BaseCommand, CommandError
from metadata.models import  Record
"""
Import a CSV file of column headers that match database fields into Gofer.
Works pretty well except doesn't handle field specific issues like ManyToMany
lookups, and fields with multiple values.
"""

class Command(BaseCommand):
    args = '<csv_filename>'
    help = 'Import a CSV file of records into Gofer'

    def handle(self, args, **options):
        csv_file = open(args, 'Urt')
        reader = csv.DictReader(csv_file)
        count = 0
        for row in reader:
            rid = row['id']
            if rid:
                r = Record.objects.filter(id=rid)
                if not r:
                    r = Record()
                else:
                    r = r[0]
            else:
                r = Record()
            for field in row.iteritems():
                if field[0] != 'id':
                    setattr(r, field[0], field[1])
            r.save()
            count += 1
                

        print "Imported %s records" % (count)
