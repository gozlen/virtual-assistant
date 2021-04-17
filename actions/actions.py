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


        
        process = next(tracker.get_latest_entity_values("physiological_process"), None).lower()

        if process == None:
            dispatcher.utter_message(text = "999")
            return []
        elif 'osmosis' in process:
            message = '301'
        elif 'water transport' in process:
            message = '302'
        elif 'transpiration' in process:
            message = '303'
        elif 'photosynthesis' in process:
            message = '304'
        elif 'nutrient transport' in process:
            message = '305'
        elif 'respiration' in process:
            message = '306'
        else:
            message = '999'

        dispatcher.utter_message(text = message)

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
            dispatcher.utter_message(text = "999")
            return []

        elif 'wind' in environment:
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
            message = '999'



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
            dispatcher.utter_message(text = "999")
            return []

        elif 'root' in plant_part:
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
            else:
                message = '999'


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
            else:
                message = '999'

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
                message = '999'

        else:
            message = '999'


        dispatcher.utter_message(text = message)

        return []        

class ActionAnswerQuestionAboutPlantPart(Action):

    def name(self) -> Text:
        return "action_answer_question_about_plant_part"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:



        plant_part = next(tracker.get_latest_entity_values("plant_part"), None)

        if plant_part == None:
            dispatcher.utter_message(text = "999")
            return []
        elif 'root' in plant_part or 'rout' in plant_part:
            message = '307'
        elif 'stem' in plant_part:
            message = '308'
        elif 'leaf' in plant_part or 'leav' in plant_part:
            message = '309'
        else:
            message = '999'
        dispatcher.utter_message(text = message)

        return []        

class ActionAnswerQuestionAboutPlantInEnvironment(Action):

    def name(self) -> Text:
        return "action_answer_question_about_plant_in_environment"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        plant_part = next(tracker.get_latest_entity_values("plant_part"), None).lower()
        adjective = next(tracker.get_latest_entity_values("environment_adjective"), None).lower()
        environment = next(tracker.get_latest_entity_values("environment"), None).lower()


        if plant_part == None or adjective == None or environment == None:
            dispatcher.utter_message(text = "999")
            return []

        if adjective != 'low' and adjective != 'high':
            dispatcher.utter_message(text = "999")
            return []

        if 'root' in plant_part or 'rout' in plant_part:
            if 'wind' in environment:
                if adjective == 'low':
                    message = '400'
                elif adjective == 'high':
                    message = '401'
            elif 'sunlight' in environment:
                if adjective == 'low':
                    message = '400'
                elif adjective == 'high':
                    message = '400'
            elif 'rainfall' in environment:
                if adjective == 'low':
                    message = '402'
                elif adjective == 'high':
                    message = '400'
            elif 'nutrients' in environment:
                if adjective == 'low':
                    message = '404'
                elif adjective == 'high':
                    message = '400'
            elif 'water table' in environment:
                if adjective == 'low':
                    message = '405'
                elif adjective == 'high':
                    message = '406'
            elif 'temperature' in environment:
                if adjective == 'low':
                    message = '407'
                elif adjective == 'high':
                    message = '400'
                
        elif 'stem' in plant_part:
            pass
        elif 'leaf' in plant_part or 'leav' in plant_part:
            pass
        else:
            message = '999'

        
        dispatcher.utter_message(text = message)

        return []     

