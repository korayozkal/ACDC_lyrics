

import plotly.graph_objs as go
from plotly import tools
from plotly.offline import plot
import plotly
# I am using a library called Plotly to make our charts.
# In the first four lines we connect Python to Plotly and get ready to use this library.

lyrics = "oi oi oi oi oi oi oi oi oi oi oi oi oi oi oi oi oi oi Cause I am TNT I am dynamite TNT I will win the fight TNT  I am a power load TNT watch me explode TNT oi oi oi TNT oi oi oi TNT oi oi oi  TNT oi oi oi"

list_of_lyrics = lyrics.split(' ')
# print(list_of_lyrics)

number_of_objects = len(list_of_lyrics)
# print(number_of_objects)

unique_words = set(list_of_lyrics)
# print(unique_words)

number_of_unique_words = len(unique_words)
# print(number_of_unique_words)
#word_histogram = dict.fromkeys(unique_words, 0)
# print(word_histogram)
# with for in:
# We are creating a dictornary with each key as a separate word,
# and then set the corresponding value to zero
# unique_words list and the fromkeys method, whose second argument is the value we set for each key


word_histogram = dict.fromkeys(unique_words, 0)
for word in list_of_lyrics:
    word_histogram[word] = word_histogram[word] + 1
# we want to find the related key in the dictionary, word_histogram, and increase the value by one.
# we will loop through each of our words in list_of_lyrics, find the related value in the dictionary, and increase it by one.
print(word_histogram)
# print(word_histogram["oi"])

# And in the last line we tell Python to plot our trace
# A trace points to a dictionary with a key of x that points to a list of x_values,
# and a key of y that points to y_values. And a type to indicate that this will be a bar chart.

trace = {'type': 'bar', 'x': list(
    unique_words), 'y': list(word_histogram.values())}

plotly.offline.plot({'data': [trace]})
