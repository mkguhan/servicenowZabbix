from servicenow import Connection
from servicenow import ServiceNow

import sys
import datetime
import logging
import logging.handlers
import os

def log_service_now(message):
    logging.basicConfig(filename='app.log', filemode='a', format='%(name)s - %(levelname)s - %(message)s')
    logging.info(msg=message)

def connect_servicenow(user, passwd, inst ):
    try:
        conn = Connection.Auth(username='zabbixicc', password="tcs#1234", instance="dev99449", api = "JSONv2")
    except:
        print('Error Connecting the ServiceNow Instance')
    finally:
        return conn


def main():
    #Variable assignments
    assignmentgroup = sys.argv[1]
    user = "zabbixicc"
    passwd = "tcs#1234"
    instance_name = "dev99449"
    description = sys.argv[2]
    detail = sys.argv[3]

    #Creating the conneciton to Service now
    connection = connect_servicenow(user, passwd, instance_name)
    #Connection the incident instance on Service now
    incident_Connection = ServiceNow.Incident(connection)
    group_conneciton = ServiceNow.Group(connection)
    new_incident = ServiceNow.Incident.create(incident_Connection,{"short_description":description,"description":detail,"priority":"3","u_requestor":"autoalert","u_contact_type":"Auto Monitoring","assignment_group": assignmentgroup})
    message = f'Incident # {new_incident} has been Created'
    log_service_now(message)


main()
