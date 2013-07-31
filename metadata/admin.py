from django.contrib import admin
from django.http import HttpResponseRedirect
from django.core import serializers
from import_export.admin import ImportExportMixin
from imagekit.admin import AdminThumbnail
from metadata.models import Record, Name, Image, Related, Tags, Role

def export_selected_objects(modeladmin, request, queryset):
    selected = request.POST.getlist(admin.ACTION_CHECKBOX_NAME)
    queryset.update(record_status='e')
    return HttpResponseRedirect("/export/?ids=%s" % (','.join(selected)))

def make_ready_for_export(modeladmin, request, queryset):
    queryset.update(record_status='r')

def make_draft(modeadmin, request, queryset):
    queryset.update(record_status='d')

make_ready_for_export.short_description = "Mark selected records as ready to export"
make_draft.short_description = "Mark selected records as a draft"

class ImageInline(admin.TabularInline):
    model = Image
    extra = 1

class RoleInline(admin.TabularInline):
    model = Role
    extra = 1
    verbose_name = "Name"
    raw_id_fields = ('name',)
    autocomplete_lookup_fields = {'m2m':['name',],}

class RecordAdmin(ImportExportMixin, admin.ModelAdmin):
    actions = [make_draft, make_ready_for_export, export_selected_objects]
    fields = (('record_status', 'format', 'item_id'), 'rights', 'title', 'abstract', ('date_created', 'date_issued'), 'pages', 'size','relatives', 'tags', 'notes', 'folder1', 'folder2', 'orig_path')
    raw_id_fields = ('relatives','tags',)
    autocomplete_lookup_fields = {'m2m':['relatives', 'tags'],}
    list_display = ('title', 'abstract', 'date_created')
    list_filter = ('record_status',)
    search_fields = ('title', 'abstract', 'notes')
    inlines = [RoleInline, ImageInline,]

class ImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'thumbnail_admin')
    thumbnail_admin = AdminThumbnail(image_field='thumbnail')

admin.site.register(Name)
admin.site.register(Related)
admin.site.register(Tags)
admin.site.register(Image, ImageAdmin)
admin.site.register(Record, RecordAdmin)
