from django.db import models

# Create your models here.
    
    
class AddExpense(models.Model):

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("DailyExpense_detail/", kwargs={"pk": self.pk})
    
    name = models.CharField(max_length=50, blank = False, null = False, verbose_name="Type")
    add_expense = models.IntegerField(blank = False, null = False, verbose_name = "Expense")

    