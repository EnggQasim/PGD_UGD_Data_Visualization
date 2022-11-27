import streamlit as st
import numpy as np
import plotly.figure_factory as ff
import pandas as pd



st.title("Graphs")
#====================p1===================
# # Add histogram data
# x1 = np.random.randn(200) - 2
# x2 = np.random.randn(200)
# x3 = np.random.randn(200) + 2

# # Group data together
# hist_data = [x1, x2, x3]

# group_labels = ['Group 1', 'Group 2', 'Group 3']

# # Create distplot with custom bin_size
# fig = ff.create_distplot(
#         hist_data, group_labels, bin_size=[.1, .25, .5])

# # Plot!
# st.plotly_chart(fig, use_container_width=True)

#====================p2==============
# chart_data = pd.DataFrame(
#     np.random.randn(20, 3),
#     columns=['a', 'b', 'c'])

# st.line_chart(chart_data)
#========================p3==========
# st.area_chart(chart_data)
#=========================p4======
# st.bar_chart(chart_data)
#========================p5========
# import matplotlib.pyplot as plt

# arr = np.random.normal(1, 1, size=100)
# fig, ax = plt.subplots()
# ax.hist(arr, bins=20)

# st.pyplot(fig)


#==========================p6==============
# import pandas as pd
# import numpy as np
# import altair as alt

# chart_data = pd.DataFrame(
#     np.random.randn(20, 3),
#     columns=['a', 'b', 'c'])

# c = alt.Chart(chart_data).mark_circle().encode(
#     x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])

# st.altair_chart(c, use_container_width=True)

#===============================p7============
# chart_data = pd.DataFrame(
#     np.random.randn(200, 3),
#     columns=['a', 'b', 'c'])

# st.vega_lite_chart(chart_data, {
#     'mark': {'type': 'circle', 'tooltip': True},
#     'encoding': {
#         'x': {'field': 'a', 'type': 'quantitative'},
#         'y': {'field': 'b', 'type': 'quantitative'},
#         'size': {'field': 'c', 'type': 'quantitative'},
#         'color': {'field': 'c', 'type': 'quantitative'},
#     },
# })
#=============================p8=======================
# import graphviz

# # Create a graphlib graph object
# graph = graphviz.Digraph()
# graph.edge('run', 'intr')
# graph.edge('intr', 'runbl')
# graph.edge('runbl', 'run')
# graph.edge('run', 'kernel')
# graph.edge('kernel', 'zombie')
# graph.edge('kernel', 'sleep')
# graph.edge('kernel', 'runmem')
# graph.edge('sleep', 'swap')
# graph.edge('swap', 'runswap')
# graph.edge('runswap', 'new')
# graph.edge('runswap', 'runmem')
# graph.edge('new', 'runmem')
# graph.edge('sleep', 'runmem')

# st.graphviz_chart(graph)

#===============p9==============
import streamlit as st
import pandas as pd
import numpy as np

df = pd.DataFrame(
    {"lat":[24.875416331103956,24.864045114946258],
    'lon':[67.05984086574581,66.99526083537985]},

    columns=['lat', 'lon'])

st.map(df)

