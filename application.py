from crypt import methods
from email.mime import application
from flask import Flask, request, jsonify, json
import sys
import os

application = Flask(__name__)

@application.route("/WriteName", methods=['POST'])
def WriteName():
    