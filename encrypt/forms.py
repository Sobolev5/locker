from django import forms


class AddRecordForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea, max_length=1600, required=True)
    password = forms.CharField(required=True)
    hours_locked = forms.IntegerField(required=False, initial=0)
    can_be_deleted = forms.BooleanField(required=False)


class ShowRecordForm(forms.Form):
    password = forms.CharField(required=True)
