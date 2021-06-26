from django.test import TestCase
from git_api.factories import PullRequestFactory
from django.test import Client
from django.apps import apps


PullRequest = apps.get_model('git_api', 'PullRequest') 


# Create your tests here.
class GitApiTests(TestCase):
    """
    """
    client = None
    pull_request_data = dict()

    def setUp(self):
        self.client = Client()
        self.pull_request_data = dict(
            author=dict(
                name="Daniel",
                last_name="Morales",
                email="mail@email.com"
            ),
            title="Title",
            description="Description",
            from_branch="",
            to_branch=""
        )

    def test_create_pull_request(self):
        title = "Pull Request Test"
        from_branch = 'dm-branch-test'
        to_branch = 'master-test'

        pull_request_data = self.pull_request_data
        pull_request_data.update(dict(title=title))
        pull_request_data.update(dict(from_branch=from_branch))
        pull_request_data.update(dict(to_branch=to_branch))
        response = self.client.post('/git_api/pull_requests', 
                                 data=pull_request_data,
                                 content_type='application/json')
        
        pull_request = PullRequest.objects.first()
        self.assertEqual(response.status_code, 201)
        self.assertIsNotNone(pull_request)
        self.assertEqual(pull_request.title, title)
        self.assertEqual(pull_request.from_branch, from_branch)
        self.assertEqual(pull_request.to_branch, to_branch)
        self.assertEqual(pull_request.status, PullRequest.Status.OPEN)

    def test_merge_pull_request(self):
        pull_request = PullRequestFactory.create()
        response = self.client.patch(f'/git_api/pull_requests/{pull_request.id}/merge',
                                     data={},
                                     content_type='application/json')


        ull_request_db = PullRequest.objects.get(id=pull_request.id)
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(ull_request_db)
        self.assertEqual(pull_request.status, PullRequest.Status.OPEN)
        self.assertEqual(ull_request_db.status, PullRequest.Status.MERGED)
    
    def test_close_pull_request(self):
        pull_request = PullRequestFactory.create()
        response = self.client.patch(f'/git_api/pull_requests/{pull_request.id}/close',
                                     data={},
                                     content_type='application/json')


        ull_request_db = PullRequest.objects.get(id=pull_request.id)
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(ull_request_db)
        self.assertEqual(pull_request.status, PullRequest.Status.OPEN)
        self.assertEqual(ull_request_db.status, PullRequest.Status.CLOSE)
    
    def test_unable_to_create_requests_with_same_branches(self):
        from_branch = "dm-branch-test"
        to_branch = "master-test"
        PullRequestFactory.create(from_branch=from_branch,
                                  to_branch=to_branch)

        pull_request_data = self.pull_request_data
        pull_request_data.update(dict(from_branch=from_branch))
        pull_request_data.update(dict(to_branch=to_branch))

        response = self.client.post(f'/git_api/pull_requests',
                                     data=pull_request_data,
                                     content_type='application/json')

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json().get('non_field_errors')[0],
                         "The fields from_branch, to_branch must make a unique set.")

