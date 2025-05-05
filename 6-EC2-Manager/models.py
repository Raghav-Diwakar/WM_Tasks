from pydantic import BaseModel, Field
from typing import List, Optional

class VolumeResizeRequest(BaseModel):
    instance_id: str
    volume_id: str
    new_size: int  # in GB

class ProtectionSettings(BaseModel):
    instance_id: str
    stop_protection: bool
    termination_protection: bool

class SecurityRule(BaseModel):
    protocol: str
    from_port: int
    to_port: int
    cidr_ip: str
    direction: str  # "inbound" or "outbound"
    action: str  # "add" or "remove"
    group_id: str

class InstanceInfo(BaseModel):
    instance_id: str
    state: str
    stop_protection: bool
    termination_protection: bool
    volumes: List[dict]
    security_groups: List[dict]
