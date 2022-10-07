from django import forms


class ContactForm(forms.Form):
    email_sender_name = forms.CharField(
        required=True, max_length=255, label="Your Name"
    )
    email_subject = forms.CharField(
        required=True, max_length=255, label="Email Subject"
    )
    email_sender_email = forms.EmailField(required=True, label="Your Email")
    email_content = forms.CharField(
        required=True, widget=forms.Textarea, label="Email Content"
    )
