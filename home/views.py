import os
from django.shortcuts import render
from .forms import FileUploadForm
from .models import UploadedFile
from django.http import HttpResponse, Http404
from django.conf import settings


def handle_uploaded_file(f):
    file_path = f'uploads/{f.name}'
    with open(file_path, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    return file_path


def upload_page(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            # ذخیره فایل
            # saved_file_path = handle_uploaded_file(request.FILES['file'])
            UploadedFile.objects.create(file=request.FILES['file'])

            print("hello")
    else:
        form = FileUploadForm()

    return render(request, 'upload.html', {'form': form})


def download_page(request):
    files_dir = os.path.join(settings.MEDIA_ROOT, 'uploaded')
    try:
        files = os.listdir(files_dir)
    except FileNotFoundError:
        files = []

    return render(request, 'download.html', {'files': files})


def download_file(request, file_name):
    file_path = os.path.join(settings.MEDIA_ROOT, 'uploaded', file_name)

    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/octet-stream")
            response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(file_path)
            return response

    raise Http404
