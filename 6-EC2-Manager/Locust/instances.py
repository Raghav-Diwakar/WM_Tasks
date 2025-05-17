from locust import HttpUser, task, between

class APIUser(HttpUser):
    wait_time = between(1, 5)  # Simulates a user waiting 1-5 seconds between tasks

    @task
    def get_instances(self):
        headers = {
            "accept": "application/json"
        }
        self.client.get("/instances", headers=headers)
