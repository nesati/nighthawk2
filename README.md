# Krajina za školou

## O projektu
Tento projekt je inspirován webovými stránkami [krajinazaskolou.cz](https://www.krajinazaskolou.cz/), nicméně jsme jej mírně zmodernizovali a přizpůsobili pro potřeby **Gymnázia Jana Keplera**.

Pracovní název je *nighthawk*, v tomto repositáři se nachází již druhá verze, využívající Django.

Administrační prostředí (`/admin`) umožňuje přihlášeným uživatelům přidávat návrhy bodů. Uživatelé s příslušným oprávněním (`accept_markerproposal`) mohou návrhy přijímat, což se promítne v API (`/markers`), ze kterého ([TODO](https://taiga.k4r.dev/project/x/task/130)) body načítá frontend.

## Uživatelská dokumentace
[TODO](https://taiga.k4r.dev/project/x/us/118)


## Development
1. Nainstalovat závislosti `pip install -r requirements.txt`
2. Inicializovat databázi `python manage.py migrate`
3. Vytvořit superuživatele (administrátorský účet) `python manage.py createsuperuser`
4. Spustit server `python manage.py runserver`
5. Přihlásit se a přidat body přes `/admin`
6. Nyní je možné získat jejich přehled přes API GET requestem na `/markers`
7. Detail bodu včetně přidružených obrázků a popisku lze získat GET requestem na `/markers/<id>`
