# Krajina za školou

## O projektu
Tento projekt je inspirován webovými stránkami [krajinazaskolou.cz](https://www.krajinazaskolou.cz/), nicméně jsme jej mírně zmodernizovali a přizpůsobili pro potřeby **Gymnázia Jana Keplera**.

Pracovní název je *nighthawk*, v tomto repositáři se nachází již druhá verze, využívající Django.

Administrační prostředí (`/admin`) umožňuje přihlášeným uživatelům přidávat návrhy bodů. Uživatelé s příslušným oprávněním (`accept_markerproposal`) mohou návrhy přijímat, což se promítne v API (`/markers`), ze kterého body načítá frontend.

## Uživatelská dokumentace

### Student - Přidání bodu

Kliknutím na tlačítko `Přidat bod!` se dostanete do administračního prostředí. Do něj se lze přihlásit školním google účtem. Zde klikněte na tlačítko `+ přidat` u `návrhy bodů` v sekci `body`. Do formuláře vyplňte název body, pozici na mapě (pro získání souřadnic lze použít např.: [mapy google](maps.google.cz) nebo [mapycz](mapy.cz)), popis, nahrajte obrázky pomocí tlačítka `Zvolit soubor` a ke každému doplňte informace o roku pořízení a zdroje. K obrázkům které jste fotili vy je zdrojem vaše jméno. Pokud chcete přidat více než dva obrázky klikněte na tlačítko `+ Přidat Obrázek`. Až bude vše vyplněné nezapomeňte zmáčknout tlačítko `ULOŽIT`. 

Kliknutím na `návrhy bodů` v sekci `body` můžete dodatečně upravovat vámi přidané body dokud nejsou zkontrolované učitelem a přidány do mapy.

### Učitel - Kontrola bodů

Kliknutím na tlačítko `Přidat bod!` se dostanete do administračního prostředí. Zde rozklikněte `Návrhy bodů` v sekci `body`. Uvidíte body, které studenti přidali, ale ještě nebyly zkontrolovány. Kliknutím na jednotlivé body je můžete upravovat (viz sekce přidání bodu). Po kontrole a případné úpravě bodu přijměte bod. Body lze také přímat přímo ze seznamu všech bodů.

Po přijmutí bodu student bod již nemůže upravovat. Pouze přijaté body se objeví na interaktivní mapě.

Kliknutím na `přijaté bodů` v sekci `body` můžete dodatečně upravovat přijaté body na mapě.

## Development
1. Nainstalovat závislosti `pip install -r requirements.txt`
2. Vytvořit .env `python gen_env.py --debug`
3. Inicializovat databázi `python manage.py migrate`
4. Vytvořit superuživatele (administrátorský účet) `python manage.py createsuperuser`
5. Spustit server `python manage.py runserver`
6. Přihlásit se a přidat body přes `/admin`
7. Nyní je možné získat jejich přehled přes API GET requestem na `/markers`
8. Detail bodu včetně přidružených obrázků a popisku lze získat GET requestem na `/markers/<id>`
