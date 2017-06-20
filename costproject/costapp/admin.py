from django.contrib import admin

from .models import *

class BudgetInline(admin.StackedInline):
    model = Budget
    extra = 0
    verbose_name_plural = 'Budgets under this category'
    # list_display = ('name', 'original_budget_amount', 'current_budget_amount')

class BudgetCategoryAdmin(admin.ModelAdmin):
    inlines = [BudgetInline]
    # list_display = ('name', 'remaining_amount')
    readonly_fields = ['total', 'current', 'remaining']

admin.site.register(Payment)
admin.site.register(PurchaseOrder)
admin.site.register(Invoice)
# admin.site.register(Budget)
admin.site.register(BudgetChange)
admin.site.register(BudgetCategory, BudgetCategoryAdmin)
admin.site.register(Supplier)
