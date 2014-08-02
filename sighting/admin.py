from django.contrib import admin
from .models import Bird, Sighting

# These statements allow CRUD access
# to the Bird and Sighting models in admin
admin.site.register(Bird)
admin.site.register(Sighting)