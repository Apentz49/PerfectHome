import datetime
from functools import reduce
import operator
from django.contrib.auth import authenticate, login
from django.core.urlresolvers import reverse
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.views.generic import ListView, DetailView
from homes.forms import CustomerCreationForm, HomeSearchForm
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
    context_object_name = "homelist"
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(HomeList, self).get_context_data(**kwargs)
        context['page_load'] = datetime.datetime.now()
        return context


# def home_search(request):
#     if request.method == 'GET':
#         results = Home.objects.all()
#
#         search = request.GET.get('search', None)
#         if search:
#             results = results.filter(Q(zipcode=search)|Q(bedrooms=search)|Q(bathrooms=search)|Q(min_price=search))
#
#         bathrooms = request.GET.get('bathrooms', None)
#         if bathrooms:
#             results = results.filter(bathrooms=bathrooms)
#
#         bedrooms = request.GET.get('bedrooms', None)
#         if bedrooms:
#             results = results.filter(bedrooms=bedrooms)
#
#         return render_to_response('property-listing.html', {'form': HomeSearchForm(request.GET), 'home': results})
#
#     return render_to_response('property-listing.html', {'form': HomeSearchForm()})


class HomeSearchListView(ListView):
    """
    Display a Home List page filtered by the search query.
    """
    paginate_by = 12
    model = Home
    context_object_name = "homesearch"

    def get_context_data(self, **kwargs):
        context = super(HomeSearchListView, self).get_context_data(**kwargs)
        q = self.request.GET.get('q')
        context['search'] = q
        return context

    def get_queryset(self):
        result = super(HomeSearchListView, self).get_queryset()

        query = self.request.GET.get('q')
        if query:
            query_list = query.split()
            result = result.filter(
                reduce(operator.and_,
                       (Q(zipcode__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                       (Q(city__icontains=q) for q in query_list))
            )

        return result


# class SearchList(ListView):
#     model = Home
#     template_name = "property-listing.html"
#     queryset = Home.objects.all()
#     context_object_name = "searchlist"
#     paginate_by = 12
#
#     def get_context_data(self, **kwargs):
#         context = super(SearchList, self).get_context_data(**kwargs)
#         context['page_load'] = datetime.datetime.now()
#         return context

class HomeDetail(DetailView):
    model = Home
    pk_url_kwarg = 'home_id'
    template_name = 'single-property-listing.html'
