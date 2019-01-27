#!/usr/bin/env python2
# -*- coding: utf-8 -*-
from hermes_python.hermes import Hermes

INTENT_HOW_ARE_YOU = "shanka1997:how_are_you"
INTENT_GOOD = "shanka1997:feeling_good"
INTENT_BAD = "shanka1997:feeling_bad"
INTENT_ALRIGHT = "shanka1997:feeling_alright"

INTENT_FILTER_FEELING = [INTENT_GOOD, INTENT_BAD, INTENT_ALRIGHT]


def main():
    with Hermes("localhost:1883") as h:
        h.subscribe_intent(INTENT_HOW_ARE_YOU, how_are_you_callback) \
         .subscribe_intent(INTENT_GOOD, feeling_good_callback) \
         .subscribe_intent(INTENT_BAD, feeling_bad_callback) \
         .subscribe_intent(INTENT_ALRIGHT, feeling_alright_callback) \
         .start()


def how_are_you_callback(hermes, intent_message):
    session_id = intent_message.session_id
    response = "I'm doing great. Tell me how are you doing?"
    hermes.publish_continue_session(session_id, response, INTENT_FILTER_FEELING)


def feeling_good_callback(hermes, intent_message):
    session_id = intent_message.session_id
    response = "That's  is what i wanted to hear! I'm very glad. "
    hermes.publish_end_session(session_id, response)


def feeling_bad_callback(hermes, intent_message):
    session_id = intent_message.session_id
    response = "Oh my god, that is bad to hear."
    hermes.publish_end_session(session_id, response)


def feeling_alright_callback(hermes, intent_message):
    session_id = intent_message.session_id
    response = "That's cool!! Enjoy."
    hermes.publish_end_session(session_id, response)


if __name__ == "__main__":
    main()
