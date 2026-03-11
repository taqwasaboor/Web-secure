from fastapi import FastAPI
from pydantic import BaseModel
from scanner.scan import run_full_scan
from database import init_db, SessionLocal, ScanResult #import db session and Scanresult table model
import json #needed to convert the scan disctionary into string for storage

app = FastAPI() #CREATING FAST API APP OBJECT

init_db() #creates database and table on startup if they dotn exist

#creates a class in which the target url which must be in text or string , we want to scan
class ScanRequest(BaseModel):
    target: str

@app.get("/") #definign home root, when someone visit / homepage
def home ():
    return{"message": "Websecure API is running"} #return  asimple json msg to confirm that apiu is rinnign

@app.get("/scan/{target}") #definign scan route
def scan(target: str): #target will b in string
    results = run_full_scan(target) ## Runs the full security scan on the given target
    db = SessionLocal() #open a new database session like opening a connection
    return results

#creates a toute that listen to POSt request
@app.post("/scan")
def scan_post(request: ScanRequest): #defines a fucntion
    results = run_full_scan(request.target)
    return results