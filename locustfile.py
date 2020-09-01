# from locust import HttpUser, task, between

# class WebsiteTestUser(HttpUser):
#     wait_time = between(0.5, 3.0)
    
#     def on_start(self):
#         pass

#     def on_stop(self):
#         pass

#     @task(1)
#     def get_request(self):
#         self.client.get("http://0.0.0.0:5002")

#     @task(2)
#     def post_request(self):
#         self.client.post("http://0.0.0.0:5002", {"key1":"covid", "key2":"usa", "begindate":"2020-6-1", "enddate":"2020-6-20", "limit":"10"})