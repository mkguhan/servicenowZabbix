#!/usr/lccal/bin/python3
from servicenow import Connection
from servicenow import ServiceNow


import sys
import datetime
import logging
import logging.handlers
import os
import io

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
    assignmentgroup = "AutomationQ"
    user = "zabbixicc"
    passwd = "tcs#1234"
    instance_name = "dev99449"

    #Creating the conneciton to Service now
    connection = connect_servicenow(user, passwd, instance_name)
    #Connection the incident instance on Service now
    incident_Connection = ServiceNow.Incident(connection)
    # Create Conneciton to Group instance
    group_conneciton = ServiceNow.Group(connection)
    # fetch the details of Group AutomationQ
    group_con = ServiceNow.Group.fetch_all(group_conneciton, {"name": "AutomationQ"})
    # Get the sys_id for AutomationQ, which is need to get the list of instance in AutomationQ
    group_sid = group_con['records'][0]['sys_id']
    fetch_incident = ServiceNow.Incident.fetch_all(incident_Connection,{"assignment_group": group_sid, "state" : 1})
    for i in range(0,len(fetch_incident['records'])):
         if len(fetch_incident['records'][i]['description'].split(",")) > 2 :
             print(fetch_incident['records'][i]['description'].split(",")[2])
    #message = f'Incident # {new_incident["records"][0]["number"]} has been Created'
    #print(message)


main()
