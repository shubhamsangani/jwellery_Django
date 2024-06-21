# # forms.py
# from django import forms
# from .models import Users

# class UserForm(forms.ModelForm):
#     password = forms.CharField(label='Password', widget=forms.PasswordInput)
#     repeat_password = forms.CharField(label='Repeat Password', widget=forms.PasswordInput)

#     class Meta:
#         model = Users
#         fields = ['user_name', 'user_email', 'user_phone_no', 'password']

#     def clean(self):
#         cleaned_data = super().clean()
#         password = cleaned_data.get("password")
#         repeat_password = cleaned_data.get("repeat_password")

#         if password and repeat_password and password != repeat_password:
#             raise forms.ValidationError("Passwords do not match.")


# class Shipping(forms.ModelForm):
#     pass