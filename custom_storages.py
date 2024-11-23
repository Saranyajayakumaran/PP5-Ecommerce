from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage

class StaticStorage(S3Boto3Storage):
    """
    Custom storage for static files, stored in a specific S3 location.
    """
    location = settings.STATICFILES_LOCATION
    file_overwrite = False  # Optional: Ensures that files are not overwritten if the same file name exists

class MediaStorage(S3Boto3Storage):
    """
    Custom storage for media files, stored in a specific S3 location.
    """
    location = settings.MEDIAFILES_LOCATION
    file_overwrite = False  # Optional: Ensures that files are not overwritten if the same file name exists
