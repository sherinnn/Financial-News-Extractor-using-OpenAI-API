# Financial Data Extractor from News 

This is a simple Streamlit app that takes a block of financial news text (e.g., earnings reports 🧾) and extracts structured financial data like:

- Company Name
- Stock Symbol
- Revenue
- Net Income
- Earnings Per Share (EPS)

It uses OpenAI's GPT-4 model to parse the text and return a JSON-formatted response which is then displayed as a tidy dataframe.

---

## Features

- Paste any financial article or earnings snippet
- AI extracts key financial metrics
- Clean and readable output as a table
- Built with Streamlit + OpenAI API

---

## Example Input

Tesla's earning this quarter blew all the estimates. They reported 4.5 billion $ profit against a revenue of \\$30 billion. Their earnings per share was 2.3 $.


## Output

| Measure        | Value         |
|----------------|---------------|
| Company Name   | Tesla         |
| Stock Symbol   | TSLA          |
| Revenue        | 30 billion $  |
| Net Income     | 4.5 billion $ |
| EPS            | $2.3          |

---

## Setup Instructions

### 1. Clone the repo
```bash
git clone https://github.com/yourusername/financial_extractor.git
cd financial_extractor
```
### 2. Install dependencies
Make sure you have Python 3.8+ installed.
```bash
pip install -r requirements.txt
```
### 3. Set your OpenAI API key
For Windows:
```bash
set OPENAI_API_KEY="your-api-key"
```
### 4. Run the app 
```bash
streamlit run app.py
```

