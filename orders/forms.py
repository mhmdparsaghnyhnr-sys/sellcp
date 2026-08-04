from django import forms
from .models import Order


CP_CHOICES = [
    ("80 CP", 90000),
    ("420 CP", 0),
    ("880 CP", 670000),
    ("2400 CP", 1650000),
    ("5000 CP", 3200000),
]


class OrderForm(forms.ModelForm):

    cp_amount = forms.ChoiceField(
        choices=[(x[0], x[0]) for x in CP_CHOICES],
        label="تعداد CP"
    )

    class Meta:
        model = Order
        fields = [
            "name",
            "email",
            "password",
            "cp_amount",
        ]

    def save(self, commit=True):
        order = super().save(commit=False)

        for cp, price in CP_CHOICES:
            if order.cp_amount == cp:
                order.price = price
                break

        if commit:
            order.save()

        return order