import requests
#from pydantic import BaseModel
import pdb
import json

#class DescriptionRequest(BaseModel):
#    user_description: str

# Base URL of your FastAPI app
BASE_URL = "http://10.112.115.25:8000"  # Change this if your app is hosted elsewhere

proxies = {
    "http": None,
    "https": None
}



assumptions= {"India_Total_Population":1400000000,"UAE_Total_Population":10000000,"UK_Total_Population":67000000,"India_Internet_Penetration (%)":45,"UAE_Internet_Penetration (%)":99,"UK_Internet_Penetration (%)":95,"India_High_Income_Share (%)":15,"India_Mid_Income_Share (%)":35,"India_Low_Income_Share (%)":50,"UAE_High_Income_Share (%)":40,"UAE_Mid_Income_Share (%)":45,"UAE_Low_Income_Share (%)":15,"UK_High_Income_Share (%)":30,"UK_Mid_Income_Share (%)":50,"UK_Low_Income_Share (%)":20,"High_Income_AI_Adoption_Rate (%)":25,"Mid_Income_AI_Adoption_Rate (%)":15,"Low_Income_AI_Adoption_Rate (%)":5,"India_Enterprise_Count":65000000,"UAE_Enterprise_Count":400000,"UK_Enterprise_Count":5700000,"Small_Enterprise_Share (%)":85,"Medium_Enterprise_Share (%)":12,"Large_Enterprise_Share (%)":3,"Small_Enterprise_AI_Adoption_Rate (%)":8,"Medium_Enterprise_AI_Adoption_Rate (%)":20,"Large_Enterprise_AI_Adoption_Rate (%)":45,"Average_Seats_Per_Small_Enterprise":5,"Average_Seats_Per_Medium_Enterprise":50,"Average_Seats_Per_Large_Enterprise":500,"India_Population_Growth_Rate (%)":2.3,"UAE_Population_Growth_Rate (%)":2.8,"UK_Population_Growth_Rate (%)":2.1,"India_Enterprise_Growth_Rate (%)":2.5,"UAE_Enterprise_Growth_Rate (%)":2.7,"UK_Enterprise_Growth_Rate (%)":2.2,"Indian_Subcontinent_High_Income_Market_Share (%)":5,"Indian_Subcontinent_Mid_Income_Market_Share (%)":3,"Indian_Subcontinent_Low_Income_Market_Share (%)":1,"Middle_East_Africa_High_Income_Market_Share (%)":12,"Middle_East_Africa_Mid_Income_Market_Share (%)":8,"Middle_East_Africa_Low_Income_Market_Share (%)":4,"UK_Europe_High_Income_Market_Share (%)":15,"UK_Europe_Mid_Income_Market_Share (%)":10,"UK_Europe_Low_Income_Market_Share (%)":6,"Indian_Subcontinent_Small_Enterprise_Market_Share (%)":2,"Indian_Subcontinent_Medium_Enterprise_Market_Share (%)":4,"Indian_Subcontinent_Large_Enterprise_Market_Share (%)":8,"Middle_East_Africa_Small_Enterprise_Market_Share (%)":6,"Middle_East_Africa_Medium_Enterprise_Market_Share (%)":10,"Middle_East_Africa_Large_Enterprise_Market_Share (%)":18,"UK_Europe_Small_Enterprise_Market_Share (%)":8,"UK_Europe_Medium_Enterprise_Market_Share (%)":12,"UK_Europe_Large_Enterprise_Market_Share (%)":22,"Indian_Subcontinent_High_Income_Churn_Rate (%)":15,"Indian_Subcontinent_Mid_Income_Churn_Rate (%)":12,"Indian_Subcontinent_Low_Income_Churn_Rate (%)":8,"Middle_East_Africa_High_Income_Churn_Rate (%)":18,"Middle_East_Africa_Mid_Income_Churn_Rate (%)":14,"Middle_East_Africa_Low_Income_Churn_Rate (%)":10,"UK_Europe_High_Income_Churn_Rate (%)":20,"UK_Europe_Mid_Income_Churn_Rate (%)":16,"UK_Europe_Low_Income_Churn_Rate (%)":12,"Indian_Subcontinent_Small_Enterprise_Churn_Rate (%)":10,"Indian_Subcontinent_Medium_Enterprise_Churn_Rate (%)":8,"Indian_Subcontinent_Large_Enterprise_Churn_Rate (%)":6,"Middle_East_Africa_Small_Enterprise_Churn_Rate (%)":12,"Middle_East_Africa_Medium_Enterprise_Churn_Rate (%)":10,"Middle_East_Africa_Large_Enterprise_Churn_Rate (%)":7,"UK_Europe_Small_Enterprise_Churn_Rate (%)":14,"UK_Europe_Medium_Enterprise_Churn_Rate (%)":11,"UK_Europe_Large_Enterprise_Churn_Rate (%)":8}#,
formula= {"Step 1: Identify the size of the population in scope":["Indian_Subcontinent_Internet_Users = India_Total_Population * India_Internet_Penetration / 100","Indian_Subcontinent_High_Income_AI_Adopters = Indian_Subcontinent_Internet_Users * India_High_Income_Share / 100 * High_Income_AI_Adoption_Rate / 100","Indian_Subcontinent_Mid_Income_AI_Adopters = Indian_Subcontinent_Internet_Users * India_Mid_Income_Share / 100 * Mid_Income_AI_Adoption_Rate / 100","Indian_Subcontinent_Low_Income_AI_Adopters = Indian_Subcontinent_Internet_Users * India_Low_Income_Share / 100 * Low_Income_AI_Adoption_Rate / 100","Middle_East_Africa_Internet_Users = UAE_Total_Population * UAE_Internet_Penetration / 100","Middle_East_Africa_High_Income_AI_Adopters = Middle_East_Africa_Internet_Users * UAE_High_Income_Share / 100 * High_Income_AI_Adoption_Rate / 100","Middle_East_Africa_Mid_Income_AI_Adopters = Middle_East_Africa_Internet_Users * UAE_Mid_Income_Share / 100 * Mid_Income_AI_Adoption_Rate / 100","Middle_East_Africa_Low_Income_AI_Adopters = Middle_East_Africa_Internet_Users * UAE_Low_Income_Share / 100 * Low_Income_AI_Adoption_Rate / 100","UK_Europe_Internet_Users = UK_Total_Population * UK_Internet_Penetration / 100","UK_Europe_High_Income_AI_Adopters = UK_Europe_Internet_Users * UK_High_Income_Share / 100 * High_Income_AI_Adoption_Rate / 100","UK_Europe_Mid_Income_AI_Adopters = UK_Europe_Internet_Users * UK_Mid_Income_Share / 100 * Mid_Income_AI_Adoption_Rate / 100","UK_Europe_Low_Income_AI_Adopters = UK_Europe_Internet_Users * UK_Low_Income_Share / 100 * Low_Income_AI_Adoption_Rate / 100","Indian_Subcontinent_Small_Enterprise_Seats = India_Enterprise_Count * Small_Enterprise_Share / 100 * Small_Enterprise_AI_Adoption_Rate / 100 * Average_Seats_Per_Small_Enterprise","Indian_Subcontinent_Medium_Enterprise_Seats = India_Enterprise_Count * Medium_Enterprise_Share / 100 * Medium_Enterprise_AI_Adoption_Rate / 100 * Average_Seats_Per_Medium_Enterprise","Indian_Subcontinent_Large_Enterprise_Seats = India_Enterprise_Count * Large_Enterprise_Share / 100 * Large_Enterprise_AI_Adoption_Rate / 100 * Average_Seats_Per_Large_Enterprise","Middle_East_Africa_Small_Enterprise_Seats = UAE_Enterprise_Count * Small_Enterprise_Share / 100 * Small_Enterprise_AI_Adoption_Rate / 100 * Average_Seats_Per_Small_Enterprise","Middle_East_Africa_Medium_Enterprise_Seats = UAE_Enterprise_Count * Medium_Enterprise_Share / 100 * Medium_Enterprise_AI_Adoption_Rate / 100 * Average_Seats_Per_Medium_Enterprise","Middle_East_Africa_Large_Enterprise_Seats = UAE_Enterprise_Count * Large_Enterprise_Share / 100 * Large_Enterprise_AI_Adoption_Rate / 100 * Average_Seats_Per_Large_Enterprise","UK_Europe_Small_Enterprise_Seats = UK_Enterprise_Count * Small_Enterprise_Share / 100 * Small_Enterprise_AI_Adoption_Rate / 100 * Average_Seats_Per_Small_Enterprise","UK_Europe_Medium_Enterprise_Seats = UK_Enterprise_Count * Medium_Enterprise_Share / 100 * Medium_Enterprise_AI_Adoption_Rate / 100 * Average_Seats_Per_Medium_Enterprise","UK_Europe_Large_Enterprise_Seats = UK_Enterprise_Count * Large_Enterprise_Share / 100 * Large_Enterprise_AI_Adoption_Rate / 100 * Average_Seats_Per_Large_Enterprise"],"Step 2: Identify the growth rate of the segment":["Total_Indian_Subcontinent_High_Income_AI_Adopters = Indian_Subcontinent_High_Income_AI_Adopters * (1 + India_Population_Growth_Rate / 100)","Total_Indian_Subcontinent_Mid_Income_AI_Adopters = Indian_Subcontinent_Mid_Income_AI_Adopters * (1 + India_Population_Growth_Rate / 100)","Total_Indian_Subcontinent_Low_Income_AI_Adopters = Indian_Subcontinent_Low_Income_AI_Adopters * (1 + India_Population_Growth_Rate / 100)","Total_Middle_East_Africa_High_Income_AI_Adopters = Middle_East_Africa_High_Income_AI_Adopters * (1 + UAE_Population_Growth_Rate / 100)","Total_Middle_East_Africa_Mid_Income_AI_Adopters = Middle_East_Africa_Mid_Income_AI_Adopters * (1 + UAE_Population_Growth_Rate / 100)","Total_Middle_East_Africa_Low_Income_AI_Adopters = Middle_East_Africa_Low_Income_AI_Adopters * (1 + UAE_Population_Growth_Rate / 100)","Total_UK_Europe_High_Income_AI_Adopters = UK_Europe_High_Income_AI_Adopters * (1 + UK_Population_Growth_Rate / 100)","Total_UK_Europe_Mid_Income_AI_Adopters = UK_Europe_Mid_Income_AI_Adopters * (1 + UK_Population_Growth_Rate / 100)","Total_UK_Europe_Low_Income_AI_Adopters = UK_Europe_Low_Income_AI_Adopters * (1 + UK_Population_Growth_Rate / 100)","Total_Indian_Subcontinent_Small_Enterprise_Seats = Indian_Subcontinent_Small_Enterprise_Seats * (1 + India_Enterprise_Growth_Rate / 100)","Total_Indian_Subcontinent_Medium_Enterprise_Seats = Indian_Subcontinent_Medium_Enterprise_Seats * (1 + India_Enterprise_Growth_Rate / 100)","Total_Indian_Subcontinent_Large_Enterprise_Seats = Indian_Subcontinent_Large_Enterprise_Seats * (1 + India_Enterprise_Growth_Rate / 100)","Total_Middle_East_Africa_Small_Enterprise_Seats = Middle_East_Africa_Small_Enterprise_Seats * (1 + UAE_Enterprise_Growth_Rate / 100)","Total_Middle_East_Africa_Medium_Enterprise_Seats = Middle_East_Africa_Medium_Enterprise_Seats * (1 + UAE_Enterprise_Growth_Rate / 100)","Total_Middle_East_Africa_Large_Enterprise_Seats = Middle_East_Africa_Large_Enterprise_Seats * (1 + UAE_Enterprise_Growth_Rate / 100)","Total_UK_Europe_Small_Enterprise_Seats = UK_Europe_Small_Enterprise_Seats * (1 + UK_Enterprise_Growth_Rate / 100)","Total_UK_Europe_Medium_Enterprise_Seats = UK_Europe_Medium_Enterprise_Seats * (1 + UK_Enterprise_Growth_Rate / 100)","Total_UK_Europe_Large_Enterprise_Seats = UK_Europe_Large_Enterprise_Seats * (1 + UK_Enterprise_Growth_Rate / 100)"],"Step 3: Company market share":["Indian_Subcontinent_High_Income_Addressable_Market = Total_Indian_Subcontinent_High_Income_AI_Adopters * Indian_Subcontinent_High_Income_Market_Share / 100","Indian_Subcontinent_Mid_Income_Addressable_Market = Total_Indian_Subcontinent_Mid_Income_AI_Adopters * Indian_Subcontinent_Mid_Income_Market_Share / 100","Indian_Subcontinent_Low_Income_Addressable_Market = Total_Indian_Subcontinent_Low_Income_AI_Adopters * Indian_Subcontinent_Low_Income_Market_Share / 100","Middle_East_Africa_High_Income_Addressable_Market = Total_Middle_East_Africa_High_Income_AI_Adopters * Middle_East_Africa_High_Income_Market_Share / 100","Middle_East_Africa_Mid_Income_Addressable_Market = Total_Middle_East_Africa_Mid_Income_AI_Adopters * Middle_East_Africa_Mid_Income_Market_Share / 100","Middle_East_Africa_Low_Income_Addressable_Market = Total_Middle_East_Africa_Low_Income_AI_Adopters * Middle_East_Africa_Low_Income_Market_Share / 100","UK_Europe_High_Income_Addressable_Market = Total_UK_Europe_High_Income_AI_Adopters * UK_Europe_High_Income_Market_Share / 100","UK_Europe_Mid_Income_Addressable_Market = Total_UK_Europe_Mid_Income_AI_Adopters * UK_Europe_Mid_Income_Market_Share / 100","UK_Europe_Low_Income_Addressable_Market = Total_UK_Europe_Low_Income_AI_Adopters * UK_Europe_Low_Income_Market_Share / 100","Indian_Subcontinent_Small_Enterprise_Addressable_Seats = Total_Indian_Subcontinent_Small_Enterprise_Seats * Indian_Subcontinent_Small_Enterprise_Market_Share / 100","Indian_Subcontinent_Medium_Enterprise_Addressable_Seats = Total_Indian_Subcontinent_Medium_Enterprise_Seats * Indian_Subcontinent_Medium_Enterprise_Market_Share / 100","Indian_Subcontinent_Large_Enterprise_Addressable_Seats = Total_Indian_Subcontinent_Large_Enterprise_Seats * Indian_Subcontinent_Large_Enterprise_Market_Share / 100","Middle_East_Africa_Small_Enterprise_Addressable_Seats = Total_Middle_East_Africa_Small_Enterprise_Seats * Middle_East_Africa_Small_Enterprise_Market_Share / 100","Middle_East_Africa_Medium_Enterprise_Addressable_Seats = Total_Middle_East_Africa_Medium_Enterprise_Seats * Middle_East_Africa_Medium_Enterprise_Market_Share / 100","Middle_East_Africa_Large_Enterprise_Addressable_Seats = Total_Middle_East_Africa_Large_Enterprise_Seats * Middle_East_Africa_Large_Enterprise_Market_Share / 100","UK_Europe_Small_Enterprise_Addressable_Seats = Total_UK_Europe_Small_Enterprise_Seats * UK_Europe_Small_Enterprise_Market_Share / 100","UK_Europe_Medium_Enterprise_Addressable_Seats = Total_UK_Europe_Medium_Enterprise_Seats * UK_Europe_Medium_Enterprise_Market_Share / 100","UK_Europe_Large_Enterprise_Addressable_Seats = Total_UK_Europe_Large_Enterprise_Seats * UK_Europe_Large_Enterprise_Market_Share / 100"],"Step 4: Factor gains and losses of customers from and to competitors":["Indian_Subcontinent_High_Income_Churn = Indian_Subcontinent_High_Income_Addressable_Market * Indian_Subcontinent_High_Income_Churn_Rate / 100","Indian_Subcontinent_Mid_Income_Churn = Indian_Subcontinent_Mid_Income_Addressable_Market * Indian_Subcontinent_Mid_Income_Churn_Rate / 100","Indian_Subcontinent_Low_Income_Churn = Indian_Subcontinent_Low_Income_Addressable_Market * Indian_Subcontinent_Low_Income_Churn_Rate / 100","Middle_East_Africa_High_Income_Churn = Middle_East_Africa_High_Income_Addressable_Market * Middle_East_Africa_High_Income_Churn_Rate / 100","Middle_East_Africa_Mid_Income_Churn = Middle_East_Africa_Mid_Income_Addressable_Market * Middle_East_Africa_Mid_Income_Churn_Rate / 100","Middle_East_Africa_Low_Income_Churn = Middle_East_Africa_Low_Income_Addressable_Market * Middle_East_Africa_Low_Income_Churn_Rate / 100","UK_Europe_High_Income_Churn = UK_Europe_High_Income_Addressable_Market * UK_Europe_High_Income_Churn_Rate / 100","UK_Europe_Mid_Income_Churn = UK_Europe_Mid_Income_Addressable_Market * UK_Europe_Mid_Income_Churn_Rate / 100","UK_Europe_Low_Income_Churn = UK_Europe_Low_Income_Addressable_Market * UK_Europe_Low_Income_Churn_Rate / 100","Indian_Subcontinent_Small_Enterprise_Churn = Indian_Subcontinent_Small_Enterprise_Addressable_Seats * Indian_Subcontinent_Small_Enterprise_Churn_Rate / 100","Indian_Subcontinent_Medium_Enterprise_Churn = Indian_Subcontinent_Medium_Enterprise_Addressable_Seats * Indian_Subcontinent_Medium_Enterprise_Churn_Rate / 100","Indian_Subcontinent_Large_Enterprise_Churn = Indian_Subcontinent_Large_Enterprise_Addressable_Seats * Indian_Subcontinent_Large_Enterprise_Churn_Rate / 100","Middle_East_Africa_Small_Enterprise_Churn = Middle_East_Africa_Small_Enterprise_Addressable_Seats * Middle_East_Africa_Small_Enterprise_Churn_Rate / 100","Middle_East_Africa_Medium_Enterprise_Churn = Middle_East_Africa_Medium_Enterprise_Addressable_Seats * Middle_East_Africa_Medium_Enterprise_Churn_Rate / 100","Middle_East_Africa_Large_Enterprise_Churn = Middle_East_Africa_Large_Enterprise_Addressable_Seats * Middle_East_Africa_Large_Enterprise_Churn_Rate / 100","UK_Europe_Small_Enterprise_Churn = UK_Europe_Small_Enterprise_Addressable_Seats * UK_Europe_Small_Enterprise_Churn_Rate / 100","UK_Europe_Medium_Enterprise_Churn = UK_Europe_Medium_Enterprise_Addressable_Seats * UK_Europe_Medium_Enterprise_Churn_Rate / 100","UK_Europe_Large_Enterprise_Churn = UK_Europe_Large_Enterprise_Addressable_Seats * UK_Europe_Large_Enterprise_Churn_Rate / 100"],"Step 5: Total user base":["Indian_Subcontinent_High_Income_Users = Indian_Subcontinent_High_Income_Addressable_Market - Indian_Subcontinent_High_Income_Churn","Indian_Subcontinent_Mid_Income_Users = Indian_Subcontinent_Mid_Income_Addressable_Market - Indian_Subcontinent_Mid_Income_Churn","Indian_Subcontinent_Low_Income_Users = Indian_Subcontinent_Low_Income_Addressable_Market - Indian_Subcontinent_Low_Income_Churn","Middle_East_Africa_High_Income_Users = Middle_East_Africa_High_Income_Addressable_Market - Middle_East_Africa_High_Income_Churn","Middle_East_Africa_Mid_Income_Users = Middle_East_Africa_Mid_Income_Addressable_Market - Middle_East_Africa_Mid_Income_Churn","Middle_East_Africa_Low_Income_Users = Middle_East_Africa_Low_Income_Addressable_Market - Middle_East_Africa_Low_Income_Churn","UK_Europe_High_Income_Users = UK_Europe_High_Income_Addressable_Market - UK_Europe_High_Income_Churn","UK_Europe_Mid_Income_Users = UK_Europe_Mid_Income_Addressable_Market - UK_Europe_Mid_Income_Churn","UK_Europe_Low_Income_Users = UK_Europe_Low_Income_Addressable_Market - UK_Europe_Low_Income_Churn","Indian_Subcontinent_Small_Enterprise_Users = Indian_Subcontinent_Small_Enterprise_Addressable_Seats - Indian_Subcontinent_Small_Enterprise_Churn","Indian_Subcontinent_Medium_Enterprise_Users = Indian_Subcontinent_Medium_Enterprise_Addressable_Seats - Indian_Subcontinent_Medium_Enterprise_Churn","Indian_Subcontinent_Large_Enterprise_Users = Indian_Subcontinent_Large_Enterprise_Addressable_Seats - Indian_Subcontinent_Large_Enterprise_Churn","Middle_East_Africa_Small_Enterprise_Users = Middle_East_Africa_Small_Enterprise_Addressable_Seats - Middle_East_Africa_Small_Enterprise_Churn","Middle_East_Africa_Medium_Enterprise_Users = Middle_East_Africa_Medium_Enterprise_Addressable_Seats - Middle_East_Africa_Medium_Enterprise_Churn","Middle_East_Africa_Large_Enterprise_Users = Middle_East_Africa_Large_Enterprise_Addressable_Seats - Middle_East_Africa_Large_Enterprise_Churn","UK_Europe_Small_Enterprise_Users = UK_Europe_Small_Enterprise_Addressable_Seats - UK_Europe_Small_Enterprise_Churn","UK_Europe_Medium_Enterprise_Users = UK_Europe_Medium_Enterprise_Addressable_Seats - UK_Europe_Medium_Enterprise_Churn","UK_Europe_Large_Enterprise_Users = UK_Europe_Large_Enterprise_Addressable_Seats - UK_Europe_Large_Enterprise_Churn","Total_User_Base = Indian_Subcontinent_High_Income_Users + Indian_Subcontinent_Mid_Income_Users + Indian_Subcontinent_Low_Income_Users + Middle_East_Africa_High_Income_Users + Middle_East_Africa_Mid_Income_Users + Middle_East_Africa_Low_Income_Users + UK_Europe_High_Income_Users + UK_Europe_Mid_Income_Users + UK_Europe_Low_Income_Users + Indian_Subcontinent_Small_Enterprise_Users + Indian_Subcontinent_Medium_Enterprise_Users + Indian_Subcontinent_Large_Enterprise_Users + Middle_East_Africa_Small_Enterprise_Users + Middle_East_Africa_Medium_Enterprise_Users + Middle_East_Africa_Large_Enterprise_Users + UK_Europe_Small_Enterprise_Users + UK_Europe_Medium_Enterprise_Users + UK_Europe_Large_Enterprise_Users"]}
assumptions={
        "India_Total_Population": 1400000000,
        "UAE_Total_Population": 10000000,
        "UK_Total_Population": 67000000,
        "India_Internet_Penetration (%)": 50,
        "UAE_Internet_Penetration (%)": 95,
        "UK_Internet_Penetration (%)": 95,
        "India_High_Income_Share (%)": 15,
        "India_Mid_Income_Share (%)": 35,
        "India_Low_Income_Share (%)": 50,
        "UAE_High_Income_Share (%)": 45,
        "UAE_Mid_Income_Share (%)": 40,
        "UAE_Low_Income_Share (%)": 15,
        "UK_High_Income_Share (%)": 30,
        "UK_Mid_Income_Share (%)": 55,
        "UK_Low_Income_Share (%)": 15,
        "High_Income_AI_Adoption (%)": 25,
        "Mid_Income_AI_Adoption (%)": 15,
        "Low_Income_AI_Adoption (%)": 5,
        "India_Enterprise_Count": 75000000,
        "UAE_Enterprise_Count": 500000,
        "UK_Enterprise_Count": 5500000,
        "Small_Enterprise_Share (%)": 70,
        "Medium_Enterprise_Share (%)": 25,
        "Large_Enterprise_Share (%)": 5,
        "Small_Enterprise_AI_Adoption (%)": 10,
        "Medium_Enterprise_AI_Adoption (%)": 35,
        "Large_Enterprise_AI_Adoption (%)": 60,
        "Small_Enterprise_Avg_Seats": 5,
        "Medium_Enterprise_Avg_Seats": 50,
        "Large_Enterprise_Avg_Seats": 500,
        "Population_Growth_Rate_Indian_Subcontinent (%)": 2.5,
        "Population_Growth_Rate_Middle_East_and_Africa (%)": 2.8,
        "Population_Growth_Rate_UK_and_Europe (%)": 2.2,
        "Enterprise_Growth_Rate_Indian_Subcontinent (%)": 3.0,
        "Enterprise_Growth_Rate_Middle_East_and_Africa (%)": 2.7,
        "Enterprise_Growth_Rate_UK_and_Europe (%)": 2.3,
        "Indian_Subcontinent_High_Income_Individual_Market_Share (%)": 0.5,
        "Indian_Subcontinent_Mid_Income_Individual_Market_Share (%)": 0.3,
        "Indian_Subcontinent_Low_Income_Individual_Market_Share (%)": 0.1,
        "Middle_East_and_Africa_High_Income_Individual_Market_Share (%)": 2.0,
        "Middle_East_and_Africa_Mid_Income_Individual_Market_Share (%)": 1.5,
        "Middle_East_and_Africa_Low_Income_Individual_Market_Share (%)": 0.8,
        "UK_and_Europe_High_Income_Individual_Market_Share (%)": 3.0,
        "UK_and_Europe_Mid_Income_Individual_Market_Share (%)": 2.5,
        "UK_and_Europe_Low_Income_Individual_Market_Share (%)": 1.0,
        "Indian_Subcontinent_Small_Enterprise_Market_Share (%)": 0.3,
        "Indian_Subcontinent_Medium_Enterprise_Market_Share (%)": 0.8,
        "Indian_Subcontinent_Large_Enterprise_Market_Share (%)": 2.0,
        "Middle_East_and_Africa_Small_Enterprise_Market_Share (%)": 1.2,
        "Middle_East_and_Africa_Medium_Enterprise_Market_Share (%)": 2.5,
        "Middle_East_and_Africa_Large_Enterprise_Market_Share (%)": 5.0,
        "UK_and_Europe_Small_Enterprise_Market_Share (%)": 2.0,
        "UK_and_Europe_Medium_Enterprise_Market_Share (%)": 4.0,
        "UK_and_Europe_Large_Enterprise_Market_Share (%)": 8.0,
        "Indian_Subcontinent_High_Income_Individual_Churn (%)": 8,
        "Indian_Subcontinent_Mid_Income_Individual_Churn (%)": 12,
        "Indian_Subcontinent_Low_Income_Individual_Churn (%)": 15,
        "Middle_East_and_Africa_High_Income_Individual_Churn (%)": 6,
        "Middle_East_and_Africa_Mid_Income_Individual_Churn (%)": 10,
        "Middle_East_and_Africa_Low_Income_Individual_Churn (%)": 12,
        "UK_and_Europe_High_Income_Individual_Churn (%)": 5,
        "UK_and_Europe_Mid_Income_Individual_Churn (%)": 8,
        "UK_and_Europe_Low_Income_Individual_Churn (%)": 10,
        "Indian_Subcontinent_Small_Enterprise_Churn (%)": 18,
        "Indian_Subcontinent_Medium_Enterprise_Churn (%)": 12,
        "Indian_Subcontinent_Large_Enterprise_Churn (%)": 8,
        "Middle_East_and_Africa_Small_Enterprise_Churn (%)": 15,
        "Middle_East_and_Africa_Medium_Enterprise_Churn (%)": 10,
        "Middle_East_and_Africa_Large_Enterprise_Churn (%)": 6,
        "UK_and_Europe_Small_Enterprise_Churn (%)": 12,
        "UK_and_Europe_Medium_Enterprise_Churn (%)": 8,
        "UK_and_Europe_Large_Enterprise_Churn (%)": 5
    }

formula = {
        "Step 1: Identify the size of the population in scope": [
            "India_Internet_Users = India_Total_Population * India_Internet_Penetration / 100",
            "UAE_Internet_Users = UAE_Total_Population * UAE_Internet_Penetration / 100",
            "UK_Internet_Users = UK_Total_Population * UK_Internet_Penetration / 100",
            "Indian_Subcontinent_High_Income_Individual_Adopters = India_Internet_Users * India_High_Income_Share / 100 * High_Income_AI_Adoption / 100",
            "Indian_Subcontinent_Mid_Income_Individual_Adopters = India_Internet_Users * India_Mid_Income_Share / 100 * Mid_Income_AI_Adoption / 100",
            "Indian_Subcontinent_Low_Income_Individual_Adopters = India_Internet_Users * India_Low_Income_Share / 100 * Low_Income_AI_Adoption / 100",
            "Middle_East_and_Africa_High_Income_Individual_Adopters = UAE_Internet_Users * UAE_High_Income_Share / 100 * High_Income_AI_Adoption / 100",
            "Middle_East_and_Africa_Mid_Income_Individual_Adopters = UAE_Internet_Users * UAE_Mid_Income_Share / 100 * Mid_Income_AI_Adoption / 100",
            "Middle_East_and_Africa_Low_Income_Individual_Adopters = UAE_Internet_Users * UAE_Low_Income_Share / 100 * Low_Income_AI_Adoption / 100",
            "UK_and_Europe_High_Income_Individual_Adopters = UK_Internet_Users * UK_High_Income_Share / 100 * High_Income_AI_Adoption / 100",
            "UK_and_Europe_Mid_Income_Individual_Adopters = UK_Internet_Users * UK_Mid_Income_Share / 100 * Mid_Income_AI_Adoption / 100",
            "UK_and_Europe_Low_Income_Individual_Adopters = UK_Internet_Users * UK_Low_Income_Share / 100 * Low_Income_AI_Adoption / 100",
            "Indian_Subcontinent_Small_Enterprise_Seats = India_Enterprise_Count * Small_Enterprise_Share / 100 * Small_Enterprise_AI_Adoption / 100 * Small_Enterprise_Avg_Seats",
            "Indian_Subcontinent_Medium_Enterprise_Seats = India_Enterprise_Count * Medium_Enterprise_Share / 100 * Medium_Enterprise_AI_Adoption / 100 * Medium_Enterprise_Avg_Seats",
            "Indian_Subcontinent_Large_Enterprise_Seats = India_Enterprise_Count * Large_Enterprise_Share / 100 * Large_Enterprise_AI_Adoption / 100 * Large_Enterprise_Avg_Seats",
            "Middle_East_and_Africa_Small_Enterprise_Seats = UAE_Enterprise_Count * Small_Enterprise_Share / 100 * Small_Enterprise_AI_Adoption / 100 * Small_Enterprise_Avg_Seats",
            "Middle_East_and_Africa_Medium_Enterprise_Seats = UAE_Enterprise_Count * Medium_Enterprise_Share / 100 * Medium_Enterprise_AI_Adoption / 100 * Medium_Enterprise_Avg_Seats",
            "Middle_East_and_Africa_Large_Enterprise_Seats = UAE_Enterprise_Count * Large_Enterprise_Share / 100 * Large_Enterprise_AI_Adoption / 100 * Large_Enterprise_Avg_Seats",
            "UK_and_Europe_Small_Enterprise_Seats = UK_Enterprise_Count * Small_Enterprise_Share / 100 * Small_Enterprise_AI_Adoption / 100 * Small_Enterprise_Avg_Seats",
            "UK_and_Europe_Medium_Enterprise_Seats = UK_Enterprise_Count * Medium_Enterprise_Share / 100 * Medium_Enterprise_AI_Adoption / 100 * Medium_Enterprise_Avg_Seats",
            "UK_and_Europe_Large_Enterprise_Seats = UK_Enterprise_Count * Large_Enterprise_Share / 100 * Large_Enterprise_AI_Adoption / 100 * Large_Enterprise_Avg_Seats"
        ],
        "Step 2: Identify the growth rate of the segment": [
            "Total_Indian_Subcontinent_High_Income_Individual_Adopters = Indian_Subcontinent_High_Income_Individual_Adopters * (1 + Population_Growth_Rate_Indian_Subcontinent / 100)",
            "Total_Indian_Subcontinent_Mid_Income_Individual_Adopters = Indian_Subcontinent_Mid_Income_Individual_Adopters * (1 + Population_Growth_Rate_Indian_Subcontinent / 100)",
            "Total_Indian_Subcontinent_Low_Income_Individual_Adopters = Indian_Subcontinent_Low_Income_Individual_Adopters * (1 + Population_Growth_Rate_Indian_Subcontinent / 100)",
            "Total_Middle_East_and_Africa_High_Income_Individual_Adopters = Middle_East_and_Africa_High_Income_Individual_Adopters * (1 + Population_Growth_Rate_Middle_East_and_Africa / 100)",
            "Total_Middle_East_and_Africa_Mid_Income_Individual_Adopters = Middle_East_and_Africa_Mid_Income_Individual_Adopters * (1 + Population_Growth_Rate_Middle_East_and_Africa / 100)",
            "Total_Middle_East_and_Africa_Low_Income_Individual_Adopters = Middle_East_and_Africa_Low_Income_Individual_Adopters * (1 + Population_Growth_Rate_Middle_East_and_Africa / 100)",
            "Total_UK_and_Europe_High_Income_Individual_Adopters = UK_and_Europe_High_Income_Individual_Adopters * (1 + Population_Growth_Rate_UK_and_Europe / 100)",
            "Total_UK_and_Europe_Mid_Income_Individual_Adopters = UK_and_Europe_Mid_Income_Individual_Adopters * (1 + Population_Growth_Rate_UK_and_Europe / 100)",
            "Total_UK_and_Europe_Low_Income_Individual_Adopters = UK_and_Europe_Low_Income_Individual_Adopters * (1 + Population_Growth_Rate_UK_and_Europe / 100)",
            "Total_Indian_Subcontinent_Small_Enterprise_Seats = Indian_Subcontinent_Small_Enterprise_Seats * (1 + Enterprise_Growth_Rate_Indian_Subcontinent / 100)",
            "Total_Indian_Subcontinent_Medium_Enterprise_Seats = Indian_Subcontinent_Medium_Enterprise_Seats * (1 + Enterprise_Growth_Rate_Indian_Subcontinent / 100)",
            "Total_Indian_Subcontinent_Large_Enterprise_Seats = Indian_Subcontinent_Large_Enterprise_Seats * (1 + Enterprise_Growth_Rate_Indian_Subcontinent / 100)",
            "Total_Middle_East_and_Africa_Small_Enterprise_Seats = Middle_East_and_Africa_Small_Enterprise_Seats * (1 + Enterprise_Growth_Rate_Middle_East_and_Africa / 100)",
            "Total_Middle_East_and_Africa_Medium_Enterprise_Seats = Middle_East_and_Africa_Medium_Enterprise_Seats * (1 + Enterprise_Growth_Rate_Middle_East_and_Africa / 100)",
            "Total_Middle_East_and_Africa_Large_Enterprise_Seats = Middle_East_and_Africa_Large_Enterprise_Seats * (1 + Enterprise_Growth_Rate_Middle_East_and_Africa / 100)",
            "Total_UK_and_Europe_Small_Enterprise_Seats = UK_and_Europe_Small_Enterprise_Seats * (1 + Enterprise_Growth_Rate_UK_and_Europe / 100)",
            "Total_UK_and_Europe_Medium_Enterprise_Seats = UK_and_Europe_Medium_Enterprise_Seats * (1 + Enterprise_Growth_Rate_UK_and_Europe / 100)",
            "Total_UK_and_Europe_Large_Enterprise_Seats = UK_and_Europe_Large_Enterprise_Seats * (1 + Enterprise_Growth_Rate_UK_and_Europe / 100)"
        ],
        "Step 3: Company market share": [
            "Indian_Subcontinent_High_Income_Individual_Addressable_Market = Total_Indian_Subcontinent_High_Income_Individual_Adopters * Indian_Subcontinent_High_Income_Individual_Market_Share / 100",
            "Indian_Subcontinent_Mid_Income_Individual_Addressable_Market = Total_Indian_Subcontinent_Mid_Income_Individual_Adopters * Indian_Subcontinent_Mid_Income_Individual_Market_Share / 100",
            "Indian_Subcontinent_Low_Income_Individual_Addressable_Market = Total_Indian_Subcontinent_Low_Income_Individual_Adopters * Indian_Subcontinent_Low_Income_Individual_Market_Share / 100",
            "Middle_East_and_Africa_High_Income_Individual_Addressable_Market = Total_Middle_East_and_Africa_High_Income_Individual_Adopters * Middle_East_and_Africa_High_Income_Individual_Market_Share / 100",
            "Middle_East_and_Africa_Mid_Income_Individual_Addressable_Market = Total_Middle_East_and_Africa_Mid_Income_Individual_Adopters * Middle_East_and_Africa_Mid_Income_Individual_Market_Share / 100",
            "Middle_East_and_Africa_Low_Income_Individual_Addressable_Market = Total_Middle_East_and_Africa_Low_Income_Individual_Adopters * Middle_East_and_Africa_Low_Income_Individual_Market_Share / 100",
            "UK_and_Europe_High_Income_Individual_Addressable_Market = Total_UK_and_Europe_High_Income_Individual_Adopters * UK_and_Europe_High_Income_Individual_Market_Share / 100",
            "UK_and_Europe_Mid_Income_Individual_Addressable_Market = Total_UK_and_Europe_Mid_Income_Individual_Adopters * UK_and_Europe_Mid_Income_Individual_Market_Share / 100",
            "UK_and_Europe_Low_Income_Individual_Addressable_Market = Total_UK_and_Europe_Low_Income_Individual_Adopters * UK_and_Europe_Low_Income_Individual_Market_Share / 100",
            "Indian_Subcontinent_Small_Enterprise_Addressable_Market = Total_Indian_Subcontinent_Small_Enterprise_Seats * Indian_Subcontinent_Small_Enterprise_Market_Share / 100",
            "Indian_Subcontinent_Medium_Enterprise_Addressable_Market = Total_Indian_Subcontinent_Medium_Enterprise_Seats * Indian_Subcontinent_Medium_Enterprise_Market_Share / 100",
            "Indian_Subcontinent_Large_Enterprise_Addressable_Market = Total_Indian_Subcontinent_Large_Enterprise_Seats * Indian_Subcontinent_Large_Enterprise_Market_Share / 100",
            "Middle_East_and_Africa_Small_Enterprise_Addressable_Market = Total_Middle_East_and_Africa_Small_Enterprise_Seats * Middle_East_and_Africa_Small_Enterprise_Market_Share / 100",
            "Middle_East_and_Africa_Medium_Enterprise_Addressable_Market = Total_Middle_East_and_Africa_Medium_Enterprise_Seats * Middle_East_and_Africa_Medium_Enterprise_Market_Share / 100",
            "Middle_East_and_Africa_Large_Enterprise_Addressable_Market = Total_Middle_East_and_Africa_Large_Enterprise_Seats * Middle_East_and_Africa_Large_Enterprise_Market_Share / 100",
            "UK_and_Europe_Small_Enterprise_Addressable_Market = Total_UK_and_Europe_Small_Enterprise_Seats * UK_and_Europe_Small_Enterprise_Market_Share / 100",
            "UK_and_Europe_Medium_Enterprise_Addressable_Market = Total_UK_and_Europe_Medium_Enterprise_Seats * UK_and_Europe_Medium_Enterprise_Market_Share / 100",
            "UK_and_Europe_Large_Enterprise_Addressable_Market = Total_UK_and_Europe_Large_Enterprise_Seats * UK_and_Europe_Large_Enterprise_Market_Share / 100"
        ],
        "Step 4: Factor gains and losses of customers from and to competitors": [
            "Indian_Subcontinent_High_Income_Individual_Churn_Loss = Indian_Subcontinent_High_Income_Individual_Addressable_Market * Indian_Subcontinent_High_Income_Individual_Churn / 100",
            "Indian_Subcontinent_Mid_Income_Individual_Churn_Loss = Indian_Subcontinent_Mid_Income_Individual_Addressable_Market * Indian_Subcontinent_Mid_Income_Individual_Churn / 100",
            "Indian_Subcontinent_Low_Income_Individual_Churn_Loss = Indian_Subcontinent_Low_Income_Individual_Addressable_Market * Indian_Subcontinent_Low_Income_Individual_Churn / 100",
            "Middle_East_and_Africa_High_Income_Individual_Churn_Loss = Middle_East_and_Africa_High_Income_Individual_Addressable_Market * Middle_East_and_Africa_High_Income_Individual_Churn / 100",
            "Middle_East_and_Africa_Mid_Income_Individual_Churn_Loss = Middle_East_and_Africa_Mid_Income_Individual_Addressable_Market * Middle_East_and_Africa_Mid_Income_Individual_Churn / 100",
            "Middle_East_and_Africa_Low_Income_Individual_Churn_Loss = Middle_East_and_Africa_Low_Income_Individual_Addressable_Market * Middle_East_and_Africa_Low_Income_Individual_Churn / 100",
            "UK_and_Europe_High_Income_Individual_Churn_Loss = UK_and_Europe_High_Income_Individual_Addressable_Market * UK_and_Europe_High_Income_Individual_Churn / 100",
            "UK_and_Europe_Mid_Income_Individual_Churn_Loss = UK_and_Europe_Mid_Income_Individual_Addressable_Market * UK_and_Europe_Mid_Income_Individual_Churn / 100",
            "UK_and_Europe_Low_Income_Individual_Churn_Loss = UK_and_Europe_Low_Income_Individual_Addressable_Market * UK_and_Europe_Low_Income_Individual_Churn / 100",
            "Indian_Subcontinent_Small_Enterprise_Churn_Loss = Indian_Subcontinent_Small_Enterprise_Addressable_Market * Indian_Subcontinent_Small_Enterprise_Churn / 100",
            "Indian_Subcontinent_Medium_Enterprise_Churn_Loss = Indian_Subcontinent_Medium_Enterprise_Addressable_Market * Indian_Subcontinent_Medium_Enterprise_Churn / 100",
            "Indian_Subcontinent_Large_Enterprise_Churn_Loss = Indian_Subcontinent_Large_Enterprise_Addressable_Market * Indian_Subcontinent_Large_Enterprise_Churn / 100",
            "Middle_East_and_Africa_Small_Enterprise_Churn_Loss = Middle_East_and_Africa_Small_Enterprise_Addressable_Market * Middle_East_and_Africa_Small_Enterprise_Churn / 100",
            "Middle_East_and_Africa_Medium_Enterprise_Churn_Loss = Middle_East_and_Africa_Medium_Enterprise_Addressable_Market * Middle_East_and_Africa_Medium_Enterprise_Churn / 100",
            "Middle_East_and_Africa_Large_Enterprise_Churn_Loss = Middle_East_and_Africa_Large_Enterprise_Addressable_Market * Middle_East_and_Africa_Large_Enterprise_Churn / 100",
            "UK_and_Europe_Small_Enterprise_Churn_Loss = UK_and_Europe_Small_Enterprise_Addressable_Market * UK_and_Europe_Small_Enterprise_Churn / 100",
            "UK_and_Europe_Medium_Enterprise_Churn_Loss = UK_and_Europe_Medium_Enterprise_Addressable_Market * UK_and_Europe_Medium_Enterprise_Churn / 100",
            "UK_and_Europe_Large_Enterprise_Churn_Loss = UK_and_Europe_Large_Enterprise_Addressable_Market * UK_and_Europe_Large_Enterprise_Churn / 100"
        ],
        "Step 5: Total User base": [
            "Indian_Subcontinent_High_Income_Individual_Net_Users = Indian_Subcontinent_High_Income_Individual_Addressable_Market - Indian_Subcontinent_High_Income_Individual_Churn_Loss",
            "Indian_Subcontinent_Mid_Income_Individual_Net_Users = Indian_Subcontinent_Mid_Income_Individual_Addressable_Market - Indian_Subcontinent_Mid_Income_Individual_Churn_Loss",
            "Indian_Subcontinent_Low_Income_Individual_Net_Users = Indian_Subcontinent_Low_Income_Individual_Addressable_Market - Indian_Subcontinent_Low_Income_Individual_Churn_Loss",
            "Middle_East_and_Africa_High_Income_Individual_Net_Users = Middle_East_and_Africa_High_Income_Individual_Addressable_Market - Middle_East_and_Africa_High_Income_Individual_Churn_Loss",
            "Middle_East_and_Africa_Mid_Income_Individual_Net_Users = Middle_East_and_Africa_Mid_Income_Individual_Addressable_Market - Middle_East_and_Africa_Mid_Income_Individual_Churn_Loss",
            "Middle_East_and_Africa_Low_Income_Individual_Net_Users = Middle_East_and_Africa_Low_Income_Individual_Addressable_Market - Middle_East_and_Africa_Low_Income_Individual_Churn_Loss",
            "UK_and_Europe_High_Income_Individual_Net_Users = UK_and_Europe_High_Income_Individual_Addressable_Market - UK_and_Europe_High_Income_Individual_Churn_Loss",
            "UK_and_Europe_Mid_Income_Individual_Net_Users = UK_and_Europe_Mid_Income_Individual_Addressable_Market - UK_and_Europe_Mid_Income_Individual_Churn_Loss",
            "UK_and_Europe_Low_Income_Individual_Net_Users = UK_and_Europe_Low_Income_Individual_Addressable_Market - UK_and_Europe_Low_Income_Individual_Churn_Loss",
            "Indian_Subcontinent_Small_Enterprise_Net_Users = Indian_Subcontinent_Small_Enterprise_Addressable_Market - Indian_Subcontinent_Small_Enterprise_Churn_Loss",
            "Indian_Subcontinent_Medium_Enterprise_Net_Users = Indian_Subcontinent_Medium_Enterprise_Addressable_Market - Indian_Subcontinent_Medium_Enterprise_Churn_Loss",
            "Indian_Subcontinent_Large_Enterprise_Net_Users = Indian_Subcontinent_Large_Enterprise_Addressable_Market - Indian_Subcontinent_Large_Enterprise_Churn_Loss",
            "Middle_East_and_Africa_Small_Enterprise_Net_Users = Middle_East_and_Africa_Small_Enterprise_Addressable_Market - Middle_East_and_Africa_Small_Enterprise_Churn_Loss",
            "Middle_East_and_Africa_Medium_Enterprise_Net_Users = Middle_East_and_Africa_Medium_Enterprise_Addressable_Market - Middle_East_and_Africa_Medium_Enterprise_Churn_Loss",
            "Middle_East_and_Africa_Large_Enterprise_Net_Users = Middle_East_and_Africa_Large_Enterprise_Addressable_Market - Middle_East_and_Africa_Large_Enterprise_Churn_Loss",
            "UK_and_Europe_Small_Enterprise_Net_Users = UK_and_Europe_Small_Enterprise_Addressable_Market - UK_and_Europe_Small_Enterprise_Churn_Loss",
            "UK_and_Europe_Medium_Enterprise_Net_Users = UK_and_Europe_Medium_Enterprise_Addressable_Market - UK_and_Europe_Medium_Enterprise_Churn_Loss",
            "UK_and_Europe_Large_Enterprise_Net_Users = UK_and_Europe_Large_Enterprise_Addressable_Market - UK_and_Europe_Large_Enterprise_Churn_Loss",
            "Total_User_Base = Indian_Subcontinent_High_Income_Individual_Net_Users + Indian_Subcontinent_Mid_Income_Individual_Net_Users + Indian_Subcontinent_Low_Income_Individual_Net_Users + Middle_East_and_Africa_High_Income_Individual_Net_Users + Middle_East_and_Africa_Mid_Income_Individual_Net_Users + Middle_East_and_Africa_Low_Income_Individual_Net_Users + UK_and_Europe_High_Income_Individual_Net_Users + UK_and_Europe_Mid_Income_Individual_Net_Users + UK_and_Europe_Low_Income_Individual_Net_Users + Indian_Subcontinent_Small_Enterprise_Net_Users + Indian_Subcontinent_Medium_Enterprise_Net_Users + Indian_Subcontinent_Large_Enterprise_Net_Users + Middle_East_and_Africa_Small_Enterprise_Net_Users + Middle_East_and_Africa_Medium_Enterprise_Net_Users + Middle_East_and_Africa_Large_Enterprise_Net_Users + UK_and_Europe_Small_Enterprise_Net_Users + UK_and_Europe_Medium_Enterprise_Net_Users + UK_and_Europe_Large_Enterprise_Net_Users"
        ]
    }

#pdb.set_trace()
#formula =json.loads(description_response6)["formula"]
#assumptions=json.loads(description_response6)["assumptions"]

#....................................................................fetching UB asss values
'''

description_payload = {
    "formula":formula,
    "assumptions":assumptions,
    "analysis_time_frame":['2025', '2026', '2027'],
    "period_ranges":[['January', 'December', 2025], ['January', 'December', 2026], ['January', 'December', 2027]],
    "user_description":"I want to open a competitor for OpenAI which provides 4 LLM subscriptions. I want to build a financial model which tests the feasibility and the overall return of this. I want to structure the model per subscription model, and want to have the model for 5 years straight, starting from 2026 January. I want to operate in both India, Dubai and London",
}

user_base_ass_val = requests.post(
    f"{BASE_URL}/estimate_user_base_assumption_values",
    json=description_payload,
    proxies=proxies
)

print("\nResponse from /user_base_ass_val.....................")
print(user_base_ass_val.text)

#......................................................................

description_payload = {
    "formula":f"""{formula}""",
    "assumptions":f"""{assumptions}""",
    "user_input":"Make the formula compact and keep only most important components",
    "user_description":"I want to open a competitor for OpenAI which provides 4 LLM subscriptions. I want to build a financial model which tests the feasibility and the overall return of this. I want to structure the model per subscription model, and want to have the model for 5 years straight, starting from 2026 January. I want to operate in both India, Dubai and London",
}

description_response7 = requests.post(
    f"{BASE_URL}/update_user_base_ass_formula",
    json=description_payload,
    proxies=proxies
)

#print("\nResponse from /update_user_base_ass_formula")
#print(description_response7.text)

formula= {"Step 1: Identify the size of the population in scope":["Indian_Subcontinent_Internet_Users = India_Total_Population * India_Internet_Penetration / 100","Indian_Subcontinent_High_Income_AI_Adopters = Indian_Subcontinent_Internet_Users * India_High_Income_Share / 100 * High_Income_AI_Adoption_Rate / 100","Indian_Subcontinent_Mid_Income_AI_Adopters = Indian_Subcontinent_Internet_Users * India_Mid_Income_Share / 100 * Mid_Income_AI_Adoption_Rate / 100","Indian_Subcontinent_Low_Income_AI_Adopters = Indian_Subcontinent_Internet_Users * India_Low_Income_Share / 100 * Low_Income_AI_Adoption_Rate / 100","Middle_East_Africa_Internet_Users = UAE_Total_Population * UAE_Internet_Penetration / 100","Middle_East_Africa_High_Income_AI_Adopters = Middle_East_Africa_Internet_Users * UAE_High_Income_Share / 100 * High_Income_AI_Adoption_Rate / 100","Middle_East_Africa_Mid_Income_AI_Adopters = Middle_East_Africa_Internet_Users * UAE_Mid_Income_Share / 100 * Mid_Income_AI_Adoption_Rate / 100","Middle_East_Africa_Low_Income_AI_Adopters = Middle_East_Africa_Internet_Users * UAE_Low_Income_Share / 100 * Low_Income_AI_Adoption_Rate / 100","UK_Europe_Internet_Users = UK_Total_Population * UK_Internet_Penetration / 100","UK_Europe_High_Income_AI_Adopters = UK_Europe_Internet_Users * UK_High_Income_Share / 100 * High_Income_AI_Adoption_Rate / 100","UK_Europe_Mid_Income_AI_Adopters = UK_Europe_Internet_Users * UK_Mid_Income_Share / 100 * Mid_Income_AI_Adoption_Rate / 100","UK_Europe_Low_Income_AI_Adopters = UK_Europe_Internet_Users * UK_Low_Income_Share / 100 * Low_Income_AI_Adoption_Rate / 100","Indian_Subcontinent_Small_Enterprise_Seats = India_Enterprise_Count * Small_Enterprise_Share / 100 * Small_Enterprise_AI_Adoption_Rate / 100 * Average_Seats_Per_Small_Enterprise","Indian_Subcontinent_Medium_Enterprise_Seats = India_Enterprise_Count * Medium_Enterprise_Share / 100 * Medium_Enterprise_AI_Adoption_Rate / 100 * Average_Seats_Per_Medium_Enterprise","Indian_Subcontinent_Large_Enterprise_Seats = India_Enterprise_Count * Large_Enterprise_Share / 100 * Large_Enterprise_AI_Adoption_Rate / 100 * Average_Seats_Per_Large_Enterprise","Middle_East_Africa_Small_Enterprise_Seats = UAE_Enterprise_Count * Small_Enterprise_Share / 100 * Small_Enterprise_AI_Adoption_Rate / 100 * Average_Seats_Per_Small_Enterprise","Middle_East_Africa_Medium_Enterprise_Seats = UAE_Enterprise_Count * Medium_Enterprise_Share / 100 * Medium_Enterprise_AI_Adoption_Rate / 100 * Average_Seats_Per_Medium_Enterprise","Middle_East_Africa_Large_Enterprise_Seats = UAE_Enterprise_Count * Large_Enterprise_Share / 100 * Large_Enterprise_AI_Adoption_Rate / 100 * Average_Seats_Per_Large_Enterprise","UK_Europe_Small_Enterprise_Seats = UK_Enterprise_Count * Small_Enterprise_Share / 100 * Small_Enterprise_AI_Adoption_Rate / 100 * Average_Seats_Per_Small_Enterprise","UK_Europe_Medium_Enterprise_Seats = UK_Enterprise_Count * Medium_Enterprise_Share / 100 * Medium_Enterprise_AI_Adoption_Rate / 100 * Average_Seats_Per_Medium_Enterprise","UK_Europe_Large_Enterprise_Seats = UK_Enterprise_Count * Large_Enterprise_Share / 100 * Large_Enterprise_AI_Adoption_Rate / 100 * Average_Seats_Per_Large_Enterprise"],"Step 2: Identify the growth rate of the segment":["Total_Indian_Subcontinent_High_Income_AI_Adopters = Indian_Subcontinent_High_Income_AI_Adopters * (1 + India_Population_Growth_Rate / 100)","Total_Indian_Subcontinent_Mid_Income_AI_Adopters = Indian_Subcontinent_Mid_Income_AI_Adopters * (1 + India_Population_Growth_Rate / 100)","Total_Indian_Subcontinent_Low_Income_AI_Adopters = Indian_Subcontinent_Low_Income_AI_Adopters * (1 + India_Population_Growth_Rate / 100)","Total_Middle_East_Africa_High_Income_AI_Adopters = Middle_East_Africa_High_Income_AI_Adopters * (1 + UAE_Population_Growth_Rate / 100)","Total_Middle_East_Africa_Mid_Income_AI_Adopters = Middle_East_Africa_Mid_Income_AI_Adopters * (1 + UAE_Population_Growth_Rate / 100)","Total_Middle_East_Africa_Low_Income_AI_Adopters = Middle_East_Africa_Low_Income_AI_Adopters * (1 + UAE_Population_Growth_Rate / 100)","Total_UK_Europe_High_Income_AI_Adopters = UK_Europe_High_Income_AI_Adopters * (1 + UK_Population_Growth_Rate / 100)","Total_UK_Europe_Mid_Income_AI_Adopters = UK_Europe_Mid_Income_AI_Adopters * (1 + UK_Population_Growth_Rate / 100)","Total_UK_Europe_Low_Income_AI_Adopters = UK_Europe_Low_Income_AI_Adopters * (1 + UK_Population_Growth_Rate / 100)","Total_Indian_Subcontinent_Small_Enterprise_Seats = Indian_Subcontinent_Small_Enterprise_Seats * (1 + India_Enterprise_Growth_Rate / 100)","Total_Indian_Subcontinent_Medium_Enterprise_Seats = Indian_Subcontinent_Medium_Enterprise_Seats * (1 + India_Enterprise_Growth_Rate / 100)","Total_Indian_Subcontinent_Large_Enterprise_Seats = Indian_Subcontinent_Large_Enterprise_Seats * (1 + India_Enterprise_Growth_Rate / 100)","Total_Middle_East_Africa_Small_Enterprise_Seats = Middle_East_Africa_Small_Enterprise_Seats * (1 + UAE_Enterprise_Growth_Rate / 100)","Total_Middle_East_Africa_Medium_Enterprise_Seats = Middle_East_Africa_Medium_Enterprise_Seats * (1 + UAE_Enterprise_Growth_Rate / 100)","Total_Middle_East_Africa_Large_Enterprise_Seats = Middle_East_Africa_Large_Enterprise_Seats * (1 + UAE_Enterprise_Growth_Rate / 100)","Total_UK_Europe_Small_Enterprise_Seats = UK_Europe_Small_Enterprise_Seats * (1 + UK_Enterprise_Growth_Rate / 100)","Total_UK_Europe_Medium_Enterprise_Seats = UK_Europe_Medium_Enterprise_Seats * (1 + UK_Enterprise_Growth_Rate / 100)","Total_UK_Europe_Large_Enterprise_Seats = UK_Europe_Large_Enterprise_Seats * (1 + UK_Enterprise_Growth_Rate / 100)"],"Step 3: Company market share":["Indian_Subcontinent_High_Income_Addressable_Market = Total_Indian_Subcontinent_High_Income_AI_Adopters * Indian_Subcontinent_High_Income_Market_Share / 100","Indian_Subcontinent_Mid_Income_Addressable_Market = Total_Indian_Subcontinent_Mid_Income_AI_Adopters * Indian_Subcontinent_Mid_Income_Market_Share / 100","Indian_Subcontinent_Low_Income_Addressable_Market = Total_Indian_Subcontinent_Low_Income_AI_Adopters * Indian_Subcontinent_Low_Income_Market_Share / 100","Middle_East_Africa_High_Income_Addressable_Market = Total_Middle_East_Africa_High_Income_AI_Adopters * Middle_East_Africa_High_Income_Market_Share / 100","Middle_East_Africa_Mid_Income_Addressable_Market = Total_Middle_East_Africa_Mid_Income_AI_Adopters * Middle_East_Africa_Mid_Income_Market_Share / 100","Middle_East_Africa_Low_Income_Addressable_Market = Total_Middle_East_Africa_Low_Income_AI_Adopters * Middle_East_Africa_Low_Income_Market_Share / 100","UK_Europe_High_Income_Addressable_Market = Total_UK_Europe_High_Income_AI_Adopters * UK_Europe_High_Income_Market_Share / 100","UK_Europe_Mid_Income_Addressable_Market = Total_UK_Europe_Mid_Income_AI_Adopters * UK_Europe_Mid_Income_Market_Share / 100","UK_Europe_Low_Income_Addressable_Market = Total_UK_Europe_Low_Income_AI_Adopters * UK_Europe_Low_Income_Market_Share / 100","Indian_Subcontinent_Small_Enterprise_Addressable_Seats = Total_Indian_Subcontinent_Small_Enterprise_Seats * Indian_Subcontinent_Small_Enterprise_Market_Share / 100","Indian_Subcontinent_Medium_Enterprise_Addressable_Seats = Total_Indian_Subcontinent_Medium_Enterprise_Seats * Indian_Subcontinent_Medium_Enterprise_Market_Share / 100","Indian_Subcontinent_Large_Enterprise_Addressable_Seats = Total_Indian_Subcontinent_Large_Enterprise_Seats * Indian_Subcontinent_Large_Enterprise_Market_Share / 100","Middle_East_Africa_Small_Enterprise_Addressable_Seats = Total_Middle_East_Africa_Small_Enterprise_Seats * Middle_East_Africa_Small_Enterprise_Market_Share / 100","Middle_East_Africa_Medium_Enterprise_Addressable_Seats = Total_Middle_East_Africa_Medium_Enterprise_Seats * Middle_East_Africa_Medium_Enterprise_Market_Share / 100","Middle_East_Africa_Large_Enterprise_Addressable_Seats = Total_Middle_East_Africa_Large_Enterprise_Seats * Middle_East_Africa_Large_Enterprise_Market_Share / 100","UK_Europe_Small_Enterprise_Addressable_Seats = Total_UK_Europe_Small_Enterprise_Seats * UK_Europe_Small_Enterprise_Market_Share / 100","UK_Europe_Medium_Enterprise_Addressable_Seats = Total_UK_Europe_Medium_Enterprise_Seats * UK_Europe_Medium_Enterprise_Market_Share / 100","UK_Europe_Large_Enterprise_Addressable_Seats = Total_UK_Europe_Large_Enterprise_Seats * UK_Europe_Large_Enterprise_Market_Share / 100"],"Step 4: Factor gains and losses of customers from and to competitors":["Indian_Subcontinent_High_Income_Churn = Indian_Subcontinent_High_Income_Addressable_Market * Indian_Subcontinent_High_Income_Churn_Rate / 100","Indian_Subcontinent_Mid_Income_Churn = Indian_Subcontinent_Mid_Income_Addressable_Market * Indian_Subcontinent_Mid_Income_Churn_Rate / 100","Indian_Subcontinent_Low_Income_Churn = Indian_Subcontinent_Low_Income_Addressable_Market * Indian_Subcontinent_Low_Income_Churn_Rate / 100","Middle_East_Africa_High_Income_Churn = Middle_East_Africa_High_Income_Addressable_Market * Middle_East_Africa_High_Income_Churn_Rate / 100","Middle_East_Africa_Mid_Income_Churn = Middle_East_Africa_Mid_Income_Addressable_Market * Middle_East_Africa_Mid_Income_Churn_Rate / 100","Middle_East_Africa_Low_Income_Churn = Middle_East_Africa_Low_Income_Addressable_Market * Middle_East_Africa_Low_Income_Churn_Rate / 100","UK_Europe_High_Income_Churn = UK_Europe_High_Income_Addressable_Market * UK_Europe_High_Income_Churn_Rate / 100","UK_Europe_Mid_Income_Churn = UK_Europe_Mid_Income_Addressable_Market * UK_Europe_Mid_Income_Churn_Rate / 100","UK_Europe_Low_Income_Churn = UK_Europe_Low_Income_Addressable_Market * UK_Europe_Low_Income_Churn_Rate / 100","Indian_Subcontinent_Small_Enterprise_Churn = Indian_Subcontinent_Small_Enterprise_Addressable_Seats * Indian_Subcontinent_Small_Enterprise_Churn_Rate / 100","Indian_Subcontinent_Medium_Enterprise_Churn = Indian_Subcontinent_Medium_Enterprise_Addressable_Seats * Indian_Subcontinent_Medium_Enterprise_Churn_Rate / 100","Indian_Subcontinent_Large_Enterprise_Churn = Indian_Subcontinent_Large_Enterprise_Addressable_Seats * Indian_Subcontinent_Large_Enterprise_Churn_Rate / 100","Middle_East_Africa_Small_Enterprise_Churn = Middle_East_Africa_Small_Enterprise_Addressable_Seats * Middle_East_Africa_Small_Enterprise_Churn_Rate / 100","Middle_East_Africa_Medium_Enterprise_Churn = Middle_East_Africa_Medium_Enterprise_Addressable_Seats * Middle_East_Africa_Medium_Enterprise_Churn_Rate / 100","Middle_East_Africa_Large_Enterprise_Churn = Middle_East_Africa_Large_Enterprise_Addressable_Seats * Middle_East_Africa_Large_Enterprise_Churn_Rate / 100","UK_Europe_Small_Enterprise_Churn = UK_Europe_Small_Enterprise_Addressable_Seats * UK_Europe_Small_Enterprise_Churn_Rate / 100","UK_Europe_Medium_Enterprise_Churn = UK_Europe_Medium_Enterprise_Addressable_Seats * UK_Europe_Medium_Enterprise_Churn_Rate / 100","UK_Europe_Large_Enterprise_Churn = UK_Europe_Large_Enterprise_Addressable_Seats * UK_Europe_Large_Enterprise_Churn_Rate / 100"],"Step 5: Total user base":["Indian_Subcontinent_High_Income_Users = Indian_Subcontinent_High_Income_Addressable_Market - Indian_Subcontinent_High_Income_Churn","Indian_Subcontinent_Mid_Income_Users = Indian_Subcontinent_Mid_Income_Addressable_Market - Indian_Subcontinent_Mid_Income_Churn","Indian_Subcontinent_Low_Income_Users = Indian_Subcontinent_Low_Income_Addressable_Market - Indian_Subcontinent_Low_Income_Churn","Middle_East_Africa_High_Income_Users = Middle_East_Africa_High_Income_Addressable_Market - Middle_East_Africa_High_Income_Churn","Middle_East_Africa_Mid_Income_Users = Middle_East_Africa_Mid_Income_Addressable_Market - Middle_East_Africa_Mid_Income_Churn","Middle_East_Africa_Low_Income_Users = Middle_East_Africa_Low_Income_Addressable_Market - Middle_East_Africa_Low_Income_Churn","UK_Europe_High_Income_Users = UK_Europe_High_Income_Addressable_Market - UK_Europe_High_Income_Churn","UK_Europe_Mid_Income_Users = UK_Europe_Mid_Income_Addressable_Market - UK_Europe_Mid_Income_Churn","UK_Europe_Low_Income_Users = UK_Europe_Low_Income_Addressable_Market - UK_Europe_Low_Income_Churn","Indian_Subcontinent_Small_Enterprise_Users = Indian_Subcontinent_Small_Enterprise_Addressable_Seats - Indian_Subcontinent_Small_Enterprise_Churn","Indian_Subcontinent_Medium_Enterprise_Users = Indian_Subcontinent_Medium_Enterprise_Addressable_Seats - Indian_Subcontinent_Medium_Enterprise_Churn","Indian_Subcontinent_Large_Enterprise_Users = Indian_Subcontinent_Large_Enterprise_Addressable_Seats - Indian_Subcontinent_Large_Enterprise_Churn","Middle_East_Africa_Small_Enterprise_Users = Middle_East_Africa_Small_Enterprise_Addressable_Seats - Middle_East_Africa_Small_Enterprise_Churn","Middle_East_Africa_Medium_Enterprise_Users = Middle_East_Africa_Medium_Enterprise_Addressable_Seats - Middle_East_Africa_Medium_Enterprise_Churn","Middle_East_Africa_Large_Enterprise_Users = Middle_East_Africa_Large_Enterprise_Addressable_Seats - Middle_East_Africa_Large_Enterprise_Churn","UK_Europe_Small_Enterprise_Users = UK_Europe_Small_Enterprise_Addressable_Seats - UK_Europe_Small_Enterprise_Churn","UK_Europe_Medium_Enterprise_Users = UK_Europe_Medium_Enterprise_Addressable_Seats - UK_Europe_Medium_Enterprise_Churn","UK_Europe_Large_Enterprise_Users = UK_Europe_Large_Enterprise_Addressable_Seats - UK_Europe_Large_Enterprise_Churn","Total_User_Base = Indian_Subcontinent_High_Income_Users + Indian_Subcontinent_Mid_Income_Users + Indian_Subcontinent_Low_Income_Users + Middle_East_Africa_High_Income_Users + Middle_East_Africa_Mid_Income_Users + Middle_East_Africa_Low_Income_Users + UK_Europe_High_Income_Users + UK_Europe_Mid_Income_Users + UK_Europe_Low_Income_Users + Indian_Subcontinent_Small_Enterprise_Users + Indian_Subcontinent_Medium_Enterprise_Users + Indian_Subcontinent_Large_Enterprise_Users + Middle_East_Africa_Small_Enterprise_Users + Middle_East_Africa_Medium_Enterprise_Users + Middle_East_Africa_Large_Enterprise_Users + UK_Europe_Small_Enterprise_Users + UK_Europe_Medium_Enterprise_Users + UK_Europe_Large_Enterprise_Users"]}

# SOlve user base equations..............................
description_payload = {
    "assumption_values":{'2025': ['', 5, 12, 5825400, 99.5, 14, 18, 410800, 16, 31, 19, 3, 48, 66625000, 520, 10280000, 85, 24, 1432200000, 96, 46, 52, 40, 50, 7, 68407000, 52, 30, 11, 52, 36, '', 3.1, 2.4, 3.0, 2.8, 2.3, 2.6, '', 7, 5, 25, 4, 12, 3, 2, 10, 10, 6, 18, 14, 7, 12, 10, 5, 20, 14, '', 13, 10, 9, 16, 6, 18, 10, 12, 7, 5, 8, 8, 8, 12, 14, 6, 10, 7, ''], '2026': ['', 5, 12, 5967208, 99.8, 13, 22, 423124, 17, 32, 18, 3, 46, 68490500, 540, 10598680, 85, 29, 1469472000, 97, 47, 54, 40, 50, 9, 69983610, 60, 36, 14, 58, 37, '', 3.4, 2.6, 3.3, 3.1, 2.5, 2.9, '', 8, 6, 28, 5, 14, 4, 3, 12, 12, 7, 21, 16, 8, 14, 12, 6, 22, 16, '', 11, 8, 7, 14, 5, 16, 8, 10, 6, 4, 6, 6, 6, 10, 12, 4, 8, 6, ''], '2027': ['', 5, 12, 6265766, 99.9, 11, 32, 447894, 19, 34, 16, 3, 42, 72142470, 580, 11224178, 85, 42, 1542926600, 98, 49, 58, 40, 50, 14, 73333000, 78, 48, 22, 72, 39, '', 4.2, 3.1, 4.0, 3.8, 3.0, 3.6, '', 11, 9, 35, 8, 19, 7, 6, 17, 17, 10, 28, 21, 11, 19, 17, 9, 27, 21, '', 8, 5, 4, 11, 3, 13, 5, 7, 4, 2, 3, 3, 3, 7, 9, 2, 5, 4, '']},
    "units":['', '#', '%', '#', '%', '%', '%', '#', '%', '%', '%', '%', '%', '#', '#', '#', '%', '%', '#', '%', '%', '#', '%', '%', '%', '#', '%', '%', '%', '%', '%', '', '%', '%', '%', '%', '%', '%', '', '%', '%', '%', '%', '%', '%', '%', '%', '%', '%', '%', '%', '%', '%', '%', '%', '%', '%', '', '%', '%', '%', '%', '%', '%', '%', '%', '%', '%', '%', '%', '%', '%', '%', '%', '%', '%', ''],
    "currency":"USD",
    "formula":formula,
    "steps":['Step 1: Identify the size of the population in scope', 'Average_Seats_Per_Small_Enterprise', 'Medium_Enterprise_Share', 'UK_Enterprise_Count', 'UAE_Internet_Penetration', 'UAE_Low_Income_Share', 'Mid_Income_AI_Adoption_Rate', 'UAE_Enterprise_Count', 'India_High_Income_Share', 'UK_High_Income_Share', 'UK_Low_Income_Share', 'Large_Enterprise_Share', 'India_Low_Income_Share', 'India_Enterprise_Count', 'Average_Seats_Per_Large_Enterprise', 'UAE_Total_Population', 'Small_Enterprise_Share', 'Medium_Enterprise_AI_Adoption_Rate', 'India_Total_Population', 'UK_Internet_Penetration', 'UAE_Mid_Income_Share', 'Average_Seats_Per_Medium_Enterprise', 'UAE_High_Income_Share', 'UK_Mid_Income_Share', 'Low_Income_AI_Adoption_Rate', 'UK_Total_Population', 'Large_Enterprise_AI_Adoption_Rate', 'High_Income_AI_Adoption_Rate', 'Small_Enterprise_AI_Adoption_Rate', 'India_Internet_Penetration', 'India_Mid_Income_Share', 'Step 2: Identify the growth rate of the segment', 'UAE_Population_Growth_Rate', 'UK_Enterprise_Growth_Rate', 'UAE_Enterprise_Growth_Rate', 'India_Enterprise_Growth_Rate', 'UK_Population_Growth_Rate', 'India_Population_Growth_Rate', 'Step 3: Company market share', 'Middle_East_Africa_Small_Enterprise_Market_Share', 'Indian_Subcontinent_Medium_Enterprise_Market_Share', 'UK_Europe_Large_Enterprise_Market_Share', 'Indian_Subcontinent_Mid_Income_Market_Share', 'Middle_East_Africa_Medium_Enterprise_Market_Share', 'Indian_Subcontinent_Small_Enterprise_Market_Share', 'Indian_Subcontinent_Low_Income_Market_Share', 'Middle_East_Africa_Mid_Income_Market_Share', 'Indian_Subcontinent_Large_Enterprise_Market_Share', 'Indian_Subcontinent_High_Income_Market_Share', 'UK_Europe_High_Income_Market_Share', 'Middle_East_Africa_High_Income_Market_Share', 'UK_Europe_Low_Income_Market_Share', 'UK_Europe_Mid_Income_Market_Share', 'UK_Europe_Small_Enterprise_Market_Share', 'Middle_East_Africa_Low_Income_Market_Share', 'Middle_East_Africa_Large_Enterprise_Market_Share', 'UK_Europe_Medium_Enterprise_Market_Share', 'Step 4: Factor gains and losses of customers from and to competitors', 'Indian_Subcontinent_High_Income_Churn_Rate', 'UK_Europe_Low_Income_Churn_Rate', 'UK_Europe_Medium_Enterprise_Churn_Rate', 'Middle_East_Africa_High_Income_Churn_Rate', 'Middle_East_Africa_Large_Enterprise_Churn_Rate', 'UK_Europe_High_Income_Churn_Rate', 'Indian_Subcontinent_Mid_Income_Churn_Rate', 'Middle_East_Africa_Mid_Income_Churn_Rate', 'Indian_Subcontinent_Medium_Enterprise_Churn_Rate', 'Indian_Subcontinent_Large_Enterprise_Churn_Rate', 'Middle_East_Africa_Low_Income_Churn_Rate', 'Middle_East_Africa_Medium_Enterprise_Churn_Rate', 'Indian_Subcontinent_Small_Enterprise_Churn_Rate', 'UK_Europe_Small_Enterprise_Churn_Rate', 'UK_Europe_Mid_Income_Churn_Rate', 'Indian_Subcontinent_Low_Income_Churn_Rate', 'Middle_East_Africa_Small_Enterprise_Churn_Rate', 'UK_Europe_Large_Enterprise_Churn_Rate', 'Step 5: Total user base'],
}

user_base_compute = requests.post(
    f"{BASE_URL}/compute_user_base",
    json=description_payload,
    proxies=proxies
)

print("\nResponse from /user_base_compute.....................")
print(user_base_compute.text)

'''


# description_payload = {
#     "user_description":"I want to provide 4 types of LLM subscriptions service. which are base subscription, premium subscription, executive subscriptions and extramile subscriptions"
# }

# revenue_split_output = requests.post(
#     f"{BASE_URL}/revenue_splits",
#     json=description_payload,
#     proxies=proxies
# )

# print("\nResponse from /revenue_splits.....................")
# print(revenue_split_output.text)

# #...................................................
# description_payload = {
#     "current_logic":revenue_split_output.text,
#     "user_input":"yes there would be cross selling between base subscription and premium subscription, premium subscription and executive subscriptions"
# }

# revenue_split_output_cross = requests.post(
#     f"{BASE_URL}/revenue_splits_with_cross_Selling",
#     json=description_payload,
#     proxies=proxies
# )

# print("\nResponse from /revenue_splits_with_cross_Selling.....................")
# print(revenue_split_output_cross.text)

#................................

description_payload = {
    "formula":formula,
}
revenue_split_output_cross = requests.post(
    f"{BASE_URL}/user_base_independent_component",
    json=description_payload,
    proxies=proxies
)

print("\nResponse from /user_base_independent_component.....................")
print(revenue_split_output_cross.text)


#......................get price.................

description_payload = {
    "user_description":"I want to open a competitor for OpenAI which provides 4 LLM subscriptions. I want to build a financial model which tests the feasibility and the overall return of this. I want to structure the model per subscription model, and want to have the model for 5 years straight, starting from 2026 January. I want to operate in both India, Dubai and London",
    "Billing_info": "base subscription is billed quarteyly, premium subscription is billed halfyearly and yearly",
    "Revenue_sources":  ["base subscription","premium subscription", "executive subscriptions", "extramile subscriptions"], 
    "currency": "USD",
    "analysis_interval": "yearly",
}
revenue_stream_price = requests.post(
    f"{BASE_URL}/price_of_each_revenue_stream",
    json=description_payload,
    proxies=proxies
)

print("\nResponse from /user_base_independent_component.....................")
print(revenue_stream_price.text)
#..................revenue formula________

price_key = list(json.loads(revenue_stream_price.text)["Price"].keys())
#pdb.set_trace()
description_payload = {
    "user_description":"I want to open a competitor for OpenAI which provides 4 LLM subscriptions. I want to build a financial model which tests the feasibility and the overall return of this. I want to structure the model per subscription model, and want to have the model for 5 years straight, starting from 2026 January. I want to operate in both India, Dubai and London",
    "total_user": ["Europe_user", "India_user","Dubai_user"],
    "billing": "Basic_LLM is billed monthly and quaterly, Standard_LLM is billed quaterly and halfyearly and Executive_LLM is billed halfyearly",
    "additional_revenue": f"yes, consider 6% of the total revene obtained from the LLM subscriptions", 
    "revenue_sources_splits":["Basic_LLM", "Standard_LLM", "Executive_LLM"],
    "revenue_sources_splits_with_cross_selling":{
    "Basic_LLM (%)": 20,
    "Standard_LLM (%)": 30,
    "Executive_LLM (%)": 20,
    "Basic_LLM_and_Standard_LLM (%)": 15,
    "Basic_LLM_and_Executive_LLM (%)": 15
  },
    "currency": "USD",
    "interval": "yearly",
    "price_key":price_key
}


revenue_assumption_formula = requests.post(
    f"{BASE_URL}/fetch_revenue_formula_assumption",
    json=description_payload,
    proxies=proxies
)

print("\nResponse from /revenue_assumption_formula.....................")
print(revenue_assumption_formula.text)
pdb.set_trace()
rev_formula =json.loads(revenue_assumption_formula.text)["formula"]
rev_assumption=json.loads(revenue_assumption_formula.text)["assumptions"]

#......................................................................................Update Revenue..............
price_key = ['base_subscription_quarterly_price (USD)', 'premium_subscription_halfyearly_price (USD)', 'premium_subscription_yearly_price (USD)', 'executive_subscriptions_yearly_price (USD)', 'extramile_subscriptions_yearly_price (USD)']
#rev_formula = {'Step 1: Identify user across different product/services': ['Total_user_base = Europe_user + India_user + Dubai_user', 'Basic_LLM_users = Total_user_base * (Basic_LLM (%) / 100) + Total_user_base * (Basic_LLM_and_Standard_LLM (%) / 100) + Total_user_base * (Basic_LLM_and_Executive_LLM (%) / 100)', 'Standard_LLM_users = Total_user_base * (Standard_LLM (%) / 100) + Total_user_base * (Basic_LLM_and_Standard_LLM (%) / 100)', 'Executive_LLM_users = Total_user_base * (Executive_LLM (%) / 100) + Total_user_base * (Basic_LLM_and_Executive_LLM (%) / 100)'], 'Step 2: Breakdown the user base by plan tenure': ['Basic_LLM_monthly_billing_users = Basic_LLM_users * (Basic_LLM_monthly_share (%) / 100) * (monthly_effective_rate (%) / 100)', 'Basic_LLM_quarterly_billing_users = Basic_LLM_users * (Basic_LLM_quarterly_share (%) / 100) * (quarterly_effective_rate (%) / 100)', 'Standard_LLM_quarterly_billing_users = Standard_LLM_users * (Standard_LLM_quarterly_share (%) / 100) * (quarterly_effective_rate (%) / 100)', 'Standard_LLM_halfyearly_billing_users = Standard_LLM_users * (Standard_LLM_halfyearly_share (%) / 100) * (halfyearly_effective_rate (%) / 100)', 'Executive_LLM_halfyearly_billing_users = Executive_LLM_users * (Executive_LLM_halfyearly_share (%) / 100) * (halfyearly_effective_rate (%) / 100)'], 'Step 3: Identify the pricing rate for each product/services': ['Basic_LLM_monthly_discounted_price (USD) = (Basic_LLM_monthly_price * (12 - Basic_LLM_monthly_discount_period) + Basic_LLM_monthly_price * Basic_LLM_monthly_discount_period * (100 - Basic_LLM_monthly_discount) / 100) / 12', 'Basic_LLM_quarterly_discounted_price (USD) = (Basic_LLM_quarterly_price * (12 - Basic_LLM_quarterly_discount_period) + Basic_LLM_quarterly_price * Basic_LLM_quarterly_discount_period * (100 - Basic_LLM_quarterly_discount) / 100) / 12', 'Standard_LLM_quarterly_discounted_price (USD) = (Standard_LLM_quarterly_price * (12 - Standard_LLM_quarterly_discount_period) + Standard_LLM_quarterly_price * Standard_LLM_quarterly_discount_period * (100 - Standard_LLM_quarterly_discount) / 100) / 12', 'Standard_LLM_halfyearly_discounted_price (USD) = (Standard_LLM_halfyearly_price * (12 - Standard_LLM_halfyearly_discount_period) + Standard_LLM_halfyearly_price * Standard_LLM_halfyearly_discount_period * (100 - Standard_LLM_halfyearly_discount) / 100) / 12', 'Executive_LLM_halfyearly_discounted_price (USD) = (Executive_LLM_halfyearly_price * (12 - Executive_LLM_halfyearly_discount_period) + Executive_LLM_halfyearly_price * Executive_LLM_halfyearly_discount_period * (100 - Executive_LLM_halfyearly_discount) / 100) / 12'], 'Step 4: Revenue computation for each product line': ['Basic_LLM_Revenue (USD) = Basic_LLM_monthly_billing_users * Basic_LLM_monthly_discounted_price * 12 + Basic_LLM_quarterly_billing_users * Basic_LLM_quarterly_discounted_price * 4', 'Standard_LLM_Revenue (USD) = Standard_LLM_quarterly_billing_users * Standard_LLM_quarterly_discounted_price * 4 + Standard_LLM_halfyearly_billing_users * Standard_LLM_halfyearly_discounted_price * 2', 'Executive_LLM_Revenue (USD) = Executive_LLM_halfyearly_billing_users * Executive_LLM_halfyearly_discounted_price * 2'], 'Step 5: Total revenue from all product/services': ['LLM_Subscription_Revenue (USD) = Basic_LLM_Revenue + Standard_LLM_Revenue + Executive_LLM_Revenue', 'Additional_Revenue (USD) = LLM_Subscription_Revenue * (Additional_Revenue_Contribution (%) / 100)', 'Total_Company_Revenue (USD) = LLM_Subscription_Revenue + Additional_Revenue']}
#rev_assumption={'Basic_LLM (%)': 20, 'Standard_LLM (%)': 30, 'Executive_LLM (%)': 20, 'Basic_LLM_and_Standard_LLM (%)': 15, 'Basic_LLM_and_Executive_LLM (%)': 15, 'Basic_LLM_monthly_share (%)': 65, 'Basic_LLM_quarterly_share (%)': 35, 'Standard_LLM_quarterly_share (%)': 55, 'Standard_LLM_halfyearly_share (%)': 45, 'Executive_LLM_halfyearly_share (%)': 100, 'monthly_effective_rate (%)': 85, 'quarterly_effective_rate (%)': 92, 'halfyearly_effective_rate (%)': 95, 'Basic_LLM_monthly_price (USD)': 60, 'Basic_LLM_quarterly_price (USD)': 180, 'Standard_LLM_quarterly_price (USD)': 360, 'Standard_LLM_halfyearly_price (USD)': 600, 'Executive_LLM_halfyearly_price (USD)': 1200, 'Basic_LLM_monthly_discount (%)': 15, 'Basic_LLM_quarterly_discount (%)': 20, 'Standard_LLM_quarterly_discount (%)': 18, 'Standard_LLM_halfyearly_discount (%)': 25, 'Executive_LLM_halfyearly_discount (%)': 30, 'Basic_LLM_monthly_discount_period (month)': 2, 'Basic_LLM_quarterly_discount_period (month)': 3, 'Standard_LLM_quarterly_discount_period (month)': 2, 'Standard_LLM_halfyearly_discount_period (month)': 4, 'Executive_LLM_halfyearly_discount_period (month)': 3, 'Additional_Revenue_Contribution (%)': 6}

# description_payload = {
#     "user_description":"I want to open a competitor for OpenAI which provides 4 LLM subscriptions. I want to build a financial model which tests the feasibility and the overall return of this. I want to structure the model per subscription model, and want to have the model for 5 years straight, starting from 2026 January. I want to operate in both India, Dubai and London",
#     "total_user": ["Europe_user", "India_user","Dubai_user"],
#     "billing": "Basic_LLM is billed monthly and quaterly, Standard_LLM is billed quaterly and halfyearly and Executive_LLM is billed halfyearly",
#     "additional_revenue": f"yes, consider 6% of the total revene obtained from the LLM subscriptions", 
#     "revenue_sources_splits":["Basic_LLM", "Standard_LLM", "Executive_LLM"],
#     "currency": "USD",
#     "interval": "yearly",
#     "price_key":price_key,
#     "revenue_formula":rev_formula,
#     "revenue_assumption":rev_assumption,
#     "instruction":"make the revenue formula compact and consize"
# }    


# updated_revenue_assumption_formula = requests.post(
#     f"{BASE_URL}/update_revenue_formula_assumption",
#     json=description_payload,
#     proxies=proxies
# )

# print("\nResponse from /update revenue_assumption_formula.....................")
# print(updated_revenue_assumption_formula.text)


#.............................................Get assumption values


description_payload = {
    "formula":rev_formula,
    "assumptions":rev_assumption,
    "analysis_time_frame":['2025', '2026', '2027'],
    "period_ranges":[['January', 'December', 2025], ['January', 'December', 2026], ['January', 'December', 2027]],
    "user_description":"I want to open a competitor for OpenAI which provides 4 LLM subscriptions. I want to build a financial model which tests the feasibility and the overall return of this. I want to structure the model per subscription model, and want to have the model for 5 years straight, starting from 2026 January. I want to operate in both India, Dubai and London",
    "currency":"USD"
}

Revenue_ass_val = requests.post(
    f"{BASE_URL}/estimate_revenue_assumption_values",
    json=description_payload,
    proxies=proxies
)

print("\nResponse from /user_base_ass_val.....................")
print(Revenue_ass_val.text)

#.......

steps=["Step 1: Identify user across different product/services","Basic_LLM_and_Executive_LLM","Standard_LLM","Basic_LLM","Executive_LLM","Basic_LLM_and_Standard_LLM","Step 2: Breakdown the user base by plan tenure","quarterly_effective_rate","halfyearly_effective_rate","Basic_LLM_quarterly_share","monthly_effective_rate","Standard_LLM_quarterly_share","Standard_LLM_halfyearly_share","Basic_LLM_monthly_share","Executive_LLM_halfyearly_share","Step 3: Identify the pricing rate for each product/services","Basic_LLM_monthly_discount_period","Standard_LLM_halfyearly_discount","Standard_LLM_quarterly_discount","Executive_LLM_halfyearly_price","Standard_LLM_quarterly_price","Standard_LLM_quarterly_discount_period","Executive_LLM_halfyearly_discount","Basic_LLM_quarterly_discount","Executive_LLM_halfyearly_discount_period","Basic_LLM_monthly_discount","Basic_LLM_monthly_price","Basic_LLM_quarterly_price","Basic_LLM_quarterly_discount_period","Standard_LLM_halfyearly_price","Standard_LLM_halfyearly_discount_period","Step 4: Revenue computation for each product line","Step 5: Total revenue from all product/services","Additional_Revenue_Contribution"]
units=["","%","%","%","%","%","","%","%","%","%","%","%","%","%","","month","%","%","USD","USD","month","%","%","month","%","USD","USD","month","USD","month","","","%"]
values={"2025":["",15,30,20,20,15,"",92,95,35,85,55,45,65,100,"",2,25,18,1200,360,2,30,20,3,15,60,180,3,600,4,"","",6],"2026":["",15,30,20,20,15,"",94,96,35,87,55,45,65,100,"",2,22,15,1280,385,2,28,18,3,12,65,195,3,640,4,"","",6],"2027":["",15,30,20,20,15,"",89,93,35,82,55,45,65,100,"",2,28,21,1150,340,2,32,22,3,18,55,165,3,560,4,"","",6]}


#["Indian_Subcontinent_High_Income_Individual_Net_Users","Indian_Subcontinent_Mid_Income_Individual_Net_Users","Indian_Subcontinent_Low_Income_Individual_Net_Users","Middle_East_and_Africa_High_Income_Individual_Net_Users","Middle_East_and_Africa_Mid_Income_Individual_Net_Users","Middle_East_and_Africa_Low_Income_Individual_Net_Users","UK_and_Europe_High_Income_Individual_Net_Users","UK_and_Europe_Mid_Income_Individual_Net_Users","UK_and_Europe_Low_Income_Individual_Net_Users","Indian_Subcontinent_Small_Enterprise_Net_Users","Indian_Subcontinent_Medium_Enterprise_Net_Users","Indian_Subcontinent_Large_Enterprise_Net_Users","Middle_East_and_Africa_Small_Enterprise_Net_Users","Middle_East_and_Africa_Medium_Enterprise_Net_Users","Middle_East_and_Africa_Large_Enterprise_Net_Users","UK_and_Europe_Small_Enterprise_Net_Users","UK_and_Europe_Medium_Enterprise_Net_Users","UK_and_Europe_Large_Enterprise_Net_Users"]

# SOlve revenue equations..............................
description_payload = {
    "assumption_values":{"2025":["",15,30,20,20,15,"",92,95,35,85,55,45,65,100,"",2,25,18,1200,360,2,30,20,3,15,60,180,3,600,4,"","",6, 256, 256, 256],"2026":["",15,30,20,20,15,"",94,96,35,87,55,45,65,100,"",2,22,15,1280,385,2,28,18,3,12,65,195,3,640,4,"","",6, 356, 356, 356],"2027":["",15,30,20,20,15,"",89,93,35,82,55,45,65,100,"",2,28,21,1150,340,2,32,22,3,18,55,165,3,560,4,"","",6,456, 456, 456]},
    "units":["","%","%","%","%","%","","%","%","%","%","%","%","%","%","","month","%","%","USD","USD","month","%","%","month","%","USD","USD","month","USD","month","","","%", '#', '#', '#'],
    "currency":"USD",
    "formula":rev_formula,
    "steps":["Step 1: Identify user across different product/services","Basic_LLM_and_Executive_LLM","Standard_LLM","Basic_LLM","Executive_LLM","Basic_LLM_and_Standard_LLM","Step 2: Breakdown the user base by plan tenure","quarterly_effective_rate","halfyearly_effective_rate","Basic_LLM_quarterly_share","monthly_effective_rate","Standard_LLM_quarterly_share","Standard_LLM_halfyearly_share","Basic_LLM_monthly_share","Executive_LLM_halfyearly_share","Step 3: Identify the pricing rate for each product/services","Basic_LLM_monthly_discount_period","Standard_LLM_halfyearly_discount","Standard_LLM_quarterly_discount","Executive_LLM_halfyearly_price","Standard_LLM_quarterly_price","Standard_LLM_quarterly_discount_period","Executive_LLM_halfyearly_discount","Basic_LLM_quarterly_discount","Executive_LLM_halfyearly_discount_period","Basic_LLM_monthly_discount","Basic_LLM_monthly_price","Basic_LLM_quarterly_price","Basic_LLM_quarterly_discount_period","Standard_LLM_halfyearly_price","Standard_LLM_halfyearly_discount_period","Step 4: Revenue computation for each product line","Step 5: Total revenue from all product/services","Additional_Revenue_Contribution","Europe_user", "India_user","Dubai_user"],
}

user_base_compute = requests.post(
    f"{BASE_URL}/compute_user_base",
    json=description_payload,
    proxies=proxies
)

print("\nResponse from /Revenue.....................")
print(user_base_compute.text)