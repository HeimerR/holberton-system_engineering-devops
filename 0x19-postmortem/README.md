-- Postmortem example --
# Frank video meme generator Postmortem (incident #001)

![alt text](https://github.com/HeimerR/holberton-system_engineering-devops/blob/master/0x19-postmortem/postmortem.jpg)

## Date

2019-10-21

## Authors

* Heimer Rojas Castellanos

## Status

Complete

## Summary

Frank video website down for 1 hour 41 minutes.

The event started at 16:51 UTC and ends at 18:30 UTC afecting 100% of the service.

## Impact

Estimated 1500 queries lost, no revenue impact.

## Root Causes

The load balancer went down due to a combination of exceptionally high load and a fan failure which end up overheating the server.

![alt text](https://github.com/HeimerR/holberton-system_engineering-devops/blob/master/0x19-postmortem/meme-it-is-fine.jpg)

## Trigger

A sudden increase in traffic when a user promotes the website on Reddit.

## Resolution

At the begging, the load balancer was eliminated from the architecture and it was necessary to set up a pass-through configuration, where the requests were served directly by the web-servers. After that, a new balancer was set up and put in the system.

## Detection

The monitor system installed on the servers sent an email.


## Timeline

2019-10-21 (*all times UTC*)

| Time  | Description |
| ----- | ----------- |
| 16:51 | A Reddit user posts the website a became viral suddenly |
| 16:53 | Traffic to Frank video increases by 100x after post |
| 16:54 | **OUTAGE BEGINS** -- the temperature in the load balancer increases so fast and some user cannot access to the website|
| 16:55 | most of the users receive pager storm, `ManyHttp500s`  |
![alt text](https://github.com/HeimerR/holberton-system_engineering-devops/blob/master/0x19-postmortem/500error.jpg)
| 16:57 | All traffic to Frank video website is failing|
| 17:01 | **INCIDENT BEGINS** the monitoring system sends an email |
| 17:02 | The DevOps Abdel receives the email and starts the analysis and calls the other engineers|
| 17:03 | Haroldo, the backend dev is notified |
| 17:04 | ping test from different locations shows that the server is isolated |
| 17:06 | Abdel calls the service provider but they inform that there is no issue in the datacenter  |
| 17:07 | Abdel insists that we cannot connect with the load balancer |
| 17:10 | The data center informs that apparently the server where the load balancer is located is overheated |
| 17:12 | Haroldo starts to change the configuration to avoid the load balancer  |
| 17:18 | Haroldo runs a puppet manifest that contains the new configuration |
| 17:28 | the new configuration has been set up |
| 17:32 | the service is partially running. some users cannot connect with the server, but more than 70% of the traffic is ok|
| 17:35 | A new server (hardware) is installed in the datacenter|
| 17:45 | The new server is set up as a load balacer|
| 18:00 | **OUTAGE ENDS**, all traffic is ok, the new load balancer starts to work |
| 18:30 | **INCIDENT ENDS**, reached exit criterion of 30 minutes' nominal performance |

## Corrective and preventative measures
Lessons Learned

 	Single points of failure are the biggest risk

* Monitoring quickly alerted us to a high rate (reaching ~100%) of HTTP 500s
* Rapidly was set up a temporary configuration

Action Items

| Action Item | Type | Owner | Bug |
| ----------- | ---- | ----- | --- |
| Update playbook with instructions for responding to load balancer failure | mitigate | Abdel | n/a **DONE** |
| puppet manifests with different configurations | prevent | Martin | Bug 5554823 **TODO** |
| Schedule to test failures | process | docbrown | n/a **TODO** |
| detect sigle points of failures | prevent | jennifer | **DONE** |
| Add a new load balancer as a backup | prevent | Haroldo | **DONE** |

## Supporting Information

* Monitoring dashboard
