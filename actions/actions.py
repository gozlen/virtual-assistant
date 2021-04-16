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


        environment = next(tracker.get_latest_entity_values("environment"), None).lower()
        adjective = next(tracker.get_latest_entity_values("environment_adjective"), None).lower()

        if environment == None or adjective == None:
            dispatcher.utter_message(text = "I'm sorry, I didn't quite catch that")
            return []

        if 'wind' in environment:
            if adjective == 'low':
                message = '210'
            elif adjective == 'high':
                message = '211'
        elif 'sunlight' in environment:
            if adjective == 'low':
                message = '220'
            elif adjective == 'high':
                message = '221'
        elif 'rainfall' in environment:
            if adjective == 'low':
                message = '230'
            elif adjective == 'high':
                message = '231'
        elif 'nutrients' in environment:
            if adjective == 'low':
                message = '240'
            elif adjective == 'high':
                message = '241'
        elif 'water table' in environment:
            if adjective == 'low':
                message = '250'
            elif adjective == 'high':
                message = '251'
        elif 'temperature' in environment:
            if adjective == 'low':
                message = '260'
            elif adjective == 'high':
                message = '261'
        
        else: 
            message = "I'm sorry I didn't quite catch that."


        dispatcher.utter_message(text = message)

        return []

class ActionAnswerQuestionAboutPartAdvantage(Action):

    def name(self) -> Text:
        return "action_answer_question_about_part_advantage"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:


        plant_part = next(tracker.get_latest_entity_values("plant_part"), None)
        adjective = next(tracker.get_latest_entity_values("adjective"), None)

        if plant_part == None or adjective == None:
            dispatcher.utter_message(text = "I'm sorry, I didn't quite catch that")
            return []

        if 'root' in plant_part:
            if adjective.lower() == 'branching':
                message = '110'
            elif adjective.lower() == 'non-branching' or adjective.lower() == 'non branching':
                message = '111'
            if adjective.lower() == 'deep':
                message = '112'
            elif adjective.lower() == 'shallow':
                message = '113'
            if adjective.lower() == 'thick':
                message = '114'
            elif adjective.lower() == 'thin':
                message = '115'

        elif 'stem' in plant_part:
            if adjective.lower() == 'long':
                message = '120'
            elif adjective.lower() == 'short':
                message = '121'
            if adjective.lower() == 'thick':
                message = '122'
            elif adjective.lower() == 'thin':
                message = '123'
            if adjective.lower() == 'bark':
                message = '124'
            elif 'no' in adjective.lower() and 'bark' in adjective.lower():
                message = '125'

        elif 'leav' in plant_part or 'leaf' in plant_part:
            if adjective.lower() == 'thick':
                message = '130'
            elif adjective.lower() == 'thin':
                message = '131'
            if adjective.lower() == 'small':
                message = '132'
            elif adjective.lower() == 'large':
                message = '133'
            if 'thick' in  adjective.lower()  and 'skinned' in  adjective.lower() :
                message = '134'
            elif 'thin' in adjective.lower() and 'skinned' in adjective.lower():
                message = '135'

        else: 
            message = "I'm sorry I didn't quite catch that."


        dispatcher.utter_message(text = message)

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

