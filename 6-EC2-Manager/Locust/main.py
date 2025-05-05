from locust import HttpUser, task, between
import random

class EC2TestUser(HttpUser):
    wait_time = between(1, 3)

    def on_start(self):
        # Fetch real instances at the start
        resp = self.client.get("/instances")
        if resp.status_code == 200:
            self.instances = resp.json()
        else:
            self.instances = []

    @task
    def get_instances(self):
        self.client.get("/instances")

    @task
    def resize_volume(self):
        if not self.instances:
            return
        inst = random.choice(self.instances)
        if inst["volumes"]:
            vol = random.choice(inst["volumes"])
            payload = {
                "instance_id": inst["instance_id"],
                "volume_id": vol["VolumeId"],
                "new_size": vol["Size"] + random.randint(1, 10)
            }
            self.client.post("/volume/resize", json=payload)

    @task
    def set_protection(self):
        if not self.instances:
            return
        inst = random.choice(self.instances)
        payload = {
            "instance_id": inst["instance_id"],
            "stop_protection": random.choice([True, False]),
            "termination_protection": random.choice([True, False])
        }
        self.client.post("/protection", json=payload)

    @task
    def modify_security_group_rule(self):
        if not self.instances:
            return
        inst = random.choice(self.instances)
        if inst["security_groups"]:
            sg = random.choice(inst["security_groups"])
            payload = {
                "protocol": "tcp",
                "from_port": 22,
                "to_port": 22,
                "cidr_ip": "0.0.0.0/0",
                "direction": "inbound",
                "action": "add",
                "group_id": sg["GroupId"]
            }
            self.client.post("/security-group/rule", json=payload)
