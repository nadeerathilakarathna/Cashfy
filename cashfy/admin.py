from django.contrib import admin
from .models import Icon
from .models import Account
from .models import Category
from .models import Transaction
from .models import Config
# Register your models here.


class AccountAdmin(admin.ModelAdmin):
    list_display = ('id', 'uid', 'name', 'icon', 'checked')  # Fields to display in the admin table
    list_filter = ('checked',)  # Add a filter for the 'checked' field
    search_fields = ('name', 'icon')  # Add search functionality for 'name' and 'icon'


class TransectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'uid', 'timestamp', 'amount', 'account', 'detail', 'category', 'expense')  # Fields to display in the admin table
    list_filter = ('expense',)  # Add a filter for the 'checked' field

class ConfigAdmin(admin.ModelAdmin):
    list_display = ('id', 'uid', 'selection', 'start', 'end')  # Fields to display in the admin table

admin.site.register(Icon)
#admin.site.register(Account)
admin.site.register(Category)
admin.site.register(Transaction, TransectionAdmin)
admin.site.register(Account, AccountAdmin)
admin.site.register(Config, ConfigAdmin)