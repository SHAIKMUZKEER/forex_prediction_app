# 📈 Forex Price Prediction using Machine Learning
## Project link : https://colab.research.google.com/drive/1QerUWKk75pYCqF3OzrkS4cNC_JjR7wwe?usp=sharing

## 📌 Project Overview

This project focuses on forecasting Forex market prices using Machine Learning techniques on the EUR/USD currency pair dataset. The project performs:

* Data preprocessing
* Time-series feature engineering
* Volatility analysis
* Liquidity analysis
* Correlation analysis
* Outlier checking
* Forecasting Bid Closing prices using Ridge Regression

The model is trained on historical Forex hourly market data and predicts the future Bid Closing price (`BC`).

---

# 🎯 Project Objective

The main objective of this project is to:

* Analyze Forex market behavior
* Understand volatility and liquidity patterns
* Build a regression-based forecasting model
* Predict future Bid Closing prices
* Perform exploratory data analysis on Forex trends

---

# 🛠️ Technologies Used

## 🔹 Programming Language

* Python

## 🔹 Libraries Used

* NumPy
* Pandas
* Matplotlib
* Seaborn
* Scikit-learn

---

# 📂 Dataset Information

The project uses an hourly EUR/USD Forex dataset.

Dataset File:

```bash
eurusd_hour.csv
```

## 📊 Dataset Features

| Column | Meaning          |
| ------ | ---------------- |
| Date   | Trading date     |
| Time   | Trading hour     |
| BO     | Bid Open price   |
| BH     | Bid High price   |
| BL     | Bid Low price    |
| BC     | Bid Close price  |
| AO     | Ask Open price   |
| AH     | Ask High price   |
| AL     | Ask Low price    |
| AC     | Ask Close price  |
| BCh    | Bid price change |
| ACh    | Ask price change |

---

# ⚙️ Project Workflow

## 1️⃣ Importing Required Libraries

The project starts by importing essential libraries for:

* Data handling
* Visualization
* Machine Learning
* Evaluation metrics

---

## 2️⃣ Data Loading and Preprocessing

### Steps Performed:

* Loaded dataset using Pandas
* Checked dataset information
* Statistical analysis using `describe()`
* Null value checking
* Converted Date and Time into DateTime format
* Set DateTime as index

---

## 3️⃣ Feature Engineering

Additional time-series features were created:

| Feature | Description  |
| ------- | ------------ |
| day     | Day of month |
| month   | Month value  |
| year    | Year value   |
| hour    | Hour value   |

---

# 📉 Volatility Analysis

Volatility measures the market price fluctuations.

## Formula Used

```python
volatility = BH - BL
```

Rolling averages were applied for smoothing:

```python
rolling(window = 168)
```

This helps analyze:

* Weekly market momentum
* Market fluctuation trends
* Price stability patterns

---

# 💧 Liquidity Analysis

Liquidity indicates how easily buyers and sellers trade in the market.

## Spread Calculation

```python
spread = AC - BC
```

## Liquidity Formula

```python
liquidity = 1 / spread
```

The project analyzes:

* Buyer and seller market activity
* Seasonal liquidity trends
* Relationship between liquidity and spread

---

# 📊 Data Visualization

Several visualizations were created:

## 🔹 Line Plots

Used for:

* Volatility trends
* Weekly market changes
* Seasonal analysis

## 🔹 Scatter Plot

Used for:

* Liquidity vs Spread relationship

## 🔹 Heatmap

Used for:

* Correlation between all features

## 🔹 Boxplot

Used for:

* Outlier detection

---

# 🤖 Machine Learning Model

## Model Used

```python
Ridge Regression
```

Ridge Regression was selected to:

* Reduce overfitting
* Handle multicollinearity
* Improve prediction stability

---

# 🧠 Target Variable

The forecasting target is:

```python
BC -> Bid Closing Price
```

---

# 🔀 Train-Test Split

The dataset was split manually:

```python
80% -> Training Data
20% -> Testing Data
```

---

# 📏 Evaluation Metrics

The model performance was evaluated using:

| Metric   | Purpose                 |
| -------- | ----------------------- |
| MSE      | Mean Squared Error      |
| RMSE     | Root Mean Squared Error |
| MAE      | Mean Absolute Error     |
| R² Score | Model accuracy          |

---

# 📈 Prediction Visualization

Scatter plots were used to compare:

* Actual prices
* Predicted prices

This helps evaluate prediction quality visually.

---

# 🚀 How to Run the Project

## Step 1 — Clone Repository

```bash
git clone <repository-url>
```

---

## Step 2 — Install Dependencies

```bash
pip install numpy pandas matplotlib seaborn scikit-learn
```

---

## Step 3 — Run Jupyter Notebook

```bash
jupyter notebook
```

Open:

```bash
forex_forcasting.ipynb
```

---

# 📁 Project Structure

```bash
Forex_Prediction/
│
├── eurusd_hour.csv
├── forex_forcasting.ipynb
├── README.md
└── requirements.txt
```

---

# 🔥 Key Learning Outcomes

Through this project:

* Time-series preprocessing was performed
* Volatility and liquidity were analyzed
* Feature engineering was applied
* Ridge Regression was implemented
* Model evaluation metrics were used
* Financial data visualization techniques were practiced

---

# 📌 Future Improvements

Future upgrades for this project:

* Use LSTM or GRU Deep Learning models
* Add real-time Forex API integration
* Deploy model using Streamlit or Flask
* Add hyperparameter tuning
* Use advanced technical indicators
* Create interactive dashboard visualization

---

# 👨‍💻 Author

Developed by Muzkeer

---

# ⭐ Conclusion

This project demonstrates an end-to-end Machine Learning workflow for Forex market prediction using historical EUR/USD data. It combines financial market analysis, feature engineering, visualization, and regression modeling to forecast Bid Closing prices effectively.
