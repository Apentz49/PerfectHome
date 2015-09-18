import datetime
from functools import reduce
import operator
from django.contrib.auth import authenticate, login
from django.core.urlresolvers import reverse
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from homes.forms import CustomerCreationForm
from homes.models import Customer, Home, Like, Dislike


def create_user(request):
    """
    Create a Customer and User
    """
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
    """
    View for home page
    """
    model = Home
    template_name = "index.html"
    queryset = Home.objects.all()
    context_object_name = "homelist"
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(HomeList, self).get_context_data(**kwargs)
        context['page_load'] = datetime.datetime.now()
        return context


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
        result = result.exclude(like__isnull=False)
        result = result.exclude(dislike__isnull=False)

        return result


class HomeDetail(DetailView):
    """
    View for a Homes detail page
    """
    model = Home
    pk_url_kwarg = 'home_id'
    template_name = 'single-property-listing.html'


class LikeHomes(ListView):

    model = Home
    context_object_name = 'like_list'
    queryset = Like.objects.all()
    template_name = 'user-overview.html'
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super(LikeHomes, self).get_context_data(**kwargs)
        return context


def home_like(request, home_id):
    user = request.user
    customer = user.customer
    home = Home.objects.get(id=home_id)

    like = Like.objects.create(user=customer, home=home)

    return HttpResponseRedirect(request.META['HTTP_REFERER'])


class DislikeHomes(ListView):

    model = Home
    context_object_name = 'dislike_list'
    queryset = Dislike.objects.all()
    template_name = 'user-overview.html'
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super(DislikeHomes, self).get_context_data(**kwargs)
        return context


def home_dislike(request, home_id):
    user = request.user
    customer = user.customer
    home = Home.objects.get(id=home_id)

    like = Dislike.objects.create(user=customer, home=home)

    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def profile_view(request, user_id):
    user = request.user
    customer = user.customer
    like_list = Like.objects.all()
    dislike_list = Dislike.objects.all()

    return render(request, 'user-overview.html', {'like_list': like_list,
                                                  'dislike_list':
                                                      dislike_list})


def profile_view_likes(request, user_id):
    user = request.user
    customer = user.customer
    like_list = Like.objects.all()

    return render(request, 'user-account-like.html', {'like_list': like_list})


def profile_view_dislikes(request, user_id):
    user = request.user
    customer = user.customer
    dislike_list = Dislike.objects.all()

    return render(request, 'user-account-dislike.html',
                  {'dislike_list': dislike_list})
