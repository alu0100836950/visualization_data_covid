from flask import Flask
from flask import Markup
from flask import render_template, request, jsonify

import plotly
import plotly.express as px
from plotly.graph_objs import Scatter

import json
import pandas as pd

from data import Header_data

from urllib.request import urlopen

app = Flask(__name__)


header_data = Header_data()



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/diagramas')
def view_diagram():
    return render_template('diagramas.html')

# @app.route('/map')
# def view_map():
#     return render_template('map.html')

@app.route('/dataFile', methods = ['POST'])
def data_file():

    response = request.get_json()
    print(response['link'])
    header_data.load_data(response['link'])

    return jsonify({'header': header_data.get_header(), 'date': header_data.get_date()})



@app.route('/figura', methods = ['POST'])
def figure():

    type_graph = request.form['type-graph']
    
    if header_data.get_date() == True:
        df = header_data.get_data()
        fig = getattr(px, type_graph)(df, x = 'fecha', y = df.columns)
        my_plot_div = plotly.offline.plot(fig, include_plotlyjs=False, output_type='div')
        return render_template('index.html', div_fig = Markup(my_plot_div), date = True)
    
    else:

        df = header_data.get_data()
        fig = getattr(px, type_graph)(df, x = request.form['data-x'], y = request.form['data-y'])
        my_plot_div = plotly.offline.plot(fig, include_plotlyjs=False, output_type='div')
        
        return render_template('index.html', div_fig = Markup(my_plot_div), data = False)



@app.route('/diagramas', methods = ['POST'])
def distribution():

    type_graph = request.form['type-graph']
    if type_graph == 'histogram':
        if header_data.get_date() == True:

            df = header_data.get_data()
            fig = getattr(px, type_graph)(df, x = 'fecha', y = df.columns)
            p = plotly.offline.plot(fig, include_plotlyjs=False, output_type='div')

            return render_template('diagramas.html', plot_div = Markup(p), date = True )
        else:

            df = header_data.get_data()
            fig = getattr(px, type_graph)(df, x = request.form['data-x-dis'], y = request.form['data-y-dis'])
            p = plotly.offline.plot(fig, include_plotlyjs=False, output_type='div')

            return render_template('diagramas.html', plot_div = Markup(p), date = False )

    if type_graph == 'box':

        df = header_data.get_data()
        fig = getattr(px, type_graph)(df, y = request.form['data-y-dis'] )
        p = plotly.offline.plot(fig, include_plotlyjs=False, output_type='div')

        return render_template('diagramas.html', plot_div = Markup(p) )



@app.route('/map')
def map():
    with urlopen('https://raw.githubusercontent.com/PublicaMundi/MappingAPI/master/data/geojson/us-states.json') as response:
        counties = json.load(response)
    df = pd.read_csv("https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv",
                   dtype={'fips': str})
    fig = px.choropleth_mapbox(df, geojson=counties, locations='fips', color='cases',
                            color_continuous_scale="Viridis",
                            range_color=(0, 20000),
                            mapbox_style="carto-positron",
                            zoom=3, center = {"lat": 37.0902, "lon": -95.7129},
                            opacity=0.5,
                            labels={'unemp':'unemployment rate'}
                            )
    
    p = plotly.offline.plot(fig, include_plotlyjs=False, output_type='div')
    return render_template('map.html', plot_div = Markup(p))

if __name__ == '__main__':
    app.run(debug=True, port=4000)
