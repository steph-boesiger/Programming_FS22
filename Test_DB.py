from sqlite3cm import OpenSqlite3db

# with OpenSqlite3db("database.db", throw_error=True) as (conn, cursor):
    # conn.execute('CREATE TABLE IF NOT EXISTS users')


import os
import spacy
from spacy import displacy
from spacytextblob.spacytextblob import SpacyTextBlob
import pandas as pd
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM


with open(os.path.join('Quellen', 'AG_AKSA.txt'), "r", encoding="utf-8") as AG_AKSA_file:
    temp = AG_AKSA_file.read()
    # print(temp)


nlp_de = spacy.load("de_core_news_lg")
nlp_de.add_pipe('spacytextblob')

random_text_doc = nlp_de(temp)

spacy.displacy.render(random_text_doc, style = "ent")






