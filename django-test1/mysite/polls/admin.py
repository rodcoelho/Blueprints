from django.contrib import admin

# import Classes(tables) from your Model you would like to have in admin website
from .models import Question
# register the Class like so
admin.site.register(Question)

