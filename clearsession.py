import os
import django

# Tell Django where your settings are
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "aruntailors.settings")

# Setup Django
django.setup()

from django.contrib.sessions.models import Session

# Delete all sessions
Session.objects.all().delete()
print("All sessions cleared.")