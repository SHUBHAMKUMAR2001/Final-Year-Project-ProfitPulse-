from matplotlib.pyplot import axis
import streamlit as st  # streamlit library
import pandas as pd  # pandas library
import yfinance as yf  # yfinance library
import datetime  # datetime library
from datetime import date
from plotly import graph_objs as go  # plotly library
from plotly.subplots import make_subplots
from prophet import Prophet  # prophet library
# plotly library for prophet model plotting
from prophet.plot import plot_plotly
import time  # time library
from streamlit_option_menu import option_menu  # select_options library


st.set_page_config(layout="wide", initial_sidebar_state="expanded")

# Get today's date, day, and current time with seconds
today_date_time = datetime.datetime.now().strftime("%A, %d %B %Y ")

# CSS style for the topmost position and gap
top_style = """
<style>
.top-section {
    position: absolute;
    top: 10px;
    left: 10px;
    font-size: 20px;
    color: #FFFFFF;
    margin-bottom: 20px;
}
</style>
"""

# Display today's date, day, and current time with seconds at the topmost position with CSS styling
st.markdown(top_style, unsafe_allow_html=True)
# st.write(f'<div class="top-section">Today is {today_date_time}</div>', unsafe_allow_html=True)

# Add a 30px gap
st.markdown('<div style="margin-top: 30px;"></div>', unsafe_allow_html=True)

st.sidebar.write(
    '''🔍 <span style="font-size: 25px;color:yellow;font-weight:bold;font-style:italic">Explorer''', unsafe_allow_html=True)

# Main content

import streamlit as st

# Define the functionalities
functionality_options = ["Select Stock Market","Indian Stock Market", "Global Stock Market"]

# Set up the dropdown menu in the sidebar
option = st.sidebar.selectbox("Select Stock Market", functionality_options)

st.markdown(f'<span style="font-size: 35px; font-weight: bold;color:yellow; font-style: italic;">📈 {option}</span>', unsafe_allow_html=True)

# Additional dropdown based on selected option
if option == "Indian Stock Market":
    additional_option = st.sidebar.selectbox("Select Topic to learn", [
                                             "Select the Topic","Stocks Performance Comparison: NSE", "Real-Time Stock Price: Indian Stocks", "Stock Prediction: Indian Stocks"])

    if additional_option == "Stocks Performance Comparison: NSE":
        st.markdown('<span style="font-size: 25px; font-weight: bold;color:skyblue; font-style: italic;">Stocks Performance Comparison</span>', unsafe_allow_html=True)
        st.write("- In this section, we analyze the performance of stocks listed on the National Stock Exchange (NSE).")
        st.write("- We compare various stocks based on their historical data, including factors such as price movements, volume, and market capitalization.")
        st.write("- By examining these metrics, investors can gain insights into market trends and make informed decisions.")
        st.write("- Performance Metrics: Evaluate stock performance using key metrics such as average return, volatility, and relative strength index (RSI).")
        st.write("- Visualization Tools: Employ various visualization techniques such as line charts, bar charts, and candlestick charts to visualize stock performance over time.")
        st.write("- Investment Insights: Leverage the insights gained from stock performance comparison to make informed investment decisions and optimize portfolio management strategies.")
    elif additional_option == "Real-Time Stock Price: Indian Stocks":
        st.markdown('<span style="font-size: 25px; font-weight: bold;color:skyblue; font-style: italic;">Real-Time Stock Price: Indian Stocks</span>', unsafe_allow_html=True)
        st.write("- In this section, we provide real-time data for stocks listed on the National Stock Exchange (NSE).")
        st.write("- The data includes live stock prices, which are updated continuously throughout the trading day.")
        st.write("- We visualize the real-time data using line charts and candlestick charts to track price movements and identify patterns.")
    elif additional_option == 'Stock Prediction: Indian Stocks':
        st.markdown('<span style="font-size: 25px; font-weight: bold; color: skyblue;">Stock Prediction: Indian Stocks</span>', unsafe_allow_html=True)
        st.write("In this section, we provide predictions for future stock prices of Indian stocks. Here's what you can expect:")
        st.write("- Machine Learning Models: Predict future stock prices using advanced algorithms.")
        st.write("- Historical Data Analysis: Analyze past stock price data for insights.")
        st.write("- Feature Engineering: Utilize additional data attributes for prediction.")
        st.write("- Time Series Analysis: Understand trends and patterns in stock prices.")
        st.write("- Model Training and Evaluation: Train and evaluate prediction models.")
        st.write("- Prediction Horizon: Choose the prediction time frame (1 to 4 years).")
        st.write("- Visualization: View predicted stock prices on interactive graphs.")
        st.write("- Error Metrics: Assess prediction accuracy using metrics.")
        st.write("- Sensitivity Analysis: Study the impact of different factors on predictions.")
    elif additional_option == 'Select the Topic':
        st.markdown('<span style="font-size: 25px; font-weight: bold; color: skyblue;">Select what you wish to learn about the Indian Stock Market !</span>', unsafe_allow_html=True)

elif option == "Global Stock Market":
    additional_option = st.sidebar.selectbox("Select Topic to learn", ["Select the Topic","Stock Index Dashboard", "Portfolio Simulation"])

    if additional_option == "Stock Index Dashboard":
        st.markdown('<span style="font-size: 25px; font-weight: bold; color: skyblue;">Stock Index Dashboard</span>', unsafe_allow_html=True)
        st.write("In this section, you can explore historical data for various stock indices from different regions. Here's what you can find:")
        st.write("- **Index Historical Closing Prices**:")
        st.write("   - Explore historical closing prices for different stock indices.")
        st.write("   - View closing prices from various regions including US & Canada, South & Latin America, ASEAN, Oceania & Middle East, Other Asia, and Europe.")

        st.write("- **Price Changes with Respect to Start Date**:")
        st.write("   - Analyze price changes of indices from the start date (2010/01/01) to the end date (2024/04/01).")

        st.write("- **Trading Volume Changes with Respect to Start Date**:")
        st.write("   - Examine changes in trading volume of indices from the start date to the end date.")

        st.write("- **Closing Price Distribution Boxplots**:")
        st.write("   - Visualize the distribution of closing prices for different indices using boxplots.")

        st.write("- **Trading Volume Distribution Boxplots**:")
        st.write("   - View the distribution of trading volumes for various indices through boxplots.")

        st.write("- **Correlation Matrix of Indices' Daily Returns**:")
        st.write("   - Understand the correlation between daily returns of different stock indices using a correlation matrix.")

    elif additional_option == "Portfolio Simulation":
        st.markdown('<span style="font-size: 25px; font-weight: bold; color: skyblue;">Portfolio Simulation</span>', unsafe_allow_html=True)
        st.write("In this section, you can explore historical data for various stock indices from different regions. Here's what you can find:")
        st.write("- Efficient Frontier simulation, by entering a custom amount and lookback period")
        st.write("- Modern Portfolio Theory (MPT)")
        st.write("- Optimal portfolios with highest expected return for a given risk level")
        st.write("- Lowest risk for a given expected return")
        st.write("- Assumptions in the market")
        st.write("  - Rational and risk-averse investors")
        st.write("  - Efficient markets")
        st.write("  - Normal distribution of asset returns")
        st.write("  - Correlation between assets")
        st.write("  - Access to same information")
        st.write("  - Risk-free rate")
        st.write("  - Trading in fractional shares")
        st.write("- Constructing portfolios for best balance of risk and return")
        st.write("- Security Market Line (SML)")
        st.write("- Portfolio Value at Risk (VaR) simulation")
        st.write("- Portfolio asset distribution and performance")
        st.write("- Minimum risk portfolio")
        st.write("- Maximum return portfolio")
        st.write("- Highest Sharpe ratio portfolio")
        st.write("- Other relevant information:")
        st.write("  - US Treasury yield")
        st.write("  - Correlation matrix of daily returns")
    elif additional_option == 'Select the Topic':
        st.markdown('<span style="font-size: 25px; font-weight: bold; color: skyblue;">Select what you wish to learn about the Global Stock Market !</span>', unsafe_allow_html=True)