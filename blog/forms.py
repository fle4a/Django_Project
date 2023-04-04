from django import forms
from .models import Employees,DismissalArticle,Document
from .views import COLUMN_NAMES
class DocumentForm(forms.ModelForm):


    emp = forms.ModelChoiceField(label = 'Cотрудник',queryset=Employees.objects.all())
    dismissal_article = forms.ModelChoiceField(label = 'Статья увольнения',queryset=DismissalArticle.objects.all())
    class Meta:
        model = Document
        fields = ['doc_id','doc_number', 'registration_date', 'dismissal_date', 'dismissal_article', 'emp', 'compensation']
        labels = COLUMN_NAMES
        widgets = {
            'doc_id': forms.TextInput(attrs={'class': 'my-input'}),
            'doc_number': forms.TextInput(attrs={'class': 'my-input'}),
            'registration_date': forms.DateInput(attrs={'class': 'my-input'}),
            'dismissal_date': forms.DateInput(attrs={'class': 'my-input'}),
            'dismissal_article': forms.Select(attrs={'class': 'my-input'}),
            'emp': forms.Select(attrs={'class': 'my-input'}),
            'compensation': forms.NumberInput(attrs={'class': 'my-input'}),
        }

class AuthForm(forms.Form):
    username = forms.CharField(label='Логин', max_length=50, widget=forms.TextInput(attrs={'class': 'my-input'}) )
    password = forms.CharField(label='Пароль', max_length=50,widget=forms.PasswordInput(attrs={'class': 'my-input'}))

class RegistrationForm(forms.Form):
    first_name = forms.CharField(label='Фамилия', max_length=50, widget=forms.TextInput(attrs={'class': 'my-input'}))
    last_name = forms.CharField(label='Имя', max_length=50, widget=forms.TextInput(attrs={'class': 'my-input'}))
    middle_name = forms.CharField(label='Отчество', max_length=50, widget=forms.TextInput(attrs={'class': 'my-input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'my-input'}))
    phone_number = forms.CharField(label='Номер телефона', max_length=20, widget=forms.TextInput(attrs={'class': 'my-input'}))
    username = forms.CharField(label='Логин', max_length=50, widget=forms.TextInput(attrs={'class': 'my-input'}))
    password = forms.CharField(label='Пароль', max_length=50, widget=forms.PasswordInput(attrs={'class': 'my-input'}))
