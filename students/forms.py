from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . models import Student, Result, Student_fees

# User registration form
class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="",
                             widget=forms.TextInput(attrs={'class': 'form-control rounded', 'placeholder': 'Email Address'}))
    first_name = forms.CharField(label="", max_length=100,
                                 widget=forms.TextInput(attrs={'class': 'form-control rounded', 'placeholder': 'First Name'}))
    last_name = forms.CharField(label="", max_length=100,
                                widget=forms.TextInput(attrs={'class': 'form-control rounded', 'placeholder': 'Last Name'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control rounded'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text-muted"><small>Required. 150 characters or fewer. ' \
                                            'Letters, digits and @/./+/-/_ only.</small></span>'
        self.fields['password1'].widget.attrs['class'] = 'form-control rounded'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class="form-text-muted small"><li>Your password can\'t be too your ' \
                                             'other personal information.' \
                                             '</li><li>Your password must contain at least 8 ' \
                                             'characters.</li><li>Your password can\'t be a commonly used ' \
                                             'password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control rounded'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted><small>Enter the same password as ' \
                                             'before, for verification.</small></span>'

# Student registration
class StudentForm(forms.ModelForm):
    
    student_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"class": "form-control rounded"}) )
    
    email = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"class": "form-control rounded"}))
    
    phone = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"class": "form-control rounded"}))
    
    address = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"class": "form-control rounded"}))
    
    student_code = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={ "placeholder": "eg. 'ST412'","class": "form-control rounded", "name":"student_code", "maxlength":"5","pattern":"ST[4-5][0-9][0-9]","title":"Enter correct format(Between ST400-ST600)"}))   
   
    class Meta:
        model = Student
        fields = ('student_name', 'email','phone','address','student_code','course',)
        labels = {
            'student_name': 'Full Name',
            'email': 'Email',            
        }
        
    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)
        self.fields['course'].empty_label = 'Select Course'
        
# Form for recording student tuition
class StudentTuitionForm(forms.ModelForm):
    
    paid = forms.IntegerField(required=True, widget=forms.widgets.TextInput(attrs={"class": "form-control rounded"}) )
  
    class Meta:
        model = Student_fees
        fields = ('student_code','paid',)
        labels = {
              
        }
        
    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)
        self.fields['student_code'].empty_label = 'Select Student'

# Form for recording Student result
class ResultForm(forms.ModelForm): 
   
    student_code = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Student Code", "class": "form-control rounded", "maxlength":"5","pattern":"ST[4-5][0-9][0-9]"}),
                                 label="")
    student_name = forms.CharField(required=True, widget=forms.widgets.TextInput(
        attrs={"placeholder": "Student Name", "class": "form-control rounded"}), label="")
    m_one = forms.IntegerField(required=True,
                              widget=forms.widgets.TextInput(attrs={"class": "form-control rounded","maxlength":"2", "placeholder":"Module one"}),
                              label="")
    m_two = forms.IntegerField(required=True, widget=forms.widgets.TextInput(attrs={"class": "form-control rounded", "placeholder":"Module two", "maxlength":"2",}),
                              label="")
    m_three = forms.IntegerField(required=True,widget=forms.widgets.TextInput(attrs={"class": "form-control rounded", "placeholder":"Module three", "maxlength":"2",}),
                              label="")
    m_four = forms.IntegerField(required=True, widget=forms.widgets.TextInput(attrs={"class": "form-control rounded", "placeholder":"Module four", "maxlength":"2",}),
                           label="")
    gpa = forms.FloatField(required=True, widget=forms.widgets.TextInput(attrs={ "class": "form-control rounded", "placeholder":"Student GPA", "maxlength":"4",}),     label="")
    
    
    class Meta:
        model = Result
        fields = ('student_code', 'student_name', 'm_one', 'm_two', 'm_three', 'm_four', 'gpa')
        
    def __init__(self, *args, **kwargs):
        super(ResultForm, self).__init__(*args, **kwargs)
        