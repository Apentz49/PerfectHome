import datetime
from django.contrib.auth import authenticate, login
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from homes.forms import CustomerCreationForm
from homes.models import Customer, Home


def create_user(request):
    if request.method == "POST":
        form = CustomerCreationForm(data=request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = form.save()
            customer = Customer()
            customer.user = user
            customer.first_name = data['first_name']
            customer.last_name = data['last_name']
            customer.email = data['email']
            customer.save()
            user = authenticate(username=request.POST['username'],
                                password=request.POST['password1'])
            login(request, user)

            return HttpResponseRedirect(reverse('index'))

    else:
        form = CustomerCreationForm()

    return render(request, 'index.html',
                  {'form': form})


class HomeList(ListView):
    model = Home
    template_name = "index.html"
    queryset = Home.objects.all()
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(HomeList, self).get_context_data(**kwargs)
        context['page_load'] = datetime.datetime.now()
        return context


class HomeDetail(DetailView):
    model = Home
    pk_url_kwarg = 'home_id'
    template_name = 'homedetail.html'
