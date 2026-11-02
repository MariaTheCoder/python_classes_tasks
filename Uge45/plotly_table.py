import plotly.graph_objects as go

# dict står for dictionary eller touple (slå op senere hvordan det staves)
fig = go.Figure(data=[go.Table(
    header=dict(values=["Navn", "Alder"]),
    cells=dict(values=[["Alice", "Bob"], [25, 30]])
)])

fig.show()