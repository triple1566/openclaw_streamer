# For async operatoin
import asyncio
# For json data type
import json 
# For base64 encoding - Openclaw expects publicKey and signature to be base64
import base64
# For importing environment variables
import os
from dotenv import load_dotenv
# To remove erratic behaviour when connection is not yet established
from typing import Optional
# For the websocket connection
from websockets.asyncio.client import connect
# Runs the server
from fastapi import FastAPI
# For json validation
from pydantic import BaseModel
# For crypto signing during openclaw handshake
from nacl.signing import SigningKey

# Load the env variables
load_dotenv()
OPENCLAW_URL = os.environ["OPENCLAW_URL"]
OPENCLAW_TOKEN = os.environ["OPENCLAW_TOKEN"]
DEVICE_FP = 000000000000

# Debugging purpose
#print(OPENCLAW_TOKEN)
#print(OPENCLAW_URL)
#print(DEVICE_FP)

#TODO: create signing key and public key fn here

async def hello():
    async with connect(OPENCLAW_URL) as websocket:
        await websocket.send("Initiating WS handshake from fastapi-odoo bridge")
        handshake1 = await websocket.recv()

        print("=====Raw handshake1==========")
        print(handshake1)
        print("==========================")

        handshake_1_reply = json.loads(handshake1)
        msg_type = handshake_1_reply.get("type")
        event_type = handshake_1_reply.get("event")
        first_payload = handshake_1_reply.get("payload")
        first_nonce = first_payload.get("nonce")
        first_ts = first_payload.get("ts")

        print("=====LOADED DATA 1========")
        print(f"msg type = {msg_type}, event type = {event_type}, payload = {first_payload}, timestamp = {first_ts}, nonce = {first_nonce}")
        print("==========================")

        #TODO: source this from an external json file
        handshake2_data = 1
        handshake2 = json.dumps(handshake2_data)
        #print(type(handshake2))
        #parsed_handshake2 = json.loads(handshake2)
        #print(parsed_handshake2)

        await websocket.send(handshake2)
        handshake_2_reply = await websocket.recv()

        print("=====LOADED DATA 2========")
        print(handshake_2_reply)
        print("==========================")

if __name__ == "__main__":
    asyncio.run(hello())