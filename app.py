# -*- coding: utf-8 -*-
#/bin/python3
"""
Sample code for using webexteamsbot
"""

import os
import requests
from webexteamsbot import TeamsBot
from webexteamsbot.models import Response
import sys
import json
import get_instant_connect_url as url


# Retrieve required details from environment variables
bot_email = os.getenv("TEAMS_BOT_EMAIL")
teams_token = os.getenv("TEAMS_BOT_TOKEN")
bot_url = os.getenv("TEAMS_BOT_URL")
bot_app_name = os.getenv("TEAMS_BOT_APP_NAME")

# Example: How to limit the approved Webex Teams accounts for interaction
#          Also uncomment the parameter in the instantiation of the new bot
# List of email accounts of approved users to talk with the bot
# approved_users = [
#     "josmith@demo.local",
# ]

# If any of the bot environment variables are missing, terminate the app
if not bot_email or not teams_token or not bot_url or not bot_app_name:
    print(
        "sample.py - Missing Environment Variable. Please see the 'Usage'"
        " section in the README."
    )
    if not bot_email:
        print("TEAMS_BOT_EMAIL")
    if not teams_token:
        print("TEAMS_BOT_TOKEN")
    if not bot_url:
        print("TEAMS_BOT_URL")
    if not bot_app_name:
        print("TEAMS_BOT_APP_NAME")
    sys.exit()

# Create a Bot Object
#   Note: debug mode prints out more details about processing to terminal
#   Note: the `approved_users=approved_users` line commented out and shown as reference
bot = TeamsBot(
    bot_app_name,
    teams_bot_token=teams_token,
    teams_bot_url=bot_url,
    teams_bot_email=bot_email,
    debug=True,
    # approved_users=approved_users,
    webhook_resource_event=[
        {"resource": "messages", "event": "created"},
        {"resource": "attachmentActions", "event": "created"},
    ],
)


# Create a custom bot greeting function returned when no command is given.
# The default behavior of the bot is to return the '/help' command response
def greeting(incoming_msg):
    # Loopkup details about sender
    sender = bot.teams.people.get(incoming_msg.personId)

    # Create a Response object and craft a reply in Markdown.
    response = Response()
    response.markdown = "Hello {}, I'm a chat bot. ".format(sender.firstName)
    response.markdown += "See what I can do by asking for **/help**."
    return response


# This function generates a basic adaptive card and sends it to the user
# You can use Microsofts Adaptive Card designer here:
# https://adaptivecards.io/designer/. The formatting that Webex Teams
# uses isn't the same, but this still helps with the overall layout
# make sure to take the data that comes out of the MS card designer and
# put it inside of the "content" below, otherwise Webex won't understand
# what you send it.
def show_card(incoming_msg):
    attachment = """
    {
        "contentType": "application/vnd.microsoft.card.adaptive",
        "content": {
            "type": "AdaptiveCard",
            "body": [{
                "type": "Container",
                "items": [{
                    "type": "TextBlock",
                    "text": "View remote rooms."
                },
                {
                    "type": "TextBlock",
                    "text": "Please select from one of the below rooms"
                },
                {
                    "type": "Input.ChoiceSet",
                    "id": "room",
                    "value": "0",
                    "choices": [
                        {
                            "title": "<please select a room>",
                            "value": "0"
                        },
                        {
                            "title": "Room 1",
                            "value": "1"
                        },
                        {
                            "title": "Room 2",
                            "value": "2"
                        },
                        {
                            "title": "Room 3",
                            "value": "3"
                        },
                                                {
                            "title": "All Rooms",
                            "value": "4"
                        }
                        ]
                }
                ]
            }],
            "actions": [{
                    "type": "Action.Submit",
                    "title": "Create Instant Connect Link",
                    "data": "add",
                    "style": "positive",
                    "id": "button1"
                }
            ],
            "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
            "version": "1.2"
        }
    }
    """
    backupmessage = "This is an example using Adaptive Cards."
    
    c = create_message_with_attachment(
        incoming_msg.roomId, msgtxt=backupmessage, attachment=json.loads(attachment)
    )
    print(c)
    return ""

# An example of how to process card actions
def handle_cards(api, incoming_msg):
    """
    Sample function to handle card actions.
    :param api: webexteamssdk object
    :param incoming_msg: The incoming message object from Teams
    :return: A text or markdown based reply
    """
    m = get_attachment_actions(incoming_msg["data"]["id"])
    #print(m)
    print(m["roomId"])
    roomSelected = m["inputs"]["room"]
    

    if roomSelected == "1":
        values = url.getInstantConnectUriRoom1() 
        hostUri = values.get('host')
        show_card_ic_response(incoming_msg,hostUri,roomSelected,m)
    elif roomSelected == "2":
        values = url.getInstantConnectUriRoom2() 
        hostUri = values.get('host')
        show_card_ic_response(incoming_msg,hostUri,roomSelected,m)
    elif roomSelected == "3":
        values = url.getInstantConnectUriRoom3() 
        hostUri = values.get('host')
        show_card_ic_response(incoming_msg,hostUri,roomSelected,m)
    elif roomSelected == "4":
        values = url.getInstantConnectUriAllRooms() 
        hostUri = values.get('host')
        show_card_ic_response(incoming_msg,hostUri,roomSelected,m)
    else: 
        return None

#Instant Connect Response Card

def show_card_ic_response(incoming_msg,hostUri,roomSelected,m):
    print(hostUri)
    print(roomSelected)
    payload = {
        "contentType": "application/vnd.microsoft.card.adaptive",
        "content": {
            "type": "AdaptiveCard",
            "body": [{
                "type": "Container",
                "items": [{
                    "type": "TextBlock",
                    "text": "Please click the below link to join your virtual room"
                }
                ]
            }],
            "actions": [{
                    "type": "Action.OpenUrl",
                    "title": "Room" + roomSelected,
                    "url": hostUri

                }
            ],
            "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
            "version": "1.2"
        }
    }
    attachment = json.dumps(payload)

    backupmessage = "This is an example using Adaptive Cards."
    
    c = create_message_with_attachment(
        m["roomId"], msgtxt=backupmessage, attachment=json.loads(attachment)
    )
    print(c)
    return None


# Temporary function to send a message with a card attachment (not yet
# supported by webexteamssdk, but there are open PRs to add this
# functionality)
def create_message_with_attachment(rid, msgtxt, attachment):
    headers = {
        "content-type": "application/json; charset=utf-8",
        "authorization": "Bearer " + teams_token,
    }

    url = "https://api.ciscospark.com/v1/messages"
    data = {"roomId": rid, "attachments": [attachment], "markdown": msgtxt}
    response = requests.post(url, json=data, headers=headers)
    return response.json()


# Temporary function to get card attachment actions (not yet supported
# by webexteamssdk, but there are open PRs to add this functionality)
def get_attachment_actions(attachmentid):
    headers = {
        "content-type": "application/json; charset=utf-8",
        "authorization": "Bearer " + teams_token,
    }

    url = "https://api.ciscospark.com/v1/attachment/actions/" + attachmentid
    response = requests.get(url, headers=headers)
    return response.json()


# Set the bot greeting.
bot.set_greeting(greeting)

# Add new commands to the bot.
bot.add_command("attachmentActions", "*", handle_cards)
bot.add_command("/rooms", "show an adaptive card", show_card)


# Every bot includes a default "/echo" command.  You can remove it, or any
# other command with the remove_command(command) method.
bot.remove_command("/echo")

if __name__ == "__main__":
    # Run Bot
    bot.run(host="0.0.0.0", port=5005)