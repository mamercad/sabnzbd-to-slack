#!/usr/local/bin/python

import json
import requests
import sys

try:
  (scriptname, notification_type, notification_title,
   notification_text, parameters) = sys.argv
  slack_message = {
    'title': notification_title,
    'pretext': notification_type,
    'text': notification_text
  }
  response = requests.post(
    parameters,
    data=json.dumps(slack_message),
    headers={'Content-Type': 'application/json'}
  )
  if response.status_code != 200:
    raise ValueError('Slack failed with {0} ({1})'.format(response.text, response.status_code))
except Exception as e:
  print e
  sys.exit(1)
