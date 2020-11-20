## Welcome to AC/DC Lyrics Counter App!

This is a simple Python CLI app to word count AC/DC lyrics and visualize data with Plotly. This small project is inspired by a Youtube Video in which an imaginary AC/DC song was created through implementing Markov Chain Analysis and Simulation using Python. https://www.youtube.com/watch?v=vpEVsDN84Hc&ab_channel=FunkTurkey

This app uses AC/DC TNT lyrics as base and visualize most used words in the song.

## Installation
1- Fork the repository and clone it 
2- Makesure Plotly is installed 
https://plotly.com/python/getting-started/
3- run ! python3 acdc_lyrics/acdc.py in your terminal

## Troubleshooting 
#HOW TO SOLVE ImportError: `iplot` can only run inside an IPython Notebook ERROR

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

## Contributing
Bug reports and pull requests are welcome on GitHub at https://github.com/korayozkal/acdc_lyrics This project is intended to be a safe, welcoming space for collaboration, and contributors are expected to adhere to the Contributor Covenant code of conduct.

## License
The gem is available as open source under the terms of the MIT License.


