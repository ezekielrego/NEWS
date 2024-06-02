from django.contrib import admin
from .models import latestnews
from .models import activitiess
from .models import weeklynews


admin.site.register(activitiess)
admin.site.register(latestnews)
admin.site.register(weeklynews)
# Register your models here.
