from fastapi import FastAPI, HTTPException
from models import VolumeResizeRequest, ProtectionSettings, SecurityRule, InstanceInfo
from ec2_utils import list_instances, modify_volume_size, set_protection, manage_security_rule
from typing import List

app = FastAPI(title="EC2 Manager API", version="1.0")


@app.get("/instances", response_model=List[InstanceInfo])
def get_instances():
    try:
        return list_instances()
    except RuntimeError as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/volume/resize")
def resize_volume(req: VolumeResizeRequest):
    try:
        modify_volume_size(req.volume_id, req.new_size)
        return {"message": f"Volume {req.volume_id} resizing initiated to {req.new_size}GB."}
    except RuntimeError as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.post("/protection")
def update_protection(req: ProtectionSettings):
    try:
        set_protection(req.instance_id, req.stop_protection, req.termination_protection)
        return {"message": f"Protection settings updated for {req.instance_id}."}
    except RuntimeError as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.post("/security-group/rule")
def modify_security_group_rule(rule: SecurityRule):
    try:
        manage_security_rule(rule.dict())
        return {"message": f"Security group rule {rule.action}ed successfully."}
    except RuntimeError as e:
        raise HTTPException(status_code=400, detail=str(e))

