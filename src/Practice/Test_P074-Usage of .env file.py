# Env File - .(dot.env)
# For using contents of .env file in this program
# Need  module ->
# pip install python-dotenv

from dotenv import load_dotenv
import os


def test_update_req():
    load_dotenv()
    username = os.getenv("USERNAME")
    password = os.getenv("PASSWORD")
    print(username)
    print(password)