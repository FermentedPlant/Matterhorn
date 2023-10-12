from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from user.models import CustomUser

# Test basic POST, GET, PUT, DELETE requests
class Test_User_Basic_Request(APITestCase):

    # 'setUp' method will be executed before every test method.
    def setUp(self):
        # Create test admin user
        admin = CustomUser.objects.create_superuser(email = "admin2", password = "admin2", username = "admin2",
                                            first_name = "admin2", last_name = "admin2")
        # Access APIClient for authentication
        client = APIClient()
        # Create test data
        self.data = {
            'email': 'test@email.com',
            'username': 'test',
            'password': 'test_passAa@=./|";', 
            'first_name': 'test_first',
            'last_name': 'test_last'
        }

    # Test POST request (User Creation)
    def test_create_account(self):
        # Authenticate as admin user
        self.client.login(email = 'admin2', password = 'admin2')
        # Map 'url' to path with name 'usercreate' 
        url = reverse('user_api:usercreate')
        # Make a POST request
        response = self.client.post(url, self.data, format='json')
        # Test if POST request has successfully gone through, and returned status HTTP 201 CREATED
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # Test data from 'response' against 'data' dictionary
        self.assertEqual(response.data, self.data)

    # Testing User Retrieve Functionality
    # 'user' & 'data' are used in 'test_retrieve_account()' method as argument 
    # because we want to access both variable from 'test_create_account() method
    def test_retrieve_account(self):
        # Authenticate as admin
        self.client.login(email = 'admin2', password = 'admin2')
        # Create test user
        # '**' takes a dictionary and extracts its contents and passes them as parameters to a function
        user = CustomUser.objects.create(**self.data)
        # Map 'url' to path with name 'userretrieve' 
        # the 'kwargs' is there for setting pk in url 'retrieve/<int:pk>'
        url = reverse('user_api:userretrieve', kwargs={'pk':user.pk})
        # Make a GET request
        response = self.client.get(url, format='json')
        # Test if GET request has successfully gone through, and returned status HTTP 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Test data from 'response' against 'data' dictionary
        self.assertEqual(response.data, self.data)

    def test_update_account(self):
        # Authenticated as admin
        self.client.login(email = 'admin2', password = 'admin2')
        # Assign user data to be updated
        updated_data = {
            'email': 'testV@test.com',
            'username': 'testV',
            'password': 'testV', 
            'first_name': 'testV',
            'last_name': 'testV'
        }
        # Create test user
        # '**' takes a dictionary and extracts its contents and passes them as parameters to a function
        user = CustomUser.objects.create(**self.data)
        # Map 'url' to path with name 'userupdate' 
        url = reverse('user_api:userupdate', kwargs={'pk':user.pk})
        # Make a PUT request with 'updated_data'
        response = self.client.put(url, updated_data, format='json')
        # Retrieve user and assign as updated_user
        updated_user = CustomUser.objects.get(pk = user.pk)
        # Check if PUT request has successfully gone through, and returned status HTTP 200 OK or HTTP 204 NO CONTENT
        self.assertEqual(response.status_code, status.HTTP_200_OK or status.HTTP_204_NO_CONTENT)
        # Test each field of 'response' against 'data' dictionary
        # updated_data["email"] and update_data.get("email") is the same
        self.assertEqual(response.data.get('email'), updated_data['email'])
        self.assertEqual(response.data.get('username'), updated_data['username'])
        self.assertTrue(updated_user.check_password('testV'))
        self.assertEqual(response.data.get('first_name'), updated_data['first_name'])
        self.assertEqual(response.data.get('last_name'), updated_data['last_name'])

    def test_destroy_account(self):
        # Authenticated as admin
        self.client.login(email = 'admin2', password = 'admin2')
        # Create test user 
        # '**' takes a dictionary and extracts its contents and passes them as parameters to a function
        user = CustomUser.objects.create(**self.data)
        # Map 'url' to path with name 'userdelete'
        url = reverse('user_api:userdestroy', kwargs={'pk':user.pk})
        # Make a DELETE request
        response = self.client.delete(url, format='json')
        # Check if DELETE request has successfully gone through, and returned status HTTP 200 OK or HTTP 204 NO CONTENT
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        # Test data from 'response' if it is nonexist
        self.assertIsNone(response.data)
