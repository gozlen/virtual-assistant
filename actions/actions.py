from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Hello World!")

        return []


# class ActionAnswerQuestion(Action):

#     def name(self) -> Text:
#         return "action_answer_question"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         plant_part = next(tracker.get_latest_entity_values("plant_part"), None)
#         adjective = next(tracker.get_latest_entity_values("adjective"), None)
#         dispatcher.utter_message(template="utter_answer_question",placeholder = plant_part +" " + adjective)
#         return []

class ActionAnswerQuestionAboutPhysiologicalProcess(Action):

    def name(self) -> Text:
        return "action_answer_question_about_physiological_process"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:


        
        process = next(tracker.get_latest_entity_values("physiological_process"), None)
        dispatcher.utter_message(template="utter_answer_question",placeholder = process)

        return []

class ActionAnswerQuestionAboutEnvironment(Action):

    def name(self) -> Text:
        return "action_answer_question_about_environment"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:


        environment = next(tracker.get_latest_entity_values("environment"), None)
        adjective = next(tracker.get_latest_entity_values("environment_adjective"), None)
        dispatcher.utter_message(template="utter_answer_question",placeholder = environment +" " + adjective)

        return []

class ActionAnswerQuestionAboutPartAdvantage(Action):

    def name(self) -> Text:
        return "action_answer_question_about_part_advantage"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:


        plant_part = next(tracker.get_latest_entity_values("plant_part"), None)
        adjective = next(tracker.get_latest_entity_values("adjective"), None)
        dispatcher.utter_message(template="utter_answer_question",placeholder = plant_part +" " + adjective)

        return []        

class ActionAnswerQuestionAboutPlantPart(Action):

    def name(self) -> Text:
        return "action_answer_question_about_plant_part"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:


        plant_part = next(tracker.get_latest_entity_values("plant_part"), None)
        dispatcher.utter_message(template="utter_answer_question",placeholder=plant_part)

        return []        

class ActionAnswerQuestionAboutPlantInEnvironment(Action):

    def name(self) -> Text:
        return "action_answer_question_about_plant_in_environment"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        plant_part = next(tracker.get_latest_entity_values("plant_part"), None)
        adjective = next(tracker.get_latest_entity_values("environment_adjective"), None)
        environment = next(tracker.get_latest_entity_values("environment"), None)
        dispatcher.utter_message(template="utter_answer_question",placeholder=plant_part +" " + adjective + " " + environment)

        return []     

