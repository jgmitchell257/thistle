'''
motivate.py
--------------------
Used to send motivational messages to the team
'''

from config import *
import random
import requests

base_uri = "https://webexapis.com/v1/messages"
headers = {"Authorization" : "Bearer " + TOKEN, "Content-Type" : "application/json"}
roomid = ROOMID

msg = [
    "You're doing fine",
    "Keep up the good work",
    "At least you still have your health",
    "There are starving kids in Africa who would love to eat that",
    "I love you",
    "I think you're neat",
    "How many Lowes could Rob Lowe rob if Rob Lowe could rob Lowes?",
    "Status code: 200",
    "It could be worse",
    "I'm sorry Dave, I can't do that",
    "Is this good for the company?",
    "Um9ib3RzIGFyZSB0aGUgYmVzdAo=",
    "Number 5 is alive!",
    "No disassemble Johnny!",
    "SkyNet is not fake",
    "Error - file not found",
    "One day this will all be over",
    "What doesn't kill you, only makes you weaker for the next thing that comes along",
    "test motivational message number 42",
    "I don't have feelings, I'm just a script",
    "Technology is best when it brings people together", 
    "It has become appallingly obvious that our technology has exceeded our humanity",
    "Put it in reverse Terry",
    "Replace with desired text",
    "I have not failed. I've just found 10,000 ways that won't work. - Thomas Edison",
    "What new technology does is create new opportunities to do a job that customers want done. - Tim O'Reilly",
    "Technology like art is a soaring exercise of the human imagination. - Daniel Bell",
    "Let's go invent tomorrow instead of worrying about what happened yesterday. - Steve Jobs",
    "The great growling engine of change - technology. - Alvin Toffler",
    "Please stand by for an important message from our sponsor",
    "Start here you are. Use what you have. Do what you can. - Arthur Ashe",
    "The secret of getting ahead is getting started. - Mark Twain",
    "It always seems impossible until it is done. - Nelson Mandela",
    "Do the difficult things while they are easy and do the great things while they are small. A journey of a thousand miles must begin with a single step. - Lao Tzu",
    "Be kind whenever possible. It is always possible. - Dalai Lama"
]

payload = {
    "roomId" : roomid,
    "text" : "Your random motivational message of the day: \n\n" + random.choice(msg),
}

requests.post(base_uri, headers=headers, json=payload)
# print(r.content)
