from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.response import Response
from django.apps import apps
from git_api import serializers
from git_api.utils.mixins import GitData
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny

Author = apps.get_model('git_api', 'Author')
PullRequest = apps.get_model('git_api', 'PullRequest')


class AuthorsViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = serializers.AuthorSerializer


class PullRequestsViewSet(ModelViewSet):
    queryset = PullRequest.objects.all()
    serializer_class = serializers.PullRequestSerializer
    permission_classes = [AllowAny, ]

    @action(detail=False, methods=['patch'])
    def merge(self, request,  pk=None):
        breakpoint()

    @action(detail=False, methods=['patch'])
    def close(self, request,  pk=None):
        breakpoint()


class BranchesViewSe(ViewSet, GitData):
    def list(self, request):
        branches = self.get_branches()
        return Response(branches)

    def retrieve(self, request, pk=None):
        branch = self.get_branch(pk)
        return Response(branch)


class CommitsViewSet(ViewSet, GitData):
    def list(self, request):
        commits = self.get_commits()
        return Response(commits)
    
    def retrieve(self, request, pk=None):
        branch = self.get_commit(pk)
        return Response(branch)
