from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from . import models

#Utilizo o ModelForm por já ter um modelo de formulário, caso não tivesse poderia iniciar do zero um 'Form'
class ContactForm(forms.ModelForm):

    picture = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                'accept': 'image/*'
            }
        )
    )
    class Meta:
        model = models.Contact
        fields = (
            'first_name', 'last_name', 'phone',
            'email', 'description', 'category',
            'picture',
        )

        # widgets = {
        #     'first_name': forms.TextInput(
        #         attrs={
        #             'class': 'classe-a classe-b',
        #             'placeholder': 'Escreva aqui',
        #         }
        #     )
        # }

    def clean(self):
        cleaned_data = self.cleaned_data
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')
        if first_name == last_name:
            msg = ValidationError(
                    'Primeiro nome não pode ser igual ao segundo',
                    code='invalid'
                )
            self.add_error('first_name', msg)
            self.add_error('last_name', msg)

        return super().clean()
    
    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')

        if first_name == 'ABC':
            self.add_error(
                'first_name',
                ValidationError(
                    'Não digitar ABC',
                    code='invalid'
                )
            )
        return first_name # O valor retornado é o valor que vai ser enviado para o banco
    
class RegisterForm(UserCreationForm):

    first_name = forms.CharField(
        required=True,
        min_length=3,
    )
    first_name = forms.CharField(
        required=True,
        min_length=3,
    )
    email = forms.EmailField()
    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'email',
            'username', 'password1', 'password2',
        )

        def clean_email(self):
            email = self.cleaned_data.get('email')

            if User.objects.filter(email=email).exists():
                self.add_error(
                    'email',
                    ValidationError('Já existe este e-mail', code='invalid')
                )
            return email