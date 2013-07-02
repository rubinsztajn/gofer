from haystack.indexes import *
from haystack import site
from metadata.models import Record

class RecordIndex(RealTimeSearchIndex):
    text = CharField(document=True, use_template=True)
    folder1 = CharField(model_attr='folder1', faceted=True)
    folder2 = CharField(model_attr='folder2', faceted=True)
    date_created = CharField(model_attr='date_created')

site.register(Record, RecordIndex)
