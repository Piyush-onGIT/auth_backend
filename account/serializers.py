from rest_framework import serializers
from account.models import User

class UserRegistrationSerializer(serializers.ModelSerializer):
    # We are writing this bcoz we need confirm password field in our Registration Request
    password2 = serializers.CharField(style={'input_type':'password'}, write_only=True)
    class Meta:
        model = User
        fields=['email', 'name', 'college', 'collegeplace', 'year', 'pnumber', 'password', 'password2']
        extra_kwargs={
            'password':{'write_only':True}
        }

    # Validating Password and Confirm Password While Registration
    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')
        if password != password2:
            raise serializers.ValidationError("Password and Confirm Password does not match")
        return attrs

    def create(self, validate_data):
        return User.objects.create_user(**validate_data)