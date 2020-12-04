from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import validate_email

class ContactForm(forms.Form):
    name = forms.CharField(max_length=20) # 名前
    email = forms.CharField(max_length=40)
    message = forms.CharField(widget=forms.Textarea, max_length=100) #問い合わせ内容
 
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['name'].widget.attrs['placeholder'] = 'お名前'
        self.fields['name'].widget.attrs['maxlength'] = '20'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['placeholder'] = 'メールアドレス'
        self.fields['email'].widget.attrs['maxlength'] = '40'
        self.fields['message'].widget.attrs['class'] = 'form-control'
        self.fields['message'].widget.attrs['placeholder'] = 'メッセージ'
        self.fields['message'].widget.attrs['maxlength'] = '200'
        self.fields['message'].widget.attrs['rows'] = '6'
 
    def clean_email(self):
        email = self.cleaned_data["email"]
        try:
            validate_email(email)
        except ValidationError:
            raise ValidationError("正しいメールアドレスを指定して下さい。")