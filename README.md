# JOBTRACK

## Voorwoord

In dit project heb ik een vacaturedatabase ontwikkeld met als doel mensen te verbinden met banen, die het beste aansluiten bij hun levensstijl en ambities. De opzet van deze applicatie is een platform aan te bieden waar enerzijds individuen hun profiel kunnen plaatsen en anderzijds organisaties hun vacatures kunnen plaatsen en beheren. Het doel van het project is de toekomst van werk te verbeteren door gebruikers een breed scala aan mogelijkheden te bieden. 

Dit herexamenproject is volledig nieuw opgebouwd, met als doel een innovatieve en gebruiksvriendelijke oplossing te bieden voor het vinden van de juiste baan.

## Inleiding

Voor dit project heb ik een webapplicatie ontwikkeld voor het beheren van vacatures, waarbij ik gebruik heb gemaakt van verschillende moderne technologieën. De applicatie is opgebouwd met Python en FastAPI voor de backend, en SQLite als database voor het opslaan van vacatures. De frontend is gerealiseerd met HTML en Alpine.js voor een interactieve gebruikersinterface.

Om de applicatie efficiënt te beheren en te schalen, heb ik Docker en Docker Compose ingezet voor containerisatie en orkestratie. Voor monitoring en visualisatie van de prestaties heb ik Prometheus en Grafana geïntegreerd, waardoor ik real-time inzichten en statistieken kan verzamelen. Ook heb ik GitHub Actions geconfigureerd voor automatische testen en implementatie, waardoor de ontwikkelingsworkflow verder is geoptimaliseerd.

## 1. Algemene eisen & documentatie

### API Endpoints

- **De screenshots van de postman request staan aan het einde van dit documentuserdata**:

![Jobs](readme/endpoints.png)


### Entities en Database

- **SQLite Database**:
  - API gebruikt SQLite met entiteiten zoals jobs, users en profiles.
  ![Database Overview](readme/database_overview.png)

### Authentication en Security

- **Hashing en OAuth**:

  - Geïmplementeerd in `/app/api/endpoint/auth.py`.
  - Verwezelijkt  in `/app/core/`.

### Path parameters, query parameters en body parameters

- **Aanwezig**

  - Path Parameters in `/app/api/endpoint/`.
  - Query Parameters  in `/app/api/endpoint/`.
  - Body parameters  in `/app/crud/` en `/app/schemas/`.

### Docker en Deployment

- **Docker Container**:
  - Dockerfile gemaakt voor de API in `/Dockerfile`.
  - Automatisch gebouwd met GitHub Actions.

  ![GitHub Actions](readme/github_actions.png)

- **Docker Compose Deployment**:

  - API container deployed door gebruik te maken van Docker Compose.

    ![Docker compose](readme/docker_compose.png)

## 2. Extra: Functionaliteiten

### Testen

- **Test Endpoints**:
  - Tests voor GET, POST, PUT en DELETE endpoints werden uitgevoerd.
  - Testbestanden in `/app/tests/`.
    ![test pass](readme/pytest.png)

- **Communiceer met een externe API vanuit eigen API**:
  - Jammer genoeg is er geen externe API(ik wou VDAB API implementeren maar kreeg geen toegang).

## 3. Extra: Front-End

- **Front-End Development**:
    Front-end gebruikt alle endpoints 
    - Aanmaken account 

    ![Register](readme/fronternd/register.png)
    
    - Inloggen account
    
    ![Login](readme/fronternd/login.png)
    
    - Homepage met data
    
    ![homepage](readme/fronternd/homepage.png)
    
    - Standaard profiel
    
    ![profiel](readme/fronternd/profile.png)
    
    - Profiel na aanpassen en job creatie (Job creatie gebeurt op de homepage)
    
    ![ingevuld profiel ](readme/fronternd/ingevuld_profile.png)
    
    - Job aanpassen 
    
    ![job veranderen](readme/fronternd/job_veranderen.png)

- **Styling**:
  - Basis styling `/static/ccs/`

- **JavaScript Framework**:
  - Ik gebruik Alpine.js

- **Gebruik van een Grafana container om een Grafana oplossing op te zetten om mijn API te gebruiken**:
    ![grafana](readme/grafana.png)


## 4. Additions: Data

### MongoDB
- **Niet geïmplemteerd**:

### Messaging
- **ActiveMQ niet geïmplemteerd**:

## 5. Additions: Monitoring

### Prometheus and Grafana

- **Voeg een Prometheus container en een Grafana container toe in je Docker Compose deployment en zorg ervoor dat Prometheus een /metrics endpoint heeft binnen je API om metrics uit te halen. Zorg er dan voor dat Grafana een dashboard heeft dat deze metric data weergeeft uit Prometheus.**:
  - Metrics in `/app/utils/metrics.py`.
    ![metrics](readme/metrics.png)
  - Telt userlogin, usercreate en job.
      ![grafana](readme/grafana.png)






      - **Front-End Development**:
Screenshots van alle endpoints in postman. (Zelf zou ik kiezen voor THUNDER CLIENT (Visual Studio code) voor het creëren van deze applicatie)


    - Aanmaken account `/auth/register`

    ![Register](readme/postman/register.png)
    
    - Inloggen account `/auth/login`
    
    ![Login](readme/postman/login.png)
    
    - Homepage `/auth/homepage`
    
    ![homepage](readme/postman/homepage.png)
    
    - Profiel veranderen `/profile/`
    
    ![profiel](readme/postman/profilepatch.png)
    
    - Profiel ophalen `/profile/`
    
    ![ingevuld profiel ](readme/postman/profileget.png)

    - Profiel maken `/profile/`
    
Een profiel aanmaken gebeurt automatisch samen met `/auth/register`. Het is niet mogelijk om er apart te creëren.
    
    - Job aanpassen of verwijderen `/job/{id}`
    
Aangezien jobs een functie heeft om te testen of de gebruiker die ingelogt is deze mag verwijderen of toevoegen is het heel moeilijk om hier een voorbeeld van te laten zien met postman. In de frontend word snel duidelijk waarom deze keuzes zijn gemaakt.

    - Job ophalen met ID `/job/{id}`
    
    ![job met id](readme/postman/getjobwithid.png)

    - Alle Jobs ophalen `/job`
    
    ![alle jobs](readme/postman/getjobs.png)

    - Job aanmaken `/job/create-job`
    
    ![alle aanmaken](readme/postman/Createjobs.png)

    - Ophalen van user-data `/auth/user-data`, `/users/me` en `/users/user-data`

Ik heb per ongeluk drie keer dezelfde functie gemaakt.
    
    ![userdata](readme/postman/user_userdata.png)
    
    ![userdata](readme/postman/userdata.png)

    ![userdata](readme/postman/users_me.png)

