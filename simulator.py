"""
Cockroach population simulator using compound interest formula with interventions.
"""

def calculate_population(initial_pop, growth_rate, periods, interventions=None):
    """
    Calculate population growth using compound interest formula with optional pest control interventions.
    
    Args:
        initial_pop (float): Initial population count.
        growth_rate (float): Growth rate per period (as decimal, e.g., 0.03 for 3%).
        periods (int): Number of periods to simulate.
        interventions (list of tuples, optional): Each tuple (period, reduction_rate) where
            reduction_rate is the fraction of population that survives after intervention.
            Example: [(20, 0.6), (40, 0.8)] means 60% survive at period 20, 80% survive at period 40.
    
    Returns:
        float: Final population after given periods.
    """
    population = initial_pop
    # Sort interventions by period to apply in order
    if interventions:
        interventions = sorted(interventions, key=lambda x: x[0])
    
    for t in range(1, periods + 1):
        population = population * (1 + growth_rate)
        # Apply any intervention scheduled for this period
        if interventions:
            for period, reduction_rate in interventions:
                if period == t:
                    population = population * reduction_rate
                    # Assuming each intervention only applies once, break inner loop
                    break
    
    return population


if __name__ == "__main__":
    # Sample simulation without interventions
    initial = 10
    rate = 0.03  # 3% weekly growth
    weeks = 52
    
    final_pop = calculate_population(initial, rate, weeks)
    print("=== Simulation without interventions ===")
    print(f"Initial population: {initial}")
    print(f"Weekly growth rate: {rate*100:.1f}%")
    print(f"Number of weeks: {weeks}")
    print(f"Final population: {final_pop:.2f}")
    print()
    
    # Sample simulation with interventions
    interventions = [(20, 0.6), (40, 0.8)]  # 40% reduction at week 20, 20% reduction at week 40
    final_pop_with = calculate_population(initial, rate, weeks, interventions)
    print("=== Simulation with interventions ===")
    print(f"Interventions: {interventions}")
    print(f"Final population: {final_pop_with:.2f}")
    print(f"Effect: {final_pop_with:.2f} vs {final_pop:.2f} without interventions")