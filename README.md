# Cockroach Population Simulator

A simulation tool modeling cockroach population growth using compound interest principles.

## Core Model

The population growth follows the compound interest formula:

```
P(t) = P0 * (1 + r)^t
```

Where:
- `P0` is the initial population
- `r` is the growth rate per period (as a decimal)
- `t` is the number of periods

## Usage

Run the simulation script `simulator.py` to see a sample calculation:

```bash
python simulator.py
```

This will output the final population after 52 weeks starting with 10 roaches and a 3% weekly growth rate.

## Future Features

- Pest control intervention events
- Visualization of population over time
- Release v1.0.0