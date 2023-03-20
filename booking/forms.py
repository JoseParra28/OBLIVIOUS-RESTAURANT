from django import forms 

class availability_form(forms.Form):
    TABLE_CATEGORIES = (
        ('TWO', 'TWO'),
        ('THREE', 'THREE'),
        ('FOUR', 'FOUR'),
        ('FIVE', 'FIVE'),
        ('GROUP', 'GROUP')
    )
    table_category = forms.ChoiceField(choices=TABLE_CATEGORIES, required=True)
    arrival_time = forms.DateTimeField(required=True, input_formats=["%d-%m-%yT%H-%M"])
    departure_time = forms.TimeField(required=True, input_formats=["T%H-%M"])
