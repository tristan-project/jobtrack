# jobtrack
In this reposetory we create an application build to connect people with the job best suited for there life. Working in diffrent offices withg diffrent people building a with span experience and score by diffrent organisation. Creating the future of working.
Opgave Herexamenproject
Voor het herexamenproject werk je wederom individueel een opdracht uit. Het thema mag je zelf kiezen. Je mag niet verder bouwen aan een project dat je in semester 1 gemaakt hebt, je begint dus met een volledig nieuw project!

De deadline voor deze opdracht is donderdag 15 augustus om 23:59.

De volledige evaluatie gebeurt op GitHub. Dit wil zeggen dat iets dat niet op GitHub staat, ook niet geëvalueerd zal worden. %-punten die je krijgt per volledige sectie liggen vast. %-punten die vervolgens afgetrokken worden voor niet-complete delen van de sectie liggen niet vast. Eigen bepaalde aanvullingen mogen natuurlijk ook!

Kies (en combineer) uit de aanvullingen zaken die je het meest interesseren. Over het algemeen is het zo dat aanvullingen met een nummer zoals 2.1.1 de aanvulling met nummer 2.1 nodig hebben om relevant te zijn of te werken.

Tijdens de oplevering geef je dan je GitHub repository links mee, je hosting links en een oplijsting van de nummers die je uitgewerkt hebt. Eigen aanvullingen vermeld je uiteraard ook.

1. ❔ ALGEMENE EISEN & DOCUMENTATIE (alles samen +50%)
Minstens 3 GET, 1 POST, 1 PUT en 1 DELETE endpoints
Minstens 3 entiteiten in je API via een SQLite databank
Minstens hashing en OAuth implementeren
Beschrijving van het gekozen thema, je API(s) en je uitbreidingen + link naar de zaken die hosted zijn op GitHub README.md
Aantoonbare werking totale API door screenshots van Postman requests op GitHub README.md
Volledige OpenAPI docs screenshot(s) op GitHub README.md
Logisch gebruik van path parameters, query parameters en body
Docker container voor de API(s), welke automatisch door GitHub Actions opgebouwd wordt
Aangetoond deployment van de API container(s) via Docker Compose (niet op Okteto)
2. 🔧 AANVULLINGEN: FUNCTIE
2.1 (+10%) Test alle GET endpoints van een van je API's via de Requests en pytest library.
2.1.1 (+10%) Test alle niet-GET endpoints.
2.2 (+5%) Communiceer met een externe API vanuit je eigen API.
3. 📳 AANVULLINGEN: FRONT-END
3.1 (+15%) Maak een front-end voor je applicatie die al je GET endpoints en POST endpoints bevat.
3.1.1 (+10%) Host de front-end in een container die bij in je Docker Compose deployment zit. 
3.1.3 (+15%) Gebruik Vue, React, Angular of Svelte als JavaScript framework.
3.2 (+10%) Maak gebruik van een Grafana container om een Grafana oplossing op te zetten om je API te consumen.
4. 📝 AANVULLINGEN: DATA
4.1 (+20%) Maak een tweede versie van je originele API, maar deze keer gebruik je een MongoDB container i.p.v. een SQL oplossing. Je plaatst deze in een nieuwe GitHub repository, met als README.md een korte uitleg van de verschillen.
4.2 (+30%) Zet een ActiveMQ message queue systeem voor een endpoint van je API, dit zit tevens ook als container in je deployment.
5. 📊 AANVULLINGEN: MONITORING
5.1 (+25%) Voeg een Prometheus container en een Grafana container toe in je Docker Compose deployment en zorg ervoor dat Prometheus een /metrics endpoint heeft binnen je API om metrics uit te halen. Zorg er dan voor dat Grafana een dashboard heeft dat deze metric data weergeeft uit Prometheus.