# Cassaiglobal Genesis - Energy Mesh
# Function: Kinetic Energy Recovery System (KERS) Logic

def calculate_wattage(vehicle_count, axle_weight_avg):
    """Converts A56 traffic into Sovereign Joules."""
    efficiency_factor = 0.18 # Piezoelectric glass-tarmac efficiency
    joules = vehicle_count * axle_weight_avg * efficiency_factor
    kwh = joules / 3600000
    return f"RECLAIMED ENERGY: {kwh:.4f} kWh. Powering Node 02."

print(calculate_wattage(1500, 2000)) # 1500 cars, 2 ton avg
