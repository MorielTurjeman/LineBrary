from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import BookStationRelation, Book, Order,Profile



stations = [
    'Tel Aviv - Savidor Center',
    'Tel Aviv - University',
    'Tel Aviv - Ha-Shalom',
    'Tel Aviv - Ha-Hagana',
    'Nahariya',
    'Akko',
    'Karmiel',
    'Ahihod',
    'Kiryat Motskin',
    'Kiryat Haim',
    'Haifa - Hutsot HaMifrats',
    'Haifa - Merkazit HaMifrats',
    'Haifa - Merkaz Hashmuna',
    'Haifa - Bat Galim',
    'Haifa - Hof Hakarmel',
    'Beit Sheaan',
    'Afula',
    'Migdal HaEmek',
    'Yofneaam',
    'Atlit',
    'Binayamina',
    'Keysaria - Pardes Hana',
    'Hedera West',
    'Netanya',
    'Netanya - Sapir',
    'Beit Yehushua',
    'Herzliya',
    'Petah Tikva - Kiryat Arye',
    'Petah Tikva - Sgula',
    'Rosh HaAin North',
    'Kfar Saba - Nordaoo',
    'Hod HaSharon - Sokolov',
    'Raanana South',
    'Airport Ben Gurion',
    "Modi'in outskirts",
    "Modi'in Center",
    'Jerusalem - Yizhak Navon',
    'Kfar Habad',
    'Lud - Ganei Aviv',
    'Lud/Ramla',
    'Beit Shemesh',
    'Jesrualem - Tanahi Zoo',
    'Jerusalem - Malha',
    'Mazkeret Batia',
    'Kiryat Malachi - Yoav',
    'Kiryat Gat',
    "Lehavim/Raha'at",
    "Be'er Sheva North - University",
    "Be'er Sheva Center",
    'Dimona',
    'Ofakim',
    'Netivot',
    'Sderot',
    'Ashkelon',
    'Asdod - Ad Halom',
    'Yavne - West',
    'Yavne - East',
    "Be'er Yakov",
    'Rishon Letsiyon - HaRishonim',
    'Rishon Letsiyon - Moshe Dayan',
    'Bat Yam - HaKomemiyut',
    'Bat Yam - Yoseftal',
    'Holon Junction'
]

class BookForm(forms.ModelForm):
    '''
    bookname = forms.CharField(label='Book Name', max_length=100)
    author = forms.CharField(label='Author/s', max_length=100)
    gener = forms.ChoiceField(label= 'Gener' , choices=categories)
    language = forms.ChoiceField(label= 'Language')
    page_count = forms.IntegerField(label='Page Count')
    condition = forms.ChoiceField(label='Condition' , choices=('Like New' , 'Used' , 'Collectible'))
    cover_type = forms.ChoiceField(label='Cover Type' , choices=('Hard' , 'Soft'))
    image = forms.ImageField(required=False, label='Image', allow_empty_file=True)
    description = forms.CharField(label='Description')
    '''
    
    class Meta:
        model = Book
        fields = ('bookname', 'author', 'gener', 'language', 'page_count', 'cover_type', 'image', 'description',)

class BookStationRelationForm(forms.ModelForm):
    '''
    station = forms.ChoiceField(choices=stations, label='Station')
    '''
    class Meta:
        model = BookStationRelation
        fields = ('station',)

class ProfileForm(ModelForm):
    username = forms.CharField(label='User Name', max_length=100)
    firstname = forms.CharField(label="First Name", max_length=30)
    lastname = forms.CharField(label="Last Name", max_length=30)
    email = forms.EmailField(label="Email")
    password1 = forms.CharField(label="Password" , widget=forms.PasswordInput)
    password2 = forms.CharField(label="Re-enter Password" , widget=forms.PasswordInput)
    image = forms.ImageField(label="Image" , required=False)
    class Meta:
        model = Profile
        fields = ('username' , 'firstname' , 'lastname' , 'email' , 'password1' , 'password2', 'image')



    

'''
class Book(models.Model):
    ISBN13 = models.CharField(max_length=13 , primary_key=True)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    publication_date = models.DateField()
    pages = models.IntegerField()
    cover_image = models.ImageField(upload_to='Books/Images')
    languague = models.CharField(max_length=20)

class BookStationRelation(models.Model):
    ISBN13 = models.ForeignKey(Book , on_delete=models.CASCADE)
    station = models.IntegerField()

class Order(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    ISBN13 = models.ForeignKey(Book , on_delete=models.CASCADE)
    station = models.IntegerField()
    

class ProfileForm(forms.ModelForm):
    image = forms.ImageField(label="Image" , required=False)
    class Meta:
        model = Profile
        fields = ('image',)
'''
'''
class ProfileForm(ModelForm):
    username = forms.CharField(label='User Name', max_length=100)
    firstname = forms.CharField(label="First Name", max_length=30)
    lastname = forms.CharField(label="Last Name", max_length=30)
    email = forms.EmailField(label="Email")
    password1 = forms.CharField(label="Password" , widget=forms.PasswordInput)
    password2 = forms.CharField(label="Re-enter Password" , widget=forms.PasswordInput)
    image = forms.ImageField(label="Image" , required=False)
    class Meta:
        model = Profile
        fields = ('userName' , 'firstname' , 'lastname' , 'email' , 'password1' , 'password2', 'image')

'''

