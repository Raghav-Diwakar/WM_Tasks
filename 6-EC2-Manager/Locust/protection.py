from locust import HttpUser, task, between
import json

class APIUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def update_protection(self):
        url = "/protection"
        headers = {
            "accept": "application/json",
            "Content-Type": "application/json"
        }
        payload = {
            "instance_id": "i-027045373a2ae75b6",
            "stop_protection": True,
            "termination_protection": True
        }

        with self.client.post(url, headers=headers, json=payload, catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure(f"Failed to update protection: {response.text}")
