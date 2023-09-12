from django import forms


class ContactForms(forms.Form):

    name = forms.CharField(label="Nombre", max_length=100, required=True,
                           widget=forms.TextInput(attrs={"placeholder": "Tu Nombre"}))

    email = forms.EmailField(label="Email", required=True, max_length=70,
                             widget=forms.EmailInput(attrs={"placeholder": "Tu Email"}))

    telepone = forms.CharField(
        max_length=20, label="Numero de telefono", required=True, widget=forms.TextInput(attrs={"placeholder": "Tu Telefono"}))

    mesage = forms.CharField(label="Escribe tu mensaje",
                             max_length=500, required=True, widget=forms.Textarea(attrs={"placeholder": "Tu Mensaje"}))
