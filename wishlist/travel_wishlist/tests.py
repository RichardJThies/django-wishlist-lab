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

class TestVisitedPlaces(TestCase):#look at wishlist.html vs visited.html, their empty list messages illuminate why the cities are placed where they are
    #arrange?
    fixtures = ['test_places']
    
    def test_visited_contains_only_visited_places_(self):
        #act?
        response = self.client.get(reverse('places_visited'))
        #assert?
        self.assertTemplateUsed(response, 'travel_wishlist/visited.html')#correct template again?
        self.assertContains(response, 'San Francisco')
        self.assertContains(response, 'Moab')
        self.assertNotContains(response, 'Tokyo')
        self.assertNotContains(response, 'New York')

class TestAddNewPlace(TestCase):#how would the 3 As work here?
    def test_add_new_unvisited_place(self):
        add_place_url = reverse('place_list')#figuring out the urls? place_list uses POST to add new places as GET to display places
        new_place_data = {'name': 'Tokyo', 'visited': False}

        response = self.client.post(add_place_url, new_place_data, follow=True)#make request to add place/create data. 
                                #^^follow=True is because POST is really 2 requests, data is saved , then a redirect to homepage.follow=True ensures the 2nd request is followed, which is not the default behavior^^

        self.assertTemplateUsed(response, 'travel_wishlist/wishlist.html') 
        response_places = response.context['places']#from views.py, pull out the places value from dictionary. Allows examination of the data being sent to template
        self.assertEqual(1, len(response_places))#ensure only 1 places is added to empty (test?) db
        tokyo_from_response = response_places[0]#element 0, of a list of places from the response

        tokyo_from_db = Place.objects.get(name="Tokyo", visited=False)#pull out that 1 added place
        self.assertEqual(tokyo_from_db, tokyo_from_response)

class TestVisitPlace(TestCase):#testing db is updating correctly after requests to visit Places
    fixtures = ['test_places']

    def test_visit_place(self):
        visit_place_url = reverse('place_was_visited', args=(2, ))#reverse can have more than 1 argument. args is a tuple of data, turns into data for url placeholder, pk 2 in this case
        response = self.client.post(visit_place_url, follow=True)#make request to add place/create data, alhtough not sending data here, it's in the url already 

        self.assertTemplateUsed(response, 'travel_wishlist/wishlist.html')#use /visited instead to redirect if testing for visited data

        self.assertNotContains(response, 'New York')#ensures pk 2 (New York) is not there. If testing /visited, reverse Contains and NotContains
        self.assertContains(response, 'Tokyo')

        new_york = Place.objects.get(pk=2)#pulling NY out of db using the pk
        self.assertTrue(new_york.visited)#is YK visited?










