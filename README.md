# PotePass Faker

En Python-bibliotek for å generere falske PotePass-data for testing og utvikling.

## Bruk

### Python
uv run main.py antall_brukere antall_hundepassere antall_bookinger

eks: uv run main.py 5 10 50 for 5 brukere, 10 hundepassere og 50 bookinger.

Generert data blir lagret i output mappen

### Github workflow:

Actions -> workflow "Generate data" -> velg antall brukere, antall hundepassere og antall bookinger. 

Zipfil med dataen kan da lastes ned.


