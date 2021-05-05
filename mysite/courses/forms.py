from .models import Product
from django.forms import ModelForm, Textarea,TextInput,DateTimeInput,FileInput,NumberInput
class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['title','start_date','end_date','quantity_lections','photo','description','small_description',"slug"]
        widgets = {
            'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'Назва курсу'}),
            "slug" : TextInput(attrs={'class': 'form-control'}) ,
            'small_description': Textarea(attrs={'class': 'form-control','placeholder': 'Наприклад,опишіть для кого цей курс'}),
            'description': Textarea(attrs={'class': 'form-control', 'placeholder': 'Опис'}),
            'start_date': DateTimeInput(attrs={'class': 'form-control',"type": "date"}),
            'end_date': DateTimeInput(attrs={'class': 'form-control',"type": "date"}),
            'quantity_lections': NumberInput(attrs={'class': 'form-control'}),
            'photo' : FileInput(attrs={'class':'form-control'})


        }


