from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import BookStationRelation, Book, Order,Profile



stations = [
    'Tel Aviv - Savidor Center',
    'Tel Aviv - University',
    'Tel Aviv - Ha-Shalom',
    'Tel Aviv - Ha-Hagana',
    'Haifa - Bat Galim',
    'Haifa - Hof Hakarmel',
    'Beit Yehushua',
    'Herzliya',
    'Petah Tikva - Kiryat Arye',
    'Kfar Saba - Nordaoo',
 
]

class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ('bookname', 'author', 'gener', 'language', 'page_count', 'cover_type', 'image', 'description')

    condition = forms.ChoiceField(label='Condition' , choices=(('Like New', 'Like New') , ('Used', 'Used') , ('Collectible','Collectible')))


class BookStationRelationForm(forms.ModelForm):
    '''
    station = forms.ChoiceField(choices=stations, label='Station')
    '''
    class Meta:
        model = BookStationRelation
        fields = ('station',)


class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'email', 'default_station',)



    



