from openai import OpenAI
import json
import pandas as pd

client = OpenAI()

def extract_financial_data(text):
    prompt = '''
    Review the company name, revenue, net income and earnings per share from the following news article. If you are unable to find this
    information then return "". Also retrieve the stock symbol corresponding to the company. For this you can use general knowledge. Always return
    the output as a valid json string.
    The format of the output must be:
    {
        "Company name": "Walmart"
        "Stock Symbol": "WMT"
        "Revenue": "1.2 million"
        "Net income": "34 million"
        "EPS": "$2.1"
    }

    ''' + text
    response = client.responses.create(
        model="gpt-4.1",
        input=[
            {
                "role": "user",
                "content": prompt
            }    ]
    )

    content = response.output_text

    try:
        data = json.loads(content) # makes the content in dictionary format
        return pd.DataFrame(data.items(), columns=["Measure","Value"]) #The rows become the dictionary elements and columns become measure and val
    except (json.JSONDecodeError, IndexError):
        pass
    
    return pd.DataFrame({
        "Measure": ["Company Name","Stock Symbol","Revenue","Net Income","EPS"],
        "Value":["","","","",""]
    })

if __name__=='__main__':
    text = '''Tesla's Earning news in text format: Tesla's earning this quarter blew all the estimates. They reported 4.5 billion $ profit against a revenue of 30 billion $. Their earnings per share was 2.3 $'''
    df = extract_financial_data(text)
    print(df.to_string())


### build a financial data extraction tool
## takes in an article as input text and generates a structured output like a dictionary