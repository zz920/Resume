# Bowen Zhi
## SKILL

- Language：Python/Golang
- Web Framework：Flask/Django/Sanic/SpringBoot
- DataBase：MySQL/PgSQL/MongoDB/Redis
- AWS Related：EC2/ECS/Elastic Beanstalk/S3/RDS

## WORK EXPERIENCE

 
### Fetchr SDE,UAE ( 11/2017 ~ now ）
#### NPS（Airwaybill generation system）
* Developed and maintained the high performance PDF generation system based on Flask, generating more than 400 A4 PDF files per second during the peak.
* Re-design the whole system with master-slave structure, seperating the CPU consumption part from the real-time requests, reduced more than 50% of response time. 
* Migrate the whole system to Docker and deployed in the ECS, reducing 50% of the CPU time consumption and 60% budget of server. 
* Rewrite the interface to WKHtmlToPDF lib, promise the zero-down time during the peak time. 

#### FMS(3rd party data syncing system)
* Optimized the code logic, re-design the db models, and migrate the data from mongodb to mysql, reduce more than 50% query time and memory consumption.
* Dockerfy the system, migrate it from EC2 to ECS with auto-scalability. Optimized and migrated the log system to Elasticsearch/Kibana server.


#### IMS/CCDS(Invoice system)
* Contributed to few APIs and Admin pages for finance team to handle the invoice generation,based on Django framework. Release reliable based on Celery. 
* Optimized PDF generation logic, reduced more 50% of generation time.


### Part time Freelancer, Top Coder ( 02/2017 ~ 09/2017 )
* Developed a Python CLT based on libclang to Parse the C code project, Traversing the call trees and Visualizing them into Functional Views.
* Implemented the popular Page Rank algorithm to rank the function nodes and produced the output graph in HTML based on Bootstrap framework.
* Won 2nd place (out of 38 registrations) and $600 prize for the project.

## PERSONAL PROJECT

 - [SANIC_PDF](https://github.com/zz920/sanic_pdf)：Pdf generation server based on the async framework.
