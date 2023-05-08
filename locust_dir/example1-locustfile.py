from locust import HttpUser,  task
import logging

class HelloWorldUser(HttpUser):
    @task
    def hello_world(self):
        self.client.get("/")
       