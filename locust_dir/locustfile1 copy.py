from locust import HttpUser, task
import logging

# log = logging.getLogger()
# log.setLevel(logging.DEBUG)
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# fh = logging.FileHandler('locust.log')
# fh.setLevel(logging.DEBUG)


# logging.basicConfig(filemode="w", filename="locust.log", level=logging.DEBUG)

# logging.debug("Debug message")
# logging.info("Info message")
# logging.warning("Warning message")
# logging.error("Error Message")
# logging.critical("Critical message")

#http://beta-loadb-9som00x2f4vq-613417815.us-west-2.elb.amazonaws.com
#http://nlb.us-east-1.beta.elliott.security-mob.aws.dev


class UserBehaviour(HttpUser):

    # @task
    # def get_request(self):
    #     # resp.info("Starting the GET Resquest")
    #     resp = self.client.get("/")
    #     print(resp.status_code)

    @task(3)
    def login_post(self):
        # logging.info("Starting reques for post")
        resp = self.client.post("/")
        #print(resp.headers)
        print(resp.request.headers)

        # logging.info(resp.status_code)
        # logging.info(resp.headers)
        # logging.info(resp.request.headers)
        #print(resp.text)


