from django import forms


class ContestForm(forms.Form):
    title = forms.CharField(label='Название', max_length=20)
    description = forms.CharField(
        label='Описание',
         widget=forms.Textarea(attrs={
            'rows': 5,
            'cols': 50,
            'placeholder': 'Введите описание...'
        })
    )
    price = forms.IntegerField(
        label='Цена',
        min_value=10,
        max_value=100,
        required=True,
        help_text='Рекомендованная розничная цена',
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите цену от 10 до 100'
        })
    )
    comment = forms.CharField(
        label='Комментарий',
        required=False,
        widget=forms.Textarea(attrs={
            'rows': 5,
            'cols': 50,
        })
    )
