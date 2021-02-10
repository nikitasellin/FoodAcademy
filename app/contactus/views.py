from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from .models import Message


class ContactUsView(CreateView):
    model = Message
    fields = \
        'first_name', 'last_name', 'email', 'phone_number', 'title', 'text'
    success_url = reverse_lazy('contactus:send_message_result')

    def form_valid(self, form):
        message = form.save(commit=False)
        message.send_emails()
        return super().form_valid(form)


class SendMessageResultView(TemplateView):
    template_name = 'contactus/send_message_result.html'
