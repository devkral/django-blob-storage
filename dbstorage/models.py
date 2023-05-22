from django.db import models
from django.utils import timezone
from django.db.models.functions import Length
from django.conf import settings


class DBFileManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().annotate(size=Length("content"))


class DBFile(models.Model):
    content = models.BinaryField(editable=False)
    name = models.CharField(max_length=255, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    accessed_on = models.DateTimeField(default=timezone.now)

    objects = DBFileManager()
    if getattr(settings, "DJANGO_DBFILE_DB", "default") != "default":
        objects = objects.db_manager(getattr(settings, "DJANGO_DBFILE_DB"))

    # size is now a virtual field

    class Meta:
        db_table = "db_file"
        verbose_name = "DB file"

    def __str__(self):
        return self.name
