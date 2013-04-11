from django.contrib import admin
from django.http import HttpResponseRedirect
from django.core import serializers
from import_export.admin import ImportExportMixin
from imagekit.admin import AdminThumbnail
from metadata.models import Record, Name, Image, Related

def export_selected_objects(modeladmin, request, queryset):
    selected = request.POST.getlist(admin.ACTION_CHECKBOX_NAME)
    return HttpResponseRedirect("/export/?ids=%s" % (','.join(selected)))

class ImageInline(admin.TabularInline):
    model = Image
    extra = 1

class RecordAdmin(ImportExportMixin, admin.ModelAdmin):
    actions = [export_selected_objects]
    fields = ('title', 'abstract', ('date_created', 'date_issued'), 'names', 'pages', 'size', 'relatives')
    raw_id_fields = ('names','relatives',)
    autocomplete_lookup_fields = {'m2m':['names', 'relatives'],}
    list_display = ('title', 'date_created')
    search_fields = ('title', 'abstract')
    inlines = [ImageInline,]

class ImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'thumbnail_admin')
    thumbnail_admin = AdminThumbnail(image_field='thumbnail')

admin.site.register(Name)
admin.site.register(Related)
admin.site.register(Image, ImageAdmin)
admin.site.register(Record, RecordAdmin)
