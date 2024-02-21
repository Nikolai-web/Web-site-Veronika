from django import forms

class EmailPostForm(forms.Form):
    # Имя чел отправляющего сообщение
    name = forms.CharField(max_length=25)
    # Адрес эл почты отправляющего чел
    email = forms.EmailField()
    # Адрес эл почты получателя
    to = forms.EmailField()
    # Комментарии, которые будут вставлятся в эл письмо
    comments = forms.CharField(required=False, widget=forms.Textarea)

