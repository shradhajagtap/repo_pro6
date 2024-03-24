from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import ProductOrderForm
from .models import ProductOrder


@login_required(login_url="login_url")
def create_order(request):
    template_name = "curd_app/create.html"
    form = ProductOrderForm()
    if request.method == "POST":
        form = ProductOrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("show_url")
    context = {"form": form}
    return render(request, template_name, context)


def show_order(request):
    template_name = "curd_app/show.html"
    orders = ProductOrder.objects.all()
    context = {"orders": orders}
    return render(request, template_name, context)


def update_order(request, pk):
    obj = ProductOrder.objects.get(id=pk)
    form = ProductOrderForm(instance=obj)
    if request.method == "POST":
        form = ProductOrderForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect("show_url")
    template_name = 'curd_app/create.html'
    context = {'form': form}
    return render(request, template_name, context)


def cancel_order(request,  pk):
    obj = ProductOrder.objects.get(id=pk)
    if request.method == "POST":
        obj.delete()
        return redirect("show_url")
    return render(request, 'curd_app/confirm.html')
