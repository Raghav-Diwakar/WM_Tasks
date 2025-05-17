from locust import HttpUser, task, between
import json

class APIUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def resize_volume(self):
        url = "/volume/resize"
        headers = {
            "accept": "application/json",
            "Content-Type": "application/json"
        }
        payload = {
            "instance_id": "i-027045373a2ae75b6",
            "volume_id": "vol-07f10fec49b2e02e2",
            "new_size": 8
        }

        with self.client.post(url, headers=headers, json=payload, catch_response=True) as response:
            if response.status_code == 400:
                response.failure(f"Failed resize: {response.json().get('detail')}")
            elif response.status_code != 200:
                response.failure(f"Unexpected status code: {response.status_code}")
            else:
                response.success()
