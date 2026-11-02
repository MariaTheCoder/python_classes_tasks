import plotly.graph_objects as go

labels = ["A", "B", "C"]
values = [10, 5, 8]

fig = go.Figure(data=[go.Bar(
    x=labels,
    y=values,
    marker_color=["red", "green", "blue"]
)])

fig.update_layout(
    title="Security Events",
    xaxis_title="Event Type",
    yaxis_title="Count"
)


fig.show()
