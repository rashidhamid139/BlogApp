from django.shortcuts import render

# Create your views here.
from .models import RemoteAPIAccount


def refresh_token():
    #get token from token api
    new_token = ""
    new_token_expires_time = ""

    RemoteAPIAccount(
        id=1,
        defaults= {
            "access_token": new_token,
            "access_token_expires": new_token_expires_time
        }
    )