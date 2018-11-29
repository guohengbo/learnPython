#https://blog.csdn.net/c__chao/article/details/78573737
from locust import HttpLocust, TaskSet, task

class WebsiteTasks(TaskSet):
    # def on_start(self):
    #     self.client.get("/login?key=00d91e8e0cca2b76f515926a36db68f5&phone=13594347817&passwd=123456")
    @task(2)
    def login(self):
        self.client.get("/login?key=00d91e8e0cca2b76f515926a36db68f5&phone=13594347817&passwd=123456")
    @task(2)
    def EmailSearch(self):
        self.client.get("/EmailSearch?number=1012002")
    @task(1)
    def recommendPoetry(self):
        self.client.get("/recommendPoetry")
    @task(3)
    def searchAuthors(self):
        self.client.get("/searchAuthors?name=李白")
    @task(5)
    def musicRankings(self):
        self.client.get("/musicRankings")

class WebsiteUser(HttpLocust):
    task_set = WebsiteTasks
    host = "https://www.apiopen.top"
    min_wait = 1000
    max_wait = 5000

#locust -f locust3.py