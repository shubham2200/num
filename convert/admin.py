from django.contrib import admin
from  .models import Person,number,words
# Register your models here.

admin.site.register(number)
admin.site.register(words)


admin.site.register(Person)