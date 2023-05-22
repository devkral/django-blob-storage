from django.apps import AppConfig


class DBStorageConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"

    name = "dbstorage"
    verbose_name = "DB Storage"
