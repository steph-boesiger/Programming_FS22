import spacy
from spacy import displacy
from spacytextblob.spacytextblob import SpacyTextBlob
import pandas as pd
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM

nlp_de = spacy.load("de_core_news_sm")
nlp_de.add_pipe('spacytextblob')

# in the terminal below: execute: python -m spacy download de_core_news_lg

def visualize_dependency(text, filename):
    doc_text = nlp_de(text)
    svg = spacy.displacy.render(doc_text, style="dep")
    with open(filename + '.svg', "w", encoding="utf-8") as file:
        file.write(svg)
    drawing = svg2rlg(filename + '.svg')
    renderPM.drawToFile(drawing, filename + '.png', fmt="PNG")
    # svg2png(svg, write_to=filename + '.png', background_color='white')




if __name__ == '__main__':

    visualize_dependency(text=temp, filename="dependency")