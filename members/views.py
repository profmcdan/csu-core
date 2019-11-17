from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from rest_framework.decorators import action
from rest_framework import viewsets, mixins, status
from rest_framework.response import Response

from .serializers import DefaultSerializer, UpdateProfileSerializer, ProfileSerializer
from .models import Profile


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = DefaultSerializer
    permission_classes = (IsAuthenticated,)

    def get_serializer_class(self):
        if self.action == 'update_profile':
            return UpdateProfileSerializer
        elif self.action == 'members':
            return ProfileSerializer
        return self.serializer_class

    @action(methods=['GET'], detail=False)
    def members(self, request, pk=None):
        members = Profile.objects.all().order_by('user')
        serializer = self.get_serializer(members, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(methods=['POST'], detail=False)
    def update_profile(self, request, pk=None):
        user = self.request.user
        profile = Profile.objects.filter(user=user).first()
        if profile is None:
            profile = Profile.objects.create(user=user)
            profile.save()
            profile.refresh_from_db()
        serializer = self.get_serializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save(user=user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)
