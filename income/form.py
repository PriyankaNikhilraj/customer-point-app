from django import forms
from .models import Login,Registration,Home
class formz(forms.ModelForm):
    name = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'container'}))
    class Meta:
        model = Login
        fields = ['name','password']

    # email = forms.CharField(max_length=50)
    # password = forms.CharField(widget=forms.PasswordInput)
class formz2(forms.ModelForm):
    name=forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class': 'form-control'}))
    phon=forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'container'}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class': 'container'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'container'}))
    # confirm_password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Registration
        fields = ['name','phon','email','password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            self.add_error('confirm_password', "Passwords do not match")


class formz3(forms.ModelForm):
    # si_number=forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    name=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    customer=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    point=forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'container'}))
    # position_counter=forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'container'}))

    class Meta:
        model = Home
        fields = ['name','customer','point']