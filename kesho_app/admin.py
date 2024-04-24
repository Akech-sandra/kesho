from django.contrib import admin
from .models import *#trying to access classes/models upon with admin are going to build interfaces for categorystay and baby from the admin panal/dashboard
#from .models import categorystay, baby
#from .models import categorystay
#from .models import baby

# Register your models here.
admin.site.register(Categorystay)
admin.site.register(Payment)
admin.site.register(Baby)

