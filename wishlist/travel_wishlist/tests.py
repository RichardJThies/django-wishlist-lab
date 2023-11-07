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
        self.assertTemplateUsed(response, 'travel_wishlist/wishlist.html')#compare response to expected template
        self.assertContains(response, 'You have no places in your wishlist')#django test: compare response to content on page

class TestWishlist(TestCase):#seperate test case for testing a populated db using fixtures dir
    #arrange?
    fixtures = ['test_places']#fixtures is the default django TestCase directory. Contains populated db

    def test_wishlist_contains_not_visited_places(self):
        #act?
        response = self.client.get(reverse('place_list'))#way of combining home_page_url = reverse('place_list') & response = self.client.get(home_page_url) statements
        #assert?
        self.assertTemplateUsed(response, 'travel_wishlist/wishlist.html')#still the correct template?
        self.assertContains(response, 'Tokyo')#not visited in test_places
        self.assertContains(response, 'New York')#not visited in test_places
        self.assertNotContains(response, 'San Francisco')#visited in test_places
        self.assertNotContains(response, 'Moab')#visited in test_places

class TestVisited(TestCase):#seperate test case that is very similar to to TestHomePage 
    def test_visited_page_shows_empty_list_message_for_empty_db(self):#Is this testing the real db? The real db doesn't have empty msg here that would allow this to be true?
        #arrange?
        visited_url = reverse('places_visited')#reverse the visited page 
        #act?
        response = self.client.get(visited_url)
        # response = self.client.get(reverse('places_visited'))#alternative combined syntax
        #assert?
        self.assertTemplateUsed(response, 'travel_wishlist/visited.html')#compare response to expected template
        self.assertContains(response, 'You have not visited any places yet')#django test: compare response to content on page

class TestVisitedPlaces(TestCase):#not quite sure if I understand this one, and how it works compared to TestWishlist
    fixtures = ['test_places']
    
    def test_visited_contains_only_visited_places_(self):
        response = self.client.get(reverse('places_visited'))
        self.assertTemplateUsed(response, 'travel_wishlist/visited.html')#correct template again?
        self.assertContains(response, 'San Francisco')#how would you change test_places so this can be true? edit fixtures?
        self.assertContains(response, 'Moab')
        self.assertNotContains(response, 'Tokyo')
        self.assertNotContains(response, 'New York')









