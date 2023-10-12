from django.test import TestCase
from rest_framework.test import APITestCase
from user.models import CustomUser

class Test_CustomUser_Model(APITestCase):
    def test_calling_user(self):
        user = CustomUser.objects.create_user(email = "testuser", username = "user_first", password = "user_last",
                                            first_name = "Cronen", last_name = "berg")
        self.assertEqual(str(user), user.username)