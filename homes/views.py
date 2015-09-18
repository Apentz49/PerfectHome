import datetime
from functools import reduce
import operator
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
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
        """
        This will generate the query_set from the search fields
        """
        result = super(HomeSearchListView, self).get_queryset()

        q = self.request.GET.get('q')
        pmin = self.request.GET.get('pmin')
        pmax = self.request.GET.get('pmax')
        bed = self.request.GET.get('bed')
        bath = self.request.GET.get('bath')

        query_list = q.split()

        if q:
            if not (((pmin or pmax) or bed) or bath):
                result = result.filter(
                    reduce(operator.and_,
                           (Q(zipcode__icontains=q) for q in query_list)) |
                    reduce(operator.and_,
                           (Q(city__icontains=q) for q in query_list)) |
                    reduce(operator.and_,
                           (Q(state__icontains=q) for q in query_list))
                )
        if (q and pmin)and pmax:
            if not (bed or bath):
                result = result.filter(
                    reduce(operator.and_,
                           (Q(zipcode__icontains=q) for q in query_list)) |
                    reduce(operator.and_,
                           (Q(city__icontains=q) for q in query_list)) |
                    reduce(operator.and_,
                           (Q(state__icontains=q) for q in query_list)),
                    Q(price__gte=pmin, price__lte=pmax)
                )
        if q and pmax:
            if not ((pmin and bed)and bath):
                result = result.filter(
                    reduce(operator.and_,
                           (Q(zipcode__icontains=q) for q in query_list)) |
                    reduce(operator.and_,
                           (Q(city__icontains=q) for q in query_list)) |
                    reduce(operator.and_,
                           (Q(state__icontains=q) for q in query_list)),
                    Q(price__lte=pmax)
                )
        if (((q and pmin)and pmax)and bed)and bath:
                result = result.filter(
                    reduce(operator.and_,
                           (Q(zipcode__icontains=q) for q in query_list)) |
                    reduce(operator.and_,
                           (Q(city__icontains=q) for q in query_list)) |
                    reduce(operator.and_,
                           (Q(state__icontains=q) for q in query_list)),
                    Q(price__gte=pmin, price__lte=pmax,
                      bedrooms__icontains=bed, bathrooms__icontains=bath)
                )

        result = result.filter(like__isnull=True)
        result = result.filter(dislike__isnull=True)

        return result


class HomeDetail(DetailView):
    """
    View for a Homes detail page
    """
    model = Home
    pk_url_kwarg = 'home_id'
    template_name = 'single-property-listing.html'


class LikeHomes(ListView):
    """
    View for the Likes List
    """
    model = Home
    context_object_name = 'like_list'
    queryset = Like.objects.all()
    template_name = 'user-overview.html'
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super(LikeHomes, self).get_context_data(**kwargs)
        return context


@login_required
def home_like(request, home_id):
    # This creates a Like on a Home #
    user = request.user
    customer = user.customer
    home = Home.objects.get(id=home_id)

    like = Like.objects.create(user=customer, home=home)

    return HttpResponseRedirect(request.META['HTTP_REFERER'])


class DislikeHomes(ListView):
    """
    View for Dislike list
    """
    model = Home
    context_object_name = 'dislike_list'
    queryset = Dislike.objects.all()
    template_name = 'user-overview.html'
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super(DislikeHomes, self).get_context_data(**kwargs)
        return context


@login_required
def home_dislike(request, home_id):
    # Create a Dislike on a Home #
    user = request.user
    customer = user.customer
    home = Home.objects.get(id=home_id)

    like = Dislike.objects.create(user=customer, home=home)

    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def profile_view(request, user_id):
    # View to display both Like and Dislike Homes on the profile #
    user = request.user
    customer = user.customer
    like_list = Like.objects.filter(user=customer).order_by('home').reverse()
    dislike_list = Dislike.objects.filter(
        user=customer).order_by('home').reverse()

    return render(request, 'user-overview.html', {'like_list': like_list,
                                                  'dislike_list':
                                                      dislike_list})


@login_required
def profile_view_likes(request, user_id):
    # View to display Like Homes in profile Like tab #
    user = request.user
    customer = user.customer
    like_list = Like.objects.filter(user=customer).order_by('home').reverse()

    return render(request, 'user-account-like.html', {'like_list': like_list})


@login_required
def profile_view_dislikes(request, user_id):
    # View to display Dislike Homes in profile Dislike tab #
    user = request.user
    customer = user.customer
    dislike_list = Dislike.objects.filter(
        user=customer).order_by('home').reverse()

    return render(request, 'user-account-dislike.html',
                  {'dislike_list': dislike_list})
