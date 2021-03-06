from django.shortcuts import render, get_object_or_404, render_to_response, redirect
from django.contrib import auth
from metadata.models import Record, Related

def home(request):
    if request.user.is_authenticated():
        parents = Related.objects.filter(type='fld')
        ready_for_export = Record.objects.filter(record_status='r')
        return render_to_response('gofer/home.html', {'user': request.user, 'ready_for_export': ready_for_export, 'parents': parents})
    else:
        return redirect('/login')

def logout(request):
    auth.logout(request)
    return redirect('/')
    
def record(request, record_id):
    record = get_object_or_404(Record, pk=record_id)
    return render(request, 'metadata/record.html', {'record': record, 'user': request.user})
    
def export(request):
    pks = request.GET.get('ids').split(',')
    records = Record.objects.filter(pk__in=pks)
    return render(request, 'metadata/export.xml', {'records': records}, content_type="text/xml")




    
