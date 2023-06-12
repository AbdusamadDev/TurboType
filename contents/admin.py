from django.contrib import admin
<<<<<<< HEAD
from .models import Contents
# Register your models here.


admin.site.register(Contents)
=======
from contents.models import ContentModel

admin.site.register(ContentModel)
>>>>>>> b76fcb9a0111a77b80b50cfd58036a0cb043b823
