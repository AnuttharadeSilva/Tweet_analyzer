from locust import HttpUser, task, between

class WebsiteTestUser(HttpUser):
    wait_time = between(0.5, 3.0)
    
    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """
        pass

    def on_stop(self):
        """ on_stop is called when the TaskSet is stopping """
        pass

    @task(1)
    def index(self):
        #self.client.get("http://0.0.0.0:5002")
        self.client.post("http://0.0.0.0:5002", {"key1":"covid", "key2":"usa", "begindate":"2020-6-1", "enddate":"2020-6-20", "limit":"10"})