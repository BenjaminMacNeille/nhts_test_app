######### Import your libraries #######
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly as py
import plotly.graph_objs as go
from plotly.graph_objs import *

###### Import a dataframe #######
df = pd.read_csv('nhts_data.csv')
options_list=list(df['group'].value_counts().sort_index().index)

#df = pd.read_csv('virginia_totals.pkl')
#options_list=list(df['jurisdiction'].value_counts().sort_index().index)

########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title='VA 2016'

####### Layout of the app ########
app.layout = html.Div([
    html.H3('NHTS New Car Buyers: 2016-2017, CA, LMI'),
    dcc.Dropdown(
        id='dropdown',
        options=[{'label': i, 'value': i} for i in options_list],
        value=options_list[0]
    ),
    html.Br(),
    dcc.Graph(id='display-value'),
    #html.Br(),
    #html.A('Code on Github', href='https://github.com/austinlasseter/virginia_election_2016'),
    #html.Br(),
    #html.A('Data Source', href='https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/LYWX3D')
])


######### Interactive callbacks go here #########
@app.callback(dash.dependencies.Output('display-value', 'figure'),
              [dash.dependencies.Input('dropdown', 'value')])
def group_picker(group_name):
    
    group_df=df[df['group']==group_name]

    concat_df = group_df

    #subgroups
    subgroups = group_df["subgroup"].unique()

    fig = go.Figure(data = [go.Bar(x=group_df["subgroup"], 
                                    y=group_df["Subset Population"],
                                    #name= group_df["subgroup"]
                                    )]
                                    )

    fig.update_layout(legend=dict(title ='',
                                    orientation="h",
                                    yanchor="bottom",
                                    y=.85,
                                    xanchor="center",
                                    x=.5,
                                    font=dict(size = 14)
                                ))

    return fig

######### Run the app #########
if __name__ == '__main__':
    app.run_server(debug=True)
