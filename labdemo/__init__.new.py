import logging
import json
import azure.functions as func
import os

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    output = {}
    for k,v in os.environ.items():
        output[k] = v
    
    joutput = json.dumps(output, indent=4, sort_keys=True)

    return func.HttpResponse(joutput,status_code=200)

