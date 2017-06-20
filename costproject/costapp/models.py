from django.db import models

class BudgetCategory(models.Model):
    name = models.CharField(max_length=200)
    class Meta:
        verbose_name_plural = 'budget categories'
    def total(self):
        budgets = Budget.objects.filter(category=self)
        total = 0
        for budget in budgets:
            total += budget.original_budget_amount
        return total
    def current(self):
        original = self.total()
        changes = BudgetChange.objects.filter(budget__category=self)
        for change in changes:
            original += change.value_of_change
        return original
    def remaining(self):
        current = self.current()
        payments = Payment.objects.filter(purchase_order__budget__category=self)
        for payment in payments:
            current -= payment.value_of_work_done
        return current
    def __str__(self):
        return self.name

class Budget(models.Model):
    original_budget_amount = models.DecimalField(decimal_places=2, max_digits=20)
    name = models.CharField(max_length=200)
    category = models.ForeignKey(BudgetCategory)
    def current_budget_amount(self):
        return 0
    def __str__(self):
        return self.category.name + ' -> ' + self.name

class BudgetChange(models.Model):
    budget = models.ForeignKey(Budget)
    value_of_change = models.DecimalField(decimal_places=2, max_digits=20)
    reason_for_change = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True, blank=True)
    STATUS = ((0, 'pending'), (1, 'rejected'), (2, 'approved'))
    status = models.IntegerField(default=0, choices=STATUS)
    def __str__(self):
        pos = self.value_of_change >= 0
        return ('Add ' if pos else 'Subtract ') \
        + ' $' + str(abs(self.value_of_change)) \
        + (' to ' if pos else ' from ') \
        + str(self.budget)

class Supplier(models.Model):
    contact_point = models.CharField(max_length=200)
    contact_phone = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class PurchaseOrder(models.Model):
    committed_amount = models.DecimalField(decimal_places=2, max_digits=20)
    description = models.CharField(max_length=200)
    budget = models.ForeignKey(Budget)
    supplier = models.ForeignKey(Supplier)
    def __str__(self):
        return self.description

class Invoice(models.Model):
    amount = models.DecimalField(decimal_places=2, max_digits=20)
    purchase_order = models.ForeignKey(PurchaseOrder)
    date = models.DateTimeField(auto_now=False)
    def __str__(self):
        return '$' + str(self.amount) + ' for ' + str(self.purchase_order)

class Payment(models.Model):
    value_of_work_done = models.DecimalField(decimal_places=2, max_digits=20)
    purchase_order = models.ForeignKey(PurchaseOrder)
    def __str__(self):
        return "Payment of $" + str(self.value_of_work_done)
