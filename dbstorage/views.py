import mimetypes
import time

from django.http.response import FileResponse, HttpResponseNotModified
from django.shortcuts import get_object_or_404
from django.utils.http import http_date
from django.views.generic.base import View
from django.views.static import was_modified_since
from django.utils import timezone
from django.conf import settings

from dbstorage.models import DBFile


class DBFileView(View):
    def get(self, request, name):
        """Endpoint to return memory storage file"""
        db_file_query = DBFile.objects.defer("content").filter(name=name)
        db_file = get_object_or_404(db_file_query)
        if getattr(settings, "DJANGO_DBFILE_TRACK_ACCESSED", False):
            db_file_query.update(accessed_on=timezone.now())

        mtime = time.mktime(db_file.updated_on.timetuple())
        modified = was_modified_since(
            header=self.request.META.get("HTTP_IF_MODIFIED_SINCE"),
            mtime=mtime,
        )

        if not modified:
            return HttpResponseNotModified()

        content_type, encoding = mimetypes.guess_type(db_file.name)
        content_type = content_type or "application/octet-stream"

        response = FileResponse(db_file.content, content_type=content_type)
        response["Last-Modified"] = http_date(mtime)
        response["Content-Length"] = db_file.size
        if encoding:
            response["Content-Encoding"] = encoding
        return response
