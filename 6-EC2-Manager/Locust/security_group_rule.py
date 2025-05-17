from locust import HttpUser, task, between
import json

class APIUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def add_security_group_rule(self):
        url = "/security-group/rule"
        headers = {
            "accept": "application/json",
            "Content-Type": "application/json"
        }
        payload = {
            "protocol": "tcp",
            "from_port": 80,
            "to_port": 80,
            "cidr_ip": "0.0.0.0/0",
            "direction": "inbound",
            "action": "add",
            "group_id": "sg-09bb7126075ab3f96"
        }

        with self.client.post(url, headers=headers, json=payload, catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            elif response.status_code == 422:
                response.failure(f"Validation error: {response.json()}")
            else:
                response.failure(f"Unexpected error: {response.status_code}")
