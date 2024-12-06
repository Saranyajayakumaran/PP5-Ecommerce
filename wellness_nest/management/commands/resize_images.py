import os
from PIL import Image
from django.conf import settings
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "Resize all images in the media folder"

    def handle(self, *args, **kwargs):
        media_root = settings.MEDIA_ROOT
        image_extensions = ['.jpg', '.jpeg', '.png', '.webp']
        target_size = (300, 300)  # Target size (width, height)

        # Walk through the media folder
        for root, dirs, files in os.walk(media_root):
            for file in files:
                if any(file.lower().endswith(ext) for ext in image_extensions):
                    file_path = os.path.join(root, file)

                    # Open and resize the image
                    try:
                        with Image.open(file_path) as img:
                            img = img.convert("RGB")  # Ensure consistent format
                            img.thumbnail(target_size)  # Resize while maintaining aspect ratio
                            img.save(file_path, format="WEBP", quality=75)
                            self.stdout.write(self.style.SUCCESS(f"Resized: {file_path}"))
                    except Exception as e:
                        self.stderr.write(self.style.ERROR(f"Error resizing {file_path}: {e}"))
