from django.shortcuts import render
from .forms import OrderForm

def order_create(request):
    if request.method == "POST":
        form = OrderForm(request.POST)

        if form.is_valid():
            form.save()
            return render(request, "success.html")

    else:
        form = OrderForm()

    return render(request, "order.html", {
        "form": form
    })