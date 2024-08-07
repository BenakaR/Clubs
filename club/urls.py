from django.urls import include,path
from .views import *
from .models import *
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

# Serializers define the API representation.
class clubSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Clubs
        fields = ['clubId']
class userSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username']
class userExtSerializer(serializers.HyperlinkedModelSerializer):
    user = userSerializer()
    # userid = serializers.RelatedField(source='User.username',read_only=True)
    class Meta:
        model = UserId
        fields = ['user']
class chatSerializer(serializers.HyperlinkedModelSerializer):
    uid = userExtSerializer()
    cid = serializers.RelatedField(source='chats.cid.clubId', read_only=True)
    # cid = clubSerializer()
    class Meta:
        model = chats
        fields = ['cid','uid','txt']


# ViewSets define the view behavior.
class chatViewSet(viewsets.ModelViewSet):
    queryset = chats.objects.all()
    serializer_class = chatSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'chats', chatViewSet)


urlpatterns = [
    path('temp/',temps,name='temp'),
    path('',login_page,name='login_page'),
    path('logout/',logingout,name='logout'),
    path('login/',loging,name='login'),
    path('home/',home,name='home'),
    path('about/',about,name='about'),
    path('event/',event,name='event'),
    path('chat/',chat,name='chat'),
    path('chatinput/',chatInput,name='chatInput'),
    path('createclub/',createClub,name='createClub'),
    path('submitclub/',submitClub,name='submitClub'),
    path('createuser/',createUser,name='createUser'),
    path('register/',register,name='register'),
    path('apis/',include(router.urls),name='rests'),
    path('api-auth/', include('rest_framework.urls'),name='rest'),
]
