from rest_framework import routers
from django.urls import include, path
from .views import VoteViewSet, IdeaViewSet, IdeaList, VoteList, IdeaDetail, VoteDetail


router = routers.DefaultRouter()
router.register(r'ideas', IdeaViewSet)
router.register(r'votes', VoteViewSet)



urlpatterns = [

    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rf')),
    path('ideas', IdeaList.as_view()),
    path('<int:pk>', IdeaDetail.as_view()),
    path('votes', VoteList.as_view()),
    path('<int:pk>', VoteDetail.as_view())
]

