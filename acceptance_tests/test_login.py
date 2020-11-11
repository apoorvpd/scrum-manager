from django.test import TestCase
from django.test import Client
from tracker_app.models import ScrumManager, Project

class TestTracker(TestCase):
    # Load the test database with records to support your test.
    def setUp(self):
        self.client = Client()
        self.user1 = ScrumManager.objects.create(username='apoorv', password='apoorv@123')
        self.project1 = Project.objects.create(name='monitor', priority='Low', scrum_manager=self.user1)




    # Write a system test using client that makes sure on an unsuccessful login the home page is redisplayed.
    def test_invalid_login(self):
        response = self.client.post('/', {'username': 'apoorv', 'password': 'password@123'})
        # print(response.context['error_messages'])
        self.assertEqual(response.context['error'], 'username/password incorrect')

    # Write a system test using client that makes sure that on a successful login the correct scrum manager's project list is displayed.
    def test_valid_login(self):
        response = self.client.post('/', {'username': 'apoorv', 'password': 'apoorv@123'})
        self.assertEqual(response.url, '/projects/')
        response2 = self.client.get('/projects/')
        # print(response2.context['things'])
        projects = list(response2.context['projects'])
        print(projects)
        for project in projects:
            self.assertEqual(project.name, self.project1.name)
            self.assertEqual(project.priority, self.project1.priority)

