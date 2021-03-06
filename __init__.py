from mycroft import MycroftSkill, intent_file_handler
import requests
import json
from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger
__author__ = 'Bhavik_Katyal'

LOGGER = getLogger(__name__)


class Skill(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('count.intent')
    def handle_count(self, message):
        try:
            number = message.data.get("number")
            response = {'number': message.data.get("number")}
            url = "https://ip0rzvwy82.execute-api.us-east-1.amazonaws.com/Test/mycroft-skill-emp-details"

            key="{\n\t\"inputparams\":"
            value=number
            key1 = "\""+value+"\"\n}"
            payload = key + key1
            headers = {
                'Content-Type': "application/json",
                'Host': "ip0rzvwy82.execute-api.us-east-1.amazonaws.com"
                }

            response = requests.request("POST", url, data=payload, headers=headers)
            data = json.loads(response.text)
            data2 = json.loads(data['body'])
            id_emp = data2['emp_id']
            designation=data2['designation']
            location=data2['location']
            birth_date=data2['birth_date']
            joining_date=data2['joining_date']
            self.speak_dialog("{}, {}, location, {} , Birth Date , {} , Joining date, {}".format(id_emp,designation,location,birth_date,joining_date))
            #self.speak_dialog("count_start", data=response)
            
        except:
            self.speak_dialog("error")

    
def create_skill():
    return Skill()
