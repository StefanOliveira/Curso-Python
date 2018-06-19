Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:14:34) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import matplotlib.pyplot as plt
>>> x = [1,2,3,4,5,6]
>>> y = [ 1500,1800,2000,1300,1200,2300]
>>> plt.plot(x,y)
[<matplotlib.lines.Line2D object at 0x00F26110>]
>>> plt.show()
>>> legenda = ['Janeiro','Fevereiro','Março','Abril','Maio','Junho']
>>> plt.xticks(x,legenda)
([<matplotlib.axis.XTick object at 0x00F763F0>, <matplotlib.axis.XTick object at 0x00F64FD0>, <matplotlib.axis.XTick object at 0x00F64E50>, <matplotlib.axis.XTick object at 0x036E9870>, <matplotlib.axis.XTick object at 0x036E9B50>, <matplotlib.axis.XTick object at 0x036E9E30>], <a list of 6 Text xticklabel objects>)
>>> plt.plot[x,y]
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    plt.plot[x,y]
TypeError: 'function' object is not subscriptable
>>> plt.plot(x,y)
[<matplotlib.lines.Line2D object at 0x036F3390>]
>>> plt.show
<function show at 0x08016348>
>>> plt.show()
>>> 
