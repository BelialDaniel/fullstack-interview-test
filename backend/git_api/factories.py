import factory
from django.apps import apps

Author = apps.get_model('git_api', 'Author')
PullRequest = apps.get_model('git_api', 'PullRequest') 


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Author
    
    name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    email = factory.LazyAttribute(
        lambda object: '{}.{}@example.com'.format(object.name,
                                                  object.last_name).lower())


class PullRequestFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = PullRequest

    author = factory.SubFactory(UserFactory)
    title = factory.Faker('text', max_nb_chars=25)
    description = factory.Faker('paragraph', nb_sentences=2)
    status = PullRequest.Status.OPEN
    from_branch = factory.Faker('uuid4')
    to_branch = factory.Faker('uuid4')