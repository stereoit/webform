from django import forms
from django.utils.translation import ugettext_lazy as _

class ApplicantForm(forms.Form):
    your_name = forms.CharField(
        label=_('your name'),
        help_text=_('applicantform.your_name.help_text'),
        max_length=100,
        required=True
    )
    test_name = forms.CharField(
        label=_('test field'),
        max_length=100,
        # help_text="`joe` => `boby`, `dan` == invalid ValidationError, anything else is just passed through"
        help_text=_("Value = `dan` => invalid ValidationError, anything else is just passed through"),
    )
    start_date = forms.DateField(
        label=_("possible join date"),
        # Translators: This message appears on the home page only
        help_text="Enter a date between now and 4 weeks.",
        required=False,
        widget=forms.widgets.DateInput(attrs={'type': 'date'})
    )
    message = forms.CharField(
        label=_('message'),
        widget=forms.Textarea,
        required=False,
    )
    tickbox = forms.BooleanField(
        label=_('tickbox'),
        required=False,
        help_text=_("This is a sample tick box."),
    )

    def clean_test_name(self):
        data = self.cleaned_data['test_name']
        if "dan" in data:
            raise forms.ValidationError("Value `dan` is invalid!", code='invalid')
        # if "joe" in data:
        #     self.data['test_name'] = "boby"
        #     data = "boby"
        return data
