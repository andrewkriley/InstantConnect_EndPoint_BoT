# syntax=docker/dockerfile:1

FROM python:3.10.8-bullseye

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

ENV TEAMS_BOT_URL=your_web_hook_destination_url_here
ENV TEAMS_BOT_TOKEN=your_webex_bot_token_here
ENV TEAMS_BOT_EMAIL=your_webex bot_email_address_here
ENV TEAMS_BOT_APP_NAME=your_webex_bot_app_name_here

ENV AUTHTOKEN=your_auth_token_for_webex_instant_connect
ENV ENDPOINTURI1=your_endpoint_sip_address
ENV ENDPOINTURI2=your_endpoint_sip_address
ENV ENDPOINTURI3=your_endpoint_sip_address
ENV ENDPOINTURI4=your_endpoint_sip_address

ENV VISITURI=https://instant.webex.com/visit/
ENV BROKERURI=https://mtg-broker-a.wbx2.com/api/v2/joseencrypt


COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=5005"]
