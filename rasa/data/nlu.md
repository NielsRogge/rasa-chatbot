## intent:begroeting
- hey
- hallo
- hello
- goeiemorgen
- goeiemiddag
- goeienavond
- hey there
- jeep
- yeetz

## intent:afscheid
- dag
- salu
- daag
- tot de volgende
- bye
- tot ziens

## intent:bedanking
- bedankt
- merci
- thanks
- danku
- dank u
- thnx
- thx

## intent:acknowledge
- goed
- good
- super
- nice
- awesome
- ok
- oké
- oke nice
- okay
- aight
- alright
- k

## intent:misunderstanding
- nevermind
- laat maar
- sorry ik ben gemist
- stop
- cancel

## intent:volgende_match
- al nieuws over onze volgende match?
- wanneer is de volgende match?
- wanneer moeten we terug spelen
- next game
- toon mij de volgende wedstrijd
- wanneer is de eerstvolgende wedstrijd
- wanneer spelen de goal diggers terug
- welke dag is er terug match
- volgende match please
- volgende match plz
- wanneer spelen de goal diggers
- wanneer spelen jullie

## intent:specifieke_maand
- welke matchen zijn er in [juli](maand)
- geef me de matchen voor [april](maand)
- toon mij de matchen voor [augustus](maand)
- kan ik de matchen zien in [december](maand)
- zijn er wedstrijden in [oktober](maand)
- graag had ik een overzicht van de matchen in [januari](maand)
- wordt er gespeeld in [maart](maand)
- toon mij de matchen in [mei](maand)
- zijn er matchen in [juni](maand)
- zijn er matchen voorzien in [september](maand)?
- spelen we in [oktober](maand)?
- zijn er matchen gepland in [januari](maand)

## lookup:maand
data/lookup_tables/maanden.txt

## intent:voeg_match_toe
- nieuwe match
- kan ik een match toevoegen
- ik zou graag een nieuwe match toevoegen
- [5 januari](datum) match tegen [team jess](tegenstander)
- nieuwe match tegen [manchester united](tegenstander), thuis op [18 februari](datum)
- is het mogelijk een nieuwe match toe te voegen op [16 maart](datum)
- op zondag [14 april](datum) spelen de goal diggers tegen [Forza Kwek](tegenstander)
- we spelen een match tegen [jacobs rangers](tegenstander), [27 mei](datum) om [15u](uur)
- we spelen [23 juni](datum) tegen [azurri laarne](tegenstander)
- maandagavond [27 juli](datum) kan [scopo](tegenstander) tegen ons
- ik had graag de volgende match toegevoegd: zaterdag [12 augustus 2020](datum) tegen [fc doomkerke](tegenstander) 
- [25 september](datum) spelen we een wedstrijd tegen [Koeketiene](tegenstander) om [18 uur](uur)
- de volgende wedstrijd is vrijdag [3 oktober](datum)
- [12 november](datum) spelen we [thuis]{"entity": "locatie", "value": "Sporthal Oostbroek Nevele"} tegen [Bevergem United](tegenstander)
- zaterdag [14 december](datum) spelen we tegen [KSV Surdac Gent](tegenstander)
- we spelen tegen [fc de rougekes](tegenstander)
- er is een match gepland tegen [zvc 't leebeekje](tegenstander)
- we spelen tegen [De Buikbierkes](tegenstander)
- we spelen [thuis](locatie) tegen [mandel united](tegenstander)
- er is een match voorzien tegen [United Lochristi](tegenstander), [thuis]{"entity": "locatie", "value": "Sporthal Oostbroek Nevele"}
- volgende match van de goal diggers is op het veld van [Skouwe Danny's](tegenstander). Locatie: [Hal 1 Laarne](locatie)
- we spelen een match tegen [borussia dortmund](tegenstander) in [Sporthal Overmere](locatie)

## lookup:datum
data/lookup_tables/datums.txt

## lookup:tegenstander
data/lookup_tables/tegenstanders.txt

## lookup:locatie
data/lookup_tables/locaties.txt

## intent:inform
- [10 januari](datum)
- [16 februari](datum)
- [4 maart](datum)
- [19 april](datum)
- [1 mei](datum)
- [28 mei](datum)
- [2 juni](datum)
- [23 juli](datum)
- [14 augustus](datum)
- [29 september](datum)
- [2 oktober](datum)
- [18 november](datum)
- [27 december](datum)
- [12 december](datum)
- [15u](uur)
- [16 uur](uur)
- om [18 uur](uur)
- [18u30](uur)
- [19 uur](uur)
- [19u45](uur)
- om [20 u](uur)
- [20u](uur)
- [21u30](uur)
- [22 u](uur)
- [forza feesters](tegenstander)
- [club brugge](tegenstander) 
- [anderlecht](tegenstander)
- [Café Sport](tegenstander)
- [KSV Surdac Gent](tegenstander)
- [jacobs rangers](tegenstander)
- [fc de rougekes](tegenstander)
- [Voet Plezier](tegenstander)
- [Golden Boys](tegenstander)
- [team de kwekkers](tegenstander)
- [scopo](tegenstander)
- tegen [biercelona](tegenstander)
- [borussia dortmund](tegenstander)
- [team jess](tegenstander)
- [fc de kampioenen](tegenstander)
- [P&V Youngboys](tegenstander)
- [azurri laarne](tegenstander)
- [oostbroek]{"entity": "locatie", "value": "Sporthal Oostbroek Nevele"}
- we spelen [thuis]{"entity": "locatie", "value": "Sporthal Oostbroek Nevele"}
- [thuis]{"entity": "locatie", "value": "Sporthal Oostbroek Nevele"}
- in [nevele]{"entity": "locatie", "value": "Sporthal Oostbroek Nevele"}
- tis [thuis]{"entity": "locatie", "value": "Sporthal Oostbroek Nevele"}
- [sporthal oostbroek]{"entity": "locatie", "value": "Sporthal Oostbroek Nevele"}
- [oostbroek nevele]{"entity": "locatie", "value": "Sporthal Oostbroek Nevele"}
- [nevele]{"entity": "locatie", "value": "Sporthal Oostbroek Nevele"}
- [rozenbroeken gent]{"entity": "locatie", "value": "Rozenbroeken Gent"}
- [rozenbroeken]{"entity": "locatie", "value": "Rozenbroeken Gent"}
- het [gusb gent](locatie)
- [sportoase leuven](locatie)
- [tolhuis gent](locatie)
- [Sint-Lievenscollege Gent](locatie)
- [college melle](locatie)
- [keiskant drongen](locatie)
- [Technologiecampus KUL Gent](locatie)
- [Hekers Zwijnaarde](locatie)
- [Sporthal St-Martens-Latem](locatie)
- [Bourgoyen Mariakerke](locatie)
- [Sint-Leocollege Hemelsdaele](locatie)
- [zaal Fitlink](locatie)

## intent:out_of_scope
- hoe is het weer vandaag
- gaat het regenen in ruiselede
- ben jij een chatbot
- wie is er keeper op 1 augustus
- gaat het regenen op 14 juni
- wie is de beste speler van de goal diggers





