from django.contrib import admin
from .models import User, VerifideUser

# Register your models here.
admin.site.register(User)
# admin.site.register(VerifideUser)


@admin.register(VerifideUser)
class VerifiedUser(admin.ModelAdmin):
    list_display = ('code', 'user', 'created', 'expiration')
    fields = (('code', 'user'), ('created', 'expiration'))
    readonly_fields = ('created', 'user', 'code')
