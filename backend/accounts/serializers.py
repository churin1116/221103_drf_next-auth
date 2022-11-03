from rest_framework.serializers import ModelSerializer
from .models import CustomUser


class UserSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["userId", "username", "email", "image_url", "password",]

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            validated_data["username"],
            validated_data["email"],
            validated_data["password"]
        )
        return user


# グーグル認証時にフロントからのAPI経由でデータベースにも登録するため追加
# https://qiita.com/cokemaniaIIDX/items/38a30ff881bca1b4b0ad
class RegisterUserSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['userId', 'username', 'email', 'image_url']
    
    def create(self, validated_data):
        request_data = validated_data
        return CustomUser.objects.create_user(request_data)