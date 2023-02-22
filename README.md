# InstantConnect_EndPoint_BoT
A simple demo bot allowing endpoints to be selected to join and Instant Connect meeting

Leverages the following API service https://instant.webex.com/

and the ability to create meeting links https://developer.webex.com/docs/instant-connect-meeting-links

NOTE - very basic and rough example. Your millage may vary.


![Screenshot 2023-02-22 at 10 53 18 am](https://user-images.githubusercontent.com/4830623/220486527-f5d9c1f4-3853-4bc4-b012-d6269628bd9d.png)

![Screenshot 2023-02-22 at 10 53 40 am](https://user-images.githubusercontent.com/4830623/220486537-24f6c468-d5dd-4d8b-b2c1-28aa5968c532.png)

![Screenshot 2023-02-22 at 10 54 11 am](https://user-images.githubusercontent.com/4830623/220486543-426f6ed7-f164-47c3-b628-a098d71cc05c.png)


To run

1) Install Docker Engine - https://docs.docker.com/engine/

2) Edit Dockerfile ENV variables

ENV TEAMS_BOT_URL=your_web_hook_destination_url_here

ENV TEAMS_BOT_TOKEN=your_webex_bot_token_here

ENV TEAMS_BOT_EMAIL=your_webex bot_email_address_here

ENV TEAMS_BOT_APP_NAME=your_webex_bot_app_name_here


ENV AUTHTOKEN=your_auth_token_for_webex_instant_connect

ENV ENDPOINTURI1=your_endpoint_sip_address

ENV ENDPOINTURI2=your_endpoint_sip_address

ENV ENDPOINTURI3=your_endpoint_sip_address

ENV ENDPOINTURI4=your_endpoint_sip_address

3) Run app.sh (./app.sh , don't forget to check execute permissions)



