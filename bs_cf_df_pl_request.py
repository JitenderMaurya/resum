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


# Revenue = {"2025": "1089208", "2026": "20189208", "2027": "20589805"}
# C_opex = {"2025": "5029208", "2026": "5069308", "2027": "5127208"}
# D_and_A = {"2025": "5204", "2026": "6301", "2027": "6903"}
# analysis_time_frame = ["2025","2026","2027"] 
# currency ="USD"
# interval = "yearly"
# #capex = {"2025": "98398", "2026": "68468", "2027": "64804"}
# # P & L Assumptions
# tax_rate_assumption = 12
# Impairment_Share = 0.01
# non_operational_income_Share = 0.23
# non_operational_costs_Share = 0.42

# # Balancesheet Assumptions
# trade_and_other_receivables_share = 3  
# prepaid_expenses_share = 2
# inventory_share = 3
# long_term_receivables_share = 5
# trade_and_other_payables_share = 3
# unearned_revenue_share = 2
# legal_reserve_Fixed_assumption ={"2025": 25000, "2026": 0, "2027": 0}
# Revaluation_Reserve_Fixed_assumption ={"2025": 25000, "2026": 0, "2027": 0}
# Sale_of_Asset = {"2025": "5204", "2026": "2301", "2027": "1103"}
# initial_PPE = 300
# dividend_share = 10
# dividend = 0
# employe_personel_cost =  {"2025": "1000000", "2026": "1500000", "2027": "2000000"} #

# # Cashflow Assumptions
# depriciation = {"2025":5900, "2026":7878, "2027":6436}

# # Debt_financing Assumptions
# Market_Interest_rates  = 10 # %
# Debt_Payback_period = 3 #year
# Minimum_Desired_Cash = 25000  
# Opening_Cash_Balance = 0
# Equity_Sale = {"2025":"0", "2026":"43322", "2027":"51422"}
# capex = {"2025": "98398", "2026": "68468", "2027": "64804"}
# P_L,B_S,C_F,D_F = compute_pl_bs_cf_fr(Revenue,C_opex,D_and_A, analysis_time_frame, currency, non_operational_income_Share, non_operational_costs_Share,Sale_of_Asset,trade_and_other_receivables_share,prepaid_expenses_share,inventory_share,long_term_receivables_share,trade_and_other_payables_share,unearned_revenue_share,legal_reserve_Fixed_assumption,Revaluation_Reserve_Fixed_assumption,employe_personel_cost,Debt_Payback_period,Market_Interest_rates,Minimum_Desired_Cash,Opening_Cash_Balance,Equity_Sale)

# print(P_L)
# print(B_S)
# print(C_F)
# print(D_F)

Revenue = {"H1 2025": "1089208", "H2 2025": "20189208", "H1 2026": "20589805"}
cost = {"H1 2025": "5029208", "H2 2025": "5069308", "H1 2026": "5127208"}
D_and_A = {"H1 2025": "5204", "H2 2025": "6301", "H1 2026": "6903"}
analysis_time_frame = ["H1 2025","H2 2025","H1 2026"] 
currency ="USD"
interval = "halfyearly"
capex = {"H1 2025": "98398", "H2 2025": "68468", "H1 2026": "64804"}
# P & L Assumptions
tax_rate_assumption = 12
impairment_share = {"H1 2025": 0.01, "H2 2025": 0.02, "H1 2026": 0.03} # Impairment share for each year
non_operational_income_Share ={"H1 2025": 0.23, "H2 2025": 0.25, "H1 2026": 0.27} # Non-operational income share for each year
non_operational_costs_Share = {"H1 2025": 0.42, "H2 2025": 0.45, "H1 2026": 0.47} # Non-operational costs share for each year
# Balancesheet Assumptions
trade_and_other_receivables_share = {"H1 2025": 3, "H2 2025": 3.1, "H1 2026": 3.2} # Trade and other receivables share for each year
prepaid_expenses_share = {"H1 2025": 2, "H2 2025": 2.1, "H1 2026": 2.2} # Prepaid expenses share for each year
inventory_share = {"H1 2025": 3, "H2 2025": 3.1, "H1 2026": 3.2} # Inventory share for each year
long_term_receivables_share = {"H1 2025": 5, "H2 2025": 5.1, "H1 2026": 5.2} # Long-term receivables share for each year
trade_and_other_payables_share={"H1 2025": 3, "H2 2025": 3.1, "H1 2026": 3.2} # Trade and other payables share for each year
unearned_revenue_share = {"H1 2025": 2, "H2 2025": 2.1, "H1 2026": 2.2} # Unearned revenue share for each year
legal_reserve_Fixed_assumption ={"H1 2025": 25000, "H2 2025": 0, "H1 2026": 0}
Revaluation_Reserve_Fixed_assumption ={"H1 2025": 25000,"H2 2025": 0, "H1 2026": 0}
Sale_of_Asset = {"H1 2025": "5204", "H2 2025": "2301", "H1 2026": "1103"}
initial_PPE = 300
dividend_share = 10
dividend = 0
employe_personel_cost =  {"H1 2025": "1000000","H2 2025": "1500000", "H1 2026": "2000000"} #

# Cashflow Assumptions
depriciation = {"H1 2025":5900, "H2 2025":7878, "H1 2026":6436}

# Debt_financing Assumptions
Market_Interest_rates = {"H1 2025": 10, "H2 2025": 10, "H1 2026": 10} # Interest rates for each year
Debt_Payback_period = 1.5 #year
Minimum_Desired_Cash = 25000  
Opening_Cash_Balance = 0
Equity_Sale = {"H1 2025":"0", "H2 2025":"43322", "H1 2026":"51422"}



description_payload = {
    "revenue":Revenue,
    "cost":cost,
    "capex":capex,
    "d_and_a":D_and_A,
    "analysis_time_frame":analysis_time_frame,
    "currency":"USD",
    "non_operational_income_share":non_operational_income_Share,
    "non_operational_costs_share":non_operational_costs_Share,
    "sale_of_asset":Sale_of_Asset,
    "trade_and_other_receivables_share":trade_and_other_receivables_share,
    "prepaid_expenses_share":trade_and_other_payables_share,
    "inventory_share":inventory_share,
    "long_term_receivables_share":long_term_receivables_share,
    "trade_and_other_payables_share":trade_and_other_payables_share,
    "unearned_revenue_share":unearned_revenue_share,
    "legal_reserve_fixed_assumption":legal_reserve_Fixed_assumption,
    "revaluation_reserve_fixed_assumption":Revaluation_Reserve_Fixed_assumption,
    "employe_personel_cost":employe_personel_cost,
    "debt_payback_period":Debt_Payback_period,
    "market_interest_rates":Market_Interest_rates,
    "minimum_desired_cash":Minimum_Desired_Cash,
    "opening_cash_balance":Opening_Cash_Balance,
    "equity_sale":Equity_Sale,
    "tax_rate_assumption":tax_rate_assumption,
    "interval":interval,
    "impairment_share":impairment_share,
    "dividend":dividend,
    "dividend_share":dividend_share,
}


cash_flow_bs_pl = requests.post(
    f"{BASE_URL}/estimate_cf_pl_bs_df",
    json=description_payload,
    proxies=proxies
)

print("\nResponse from /Cost.....................")
print(cash_flow_bs_pl.text)
