import matplotlib.pyplot as plt # plotting the chart
import matplotlib.patches as patches # add yellow rectangle
import pandas as pd # data manipulation
from matplotlib.patches import Rectangle


# df = pd.read_csv('CL_1min.csv', sep=',')
# open1 = round(df['open'], 2)
# timestamp1 = pd.to_datetime(df['timestamp'])
#
# # df.hist()
# df.hist(by='timestamp', figsize=[12, 8], bins=6)
url = 'https://raw.githubusercontent.com/holtzy/The-Python-Graph-Gallery/master/static/data/insee_salaries.csv'

df = pd.read_csv(url)

# Initialize layout in polar coordinates
fig, ax = plt.subplots(figsize=(6, 8))

# Add grey background in the ax and fig
ax.set_facecolor('whitesmoke')
fig.set_facecolor('whitesmoke')

# Define colors to use for each bar
colors = ['navy', 'steelblue', 'steelblue', 'black', 'black', 'darkred',
          'darkred', 'darkred', 'darkred', 'red', 'red', 'lightcoral', 'lightsalmon',
          'orange', 'yellow', 'lightyellow']

# Create the plot
ax.barh(df['range'], df['people'],
        color=colors, # colors that we want
        zorder=2, # specify that the bars is drawn after the grid
       )

# Add a vertical grey line at the relative position
ax.grid(linestyle='-', # type of lines
        alpha=0.5, # opacity
        axis='x', # specify that we only want vertical lines
       )

# Title of our graph
title = 'La pyramide des salaires'
fig.text(-0.08, 1.01, # relative postion
         title,
         fontsize=25, # High font size for style
         fontweight = 'bold',
         ha='left', # align to the left
         family='dejavu sans'
        )

# Subtitle of our graph
subtitle = 'Distribution des salaires mensuels en 2021*'
fig.text(-0.08, 0.94, # relative postion
         subtitle,
         fontsize=13, # High font size for style
         color='dimgrey',
         ha='left', # align to the left
         family='dejavu sans'
        )

# Details and Credit
text = '*France hors Mayotte, salariés du privé et des entreprises publiques\nSource Insee'
fig.text(-0.08, 0.05, # relative postion
         text,
         fontsize=10, # High font size for style
         color='dimgrey',
         ha='left', # align to the left
         family='dejavu sans'
        )

# Remove the spines (border lines) from the chart
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)

# Change axis position and labels
ax.tick_params(axis='y', labelsize=12)
ax.set_xticklabels(['0', '1M', '2M', '3M', '4M', '5M', '6M'])
ax.xaxis.tick_top()

# Add yellow rectangle
rectangle_color = 'gold'
rect = patches.Rectangle((-0.13, 0.93), 0.03, 0.13,
                         linewidth=1, edgecolor=rectangle_color,
                         facecolor=rectangle_color, transform=fig.transFigure)
fig.patches.append(rect)

# Add percents
ax.text(0.6,0.93, # relative position
        '19,5%', # label
        transform=ax.transAxes,
        size=10, # text size
       )
ax.text(0.98,0.87, # relative position
        '30,2%', # label
        transform=ax.transAxes,
        size=10, # text size
       )
ax.text(0.62,0.8, # relative position
        '18,6%', # label
        transform=ax.transAxes,
        size=10, # text size
       )
ax.text(0.37,0.74, # relative position
        '10,8%', # label
        transform=ax.transAxes,
        size=10, # text size
       )
ax.text(0.25,0.65, # relative position
        '10,6%', # label
        transform=ax.transAxes,
        size=10, # text size
       )
ax.text(0.14,0.46, # relative position
        '6,7%', # label
        transform=ax.transAxes,
        size=10, # text size
       )
ax.text(0.08,0.22, # relative position
        '1,8%', # label
        transform=ax.transAxes,
        size=10, # text size
       )
ax.text(0.1,0.06, # relative position
        '1,6%', # label
        transform=ax.transAxes,
        size=10, # text size
       )

# Display the final chart
plt.show()