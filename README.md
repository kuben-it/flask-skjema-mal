# Skjema-mal

En enkel Flask-app med ett skjema og én resultatside.

Start prorgrammet ved å åpne denne mappen i terminalen, kjør python app.py, og åpne `http://localhost:8080/skjema` i nettleseren.


## Slik tilpasser du malen

Du skal bruke malen til å lage din egen spørreundersøkelse. Du må endre **to steder** for hvert spørsmål:

1. **`templates/skjema.html`** – spørsmålsteksten i `<label>` og svaralternativene
2. **`templates/resultat.html`** – kolonneoverskriftene i tabellen

Ikke endre `name="question1"` og `request.form["question1"]` i `app.py` – de henger sammen og er allerede koblet riktig


## Forslag til spørsmål

- Hva spiser du til lunsj?
- Hva gjør du på fritiden?
- Hva er favorittsangen din akkurat nå?
- Hvor mange timer sover du vanligvis?


## Integrere i din egen app.py

Kopier linjer 9 til 20 fra denne app.py til app.py i ditt statusside-prosjekt. Kopier også `templates/`-mappen og lim den inn samme sted.

Legg til en lenke som går til skjemaet i `status.html`:
```html
<a href="/skjema">Mitt skjema</a>
```