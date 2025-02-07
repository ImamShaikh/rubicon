from django.shortcuts import render,HttpResponseRedirect
from .models import product
from .forms import productForm

# Create your views here.
def home(request):
    data = product.objects.all()
    request.method == 'POST'
    form = productForm(request.POST)
    if form.is_valid():
         form.save()
         form = productForm()
    else:
         form = productForm()
    return render(request,'ekart/index.htm',{'data':data,'form':form})

def update_data(request,id):
    if request.method == 'POST':
            pi = product.objects.get(pk=id)
            form = productForm(request.POST, instance=pi)
            if form.is_valid():
                 form.save()

    else:
         pi=product.objects.get(pk=id)
         form = productForm(instance=pi)

    return render(request,'ekart/update.html',{'form':form})    

def delete_data(request,id):
     if request.method == 'POST':
          pi = product.objects.get(pk=id)    
          pi.delete()
          return HttpResponseRedirect("/")