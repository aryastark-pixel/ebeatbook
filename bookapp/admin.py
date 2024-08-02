from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from bookapp.models import District,HotelsAndRestraunts

# CustomUserDefinition
# class CustomUserAdmin(UserAdmin):
#     # Define the fieldsets for the CustomUser admin interface
#     fieldsets = (
#         (None, {'fields': ('username', 'password')}),
#         ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'phonenumber')}),
#         ('Permissions', {
#             'fields': ('is_active', 'is_staff', 'is_superuser'),
#             'classes': ('collapse',),
#         }),
#         ('Important dates', {'fields': ('last_login', 'date_joined')}),
#     )
#     # Customizinf the fieldsets for adding new users
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('username', 'password1', 'password2', 'phonenumber'),
#         }),
#     )
#     # Use the default UserAdmin options
#     list_display = ('username', 'email', 'first_name', 'last_name', 'phonenumber', 'is_staff')
#     search_fields = ('username', 'email', 'first_name', 'last_name', 'phonenumber')
#     ordering = ('username',)
#DistritAdmin


class DistrictAdmin(admin.ModelAdmin):
    list_display=('State','District','DistrictCode')
    search_fields=('State','District','DistrictCode')
    list_filter=('District','DistrictCode')

admin.site.register(District, DistrictAdmin)
# admin.site.register(CustomUser, CustomUserAdmin)
# Register your models here.

class HotelAdmin(admin.ModelAdmin):
    list_display = ('HotelName', 'HotelOwner', 'phonenumber', 'Remarks')  # Adjust fields to match your model
    search_fields = ('HotelName', 'HotelOwner', 'phonenumber')
    list_filter = ('HotelOwner', 'phonenumber')  # Adjust filters as needed

# Register the Hotel model with the admin site
admin.site.register(HotelsAndRestraunts, HotelAdmin)
