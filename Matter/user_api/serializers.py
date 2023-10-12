from rest_framework import serializers
from user.models import CustomUser

# Serialize account POST, GET, RETRIEVE, DESTROY request
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email', 'username', 'password', 'first_name', 'last_name']

    # update() in Serializer deals more with validating user info before saving it to database
    def update(self, instance, validated_data):
        # Call the parent class's update method first
        # It's generally a good practice to call it at the beginning of the custom update method 
        # to ensure that any necessary parent class logic is executed before any additional custom logic.
        instance = super().update(instance, validated_data)

        # Get newly entered password from 'validate_data' and set it to 'new_password'
        new_password = validated_data.get('password')
        
        if new_password:
            # set_password() automatically hash the password 
            instance.set_password(new_password)
            instance.save()

        return instance
