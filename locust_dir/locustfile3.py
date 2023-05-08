from locust import HttpUser, SequentialTaskSet, task, constant
import logging

#locust -f locustfile3.py --headless --user 10 --spawn-rate 60 -H http://nlb.us-east-1.beta.elliott.security-mob.aws.dev --logfile=c.log

#http://beta-loadb-9som00x2f4vq-613417815.us-west-2.elb.amazonaws.com
#http://nlb.us-east-1.beta.elliott.security-mob.aws.dev

class UserBehaviour(SequentialTaskSet):

    @task
    def get_request(self):
        with self.client.get("/", catch_response=True, name="HomePage") as response:
            if "PIZZA PIZZA!" in response.text:
                response.success()
                logging.info("Home Page Reached")
            else:
                response.failure("Failed to load home Page")
                logging.error("Home page failed to load")

class LoadTest(HttpUser):
    host = "http://nlb.us-east-1.beta.elliott.security-mob.aws.dev"
    wait_time = constant(1)
    tasks = [UserBehaviour]