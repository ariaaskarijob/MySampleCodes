from traitlets import link

a = FloatText()
b = FloatSlider()

display(a,b)

mylink = link((a,'value'),(b,'value'))

