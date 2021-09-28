from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


class Tag(models.Model):
    label = models.CharField(max_length=255)
    attached_file = models.FileField(upload_to='tags')

    def __str__(self):
        return self.label


class TaggedItem(models.Model):
    label = models.CharField(max_length=255, null=True)
    attached_file = models.FileField(upload_to='tags', null=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.PROTECT)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()
