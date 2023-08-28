from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class User_Registration(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'text-lg placeholder-gray-500 pl-10 pr-4 rounded-2xl border border-gray-400 w-full py-2 focus:outline-none focus:border-blue-400'
        
        

    class Meta:
        model = User
        fields = [
            "username","email","password","first_name","last_name"
        ]

    

    def clean_email(self):
        email = self.cleaned_data.get('email')
        obj = User.objects.filter(email=email)
        if obj:
            raise forms.ValidationError('this mail is already registered')
        return email
    
    def clean_username(self):
        username = self.cleaned_data.get('username')
        obj  = User.objects.filter(username=username)
        if obj :
            raise forms.ValidationError('this username is already registered')
        return username

    
    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) >= 8 :
            if password.isalnum():
                return password
            raise forms.ValidationError('Password should be a combination of letters and numbers')
        raise forms.ValidationError('password must be at least 8 characters')
    
    
    

class Login(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'id': 'username',
                'class': 'text-lg placeholder-gray-500 pl-10 pr-4 rounded-2xl border border-gray-400 w-full py-2 focus:outline-none focus:border-blue-400'
                }
        )
    )
    password = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'id': 'password',
                'class': 'text-lg placeholder-gray-500 pl-10 pr-4 rounded-2xl border border-gray-400 w-full py-2 focus:outline-none focus:border-blue-400'
                }
        )
    )

    def clean_username(self):
        username = self.cleaned_data.get('username')
        obj = User.objects.filter(username=username)
        if obj is not None:
            return username
        raise forms.ValidationError('username does not exist')
    


    