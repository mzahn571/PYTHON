from locust import task, FastHttpUser
import logging

#locust -f locustfile2.py --headless --user 10 --spawn-rate 60 -H http://nlb.us-east-1.beta.elliott.security-mob.aws.dev --logfile=b.log

#http://beta-loadb-9som00x2f4vq-613417815.us-west-2.elb.amazonaws.com
#http://nlb.us-east-1.beta.elliott.security-mob.aws.dev


class User(FastHttpUser):
    #wait_time = 5

    @task
    def todos(self):
        logging.info("Starting request for todos")
        response = self.client.get("/")
        #logging.info(response.text)
        #logging.info(response.headers)
        #logging.info(response.status_code)


    @task
    def posts(self):
        logging.info("Starting request for posts")
        response = self.client.post("/")
        #logging.info(response.text)
        logging.info(response.text)

