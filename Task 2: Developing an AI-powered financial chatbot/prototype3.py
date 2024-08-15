from flask import Flask, request, render_template, jsonify
import pandas as pd

# Initialize Flask app
app = Flask(__name__)

# Load datasets
trends_data = pd.read_csv('trends_data.csv')
summary_trends_data = pd.read_csv('summary_trends_data.csv')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/query', methods=['POST'])
def handle_query():
    company_input = request.form['company'].capitalize()
    fiscal_year = int(request.form['fiscal_year'])
    user_query = request.form['query'].strip().lower()

    def financial_chatbot():
        # Process the query
        if user_query == "total revenue":
            result = trends_data[(trends_data['Fiscal Year'] == fiscal_year) & (trends_data['Company'] == company_input)]['Total Revenue'].values[0]
            return f"The Total Revenue for {company_input} for fiscal year {fiscal_year} is $ {result}"
        
        elif user_query == "net income":
            result = trends_data[(trends_data['Fiscal Year'] == fiscal_year) & (trends_data['Company'] == company_input)]['Net Income'].values[0]
            return f"The Net Income for {company_input} for fiscal year {fiscal_year} is $ {result}"
        
        elif user_query == "sum of total assets":
            result = trends_data[(trends_data['Fiscal Year'] == fiscal_year) & (trends_data['Company'] == company_input)]['Total Assets'].values[0]
            return f"The Sum of Total Assets for {company_input} for fiscal year {fiscal_year} is $ {result}"
        
        elif user_query == "sum of total liabilities":
            result = trends_data[(trends_data['Fiscal Year'] == fiscal_year) & (trends_data['Company'] == company_input)]['Total Liabilities'].values[0]
            return f"The Sum of Total Liabilities for {company_input} for fiscal year {fiscal_year} is $ {result}"
        
        elif user_query == "cash flow from operating activities":
            result = trends_data[(trends_data['Fiscal Year'] == fiscal_year) & (trends_data['Company'] == company_input)]['Cash Flow from Operating Activities'].values[0]
            return f"The Cash Flow from Operating Activities for {company_input} for fiscal year {fiscal_year} is $ {result}"
        
        elif user_query == "revenue growth(%)":
            result = trends_data[(trends_data['Fiscal Year'] == fiscal_year) & (trends_data['Company'] == company_input)]['Revenue Growth (%)'].values[0].round(4)
            return f"The Revenue Growth(%) for {company_input} for fiscal year {fiscal_year} is {result}%"
        
        elif user_query == "net income growth(%)":
            result = trends_data[(trends_data['Fiscal Year'] == fiscal_year) & (trends_data['Company'] == company_input)]['Net Income Growth (%)'].values[0].round(4)
            return f"The Net Income Growth(%) for {company_input} for fiscal year {fiscal_year} is {result}%"
        
        elif user_query == "assets growth(%)":
            result = trends_data[(trends_data['Fiscal Year'] == fiscal_year) & (trends_data['Company'] == company_input)]['Assets Growth (%)'].values[0].round(4)
            return f"The Assets Growth(%) for {company_input} for fiscal year {fiscal_year} is {result}%"
        
        elif user_query == "liabilities growth(%)":
            result = trends_data[(trends_data['Fiscal Year'] == fiscal_year) & (trends_data['Company'] == company_input)]['Liabilities Growth (%)'].values[0].round(4)
            return f"The Liabilities Growth(%) for {company_input} for fiscal year {fiscal_year} is {result}%"
        
        elif user_query == "cash flow from operations growth(%)":
            result = trends_data[(trends_data['Fiscal Year'] == fiscal_year) & (trends_data['Company'] == company_input)]['Cash Flow from Operations Growth(%)'].values[0].round(4)
            return f"The Cash Flow from Operations Growth(%) for {company_input} for fiscal year {fiscal_year} is {result}%"
        
        elif user_query == "year by year average revenue growth rate(%)":
            result = summary_trends_data[(summary_trends_data['Company'] == company_input)]['Revenue Growth (%)'].values[0].round(4)
            return f"The Year By Year Average Revenue Growth Rate(%) from 2021 to 2023 for {company_input} is {result}%"
        
        elif user_query == "year by year average net income growth rate(%)":
            result = summary_trends_data[(summary_trends_data['Company'] == company_input)]['Net Income Growth (%)'].values[0].round(4)
            return f"The Year By Year Net Income Growth Rate(%) from 2021 to 2023 for {company_input} is {result}%"
        
        elif user_query == "year by year average assets growth rate(%)":
            result = summary_trends_data[(summary_trends_data['Company'] == company_input)]['Assets Growth (%)'].values[0].round(4)
            return f"The Year By Year Average Assets Growth Rate(%) from 2021 to 2023 for {company_input} is {result}%"
        
        elif user_query == "year by year average liabilities growth rate(%)":
            result = summary_trends_data[(summary_trends_data['Company'] == company_input)]['Liabilities Growth (%)'].values[0].round(4)
            return f"The Year By Year Average Liabilities Growth Rate(%) from 2021 to 2023 for {company_input} is {result}%"
        
        elif user_query == "year by year average cash flow from operations growth rate(%)":
            result = summary_trends_data[(summary_trends_data['Company'] == company_input)]['Cash Flow from Operations Growth(%)'].values[0].round(4)
            return f"The Year By Year Average Cash Flow from Operations Growth Rate(%) from 2021 to 2023 for {company_input} is {result}%"
        
        else:
            return "Invalid Query"
        
    response = financial_chatbot()
    return response

if __name__ == '__main__':
    app.run(debug=True)
