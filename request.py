import requests
#from pydantic import BaseModel
import pdb
import json
#class DescriptionRequest(BaseModel):
#    user_description: str

# Base URL of your FastAPI app
BASE_URL = "http://10.112.115.25:8000"  # Change this if your app is hosted elsewhere








# Test /isSufficientUserDescription endpoint
description_payload = {
    "user_description": "I want to open a competitor for OpenAI which provides 4 LLM subscriptions. I want to build a financial model which tests the feasibility and the overall return of this. I want to structure the model per subscription model, and want to have the model for 5 years straight, starting from 2026 January. I want to operate in both India, Dubai and London"
}

description_response = requests.post(
    f"{BASE_URL}/isSufficientUserDescription",
    json=description_payload
)

print("\nResponse from /isSufficientUserDescription:")
print(description_response.text)

#OUTPUT-------->Response from /isSufficientUserDescription:
#{"Question 1":"Yes","Question 2":"Yes","Question 3":"Yes","Question 4":"No"}

# Test /isSufficientUserDescription endpoint
#@app.post('/restructure_user_description')
#async def restructure_user_description(description: StringSchema):
#    return restructure_user_description(description)

description_payload = {
    "user_description": "I want to open a competitor for OpenAI which provides 4 LLM subscriptions. I want to build a financial model which tests the feasibility and the overall return of this. I want to structure the model per subscription model, and want to have the model for 5 years straight, starting from 2026 January. I want to operate in both India, Dubai and London"}

description_response2 = requests.post(
    f"{BASE_URL}/restructure_user_description",
    json=description_payload
)

print("\nResponse from /restructure_user_description:")
print(description_response2.text)

#  update_financial_model............pay load
description_payload = {
    "current_logic":str({"financial_model_structure":{"1. Output": [ "1.1 Control Panel", "1.2 Financial Output"], "2. Financial_Statements" : ["2.1 Profit and Loss Statement", "2.2 Balance Sheet", "2.3 Cashflow Statement"], "3. Calculations" : ["3.1 User Base","3.2 Revenue","3.3 Cost","3.4 CapEx","3.5 Depreciation","3.6 Debt Financing"]}}),
    "user_input":"add a step 'overall display' in Output"
}

description_response3 = requests.post(
    f"{BASE_URL}/update_financial_model",
    json=description_payload
)

print("\nResponse from /update_financial_model")
print(description_response3.text)



#  User BAse logic...........pay load
description_payload = {
    "user_description":"I want to open a competitor for OpenAI which provides 4 LLM subscriptions. I want to build a financial model which tests the feasibility and the overall return of this. I want to structure the model per subscription model, and want to have the model for 5 years straight, starting from 2026 January. I want to operate in both India, Dubai and London",
    "user_base_start_month_init":"January",
    "user_base_end_month_init":"December",
    "user_base_year_init":"2025"
}

description_response4 = requests.post(
    f"{BASE_URL}/get_user_base_logic",
    json=description_payload
)

print("\nResponse from /get_user_base_logic")
print(description_response4.text)
#pdb.set_trace()
ub_logic =json.loads(description_response4.text)['user_base_logic']


#  Update User BAse logic...........pay load
description_payload = {
    "current_logic":ub_logic,
    "user_input":"Remove last steps",
    "user_description":"I want to open a competitor for OpenAI which provides 4 LLM subscriptions. I want to build a financial model which tests the feasibility and the overall return of this. I want to structure the model per subscription model, and want to have the model for 5 years straight, starting from 2026 January. I want to operate in both India, Dubai and London"
}

description_response5 = requests.post(
    f"{BASE_URL}/update_user_base_logic",
    json=description_payload
)

print("\nResponse from /update_user_base_logic")
print(description_response5.text)



#  Update User BAse assumption and formula ........pay load
description_payload = {
    "user_description":"I want to open a competitor for OpenAI which provides 4 LLM subscriptions. I want to build a financial model which tests the feasibility and the overall return of this. I want to structure the model per subscription model, and want to have the model for 5 years straight, starting from 2026 January. I want to operate in both India, Dubai and London",
    "User_Base_logic":ub_logic,
    "base_period":["January","December","2025"],
}

description_response6 = requests.post(
    f"{BASE_URL}/get_user_base_ass_formula",
    json=description_payload
)

print("\nResponse from /get_user_base_ass_formula")
print(description_response6.text)



