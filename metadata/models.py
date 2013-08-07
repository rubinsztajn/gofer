from django.db import models
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill, Adjust


class Name(models.Model):
    TYPES = (
        ('p', 'Personal'),
        ('c', 'Corporate'),
    )

    first_name = models.CharField(max_length=200, blank=True)
    last_name = models.CharField(max_length=200)
    dates = models.CharField(max_length=20, blank=True)
    type = models.CharField(max_length=3, choices=TYPES, blank=True)


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
        ('fld', 'Folder'),
    )

    title = models.CharField(max_length=200, blank=True)
    identifier = models.CharField(max_length=100)
    type = models.CharField(max_length=4, choices=TYPES)

    @staticmethod 
    def autocomplete_search_fields():
        return ('title__icontains', 'identifier__icontains')

    def __unicode__(self):
        return "%s (%s)" % (self.title, self.identifier)
        
class Tags(models.Model):
    name = models.CharField(max_length=100)
    
    @staticmethod
    def autocomplete_search_fields():
        return ('name__icontains',)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = "tag"

class Record(models.Model):
    STATUS = (
        ('d', 'Draft'),
        ('r', 'Ready for export'),
        ('e', 'Exported'),
    )

    FORMATS = (
        ('i', 'Image'),
        ('v', 'Video'),
        ('a', 'Audio'),
    )

    title = models.TextField()
    abstract = models.TextField(blank=True)
    names = models.ManyToManyField(Name, through="Role", blank=True)
    date_created = models.CharField(max_length=100, blank=True)
    date_issued = models.CharField(max_length=100, blank=True)
    pages = models.CharField(max_length=10, blank=True)
    size = models.CharField(max_length=100, blank=True)
    place = models.CharField(max_length=100, blank=True)
    tags = models.ManyToManyField(Tags, blank=True)
    relatives = models.ManyToManyField(Related, blank=True)
    notes = models.TextField(blank=True)
    record_status = models.CharField(max_length=1, choices=STATUS, default=STATUS[0])
    format = models.CharField(max_length=1, choices=FORMATS, blank=True)
    rights = models.BooleanField()
    folder1 = models.CharField(max_length=100, blank=True)
    folder2 = models.TextField(blank=True)
    orig_path = models.CharField("Original path", max_length=100, blank=True)
    item_id = models.CharField(max_length=100, blank=True)
    
    def __unicode__(self):
        return self.title

    def get_thumb(self):
        if self.image_set.all():
            # display the first image in the set if multiple
            return self.image_set.all()[0].thumbnail.url
        else:
            return None
    
    def get_image(self):
        if self.image_set.all():
            return self.image_set.all()[0].image.url
        else:
            return None
    
class Role(models.Model):
    ROLES = (
        ('cre', 'Creator'),
        ('pht', 'Photographer'),
    )

    name = models.ForeignKey(Name)
    record = models.ForeignKey(Record)
    role = models.CharField(max_length=3, choices=ROLES, blank=True)

class Image(models.Model):
    image = ProcessedImageField(upload_to='media', format='JPEG', options={'quality':90})
    thumbnail = ImageSpecField([Adjust(contrast=1.2, sharpness=1.1), 
                                ResizeToFill(50,50)], image_field='image',
                                format='JPEG', options={'quality':90})
    original_path = models.CharField(max_length=100, blank=True)
    title = models.CharField(max_length=200)
    record = models.ForeignKey(Record, blank=True)

    
