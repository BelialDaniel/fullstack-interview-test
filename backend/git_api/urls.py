from git_api import views
from rest_framework.routers import DefaultRouter

app_name = 'git_api'

router = DefaultRouter(trailing_slash=False)
router.register(r'pull_requests', views.PullRequestsViewSet, basename="pullrequests")
router.register(r'branches', views.BranchesViewSe, basename="branches")
router.register(r'commits', views.CommitsViewSet, basename="commits")

urlpatterns = [] + router.urls