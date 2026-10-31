from django import forms

from .models import ContactInquiry, RepairRequest


class ContactInquiryForm(forms.ModelForm):
    class Meta:
        model = ContactInquiry
        fields = ['customer_name', 'email', 'phone', 'subject', 'message']
        widgets = {
            'customer_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your full name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'your@email.com'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+1 234 567 890'}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'How can we help?'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Tell us about your inquiry...'}),
        }

    def clean_phone(self):
        phone = self.cleaned_data.get('phone', '').strip()
        if len(phone) < 7:
            raise forms.ValidationError('Please enter a valid phone number.')
        return phone

    def clean_message(self):
        message = self.cleaned_data.get('message', '').strip()
        if len(message) < 10:
            raise forms.ValidationError('Please provide a more detailed message.')
        return message


class RepairRequestForm(forms.ModelForm):
    class Meta:
        model = RepairRequest
        fields = [
            'customer_name',
            'email',
            'phone',
            'mobile_brand',
            'mobile_model',
            'repair_category',
            'problem_description',
            'preferred_contact',
        ]
        widgets = {
            'customer_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'your@email.com'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+1 234 567 890'}),
            'mobile_brand': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apple, Samsung, Xiaomi...'}),
            'mobile_model': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. iPhone 14 Pro'}),
            'repair_category': forms.Select(attrs={'class': 'form-select'}),
            'problem_description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Describe the issue in detail...'}),
            'preferred_contact': forms.Select(attrs={'class': 'form-select'}),
        }

    def clean_phone(self):
        phone = self.cleaned_data.get('phone', '').strip()
        if len(phone) < 7:
            raise forms.ValidationError('Please enter a valid phone number.')
        return phone

    def clean_problem_description(self):
        problem = self.cleaned_data.get('problem_description', '').strip()
        if len(problem) < 10:
            raise forms.ValidationError('Please describe the issue in more detail.')
        return problem
