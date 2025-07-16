import requests
#from pydantic import BaseModel
import pdb
import json
import pandas as pd
#class DescriptionRequest(BaseModel):
#    user_description: str

# Base URL of your FastAPI app
BASE_URL = "http://10.112.115.25:8000"  # Change this if your app is hosted elsewhere

proxies = {
    "http": None,
    "https": None
}



capex_formula={"Step 1: Estimate the cost required to set-up the LLM subscription service industry":["GPU_Infrastructure_Setup_Cost (USD) = Number_of_Geographic_Regions * GPU_Clusters_per_Region * High_Performance_GPUs_per_Cluster * Cost_per_High_Performance_GPU","Data_Center_Infrastructure_Cost (USD) = Number_of_Geographic_Regions * Data_Centers_per_Region * Data_Center_Setup_Cost_per_Location","Core_Infrastructure_Cost (USD) = Number_of_Geographic_Regions * Core_Infrastructure_Servers_per_Region * Cost_per_Infrastructure_Server","Network_and_Security_Setup_Cost (USD) = Number_of_Geographic_Regions * (Network_Infrastructure_Cost_per_Region + Security_and_Compliance_Setup_per_Region)","Regulatory_and_Backup_Setup_Cost (USD) = Number_of_Geographic_Regions * (Regulatory_Compliance_Setup_per_Region + Initial_Backup_and_Disaster_Recovery_per_Region)","LLM_Service_Setup_Costs (USD) = GPU_Infrastructure_Setup_Cost + Data_Center_Infrastructure_Cost + Core_Infrastructure_Cost + Network_and_Security_Setup_Cost + Regulatory_and_Backup_Setup_Cost + LLM_Model_Development_and_Training_Cost + Software_Licensing_and_Development_Tools"],"Step 2: Estimate the cost required to set-up systems for operations":["API_Analytics_Systems_Cost (USD) = Number_of_Geographic_Regions * API_Analytics_Dashboard_Systems_per_Region * Cost_per_API_Analytics_Dashboard_System","User_Analytics_Platform_Cost (USD) = Number_of_Geographic_Regions * User_Facing_Analytics_Platform_per_Region * Cost_per_User_Facing_Analytics_Platform","Subscription_Management_Cost (USD) = Number_of_Geographic_Regions * Subscription_Management_Systems_per_Region * Cost_per_Subscription_Management_System","Performance_Monitoring_Cost (USD) = Number_of_Geographic_Regions * Performance_Monitoring_Systems_per_Region * Cost_per_Performance_Monitoring_System","Customer_Support_Systems_Cost (USD) = Number_of_Geographic_Regions * Customer_Support_Platform_per_Region * Cost_per_Customer_Support_Platform","Data_Analytics_Tools_Cost (USD) = Number_of_Geographic_Regions * Data_Analytics_and_ML_Tools_per_Region * Cost_per_Data_Analytics_and_ML_Tool","Billing_Payment_Systems_Cost (USD) = Number_of_Geographic_Regions * Billing_and_Payment_Processing_Systems_per_Region * Cost_per_Billing_and_Payment_Processing_System","Total_Operational_Systems_Setup_Cost (USD) = API_Analytics_Systems_Cost + User_Analytics_Platform_Cost + Subscription_Management_Cost + Performance_Monitoring_Cost + Customer_Support_Systems_Cost + Data_Analytics_Tools_Cost + Billing_Payment_Systems_Cost"],"Step 3: Estimate the capEx to set-up the office furniture and networking infrastructure":["Employee_Workstation_Setup_Cost (USD) = Number_of_Geographic_Regions * Office_Locations_per_Region * Employees_per_Office_Location * Workstations_per_Employee * Cost_per_Workstation_Setup","Conference_Room_Setup_Cost (USD) = Number_of_Geographic_Regions * Office_Locations_per_Region * Conference_Rooms_per_Office * Cost_per_Conference_Room_Setup","Reception_Common_Areas_Cost (USD) = Number_of_Geographic_Regions * Office_Locations_per_Region * Reception_and_Common_Areas_per_Office * Cost_per_Reception_and_Common_Area","Executive_Office_Setup_Cost (USD) = Number_of_Geographic_Regions * Office_Locations_per_Region * Executive_Offices_per_Office * Cost_per_Executive_Office_Setup","Office_Furniture_Cost (USD) = Employee_Workstation_Setup_Cost + Conference_Room_Setup_Cost + Reception_Common_Areas_Cost + Executive_Office_Setup_Cost","Office_Networking_Hardware_Cost (USD) = Number_of_Geographic_Regions * Office_Locations_per_Region * (Office_Routers_per_Office * Cost_per_Office_Router + Network_Switches_per_Office * Cost_per_Network_Switch)","Office_Infrastructure_Setup_Cost (USD) = Number_of_Geographic_Regions * Office_Locations_per_Region * (Cabling_and_Wiring_per_Office + WiFi_Infrastructure_per_Office + Security_Systems_per_Office)","Networking_Infrastructure_Cost (USD) = Office_Networking_Hardware_Cost + Office_Infrastructure_Setup_Cost","Total_Office_Setup_Cost (USD) = Office_Furniture_Cost + Networking_Infrastructure_Cost"],"Step 4: Estimate the capEx for IT-staff laptops mobiles and operational needs":["Total_Current_Staff_Increase (USD) = Production_staff + Back_office_staff","New_Staff_IT_Cost (USD) = Total_Current_Staff_Increase * Laptop_License_and_Phones_Budget_per_staff","Existing_Staff_Replacement_Cost (USD) = Previous_period_Total_staff * Laptop_License_and_Phones_Budget_per_staff * Older_staff_replacement_share / 100","Total_IT_Staff_Cost (USD) = New_Staff_IT_Cost + Existing_Staff_Replacement_Cost"],"Step 5: Total capex by company":["Other_Capex (USD) = Total_Revenue * other_capex_Share / 100","Total_Capex (USD) = LLM_Service_Setup_Costs + Total_Operational_Systems_Setup_Cost + Total_Office_Setup_Cost + Total_IT_Staff_Cost + Other_Capex"]}
#.....................................

description_payload = {
    "capex_formula":capex_formula,
    "user_description":"I want to open a competitor for OpenAI which provides 4 LLM subscriptions. I want to build a financial model which tests the feasibility and the overall return of this. I want to structure the model per subscription model, and want to have the model for 5 years straight, starting from 2026 January. I want to operate in both India, Dubai and London",
    "revenue_sources_splits":["Basic_LLM", "Standard_LLM", "Executive_LLM"],
    "interval": "yearly",
}

depriciation_time = requests.post(
    f"{BASE_URL}/get_depriciation_time",
    json=description_payload,
    proxies=proxies
)

print("\nResponse from /get_depriciation_time")
print(depriciation_time.text)

#....................................
description_payload = {
    "capex_formula":capex_formula,
}

depriciation_key = requests.post(
    f"{BASE_URL}/get_depriciation_key",
    json=description_payload,
    proxies=proxies
)

print("\nResponse from /get_depriciation_key")
print(depriciation_key.text)
#.................................................................

# def dataframe_dict(df):
#     steps = df[df.columns[0]].tolist()
#     units = df['Unit'].tolist()

#     # Extract values per year into a dictionary
#     years = df.columns[2:]  # ['2025', '2026', '2027']
#     values = {year: df[year].tolist() for year in years}

#     # Final dict representation
#     result = {
#         "steps": steps,
#         "unit": units,
#         "Values": values
#     }
#     return result


# def depreciation_from_capex(interval, capex_df, depreciation_time):
#     period_map = {
#     "yearly": 1,
#     "halfyearly": 2,
#     "quarterly": 4,
#     "monthly": 12
#     }
#     period_multiplier = period_map.get(interval.lower(), 1)
#     time_period = capex_df.columns[2:].to_list()
#     depreciation_df = pd.DataFrame(columns=["CapEx_Category", "Unit"] + time_period )
    
#     depreciation_df["CapEx_Category"] = list(depreciation_time.keys())
#     filtered_df = capex_df[capex_df["CapEx_Category"].isin(depreciation_time.keys())]
#     units_list = filtered_df["Unit"].tolist()
#     depreciation_df["Unit"] = units_list

    

#     for capex_item, useful_life in depreciation_time.items():
#         # Calculating for each items for which depriciation period is defined
#         row = capex_df[capex_df["CapEx_Category"] == capex_item]
#         capex_row_number = capex_df[capex_df["CapEx_Category"] == capex_item].index[0]
#         depr_row_number = depreciation_df[depreciation_df["CapEx_Category"] == capex_item].index[0]
        
#         if not row.empty:
#             row_values = row.iloc[0]
#             yearly_depr = {}
#             #pdb.set_trace()
#             for index, year in enumerate(time_period):
#                 ind = index
#                 count = 0
#                 val = 0 
#                 while(ind>=0 and count<useful_life * period_multiplier):
#                     #pdb.set_trace()
#                     val = val + round(row_values.iloc[2+ind] / (useful_life * period_multiplier), 2)
#                     ind = ind - 1
#                     count = count + 1
#                 #print('val ', val)
#                 depreciation_df.iloc[depr_row_number , 2 + index] = round(val)
                            

#     return dataframe_dict(depreciation_df)

depriciation_Time = json.loads(depriciation_time.text)
steps = json.loads(depriciation_key.text)['component']
units = ['usd']*len(steps)
values = {"2025":[267367, 729839, 893983, 75753, 199398],"2026":[7858,785485,67893, 826828, 2587358],"2027":[35355,1288,99740,868998,758389]}
# depreciation_t ={}
# #pdb.set_trace()
# for i in range(len(depriciation_Time["steps"])):
#     depreciation_t[steps[i]] =depriciation_Time["values"][i]

# data = {
# "CapEx_Category": steps,
# "Unit":units}
# data = {**data, **values}

# capex_df = pd.DataFrame(data)
# interval="yearly"
# #depriciation = depreciation_from_capex(interval, capex_df, depreciation_t)
# pdb.set_trace()

description_payload = {
    "steps":steps,
    "units":units,
    "values":values,
    "depriciation_time_value":depriciation_Time['values'],
    "interval":"yearly"
}

depriciation_key = requests.post(
    f"{BASE_URL}/get_depriciation",
    json=description_payload,
    proxies=proxies
)

print("\nResponse from /get_depriciation")
print(depriciation_key.text)