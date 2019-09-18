from django.shortcuts import render
from interface.models import DocumentDownload
from django.http import StreamingHttpResponse, HttpResponse
import os
from django.utils.encoding import escape_uri_path
# Create your views here.


def download_show_file(request):
    files = DocumentDownload.objects.all()
    return render(request, 'index.html', {'files': files})


def file_iterator(filename, chunk_size=512):
    with open(filename, 'rb') as f:
        while True:
            c = f.read(chunk_size)
            if c:
                yield c
            else:
                break


def download_file_text(request, file_name):
    name = file_name.split('/')[-1]  # 显示在弹出对话框中的默认的下载文件名
    file_local = 'media/'+file_name  # 要下载的文件路径

    if not os.path.exists(file_local):
        return HttpResponse('File not found, 404')

    response = StreamingHttpResponse(file_iterator(file_local))
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{}"'.format(escape_uri_path(name))
    return response
