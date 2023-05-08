from locust import HttpUser, task
import logging

#http://beta-loadb-9som00x2f4vq-613417815.us-west-2.elb.amazonaws.com
#http://nlb.us-east-1.beta.elliott.security-mob.aws.dev

console_logger = logging.getLogger("console_logger")
fh = logging.FileHandler(filename="stats.log")
fh.setFormatter(logging.Formatter('%(message)s'))
console_logger.addHandler(fh)

class UserBehaviour(HttpUser):

    @task
    def hello_world(self):
        self.client.get("/")

    @task(3)
    def login_post(self):
        resp= self.client.post("/")

        print(resp.status_code)
        print(resp.headers)
        print(resp.request.headers)
        #print(resp.text)


