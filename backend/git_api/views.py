from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.response import Response
from django.apps import apps
from git_api import serializers
from git_api.utils.mixins import GitData
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework import status

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
        pull_request = self.get_object()
        pull_request.status = PullRequest.Status.MERGED
        try:
            pull_request.save()
        except:
            return Response(dict(error="Could not merge pull request"),
                                 status=status.HTTP_400_BAD_REQUEST)
        
        return Response(serializer_class(pull_request).data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['patch'])
    def close(self, request,  pk=None):
        pull_request = self.get_object()
        pull_request.status = PullRequest.Status.CLOSE
        try:
            pull_request.save()
        except:
            return Response(dict(error="Could not close pull request"),
                                 status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer_class(pull_request).data, status=status.HTTP_200_OK)


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
