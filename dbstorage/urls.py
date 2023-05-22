import re

from django.conf import settings
from django.urls import re_path

from dbstorage import views


urlpatterns = [
    re_path(
        r"^%s(?P<name>.*)$" % re.escape(settings.MEDIA_URL.lstrip("/")),
        views.DBFileView.as_view(),
        name="db_file",
    ),
]
