from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    mobile_number = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class Expense(models.Model):
    EQUAL = 'EQUAL'
    EXACT = 'EXACT'
    PERCENT = 'PERCENT'
    EXPENSE_TYPES = [
        (EQUAL, 'Equal'),
        (EXACT, 'Exact'),
        (PERCENT, 'Percentage'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    expense_type = models.CharField(max_length=10, choices=EXPENSE_TYPES)
    participants_data = models.JSONField()
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Expense of {self.amount} by {self.user}"


class Balance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_balances')
    with_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='with_user_balances')
    amount = models.DecimalField(max_digits=12, decimal_places=2)

    class Meta:
        unique_together = ('user', 'with_user')

    def __str__(self):
        return f"{self.user} owes {self.amount} to {self.with_user}"
