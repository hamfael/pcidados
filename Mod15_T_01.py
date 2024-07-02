import streamlit as st
import pandas as pd
import numpy as np
import time

#seguindo o main concepts tutorial

st.write("# This is my tutorial following of streamlit #")

# 1 displaying a data frame without st.write()
st.write("1. displaying a data frame without st.write()")
df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

df

# 2 using st.write() for the same df
st.write("2. Here's our first attempt at using data to create a table:")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))

# 3 styling a data frame
st.write("3. styling a data frame")
dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))

st.dataframe(dataframe.style.highlight_max(axis=0))

# 4 streamlit also generates a table with st.table()
st.write("4. streamlit also generates a table with st.table()")
dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))
st.table(dataframe)

# 5 drawing a line chart
st.write("5. drawing a line chart")
chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)

# 6 plotting a map
st.write("6. plotting a map")
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)

# 7 widgets with st.slider()
st.write("7. widgets with st.slider(), squaring a number")
import streamlit as st
x = st.slider('x')  # 👈 this is a widget
st.write(x, 'squared is', x * x)

# 8 using checkboxes to show or hide data
st.write("8. using checkboxes to show or hide data")
if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    chart_data

# 9 using a selectbox for any options that i want
st.write("9. using a selectbox for any options that i want")
df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
    })

option = st.selectbox(
    'Which number do you like best?',
     df['first column'])

'You selected: ', option

# 10 organizing my layout with sidebar
# Add a selectbox to the sidebar:
add_selectbox = st.sidebar.selectbox(
    '10. How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)

# Add a slider to the sidebar:
add_slider = st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)

# 11 organize with st.columns

left_column, right_column = st.columns(2)
# You can use a column just like st.sidebar:
left_column.button('11. Press me!')

# Or even better, call Streamlit functions inside a "with" block:
with right_column:
    chosen = st.radio(
        '11. Sorting hat',
        ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
    st.write(f"You are in {chosen} house!")

# 12 show progrees of long computations

# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'11. Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.1)

'...and now we\'re done! OR NOT!'

# 13 second tutorial starting, Uber pickups
st.title('Num 13-20 - Uber pickups in NYC')

# 14 fetching some data
DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
         'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

# 15  testing the output

# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')
# Load 10,000 rows of data into the dataframe.
data = load_data(10000)
# Notify the reader that the data was successfully loaded.
#data_load_state.text('Loading data...done!')

# 16 changing the fetch to a better code
data_load_state.text("Done! (using st.cache_data)")

# 17 inspecting raw data
st.subheader('Raw data')
st.write(data)

# 18 drawing a histogram
st.subheader('Number of pickups by hour')
hist_values = np.histogram(
    data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
st.bar_chart(hist_values)

# 19 plotting data on a map
st.subheader('Map of all pickups')
st.map(data)

# 20 selecting best hour to pickup
hour_to_filter = 17
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]
st.subheader(f'Map of all pickups at {hour_to_filter}:00')
st.map(filtered_data)