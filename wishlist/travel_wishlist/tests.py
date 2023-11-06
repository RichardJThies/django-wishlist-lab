from django.test import TestCase#fjango has special extention to help test web apps
from django.urls import reverse#looks up urls/requests from the names of those urls/requests
from .models import Place#testing db, so need to import the model

# Create your tests here.

class TestHomePage(TestCase):#django will create a test db automatically for each test, and destroy it after each test?
    def test_home_page_shows_empty_list_message_for_empty_db(self):#self is the TestCase?
        #arrange?
        home_page_url = reverse('place_list')#reverse allows using the name of the path to turn the path into a usable url
        #act?
        response = self.client.get(home_page_url)#making request, and saving it in the response variable. TestCase (self) has a client, the client makes the request to web app server using the reversed url
        #assert?
        self.assertTemplateUsed(response, 'travel_wishlist/wishlist.html')#compare response to excpected template
        self.assertContains(response, 'You have no places in your wishlist')#django test: compare response to content on page








