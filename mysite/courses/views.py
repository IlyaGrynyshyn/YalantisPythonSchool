from .models import Product
from django.shortcuts import render, redirect
from django.views.generic import DetailView, ListView,UpdateView,DeleteView,View
from .forms import ProductForm
from django.db.models import Q
from .filters import ProductFilter


def create(request):

    error = ''
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма не правильна'
    form = ProductForm()

    data = {
        'form' : form,
        "error" : error
    }
    return render(request,"create_product.html",data)


class BaseView(ListView):
    model = Product
    template_name = 'base.html'
    context_object_name = 'products'
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = ProductFilter(self.request.GET,queryset=self.get_queryset())
        return context




class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'
    context_object_name = 'product'



class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'create_product.html'
    form_class = ProductForm

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'delete_product.html'
    success_url = 'home'

class SearchResultsView(ListView):
    model = Product
    template_name = 'search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('search')
        object_list = Product.objects.filter(
            Q(title__icontains=query)
        )
        return object_list