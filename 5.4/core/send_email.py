from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings

def send_email(request):
    subject = 'Hello from Django!'
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [request.user.email]

    # 1. Pass data to your HTML email template (optional)
    context = {
        'username': request.user.username,
        'message_body': 'Hello brother, welcome aboard!'
    }
    
    # 2. Convert the HTML file into a raw text string
    html_message = render_to_string('email.html', context)
    
    # 3. Strip HTML tags to create a plain text fallback version 
    # (Crucial for older email clients or strict spam filters)
    plain_message = strip_tags(html_message)

    try:
        send_mail(
            subject=subject,
            message=plain_message,       # Fallback plain text version
            from_email=from_email,
            recipient_list=recipient_list,
            html_message=html_message,   # <-- This sends the HTML page!
            fail_silently=False,         # Keep this False while debugging so you catch errors
        )
        # This renders a success confirmation page in the user's browser
        return render(request, 'email_success_status.html') 
        
    except Exception as e:
        return HttpResponse(f"Failed to send email. Error: {e}")