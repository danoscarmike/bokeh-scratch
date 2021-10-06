from bokeh.plotting import figure, show
from math import sin
from random import randint


x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y1 = [randint(0, 10) for _ in range(10)]
y2 = [sin(i) + 1 for i in x]

# create a new plot with a title and axis labels
p = figure(title="Simple lines", x_axis_label="x", y_axis_label="y")

# add a line renderer with legend and line thickness to the plot
p.line(x, y1, legend_label="Random y", line_width=2)
p.line(x, y2, legend_label="Sin(x) + 1", line_color="red", line_width=2)

show(p)
