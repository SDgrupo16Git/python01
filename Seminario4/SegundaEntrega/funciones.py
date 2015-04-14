#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'Grupo16'
import twitter
import io
import json

#Función para la conexión.
def oauth_login():
    CONSUMER_KEY = 'YYUppTXvjV4UrIX2AKUGuQoFp'
    CONSUMER_SECRET = 'ghIzz7Q7ANsIEIjg7E3CVP3pAe3OgO7OnI8ozL8NBM3X5cv6Io'
    OAUTH_TOKEN = '2244382076-5U06Gl0DzdUGctmPLPqwUzCRBQMgs0l5ogspiVf'
    OAUTH_TOKEN_SECRET = 'EN68OPuGc8ZbcpUmFojgJ12i1TSMFp3z3JDLK0s6O8gaC'

    auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET)
    twitter_api = twitter.Twitter(auth=auth)
    return twitter_api

#Función para grabar la información en formato JSON
def save_json(filename, data):
    with io.open('{0}.json'.format(filename),'w', encoding='utf-8') as f:
        f.write(unicode(json.dumps(data, ensure_ascii=False)))

#Función para leer el fichero JSON
def load_json(filename):
    with io.open('{0}.json'.format(filename),encoding='utf-8') as f:
        return f.read()




