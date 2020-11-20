
##HOW TO RUN APP 
! python3 acdc_lyrics/acdc.py

##HOW TO SOLVE ImportError: `iplot` can only run inside an IPython Notebook ERROR

Original Code was 
import plotly
from plotly.offline import iplot, init_notebook_mode
from plotly import tools
import plotly.graph_objs as go
init_notebook_mode(connected=True)
 
trace = {'type': 'bar', 'x': list(unique_words), 'y': list(word_histogram.values())}
plotly.offline.iplot({'data': [trace]})

##SOLUTION 
If we run plotly interactive functions (i prefix) in a normal Python code (i.e. not IPython Notebook). iplot provides an interactive graph with which we can play inside the notebook.

We can solve this issue by removing iplot import and replacing it with normal plot. Then we need to remove iplot_mpl and init_notebook_mode from imports







https://stackoverflow.com/questions/53978924/importerror-iplot-can-only-run-inside-an-ipython-notebook