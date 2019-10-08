import random, copy
from random import shuffle

"""
Questions and corresponding options
The first option is the correct answer
When a user is presented with the questions the options will be shuffled
""" 

social_eng = {
    'A situation in which an unauthorized person can view another user\'s display or keyboard to learn their password or other confidential information is referred to as:': ['Spear phishing', 'Tailgating', 'Shoulder surfing', 'Spoofing'],
    "Which social engineering attack relies on identity theft?": ['Impersonation', 'Dumpster diving', 'Watering hole attack', 'Shoulder surfing'],
    'The practice of using a telephone system to manipulate user into disclosing confidential information is called:': ['Whaling', 'Spear phishing', 'Vishing', 'Pharming'], 
    "What is tailgating": ['Acquiring unauthorized access to confidential data', 'Looking over someone\'s shoulder to get information', 'Gaining unauthorized acces to restricted areas by following another person', 'Manipulating a user into disclosing confidential information'],
    'Phishing scams targeting people holding high positions in an organization or business are known as:':  ["Vishing", 'Bluesnarfing', 'Whaling', "Bluejacking"],
    'Phishing scams targeting a specific group of people are referred to as:': ['Vishing', 'Spear phishing', 'Spoofing', 'Whaling'],
    'A social engineering technique whereby attackers under disguise of legitimate request attempt to gain access to confidential information they shouldn\'t have access to is commonly referred to as:': ['Phishing', 'Privilege escalation', 'Backdoor access', 'Shoulder surfing'],
    'An unauthorized practice of obtaining confidential information by manipulating people into disclosing sensitive data is referred to as:': ['Shoulder surfing', 'privilege escalation', 'Social engineering', 'Penetration testing'], 
    'Which of the terms listed below refers to a platform used for watering hole attacks?': ['Mail gateways', 'Websites', 'PBX systems', 'Web browsers'], 
    'A fraudulent email requesting its recipient to reveal sensitive information (e.g. user name and password) used later by an attacker for the purpose of identity theft is an example of:':['Vishing', 'Watering hole attack', 'Social engineering', 'Bluejacking']
}

questions={}
questions["correct"]=[]
questions["wrong"]=[]
questions["curretq"]=1
social_engs = copy.deepcopy(social_eng)
