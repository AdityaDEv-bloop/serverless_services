import json

from django.contrib.auth.hashers import check_password
from django.forms.models import model_to_dict
from rest_framework_simplejwt.tokens import RefreshToken

from easyship.models import Account, Member


def get_tokens_for_user(user: Account):
    refresh = RefreshToken.for_user(user)
    members = Member.objects.filter(user=user).all()
    membersdata = []
    for member in members:
        data = {
            "id": member.id,
            "ref": member.ref,
            "bankdetails": {
                "id": member.bankdetails.id,
                "bankname": member.bankdetails.bankname,
                "accountno": member.bankdetails.accountno,
                "ifsccode": member.bankdetails.ifsccode,
                "branchname": member.bankdetails.branchname,
            },
            "companyname": member.companyname,
        }
        membersdata.append(data)
    return {
        "refresh": str(refresh),
        "access": str(refresh.access_token),
        "user": {
            "id": user.id,
            "email": user.email,
        },
        "members": membersdata,
    }


def ValidateUser(Email=None, Password=None):
    try:
        UserPass = Account.objects.filter(email=Email).values("password")[0]["password"]
        isPassCheck = check_password(Password, UserPass)
        if isPassCheck:
            Account.objects.filter(email=Email).update(is_active=True)
            UserObj = Account.objects.get(email=Email)
            return UserObj
    except:
        return None


def get_User(user):
    try:
        UserObject = Account.objects.get(email=user)
        return UserObject
    except:
        return None
