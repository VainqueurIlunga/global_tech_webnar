from django.shortcuts import render
from django.views import View
from .models import Product
# Create your views here.


class IndexView(View):
    template_name='pages/index.html'
    
    def get (self, request):
        products = Product.objects.all()
        context= {
            'products': products
        }
        return render(request, self.template_name, context)