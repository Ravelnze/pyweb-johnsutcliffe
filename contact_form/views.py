from django.shortcuts import render, redirect
from forms import EnquiryForm
from django.core.urlresolvers import reverse


def load_form(request):
    if request.method == 'POST':
        form = EnquiryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('contact:complete'))
    else:
        form = EnquiryForm()

    context = {'form': form}
    return render(request, 'contact.html', context)


def complete_form(request):
    return render(request, 'complete.html')
