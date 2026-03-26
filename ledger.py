# Cassaiglobal Genesis Kernel - Sovereign Ledger
# Function: Economic Reclamation & ROI Calculation

def calculate_system_failure(hostel_weekly_cost, trauma_index):
    """Calculates the true cost of 'Static' housing."""
    annual_drain = hostel_weekly_cost * 52
    # The 'Trauma Multiplier' represents long-term cost to the 18 Sons
    social_debt = annual_drain * (trauma_index * 1.5)
    
    return {
        "Annual_Cash_Waste": annual_drain,
        "Total_Social_Debt": social_debt,
        "Genesis_Solution_Cost": annual_drain * 0.4 # 60% more efficient
    }

# Audit: £400/week hostel room vs. Sovereign Node
audit = calculate_system_failure(400, 10)
print(f"STATIC SYSTEM DEBT: £{audit['Total_Social_Debt']}")
print(f"GENESIS RECLAMATION SAVINGS: £{audit['Annual_Cash_Waste'] - audit['Genesis_Solution_Cost']}")
