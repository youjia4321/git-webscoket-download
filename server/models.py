from django.db import models

# Create your models here.


class DocumentDownload(models.Model):
    filename = models.CharField(max_length=100, verbose_name='文件名称')
    document = models.FileField(upload_to='documents', default='', verbose_name='文件')
    version = models.CharField(max_length=50, default='1.0.0', verbose_name='版本号')

    class Meta:
        db_table = 'document_download'
        verbose_name = '文件管理下载'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.document)
