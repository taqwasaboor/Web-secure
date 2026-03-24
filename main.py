from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from scanner.scan import run_full_scan
from database import init_db, SessionLocal, ScanResult #import db session and Scanresult table model
import json #needed to convert the scan disctionary into string for storage

app = FastAPI() #CREATING FAST API APP OBJECT

#allow cross origin requests so the react which is running on different port can interact with this api
app.add_middleware( #calling this fucntion that exist on app object
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:5174"], #this url is allowed to make request
    allow_methods=["*"], #allows http methis such as get, post, put, delete
    allow_headers=["*"], #all headers are allowed to request
)

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
    scan_record = ScanResult(target=target, result=json.dumps(results)) #convert result disctionary into json so it can be stored as text
    db.add(scan_record) #add new record to the session
    db.commit() #commit saves it permenently
    db.close() #close the session when its done
    return results

#creates a toute that listen to POSt request
@app.post("/scan")
def scan_post(request: ScanRequest): #defines a fucntion
    results = run_full_scan(request.target)
    return results