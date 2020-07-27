# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction

import pandas as pd
from babel.dates import format_date
from difflib import SequenceMatcher
import locale
from datetime import datetime

class ActionZoekVolgendeMatch(Action):

     def name(self) -> Text:
         return "action_zoek_volgende_match"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

         # read in data
         data = pd.read_excel("Matchen.xlsx")
         # filter rows 
         data_row = data[data.Datum >= pd.Timestamp.now()].iloc[0]

         if data_row is not None:
            message = "De volgende match is {0} om {1}, tegen {2}.".format(format_date(data_row.Datum, format='full', locale='nl'), data_row.Datum.hour, data_row.Tegenstander)
            message += " Locatie: {0}".format(data_row.Locatie)
         else:
             message = "Er zijn momenteel geen matchen gepland."
         
         dispatcher.utter_message(message)

         return []

class ActionZoekSpecifiekeMaand(Action):

     def name(self) -> Text:
         return "action_zoek_specifieke_maand"
     
     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

         maand = tracker.get_slot("maand")

         months = {
                "januari":1,
                "februari":2,
                "maart":3,
                "april":4,
                "mei":5,
                "juni":6,
                "juli":7,
                "augustus":8,
                "september":9,
                "oktober":10,
                "november":11,
                "december":12
            }

         def similar(a, b):
             return SequenceMatcher(None, a, b).ratio()
         
         # normalize the month (spell check)
         best_similarity = 0
         month_normalized = None
         for month in months.keys():
             similarity = similar(maand.lower(), month)
             if similarity > best_similarity:
                 best_similarity = similarity
                 month_normalized = month

         # read in data
         data = pd.read_excel("Matchen.xlsx")
         # filter rows
         rows = data[data.Datum.dt.month == months[month_normalized]]

         if len(rows) == 0:
             message = "Er zijn momenteel geen matchen gepland in {}.".format(month_normalized)
         else:
            message = "In " + month_normalized + " staat het volgende gepland:\n"
            for x in rows.iterrows():
                data_row = x[1]
                message += "- {0} om {1}, tegen {2}.".format(format_date(data_row.Datum, format='full', locale='nl'), data_row.Datum.hour, data_row.Tegenstander)
                message += " Locatie: {0}".format(data_row.Locatie) + "\n"
         
         dispatcher.utter_message(message)

         return []

class MatchForm(FormAction):
    """Custom form action for adding matches to the Excel file"""

    def name(self) -> Text:
        """Unique identifier of the form"""

        return "match_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["datum", "uur", "tegenstander", "locatie"]

    def slot_mappings(self) -> Dict[Text, Any]:
        """A dictionary to map required slots to
        - an extracted entity
        - intent: value pairs
        - a whole message
        or a list of them, where a first match will be picked"""

        return {
            "datum": self.from_text(),
            "uur": [
                self.from_entity(
                    entity="uur", intent=["inform", "voeg_match_toe"]),
                self.from_text(),
            ],
            "tegenstander": [
                self.from_entity(entity="tegenstander", intent=["inform", "voeg_match_toe"]),
                self.from_text(),
            ],
            "locatie": [
                self.from_entity(entity="locatie", intent=["inform", "voeg_match_toe"]),
                self.from_text(),
            ]
        }

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""

        datum = tracker.get_slot("datum")
        uur = tracker.get_slot("uur")
        tegenstander = tracker.get_slot("tegenstander")
        locatie = tracker.get_slot("locatie")

        # normalize date (does not work if there's a typo)
        locale.setlocale(locale.LC_ALL, 'nl_BE')
        datum_normalized = datetime.strptime(datum, '%d %B')
        datum_normalized = datum_normalized.replace(year=datetime.now().year)

        # normalize hour and apply it to the normalized date
        uur_normalized =""
        for character in uur:
            if character.isdigit(): 
                uur_normalized += character
        datum_normalized = datum_normalized.replace(hour=int(uur_normalized))
        datum_normalized = datum_normalized.strftime('%Y-%m-%d %X')

        # append to dataframe and sort
        data = pd.read_excel("Matchen.xlsx")
        new_data_row = {'Datum': pd.Timestamp(datum_normalized), 
                'Tegenstander': tegenstander,
                'Locatie': locatie}

        data = data.append(new_data_row, ignore_index=True, sort=True)
        data = data.sort_values(by='Datum')

        data.to_excel("Matchen.xlsx", index=False)

        message= "Bedankt voor de info! Ik heb de match toegevoegd in excel :)"

        dispatcher.utter_message(message)
        return []
