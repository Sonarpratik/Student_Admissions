from django.contrib import admin

# Register your models here.

from .models import *
# admin.site.register(Student)
# admin.site.register(Book)
# admin.site.register(Category)
# admin.site.register(Song)
# admin.site.register(Singer)
admin.site.site_header="Web Spirits"
admin.site.site_title="Web Spirits"
admin.site.index_title="Web Spirits"
admin.site.register(StudentAdmission)
# admin.site.register(User)
# admin.site.register(Items)
# admin.site.register(Category)
# admin.site.register(Status)/
# admin.site.register(InteriorGallery)
# admin.site.register(DesignGallery)

# @admin.register(Client)
# class ClientAdmin(admin.ModelAdmin):
#  list_display=['id','contact_person_name','company_name']

# @admin.register(Inventorys)
# class InventorysAdmin(admin.ModelAdmin):
#  list_display=['id','sac','rate']
# admin.site.register(Shipping)