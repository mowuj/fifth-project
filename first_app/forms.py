from django import forms
from django.core import validators

class contactForm(forms.Form):
    # widgets == files to html input 
    name = forms.CharField(label="Full Name : ",help_text="Total length must be within 70 characters",required=False,disabled=False,widget=forms.Textarea(attrs={'id':'textarea','class':'form-control','placeholder':'Enter Your Name'}))
    # file upload
    # file=forms.FileField()
    # name=forms.CharField(label="User Name")
    email=forms.EmailField(label="User Email")
    age=forms.CharField(widget=forms.NumberInput)
    weight=forms.FloatField()
    balance=forms.DecimalField()
    check=forms.BooleanField()
    birthday=forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    appointment=forms.DateTimeField(widget=forms.DateInput(attrs={'type':'datetime-local'}))
    CHOICES=[('S','Small'),('M','Medium'),('L','Large')]
    size=forms.ChoiceField(choices=CHOICES,widget=forms.RadioSelect)
    MEAL=[('P','Pepperoni'),('M','Mashroom'),('B','Beef')]
    pizza=forms.MultipleChoiceField(choices=MEAL,widget=forms.CheckboxSelectMultiple)

# class StudentData(forms.Form):
#     name=forms.CharField(widget=forms.TextInput)
#     email=forms.CharField(widget=forms.EmailInput)
#     # def clean_name(self):
#     #     valname=self.cleaned_data['name']
#     #     if len(valname) <10:
#     #         raise forms.ValidationError('Enter a name at least 10 characters')
#     #     return valname
    
#     # def clean_email(self):
#     #     valemail=self.cleaned_data['email']
#     #     if '.com' not in valemail:
#     #         raise forms.ValidationError('Please enter a valid email address')
#     #     return valemail

#     def clean(self):
#         cleaned_data=super().clean()        
#         valname=self.cleaned_data['name']
#         valemail=self.cleaned_data['email']
#         if len(valname) <10:
#             raise forms.ValidationError('Enter a name at least 10 characters')
    
#         if '.com' not in valemail:
#             raise forms.ValidationError('Please enter a valid email address')
    
def len_check(value):
    if len(value) < 10:
        raise forms.ValidationError('Enter a value at least 10 characters')
class StudentData(forms.Form):
    name = forms.CharField(widget=forms.TextInput, validators=[
                        validators.MinLengthValidator(10, message='Enter a name at least 10 characters')])
    text=forms.CharField(widget=forms.TextInput,validators=[len_check])
    email = forms.CharField(widget=forms.EmailInput,validators=[validators.EmailValidator(message='enter a valid email address')])
    age=forms.IntegerField(validators=[validators.MaxValueValidator(34,message='age must be maximum 34'),validators.MinValueValidator(24,message='age must be at least 24')])
    file=forms.FileField(validators=[validators.FileExtensionValidator(allowed_extensions=['pdf','png'],message='file extension must be ended with pdf')])
    # Regex,url, 

class PasswordValidationProject(forms.Form):
    name=forms.CharField(widget=forms.TextInput)
    password=forms.CharField(widget=forms.PasswordInput)
    confirm_password=forms.CharField(widget=forms.PasswordInput)
    
    def clean(self):
        cleaned_data=super().clean()
        val_pass=self.cleaned_data["password"]
        val_conpass=self.cleaned_data["confirm_password"]
        val_name=self.cleaned_data["name"]       
        if val_conpass != val_pass:
            raise forms.ValidationError('Passwords do not match')
        if len(val_name)<10:
            raise forms.ValidationError("Name must be at least 10 characters")
