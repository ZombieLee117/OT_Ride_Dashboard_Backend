from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow your React app to talk to this backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Fake OT assets
assets = [
    {"id": "PLC-01", "name": "Ride PLC", "zone": "Ride Control", "type": "PLC", "status": "Online", "ip": "10.10.1.10", "risk": "Medium"},
    {"id": "HMI-01", "name": "Operator HMI", "zone": "Operations", "type": "HMI", "status": "Online", "ip": "10.10.1.20", "risk": "Medium"},
    {"id": "EWS-01", "name": "Engineering Workstation", "zone": "Maintenance", "type": "Workstation", "status": "Online", "ip": "10.10.1.30", "risk": "High"},
    {"id": "RTU-01", "name": "Pump RTU", "zone": "Pump Skid", "type": "RTU", "status": "Online", "ip": "10.10.2.10", "risk": "Low"},
    {"id": "FLOW-01", "name": "Flow Sensor", "zone": "Pump Skid", "type": "Sensor", "status": "Online", "ip": "10.10.2.40", "risk": "Low"},
    {"id": "SAFE-01", "name": "Safety Interlock", "zone": "Safety", "type": "Safety Controller", "status": "Online", "ip": "10.10.3.5", "risk": "Critical"},
]

# Fake alerts
alerts = [
    {
        "id": 1,
        "time": "08:41:12",
        "severity": "Critical",
        "title": "Unauthorized start command blocked",
        "asset": "PLC-01",
        "source": "10.10.9.77",
        "detail": "Command origin was not in the approved engineering subnet."
    },
    {
        "id": 2,
        "time": "08:43:07",
        "severity": "High",
        "title": "Pump ON but no flow detected",
        "asset": "RTU-01",
        "source": "FLOW-01",
        "detail": "Process anomaly persisted for 6 seconds beyond threshold."
    },
    {
        "id": 3,
        "time": "08:46:51",
        "severity": "Medium",
        "title": "Rapid start/stop cycling detected",
        "asset": "PLC-01",
        "source": "HMI-01",
        "detail": "Three state changes occurred inside the configured rate window."
    }
]

# Fake process state
process_state = {
    "pumpRunning": True,
    "flowRate": 62,
    "estop": False
}

# Routes (API endpoints)

@app.get("/")
def root():
    return {"message": "OT Dashboard API is running"}

@app.get("/assets")
def get_assets():
    return assets

@app.get("/alerts")
def get_alerts():
    return alerts

@app.get("/process")
def get_process():
    return process_state