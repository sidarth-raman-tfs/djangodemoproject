from django.shortcuts import render, get_object_or_404, redirect
from rest_framework import viewsets
from .models import ItemOne
from .serializers import ItemOneSerializer
from .forms import ItemOneForm

class ItemOneViewSet(viewsets.ModelViewSet):
    queryset = ItemOne.objects.all()
    serializer_class = ItemOneSerializer

def movie1_list_html(request):
    items = ItemOne.objects.all()
    thedict = {'items': items}
    return render(request, 'app1/itemone_list.html',context = thedict)

def itemone_update_html(request, pk):
    item = get_object_or_404(ItemOne, pk=pk)
    if request.method == 'POST':
        form = ItemOneForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('itemone-list-html')
    else:
        form = ItemOneForm(instance=item)

    return render(request, 'app1/itemone_form.html', {
        'form': form,
        'item': item,
    })


def itemone_delete_html(request, pk):
    item = get_object_or_404(ItemOne, pk=pk)

    if request.method == 'POST':
        item.delete()
        return redirect('itemone-list-html')

    return render(request, 'app1/itemone_confirm_delete.html', {
        'item': item,
    })
