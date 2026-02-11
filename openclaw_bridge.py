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
import websockets
# Runs the server
from fastapi import FastAPI
# For json validation
from pydantic import BaseModel
# For crypto signing during openclaw handshake
from nacl.signing import SigningKey

