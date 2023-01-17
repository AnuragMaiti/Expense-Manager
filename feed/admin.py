from django.contrib import admin
from .models import AddExpense

# Register your models here.

class AddExpenseAdmin(admin.ModelAdmin):
    pass

admin.site.register(AddExpense,AddExpenseAdmin)