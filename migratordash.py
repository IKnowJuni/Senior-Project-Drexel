from pydoc import classname
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import dash_dangerously_set_inner_html
#import plotly.express as px
#import pandas as pd

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1('Migrator'),
    html.P('''
    (A web application containing data and analysis related to migration flow,
    poverty, median income and unemployment rate on states and counties)
    '''),
    html.Br(),

    dcc.Tabs(
        parent_className='custom-tabs',
        className='custom-tabs-container',
        children=[
            dcc.Tab(label='County Dataset',
            className='custom-tab',
            selected_className='custom-tab--selected',
            children=[
            dcc.RadioItems(
                id="radioitems",
                style={"padding": "10px", "max-width": "800px", "margin": "auto"},
                options=[
                    {'label': 'County to County Migration Flow', 'value': 'CMF'},
                    {'label': 'County Income & Poverty', 'value': 'CIP'},
                    {'label': 'County Unemployment Rate', 'value': 'CUER'}
                ],
                value='CMF',
                labelStyle={'display': 'inline-block'}
            ),
            html.Div(id='body-div')
        ]),
        dcc.Tab(label='State Dataset', 
            className='custom-tab',
            selected_className='custom-tab--selected',
            children=[
                dcc.Graph()
        ])
    ])
])


@app.callback(
    Output(component_id='body-div', component_property='children'),
    [Input(component_id='radioitems', component_property='value')]
)
def build_graph(value):
    if value == 'CMF':
        return html.Div(classname='tableauPlaceholder',id='viz1643655295286',style={'position': 'relative'}[
                html.ObjectEl(classname='tableauViz',style={'display':'none'}[
                    html.Param(name='host_url',value='https%3A%2F%2Fpublic.tableau.com%2F'),
                    html.Param(name='embed_code_version',value='3'),
                    html.Param(name='site_root',value=''),
                    html.Param(name='name',value='CountytoCountyMigration&#47;Story1'),
                    html.Param(name='tabs',value='no'),
                    html.Param(name='toolbar',value='yes'),
                    html.Param(name='animate_transition',value='yes'),
                    html.Param(name='display_static_image',value='yes'),
                    html.Param(name='display_spinner',value='yes'),
                    html.Param(name='display_overlay',value='yes'),
                    html.Param(name='display_count',value='yes'),
                    html.Param(name='language',value='en-US'),
                ]),
            ]), html.Script(dir='assets/custom-scripts.js')
    elif value == 'CIP':
        return html.H1('CIP')
    else:
        return html.H1('CUER')

if __name__ == '__main__':
    app.run_server(debug=True)







# html.Div(classname='tableauPlaceholder',id='viz1643655295286',style={'position': 'relative'}[
#     html.ObjectEl(classname='tableauViz',style={'display':'none;'}[
#         html.Param(name='host_url',value='https%3A%2F%2Fpublic.tableau.com%2F'),
#         html.Param(name='embed_code_version',value='3'),
#         html.Param(name='site_root',value=''),
#         html.Param(name='name',value='CountytoCountyMigration&#47;Story1'),
#         html.Param(name='tabs',value='no'),
#         html.Param(name='toolbar',value='yes'),
#         html.Param(name='animate_transition',value='yes'),
#         html.Param(name='display_static_image',value='yes'),
#         html.Param(name='display_spinner',value='yes'),
#         html.Param(name='display_overlay',value='yes'),
#         html.Param(name='display_count',value='yes'),
#         html.Param(name='language',value='en-US'),
#     ]),
# ])










#<div class='tableauPlaceholder' id='viz1643655295286' style='position: relative'><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='CountytoCountyMigration&#47;Story1' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>

# Inside Layout
    # dcc.Tabs(id='tabs_content', value='county_tab', children=[
    #     dcc.Tab(label='County Dataset', value='county_tab'),
    #     dcc.Tab(label='State Dataset', value='state_tab'),
    # ]),
    # html.Div(id='tabs_contents')

# Inside Callbacks

# @app.callback(
#     Output('tabs_contents', 'children'),
#     Input('tabs_content', 'value')
# )
# def render_content(tab):
#     if tab == 'county_tab':
#         return html.Div([
#             html.H3('County Content'),
            
#             dcc.Graph()
#         ])
#     elif tab == 'state_tab':
#         return html.Div([
#             html.H3('State Content'),
#             dcc.Graph()
#         ])