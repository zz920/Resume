# Info

 - Bowen Zhi/male/1992 
 - Master Of Computer Engineering/NEU,US
 - 2 years work experience
 - Github：http://github.com/zz920

---

# CONTACT

- Phone/Whatsup：+971504388108 
- Email：zhi.b@husky.neu.edu
- LinkedIn: https://www.linkedin.com/in/bowen-zhi-878756112/

---

# SKILL

- Language：Python/Java
- Web Framework：Flask/Django/Sanic/SpringBoot
- DataBase：MySQL/PgSQL/MongoDB/Redis
- AWS Related：EC2/ECS/Elastic Beanstalk/S3/RDS
- Tools：Git/Docker/FileBeat/Kibana/Elaticsearch

---

# WORK EXPERIENCE

 
## Fetchr,UAE （ 11/2017 ~ now ）
Software Engineer
### NPS（Airwaybill generation system）
* Developed and maintained the PDF generation system based on Flask, generating more than 400 A4 PDF files per second during the peak.
* Re-design the whole system with master-slave structure, seperating the CPU consumption part from the real-time requests, reduced more than 50% of response time. 
* Migrate the whole system to Docker and deployed in the ECS, reducing 50% of the CPU time consumption and 60% budget of server. 
* Rewrite the interface to WKHtmlToPDF lib, promise the zero-down time during the peak time. 

### FMS(3rd party data syncing system)
优化了原有的代码逻辑，重新设计了数据模型，将后端mongodb迁移到mysql，减小了大量内存开销。重写了大部分第三方同步逻辑，使代码更清晰易于维护。将系统容器化，重写了内部服务接口，并将系统从EC2迁移至ECS实现服务的自动弹性扩容/缩容。同时负责开发了日志系统，将日志文件自动同步至Elasticsearch服务器，并使用Kibana可视化。


### IMS/CCDS(Invoice system)
* Contributed to few APIs and Admin pages for finance team to handle the invoice generation,based on Django framework.
* Release reliable based on Celery. 
* Optimized PDF generation logic, reduced more 50% of generation time.


### Other Server
* Maintain few more servers, also contribute some Spring code to some Java system.

## Part time Freelancer, Top Coder( 02/2017 ~ 09/2017 )


## NIHON KHONDEN, CHINA （ 09/2014 ~ 05/2015 ）

### ECG Team
* Worked in a team responsible for design and maintenance of embedded operating system.
* Improved older system transmission capability and reduce cardiogram storage memory cost by 60%

---

# PERSONAL PROJECT

 - [SANIC_PDF](https://github.com/zz920/sanic_pdf)：The pdf server based on the async framework, converting html to pdf and uploading to s3 bucket.
