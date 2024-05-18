import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.title('IPL 2018-2023')

st.sidebar.title('Choose Category here....!')

st.sidebar.selectbox('Batting',['Most Run', 'Highest Scores', 'Best Batting Average', 'Best Batting Strike Rate', 'Most Hundreds', 'Most Fities', 'Mosst Fours', 'Most Sixes'])
st.sidebar.selectbox('Bowling',['Most Wickets', 'Best Bowling Average', 'Best Bowling', 'Most 5 Wickets Haul', 'Best Economy', 'Best Bowling Strike Rate'])




