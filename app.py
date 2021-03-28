# This is a webpage devoted to honoring those who served on the USS Russell during WWII.
# Also the Gwin, Princeton and Columbus
# Machine learning to identify ships and people that were together in various battles or at different times during the war
# First iteration: create a map with the routes traveled over the course of the war. Animated map by month - try plotly with mapbox.
# Follow structure of news-app for initial construction.

import json
import requests
from flask import Flask, jsonify, render_template, request, make_response
import numpy as np
import pandas as pd
import plotly
import plotly.express as px
import plotly.graph_objects as go
import os
from datetime import datetime
from config import api_key, mapbox_token
from uss_russell.py import russ_map

app = Flask(__name__)

# mapbox_token = os.getenv("mapbox_token")
# px.set_mapbox_access_token(mapbox_token)

@app.route("/")
def index():
    # Read in the data
    # FILE_PATH = os.path.join("USS_Russell", "static", "data", "CSV file")
    # df = pd.read_csv(FILE_PATH)
    # russell_map = russ_map(df)

    # with open(os.path.join("USS_Russell", "static", "js", "russ_map.json"), "r") as file:
    #     russ_dict = json.load(file)

    # loc_map = json.dumps(russ_dict)

    fig = russ_map()

    return render_template("russ.html", fig=fig)

# @app.route("/maps")
# def map():
    
    
    
#     return render_template(
    # "visualizations.html", 
    # article_headline_figure=article_headline_figure,
    # boxplot_data=boxplot_data,
    # boxplot_layout=boxplot_layout, 
    # calendar_heatmap_data=calendar_heatmap_data,
    # calendar_heatmap_layout=calendar_heatmap_layout,
    # linechart_figure=linechart_figure,
    # bigram_json=bigram_json,
    # trigram_json=trigram_json,
#   )

# @app.route("/people")
# def bios():
#     return

# @app.route("/places")
# def places():
#     return

# @app.route("/things")
# def resources():
#     return



# Home page with brief intro and history
# Interactive Map page with animation of routes traveled during the war, statistics and plots
# Page with bios of the crew (definitely Grandpa and Grandma)
# history and present-day info about the locations visited by the ship
# Resources page with links to media
# Challenge: ML to network ships and crewmembers who crossed paths during the war

# @app.route("/")
# def index():
#     tri_data, tri_layout = trigram_plot()
#     return render_template("index.html", data=tri_data, layout=tri_layout)

# @app.route("/map")
# def map():
#     bi_data, bi_layout = bigram_plot()
#     return render_template("bigram.html", data=bi_data, layout=bi_layout)

# @app.route("/bios")
# def bios():
#     bi_data, bi_layout = bigram_plot()
#     return render_template("bigram.html", data=bi_data, layout=bi_layout)

# @app.route("/places")
# def places():
#     bi_data, bi_layout = bigram_plot()
#     return render_template("bigram.html", data=bi_data, layout=bi_layout)

# @app.route("/resources")
# def resources():
#     bi_data, bi_layout = bigram_plot()
#     return render_template("bigram.html", data=bi_data, layout=bi_layout)

# @app.route("/MLnetwork")
# def MLnetwork():
#     bi_data, bi_layout = bigram_plot()
#     return render_template("bigram.html", data=bi_data, layout=bi_layout)

if __name__ == "__main__":
    app.run(debug=True)