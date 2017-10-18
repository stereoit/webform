from django import forms

class ApplicantForm(forms.Form):
    your_name = forms.CharField(
        label='Your name',
        max_length=100,
        required=True
    )
    test_name = forms.CharField(
        label='Test field',
        max_length=100,
        # help_text="`joe` => `boby`, `dan` == invalid ValidationError, anything else is just passed through"
        help_text="Value = `dan` => invalid ValidationError, anything else is just passed through"
    )
    start_date = forms.DateField(
        help_text="Enter a date between now and 4 weeks.",
        required=False,
        widget=forms.widgets.DateInput(attrs={'type': 'date'})
    )
    message = forms.CharField(widget=forms.Textarea, required=False)
    tickbox = forms.BooleanField(
        required=False,
        help_text="Just tick it"
    )

    def clean_test_name(self):
        data = self.cleaned_data['test_name']
        if "dan" in data:
            raise forms.ValidationError("Value `dan` is invalid!", code='invalid')
        # if "joe" in data:
        #     self.data['test_name'] = "boby"
        #     data = "boby"
        return data
