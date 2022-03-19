from django import forms

from mayan.apps.views.forms import DetailForm

from .models import Theme, UserThemeSetting


class ThemeForm(forms.ModelForm):
    file_data = forms.FileField(required=False)

    class Meta:
        fields = ('label','defaulttheme','file_data','fontname','stylesheet', 'logo',)
        model = Theme
        widgets = {
            'file_data': forms.FileInput(
                attrs={
                    'accept': '.css, .xml'
                }
            )
        }

    def save(self, commit=True):
        obj = super().save(commit=False)

        uploaded_file = self.cleaned_data['file_data']
        if uploaded_file is not None:
            obj.stylesheet = uploaded_file.read().decode()

        if commit:
            obj.save()

        return obj

class UserThemeSettingForm(forms.ModelForm):
    class Meta:
        fields = ('theme',)
        model = UserThemeSetting
        widgets = {
            'theme': forms.Select(
                attrs={
                    'class': 'select2'
                }
            ),
        }


class UserThemeSettingForm_view(DetailForm):
    class Meta:
        fields = ('theme',)
        model = UserThemeSetting
