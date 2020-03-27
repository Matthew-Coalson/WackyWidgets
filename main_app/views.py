from django.shortcuts import render, redirect
from .models import Widget
from .forms import AddWidgetForm

def home(request):
    if request.method == 'POST':
        form = AddWidgetForm(request.POST)
        if form.is_valid():
            new_widget = form.save(commit=False)
            new_widget.save()
    widgets = Widget.objects.all()
    add_widget_form = AddWidgetForm()
    total = 0
    for widget in widgets:
        total += widget.quantity
    return render(request, 'home.html', {
        'widgets': widgets,
        'add_widget_form': add_widget_form,
        'total': total,
    })

def delete(request, widget_id):
    Widget.objects.get(id=widget_id).delete()
    return redirect('home')