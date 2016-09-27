from django.shortcuts import render, redirect
from forms import EnquiryForm
from django.core.urlresolvers import reverse
from django.core.mail import send_mail
from datetime import datetime


def load_form(request):
    if request.method == 'POST':
        form = EnquiryForm(request.POST)
        if form.is_valid():
            if form.cleaned_data.get('wedding_date') is None:
                date = 'No date given'
            else:
                date = datetime.strftime(form.cleaned_data.get('wedding_date'), '%d/%m/%Y')
            message = \
                'Name: \n{name}\n\n' \
                'Email: \n{email}\n\n' \
                'Phone: \n{phone}\n\n' \
                'Date: \n{date}\n\n' \
                'Venue: \n{venue}\n\n' \
                'Comments: \n{comment}'.format(
                    name='%s %s' % (form.cleaned_data.get('first_name'), form.cleaned_data.get('last_name')),
                    email=form.cleaned_data.get('email_contact'),
                    phone=form.cleaned_data.get('phone_contact'),
                    date=date,
                    venue=form.cleaned_data.get('venue'),
                    comment=form.cleaned_data.get('comments').encode('ascii', 'ignore')
                )
            form.save()
            send_mail(subject='Wedding Enquiry',
                      message=message,
                      from_email='info@johnsutcliffe.com.au',
                      recipient_list=['ravelnze@icloud.com'  # change this to info@johnsutcliffe.com.au
                                      ])
            return redirect(reverse('contact:complete'))
    else:
        form = EnquiryForm()

    context = {'form': form}
    return render(request, 'contact.html', context)


def complete_form(request):
    return render(request, 'complete.html')
