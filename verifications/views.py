from django.shortcuts import render
from datetime import datetime
import pyotp
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.views import APIView
from .models import phoneModel
import base64

# This class return the string needed to generate the key.


class generateKey:
    @staticmethod
    def returnValue(phone):
        return str(phone) + str(datetime.date(datetime.now())) + "Some random Secret Key"


class getPhoneNumberRegistered(APIView):

    # Get to create a call to OTP
    @staticmethod
    def get(request, phone):
        try:
            Mobile = phoneModel.objects.get(Mobile=phone)

        except ObjectDoesNotExist:
            phoneModel.objects.create(Mobile=phone)

        Mobile = phoneModel.objects.get(Mobile=phone)
        Mobile.counter += 1
        Mobile.save()
        keygen = generateKey()
        print(keygen)
        key = base64.b32encode(keygen.returnValue(phone).encode())
        OTP = pyotp.HOTP(key)
        print(OTP.at(Mobile.counter))
        return Response({
            "OTP": OTP.at(Mobile.counter),
            "status": 200
        })

    @staticmethod
    def post(request, phone):
        try:
            Mobile = phoneModel.objects.get(Mobile=phone)
        except ObjectDoesNotExist:
            return Response("user doesn't esxist", status=404)

        keygen = generateKey()
        key = base64.b32encode(keygen.returnValue(
            phone).encode())  # Generating Key
        OTP = pyotp.HOTP(key)  # HOTP Model
        if OTP.verify(request.data["otp"], Mobile.counter):
            Mobile.isVerified = True
            Mobile.save()
            return Response("You are authorised", status=209)
        return Response("OTP is wrong", status=400)


EXPIRY_TIME = 50


class getPhoneNumberRegistered_TimeBased(APIView):

    @staticmethod
    def get(request, phone):
        try:
            Mobile = phoneModel.objects.get(Mobile=phone)
        except ObjectDoesNotExist:
            phoneModel.objects.create(
                Mobile=phone,
            )
        Mobile = phoneModel.objects.get(Mobile=phone)
        Mobile.save()

        keygen = generateKey()
        key = base64.b32encode(keygen.returnValue(phone).encode())
        OTP = pyotp.TOTP(key, interval=EXPIRY_TIME)
        print(OTP.now())
        return Response(
            OTP.now(),
            status=200
        )

    # This Method verifies the OTP
    @staticmethod
    def post(request, phone):
        try:
            Mobile = phoneModel.objects.get(Mobile=phone)
        except ObjectDoesNotExist:
            return Response("User does not exist", status=404)  # False Call

        keygen = generateKey()
        key = base64.b32encode(keygen.returnValue(
            phone).encode())  # Generating Key
        OTP = pyotp.TOTP(key, interval=EXPIRY_TIME)  # TOTP Model
        if OTP.verify(request.data["otp"]):  # Verifying the OTP
            Mobile.isVerified = True
            Mobile.save()
            return Response("You are authorised", status=200)
        return Response("OTP is wrong/expired", status=400)
