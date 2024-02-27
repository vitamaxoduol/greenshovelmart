from django.shortcuts import render
from django.views import View

class ThankYouView(View):
    def get(self, request):
        return render(request, 'thank_you.html')