import decimal

from bokeh.plotting import figure, show
from math import sin


def drange(start, end, step):
    while start < end:
        yield start
        start += start + step


x = [i for i in range(0,10)]
y = [sin(i) + 1 for i in x]

p = figure(title="Multiple glyphs", x_axis_label="x", y_axis_label="y")

circle = p.circle(x, y, line_color="red", fill_color="blue", size=10, legend_label="Discrete sin")
bar = p.vbar(x=x, top=[j-0.25 for j in y], color="DodgerBlue", fill_alpha=0.5, width=0.5)

show(p)
