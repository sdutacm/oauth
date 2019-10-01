from rest_framework import serializers

from .models import UserEdu, UserInfo, UserPriv, UserSocial


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = ("userid", "user_name", "nick_name", "image")


class UserPrivSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPriv
        fields = ("email", "tel", "birthday")


class UserEduSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserEdu
        fields = (
            "verified",
            "student_no",
            "school",
            "college",
            "major",
            "grade",
            "clazz",
        )


class UserSocialSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSocial
        fields = ("site",)
