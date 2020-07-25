import dash
import dash_html_components as html
import dash_core_components as dcc

from iexfinance.stocks import get_historical_data
import datetime
from dateutil.relativedelta import relativedelta
import plotly.graph_objs as go

start = datetime.datetime.today() - relativedelta(years=5)
end = datetime.datetime.today()

inputStock = "V2"
df = get_historical_data("TSLA", start=start, end=end, output_format="pandas", token="sk_99b480a1de7547f38575b920c9a03b7a")

trace_close = go.Scatter(x=list(df.index),
                         y=list(df.close),
                         name="Close",
                         line=dict(color="#f44242"))


layout = dict(title="Stock Chart",
              showlegend=False)

app = dash.Dash(__name__)

app.layout = html.Div([
    html.Div([
         html.H1("Stock App"),
         html.Img(src="assets/stock-icon.png")
    ], className="banner"),
])

# app.css.append_css({
#     "external_url":"http://"
# })

if __name__ == '__main__':
    app.run_server(debug = True)
