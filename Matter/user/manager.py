from django.contrib.auth.base_user import BaseUserManager

# Set custom manager for custom user
class CustomUserManager(BaseUserManager): 

    # Create user
    def create_user(self, email, username, password, first_name, last_name, **extra_fields):

        # Return the value of is_staff, is_active, and is_superuser,
        # If the values are not set then set the values of is_staff, is_active, and is_superuser 
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        extra_fields.setdefault("is_active", True)

        return self._create_user(email, username, password, first_name, last_name, **extra_fields)
        
    # Create superuser
    def create_superuser(self, username, email, first_name, last_name, password, **extra_fields):

        # Return the value of is_staff, is_active, is_superuser, and balance
        # If the values are not set then set the values of is_staff, is_active, is_superuser, and balance 
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        # Set balance to Null for superuser 
        extra_fields.setdefault("balance", None)            


        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must be a staff")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must be a superuser")
        
        return self._create_user(email, username, password, first_name, last_name, **extra_fields)

        
    # Set base user creation logic
    def _create_user(self, username, email, first_name, last_name, password, **extra_fields):

        if not email:
            raise ValueError("The given username must be set")

        # 'self' is used in order to call sibling method from another sibling method of the same class
        # ---EXAMPLE---
        # class student()
        #    def calculate():
        #       count()
        #    def study():
        #       self.calculate()
        # --------
        email = self.normalize_email(email)

        # Create an instance of a model
        # 'self.model' refers to the model class, the CustomUser [https://stackoverflow.com/questions/51163088/self-model-in-django-custom-usermanager]
        user = self.model(email=email, username=username, first_name=first_name, last_name=last_name, **extra_fields)
        user.set_password(password)
        user.save()

        return user
