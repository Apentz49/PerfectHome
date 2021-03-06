from django.db import models
from django.contrib.auth.models import User


class Home(models.Model):
    """
    model for creating a Home object.

    """
    address = models.CharField(max_length=150)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=20)
    zipcode = models.CharField(max_length=10)
    bedrooms = models.CharField(max_length=50, null=True, blank=True)
    bathrooms = models.CharField(max_length=100)
    sqft = models.CharField(max_length=12, null=True, blank=True)
    lot_size = models.CharField(max_length=50, blank=True)
    year_built = models.CharField(max_length=5, null=True, blank=True)
    price = models.CharField(max_length=50, null=True)
    price_per_sqft = models.CharField(max_length=10, null=True, blank=True)
    img = models.CharField(max_length=500, null=True, blank=True)
    user = models.ManyToManyField(User)

    def __str__(self):
        return ("Address:{}, City: {}, State {}, Zipcode {},"
                "Bedrooms: {}, Bathrooms: {}, Sqft: {}, "
                "Lot Size: {}, Year Built: {}, Price: {}, "
                "Price Per Sqft: {}, Img: {}".format(self.address, self.city,
                                                     self.state, self.zipcode,
                                                     self.bedrooms,
                                                     self.bathrooms, self.sqft,
                                                     self.lot_size,
                                                     self.year_built,
                                                     self.price,
                                                     self.price_per_sqft,
                                                     self.img))


class Customer(models.Model):
    """
    model for creating a Customer/User object

    """
    user = models.OneToOneField(User)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return ("User: {}, "
                "First Name: {}, "
                "Last Name: {}, "
                "Email: {}".format(self.user, self.first_name,
                                   self.last_name, self.email))


class Like(models.Model):
    """
    model for creating a liked Home by a User

    """
    user = models.ForeignKey(Customer)
    home = models.ForeignKey(Home)

    def __str__(self):
        return "User: {} Home: {}".format(self.user, self.home)


class Dislike(models.Model):
    """
    model for creating a disliked Home by a User

    """
    user = models.ForeignKey(Customer)
    home = models.ForeignKey(Home)

    def __str__(self):
        return "User: {}, Home: {}".format(self.user, self.home)
