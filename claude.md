I am the AVP of Product at CLIRNET.

**About CLIRNET-**
CLIRNET is an engagement platform for doctors with a entrenched market position in India.
CLIRNET has recently started to expand globally, primarily in the Africa area.


**About Products at CLIRNET:**
doctor.clirnet.com is the react frontend for doctors.
apigl.clirnet is the backend api which powers the doctor.clirnet.com frontend
clirnet.ai- Contains Reporting data for Banner Ads, Sponsored Content and other Client Projects



**Projects (v0.1)-**

doctor.clirnet.com
- Speed Improvement
- Image Optimisation at delivery time
- WebSocket usage decision
- CPD Points - Redesign
- Session Flow- Redesign and Development
- Notifications Rewrite- Frontend

apigl.clirnet.com
- DB migration to PlanetScale
- Java migration of apis
  - JAVA api design
- MongoDB vs PlanetScale
- Bring VetNet and DentalNet inside CLIRNET

Admin- be.clirnet.com
- CTA
- Banner
- Files Migration
- E-connect Admin
- Community- Notifications

Banner- Microservice
- Complete Rewrite

MasterCast- mc.clirnet.com
- Migration of old admin to be.clirnet.com
- doctor.clirnet.com as streaming platform
- DB migration to PlanetScale
- Payments refactoring

clirnet.ai- reporting portal for Clients
- Make download report process async as report downloads are silently failing
- Sponsored Commmunity Project (Common Date Filter, Downloadable Reports, Speciality/State Mapping, Data Sync Manual Button)

Mobile App - CLIRNET
- ?

Infrastructure- DevOps
- Redis vs DragonFly
- VMs, where after Azure?
- High Transfer bandwidth usage in VMs?
- Google Migration Out
- Cloud Security


Infrastructure- Data
- Complete Migration from BigQuery to ClickHouse


**Teams (v0.1)-**

Frontend
- Aritra (Leader)
- Debanjan Posto
- Bikram
-


API
- Debmalya

Backend
- Tapas (Leader)
- Bhanjo
- Agniva

MLOps
- Arnab
- Nirmalendu
- Soumya
- Ajmal
- Siddharth Nawalgaria

Design
- Sanjoy
- Krishna
- Souvik

**MLOps Team Tooling**
- MLOps team primarily uses python for scripts and fastapi for creating servers.
- uv is used for dependency management and running python scripts by creating venvs
- development is happening in python
- a good design pattern is to run the scripts in background and continuously updating a file which can be monitored on the progress of the script
