## volgende_match happy path 
* begroeting
  - utter_hallo
* volgende_match
  - action_zoek_volgende_match
* afscheid
  - utter_afscheid

## volgende_match happy path zonder begroeting
* volgende_match
  - action_zoek_volgende_match
* afscheid
  - utter_afscheid

## volgende_match happy path met bedanking
* begroeting
  - utter_hallo
* volgende_match
  - action_zoek_volgende_match
* bedanking
  - utter_graag_gedaan

## specifieke_maand happy path
* begroeting
  - utter_hallo
* specifieke_maand{"maand":"juli"}
  - action_zoek_specifieke_maand
* afscheid
  - utter_afscheid

## match toevoegen happy path
* begroeting
    - utter_hallo
* voeg_match_toe
    - match_form
    - form{"name": "match_form"}
    - form{"name": null}
* bedanking
    - utter_graag_gedaan

## match toevoegen happy path waarbij datum, tegenstander en locatie reeds meegegeven worden
* begroeting
    - utter_hallo
* voeg_match_toe{"datum":"19 december", "tegenstander":"Lotenhulle", "locatie": "Sporthal Oostbroek Nevele"}
    - match_form
    - form{"name": "match_form"}
    - form{"name": null}
* bedanking
    - utter_graag_gedaan

## match toevoegen happy path waarbij datum, uur en tegenstander reeds meegegeven worden
* voeg_match_toe{"datum":"26 augustus", "uur": "18u", "tegenstander":"FC De Rougekes"}
    - match_form
    - form{"name": "match_form"}
    - form{"name": null}
* bedanking
    - utter_graag_gedaan

## match toevoegen unhappy path 1
* voeg_match_toe
    - match_form
    - form{"name": "match_form"}
* misunderstanding
    - action_deactivate_form
    - form{"name": null}
    - action_restart

## match toevoegen unhappy path 2
* voeg_match_toe{"datum":"10 maart"}
    - match_form
    - form{"name": "match_form"}
* misunderstanding
    - utter_no_problem
    - action_deactivate_form
    - form{"name": null}
    - action_restart

## zeg afscheid
* afscheid
  - utter_afscheid

## simple acknowledgement
* acknowledge
  - utter_positieve_feedback

## restart conversation
* misunderstanding
  - utter_no_problem
  - action_restart

## fallback story
* out_of_scope
  - action_default_fallback
