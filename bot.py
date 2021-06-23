from rasa.core import utils
from rasa.core.agent import Agent
from rasa.core.interpreter import RasaNLUInterpreter
from rasa.core.channels import HttpInputChannel
from rasa.core.channels.facebook import FacebookInput
import logging

logger = logging.getLogger(__name__)

def run(serve_forever=True):
    # create rasa NLU interpreter
    # interpreter = RasaNLUInterpreter("models/nlu/current")
    agent = Agent.load("./models/20210127-153235.tar.gz")

    # input_channel = FacebookInput(
    #     fb_verify="your_fb_verify_token", # you need tell facebook this token, to confirm your URL
    #     fb_secret="your_app_secret", # your app secret
    #     fb_tokens={"your_page_id": "your_page_token"}, # page ids + tokens you subscribed to
    #     debug_mode=True # enable debug mode for underlying fb library
    # )

    if serve_forever:
        agent.handle_channel(HttpInputChannel(5004, "/app"))
    return agent

if __name__ == '__main__':
    utils.configure_colored_logging(loglevel="DEBUG")
run()

# import json
# import asyncio

# from flask import Flask, request, abort
# from flask_cors import CORS, cross_origin

# from rasa.core.agent import Agent

# app = Flask(__name__)
# CORS(app)
# cors = CORS(app, resources={r"/*": {"origins": "*"}})

# action_endpoint = "http://localhost:5055/webhook"

# def agent_get(orgid):
#     agents_org = {
#         "agent_one": './models/20210127-153235.tar.gz',
#         "agent_two": './models/20210528-191913.tar.gz',
#         "agent_three": './models/20210527-192121.tar.gz',
#         "agent_four": './models/20200728–140043.tar.gz'
#     }
#     agent = Agent.load(agents_org[orgid])#,action_endpoint=EndpointConfig(action_endpoint))
#     return agent

# async def process(agent, msg):
#   output = await agent.handle_text(msg)
#   print(output)
#   return output

# @app.route('/message', methods=['POST'])
# @cross_origin(origin='*')
# def new_message():
#   if not request.json:
#     abort(400)
#   orgId = request.args.get('orgId')
#   current_agent=agent_get(orgId)
#   user = request.json['sender']
#   message = request.json['message']
#   res = (current_agent.handle_text(text_message=message, sender_id=user))
#   message= asyncio.run(process(current_agent, message))
#   message= json.dumps(message)
#   return message

# if __name__ == '__main__':
#     app.run(host='localhost', port=5000, debug=True, use_reloader=False)