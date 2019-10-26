# Bowen Zhi

## SKILL

* Language: Python/Golang
* Web Framework: Flask/Django/Sanic/SpringBoot
* DataBase: MySQL/PgSQL/MongoDB/Redis
* AWS Related: EC2/ECS/Elastic Beanstalk/S3/RDS
* Tools: Git/Docker/FileBeat/Kibana/Elaticsearch

## EDUCATION

### Northeastern University(NEU), Boston, MA, USA (09/2015 ~ 05/2017)
* Master's degree in Computer Engineering
### Shanghai Jiao Tong University(SJTU), Shanghai, China (09/2010 ~ 06/2014)
* Bachelor's degree in Electrical Engineering


## WORK EXPERIENCE

### Fetchr SDE,UAE ( 11/2017 ~ now ）
#### NPS（Airwaybill generation system）
* Developed and maintained the high performance PDF generation system based on Flask, generating more than 400 A4 PDF files per second during the peak.
* Re-design the whole system with master-slave structure, seperating the CPU consumption part from the real-time requests, reduced more than 50% of response time. 
* Migrate the whole system to Docker and deployed in the ECS, reducing 50% of the CPU time consumption and 60% budget of server. 
* Rewrite the interface to WKHtmlToPDF lib, promise the zero-down time during the peak time. 

#### FMS(3rd party data syncing system)
* Optimized the code logic, re-design the db models, and migrate the data from mongodb to mysql, reduce more than 50% query time and memory consumption.
* Rewrite the syncing logic with 3rd Party delivery system. Enhance the reliability and maintainability of the server.
* Dockerfy the system, migrate it from EC2 to ECS with auto-scalability. Optimized and migrated the log system to Elasticsearch/Kibana server.


#### IMS/CCDS(Invoice system)
* Contributed to few APIs and Admin pages for finance team to handle the invoice generation,based on Django framework. 
* Release reliable based on Celery. 
* Optimized PDF generation logic, reduced more 50% of generation time.


### Part time Freelancer, Top Coder ( 02/2017 ~ 09/2017 )
* Developed a Python CLT based on libclang to Parse the C code project, Traversing the call trees and Visualizing them into Functional Views.
* Implemented the popular Page Rank algorithm to rank the function nodes and produced the output graph in HTML based on Bootstrap framework.
* Won 2nd place (out of 38 registrations) and $600 prize for the project.


### NIHON KHONDEN, CHINA （ 09/2014 ~ 05/2015 ）

#### ECG Team
* Worked in a team responsible for design and maintenance of embedded operating system.
* Improved older system transmission capability and reduce cardiogram storage memory cost by 60%


## PROJECT
### Sanic PDF generation Server
Project link: https://github.com/zz920/sanic_pdf
* Developed the backend system for users to generate pdf by html file with low lantency.
* Implemented PDF generation Server basic on the ASYNC python framework, handle hundreds of PDF generation requests with single process. 
* Optimized the WKHtmlToPDF lib interface to handle hundreds of converting task parallelly in 1 seconds. 
* Intergrate with AWS S3 to provide stable download link as the response.

### A-share stock data crawler
Project link: https://github.com/zz920/A-share-Downloader
* Developed efficient multiprocessing crawler based on tushare web crawler.
* Built flexible interface to multi relational databases (MySQL, PostgreSQL, SQLite).
* Made special optimization to PostgreSQL, increase insert operation speed by 3 times.
* Established A-share stock records database, containing about 1 billion trade records, single query within
milliseconds.

### Java Web Service Development - Business Search and Recommendation
Contributor of project: https://github.com/WTY1/Dashi
* Developed a dynamic web page for users to search businesses and update preference.
* Improved personalized business recommendation based on search history and favorite records.
* Implemented some RESTful APIs features based on Java servlets framework to handle HTTP requests and
responses.
* Built up interfaces to relational and NoSQL databases (MySQL, MongoDB), used to capture real business
data from Yelp API.
