from django import forms
from django.core.exceptions import ValidationError
from django.core.files.base import ContentFile
from django.utils.text import slugify
from .models import PcBase, PcType


class PcAddForm(forms.ModelForm):
    pc_type = forms.ModelChoiceField(queryset=PcType.objects.all(), empty_label="Тип не выбран", label="Тип оборудования *")

    class Meta:
        model = PcBase
        fields = ['pc_model', 'pc_slug', 'pc_type', 'pc_cpu', 'pc_disk_size', 'pc_photo', 'pc_about', 'pc_pub']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'pc_about': forms.Textarea(attrs={'cols': 50, 'rows': 5}),
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 50:
            raise ValidationError("Длина превышает 50 символов")

        return title
