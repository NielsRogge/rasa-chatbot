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

class ActionZoekVolgendeMatch(Action):

     def name(self) -> Text:
         return "action_zoek_volgende_match"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

         # read in data
         data = pd.read_excel("Matchen.xlsx")
         # set 'Datum' column as index of the dataframe such that we can search for the nearest date
         df = data.set_index("Datum")
         # filter rows
         data_row = data.iloc[df.index.get_loc(pd.Timestamp.now(), method='nearest')]

         if data_row is not None:
            message = "De volgende match is {0} om {1}, tegen {2}.".format(format_date(data_row.Datum, format='full', locale='nl'), data_row.Uur, data_row.Tegenstander)
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
                message += "- {0} om {1}, tegen {2}.".format(format_date(data_row.Datum, format='full', locale='nl'), data_row.Uur, data_row.Tegenstander)
                message += " Locatie: {0}".format(data_row.Locatie) + "\n"
         
         dispatcher.utter_message(message)

         return []

class MatchForm(FormAction):
    """Example of a custom form action"""

    def name(self) -> Text:
        """Unique identifier of the form"""

        return "match_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["datum", "uur", "tegenstander", "locatie"]

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""

        message= "Bedankt voor de info! Het toevoegen aan de excel moet ik nog implementeren"
        
        dispatcher.utter_message(message)
        return []
