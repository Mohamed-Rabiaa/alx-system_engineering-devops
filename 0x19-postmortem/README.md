
Website Connectivity Incident Report  
This week we have experienced outage in our website. Today we are providing an incident  
report that details the nature of the outage and our response.  
The following is the incident report for our website outage that occured on June 5, 2024:  

Issue Summary:  

From 1:13 PM to 1:50 PM EAT, requests to our website resulted in connection errors (ERR_CONNECTION_REFUSED).  
At its peak, the issue affected 100% of traffic to the website, preventing users from accessing any pages.  
The root cause of this outage was failing to enable the Nginx default file after making changes, which prevented Nginx  
from listening on port 80.  

Timeline(all times EAT Time):  
* 1:00 PM: Configuration push begins  
* 1:13 PM: Outage begins  
* 1:13 PM: Pagers alerted teams  
* 1:40 PM: Deletion of the symbolic link for the Nginx default configuration file  
* 1:41 PM: New symbolic link created  
* 1:42 PM: Nginx server restart begins  
* 1:50 PM: 100% of traffic back restored  

Root Cause:  

At 1:00 PM EAT, changes were made to the Nginx default configuration file without deleting the existing symbolic link in  
/etc/nginx/sites-enabled/default. These changes were pushed to production without prior testing in a staging environment.  
As a result, the changes were not activated, and Nginx did not listen on port 80. This prevented users from reaching our website,  
resulting in connection errors as their browsers could not establish a connection.  


Resolution and recovery:  

At 1:13 PM EAT, monitoring systems alerted our software engineers who investigated and escalated the issue.  
At 1:40 PM, the issue was resolved by deleting the symbolic link for the Nginx default file in /etc/nginx/sites-enabled,  
creating a new link, and restarting the Nginx server to activate the changes.  
By 1:50 PM, users were able to access the website again, with 100% of traffic restored.  
 

Corrective and Preventative Measures:  

Over the last two days, we’ve conducted an internal review and analysis of the outage. The following are actions  
we are taking to address the underlying causes of the issue and to help prevent recurrence and improve response times:  
* Disable the current configuration release mechanism until safer measures are implemented. (Completed)    
* Improve process for auditing all high-risk configuration options.  
* Develop better mechanism for quickly delivering status notifications during incidents.  
* Set up a staging environment that mirrors the production environment to test all configuration  
changes before deploying them to production.  
* Develop automated scripts to validate configuration files before they are applied.  
These scripts should check for syntax errors and potential conflicts.  
* Enhance monitoring tools to detect configuration issues and service downtime more rapidly.  
* Provide regular training sessions for engineers on best practices for configuration management,  
deployment processes, and incident response.  
* Schedule regular audits of all configuration files to ensure they adhere to best practices  
and are free from potential issues.  










