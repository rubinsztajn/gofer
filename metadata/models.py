from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill, Adjust

class Name(models.Model):
    TYPES = (
        ('p', 'Personal'),
        ('c', 'Corporate'),
    )
    ROLES = (
        ('cre', 'Creator'),
        ('pht', 'Photographer'),
    )

    first_name = models.CharField(max_length=200, blank=True)
    last_name = models.CharField(max_length=200)
    dates = models.CharField(max_length=20, blank=True)
    type = models.CharField(max_length=3, choices=TYPES)
    role = models.CharField(max_length=3, choices=ROLES, blank=True)

    @staticmethod
    def autocomplete_search_fields():
        return ('first_name__icontains', 'last_name__icontains',)

    def __unicode__(self):

        if self.type == 'p':
            name = self.last_name
            if self.first_name:
                name += ", " + self.first_name
            if self.dates:
                name += ", " + self.dates
            return name
        else:
            return self.last_name

class Related(models.Model):
    TYPES = (
        ('c', 'Collection'),
        ('s', 'Series'),
        ('enc', 'Enclosure'),
        ('encd', 'Enclosed in'),
    )

    title = models.CharField(max_length=200, blank=True)
    identifier = models.CharField(max_length=100)
    type = models.CharField(max_length=4, choices=TYPES)

    @staticmethod 
    def autocomplete_search_fields():
        return ('title__icontains', 'identifier__icontains')

    def __unicode__(self):
        return "%s (%s)" % (self.title, self.identifier)
        

class Record(models.Model):
    title = models.TextField()
    abstract = models.TextField(blank=True)
    names = models.ManyToManyField(Name, blank=True)
    date_created = models.CharField(max_length=100, blank=True)
    date_issued = models.CharField(max_length=100, blank=True)
    pages = models.CharField(max_length=10, blank=True)
    size = models.CharField(max_length=100, blank=True)
    relatives = models.ManyToManyField(Related, blank=True)
    
    def __unicode__(self):
        return self.title

    def get_thumb(self):
        if self.image_set.all():
            return self.image_set.all()[0].thumbnail.url
        else:
            return None
    
class Image(models.Model):
    image = models.ImageField(upload_to='media')
    thumbnail = ImageSpecField([Adjust(contrast=1.2, sharpness=1.1), 
                                ResizeToFill(50,50)], image_field='image',
                                format='JPEG', options={'quality':90})
    filename = models.CharField(max_length=100)
    title = models.CharField(max_length=200, blank=True)
    record = models.ForeignKey(Record, blank=True)

