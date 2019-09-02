from django.core.files.storage import FileSystemStorage
from django.db import IntegrityError
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, generics, status
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework_jwt.settings import api_settings
from rest_framework.permissions import IsAuthenticated
import base64
import os
import errno
from twilio.rest import Client
from django.utils import timezone
from django.shortcuts import render

image_root = os.path.join(settings.MEDIA_ROOT, 'avatars/user/')

def index(request):
    return render(request, 'index.html', )

def generate_token(user):
    jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
    jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
    payload = jwt_payload_handler(user)
    return jwt_encode_handler(payload)


class Signup(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = (JSONWebTokenAuthentication,)

    def post(self, request, format=None):
        if request.data.get('email') is not None:
            request.data['email'] = request.data['email'].lower()
        else:
            return Response({"errors": "email field is required"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            User.objects.get(email=request.data['email'])
            return Response({"error": "A user with that email address already exists"}, status=status.HTTP_409_CONFLICT)
        except User.DoesNotExist:
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():

                user = serializer.save()
                user.password_unhashed = request.data['password']
                user.save()
                token = generate_token(user)
                return Response({"token": token, "id": user.id}, status=status.HTTP_201_CREATED)
            return Response({"errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class Profile(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    exclude = 'mobile'
    permission_classes = (IsAuthenticated,)

    def retrieve(self, request, pk=None):
        if request.user:
            serializer = self.get_serializer_class()(request.user)
            return Response(serializer.data)
        return super(Profile, self).retrieve(request, pk)

    def update(self, request, pk=None):
        if request.user:
            serializer = self.get_serializer_class()(
                request.user, request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return super(Profile, self).retrieve(request, pk)


def get_image_name(id, ext):
    from django.utils import timezone
    time = str(timezone.now())
    time = "{}{}".format(time.split('.')[0], time.split('.')[1])
    time = "{}{}".format(time.split(' ')[0], time.split(' ')[1])
    time = time.replace(":", "")
    time = time.replace("+", "")
    return "{}-{}.{}".format(id, time, ext)


class UpdateProfileImage(APIView):
    permission_classes = (IsAuthenticated,)

    def put(self, request, format=None):
        data = request.data.get("avatar")
        if not data is None:
            try:
                format, imgstr = data.split(';base64,')
                ext = format.split('/')[-1]
                imgdata = base64.b64decode(imgstr)
                user = request.user

                image_name = get_image_name(user.id, ext)
                image_path = "/media/avatars/user/{}".format(image_name)
                user = request.user
                image_path_to_delete = "{}{}".format(
                    settings.STATIC_ROOT, user.avatar)
                user.avatar = image_path
                filename = "{}{}".format(str(image_root), image_name)
                    # str(self.request.user.id) + str(timezone.now().date) + '.' + ext
                if not os.path.exists(os.path.dirname(filename)):
                    try:
                        os.makedirs(os.path.dirname(filename))
                    except OSError as exc:  # Guard against race condition
                        if exc.errno != errno.EEXIST:
                            raise Response(str(exc))
                with open(filename, 'wb') as f:
                    try:
                        f.write(imgdata)
                    except Exception as e:
                        raise Response(str(e))
            except Exception as e:
                return Response(str(e))
            # try:
            #     os.remove(image_path_to_delete)
            # except:
            #     pass
            user.save()
            return Response({"Image updated successfully"}, status=status.HTTP_200_OK)
        return Response({"detail": "Avatar field is required!"}, status=status.HTTP_400_BAD_REQUEST)


class GetProfileById(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk, format=None):
        if self.request.user:
            try:
                user = User.objects.get(id=pk)
            except User.DoesNotExist:
                return Response({"detail": "User doesn't exist"})
            serializer = UserSerializer(user)
            return Response(serializer.data)
        else:
            return Response({"detail": "You have no access to this page"}, status=status.HTTP_400_BAD_REQUEST)


class Password(APIView):
    def post(self, request, format=None):
        user = request.user
        serializer = ChangePasswordSerializer(data=request.data)
        if serializer.is_valid():
            if not user.check_password(serializer.data.get("old_password")):
                return Response({"old_password": "wrong password."}, status=status.HTTP_400_BAD_REQUEST)
            user.password_unhashed = request.data["new_password"]
            user.set_password(serializer.data.get("new_password"))
            user.save()
            return Response("Success.", status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ImageUpdate(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, format=None):
        image_file = request.FILES['avatar']
        fs = FileSystemStorage()
        filename = fs.save('avatars/user/{}.jpg'.format(image_file.name), image_file)
        uploaded_file_url = fs.url(filename)
        request.user.avatar = uploaded_file_url
        request.user.save()
        return Response({"file":uploaded_file_url})

class Verification(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = (JSONWebTokenAuthentication,)
    def post(self, request, format=None):
        account_sid = 'ACa8834f463787bf31a6aad422500af769'
        auth_token = '843986ef37b1d681ddda4a5fa442c0f4'
        client = Client(account_sid, auth_token)

        verification = client.verify \
                            .services('VAc3b5d947d496668820515354c45f7a5b') \
                            .verifications \
                            .create(to=request.data.get('mobile'), channel='sms')

        print(verification.status)
        return Response({"sms_status":verification.status})

class CheckVerificationCode(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = (JSONWebTokenAuthentication,)
    def post(self, request, format=None):
        account_sid = 'ACa8834f463787bf31a6aad422500af769'
        auth_token = '843986ef37b1d681ddda4a5fa442c0f4'
        client = Client(account_sid, auth_token)

        verification = client.verify \
                            .services('VAc3b5d947d496668820515354c45f7a5b') \
                           .verification_checks \
                           .create(to=request.data.get('mobile'), code=request.data.get('code'))

        print(verification.status)
        return Response({"status":verification.status})
        