#getting a toolbar, widget on GUI with value shown

from traitlets import link

a = FloatText()
b = FloatSlider()

display(a,b)

mylink = link((a,'value'),(b,'value'))

