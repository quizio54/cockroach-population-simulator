"""
Cockroach population simulator using compound interest formula.
"""

def calculate_population(initial_pop, growth_rate, periods):
    """
    Calculate population growth using compound interest formula.
    
    Args:
        initial_pop (float): Initial population count.
        growth_rate (float): Growth rate per period (as decimal, e.g., 0.03 for 3%).
        periods (int): Number of periods to simulate.
    
    Returns:
        float: Final population after given periods.
    """
    return initial_pop * ((1 + growth_rate) ** periods)


if __name__ == "__main__":
    # Sample simulation
    initial = 10
    rate = 0.03  # 3% weekly growth
    weeks = 52
    
    final_pop = calculate_population(initial, rate, weeks)
    print(f"Initial population: {initial}")
    print(f"Weekly growth rate: {rate*100:.1f}%")
    print(f"Number of weeks: {weeks}")
    print(f"Final population: {final_pop:.2f}")