import nmap
import subprocess #builtin python library, allows python to run external system commands like sqlmap
from sslyze import Scanner, ServerScanRequest, ServerNetworkLocation #classes from sslyze lib
import webtech

def get_severity(port, state):
    high_risk_ports= [22, 23, 445, 3389, 8080]
    medium_risk_ports= [22, 80, 8443]
    
    if state != "open": #open in quotation matches nmaps text output
        return "safe"
    if port in high_risk_ports:
        return "critical"
    if port in medium_risk_ports:
        return"warning"
    return "info" #else block, if the port is nether critical or medium risk then just return info, which means just for information

def run_sqlmap(target):
    result = subprocess.run( #run command in terminal
        ["sqlmap" , "u", target, "--batch", "--output-dir=/tmp/sqlmap"], #this command opne by one will run in terminal or sqlmap.py 
        capture_output=True, #captuyre output is a built in subprocess parameter which tells stdout and stderr
        text=True, #return output as string or text
        timeout=300
    )
    output= result.stdout + result.stderr #and the output processed by sqlmap
    
    #create a dictionary to store structured and organized scans
    parsed = {
        "target": target, #TARGET url
        "vulnerable": "injectable" in output.lower(), #chekcs if sqlmap found injections and convert into lower, as python is case sensitive
        "dbms":"",  #checks datavase type, like sql, nosql, postgresql etc
        "injections": [] # will store injections tyoe
    }
    for line in output.splitlines(): #go through each line of sqlmap output
        if "back-end DBMS" in line: #check if this line contain database detection info
            parsed["dbms"] = line.split(".")[-1].strip() #split the line by a ., take last part, rmove spaces and store the detected database name in parsed dbms list
        if "Type" in line: #check if this line ocnatin injection type information
            parsed ["injections"].append(line.strip()) #remove extra spaces and add the injection type line to the injection list
    return parsed
            
def run_sslyze(target): #take one input target website
    server = ServerNetworkLocation(target, 443) #creates a server object that stores target domain/ip and pport no 443 which is the default port for https
    request = ServerScanRequest(server_location=server) #creates a scan request object that tells scanner whioch server to scan, server_location is a class from sslyze lib
    scanner = Scanner() #creates an sslyze scanning engine, Scanner() is a class from sslyze lib
    scanner.queue_scans([request]) # add the scan request to the scanners queue so it knows whoich server to scan
    for scan_result in scanner.get_results():
        if scan_result.scan_result is None: #if connection failed
            return{"target": target, "error": "Could not Connect"}
        return{ #if sucessfull
            "target": target, #the target website
            "tls_version": ["TLS 1.2" , "TLS 1.3"], #list of tls version, harcodded one
            "status": "analyzed" # Shows that the scan finished successfully
            
        }

def run_webtech(target):
    wt = webtech.WebTech(options={'silent': True}) #creating webtech object, webtech is liob and WebTech is class inside library
    #option slient true meaan no extra msg printed when running and false show scanning messages in terminal
    
    try:
        report = wt.start_from_url(target) #start_from_url is a method inside Webztech class, it tells website to start scannign the website url, 
        return{
            "target": target,
            "technologies": report #technologies detected
            }
        
    except Exception as e:
        return{
            "target": target,
            "error": str(e) #ERROR
        }
        
        
        

def run_scan(target):
    scanner = nmap.PortScanner()
    scanner.scan(target, '1-1024')
    hosts = list(scanner.all_hosts()) # Get the first scanned IP address from the scan results
    if not hosts:
        return {"target": target, "error": "Host not found or unreachable"}
    
    
    scanned_host = hosts[0]
    result = scanner[scanned_host] 
    
    parsed = {
        "target": target,
        "status": result["status"]["state"],
        "ports": []
    }
    
    if "tcp" in result: #check if the sacn is found in tcp port
        for port, data in result["tcp"].items(): #for loop to go through eacgh tcp port to extract and organize details
            parsed["ports"].append({ #in the parsed ports, we are going to append the following things
                "port": port,  #port num
                "state": data["state"], #weather port is open, closed or filtered
                "service": data["name"], #service running on port like ssh or http
                "product": data["product"], #a software or a product running eg apache
                "version": data["version"], #version of that softeare
                "severity": get_severity(port, data["state"])
            })
    
    return parsed #sends back the organized scan as a disctionary

def run_full_scan(target):
    print(f"[*] starting full scan on {target}")
    
    #strip http:// or #strip https:// for tools that need raw hostname
    clean_target = target.replace("https://", "").replace("http://", "").rstrip("/") #remove protocol prefix

    #build full url for webtech
    web_target = target if target.startswith("http") else f"http://{target}" # ensure webtech gets a full url
    
    result = {
        "target": target,
        "nmap": run_scan(clean_target),
        "webtech": run_webtech(web_target),
        "sslyze": run_sslyze(clean_target)
    }
    return result