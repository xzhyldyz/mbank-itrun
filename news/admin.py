from django.contrib import admin
from .models import News,SliderHomepage,ServiceHomepage,PaymentMethod

admin.site.register(News)
admin.site.register(SliderHomepage)
admin.site.register(ServiceHomepage)
admin.site.register(PaymentMethod)

