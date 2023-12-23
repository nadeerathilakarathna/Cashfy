from django.contrib import admin
from .models import Icon
from .models import Account
from .models import Category
from .models import Transaction
# Register your models here.


class AccountAdmin(admin.ModelAdmin):
    list_display = ('id', 'uid', 'name', 'icon', 'checked')  # Fields to display in the admin table
    list_filter = ('checked',)  # Add a filter for the 'checked' field
    search_fields = ('name', 'icon')  # Add search functionality for 'name' and 'icon'

admin.site.register(Icon)
#admin.site.register(Account)
admin.site.register(Category)
admin.site.register(Transaction)
admin.site.register(Account, AccountAdmin)