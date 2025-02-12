from django.contrib.auth.models import User
from django import forms

class UserRegistrationForm(forms.ModelForm):

    password = forms.CharField(label="Senha", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repita a senha", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ("username", 'first_name', "email")

        labels = {
            "username": "Usuário",
            "first_name": "Nome",
            "email": "E-mail"
        }

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError("As senhas não coincidem!")
        return cd['password2']
    
    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Este e-mail já está em uso. Escolha outro.")
        return email