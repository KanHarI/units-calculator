# units-calculator

#### A simple units python calculator optimized for convenience over performance.

## Basic usage

### Parsing units

#### Usage example 1 - solving a basic kinematic problem

A ball is thrown upwards (from the ground) at a vertical speed of 40.5 feet 
per second and a horizontal speed of 20 km/h. How far away
will it land, it meters?

```python
from units_calculator.all import parse

vertical_velocity = parse("40.5ft/s")
gravitational_acceleration = parse("-9.8m/s^2")
horizontal_velocity = parse("20km/h")
time_to_peak = -vertical_velocity / gravitational_acceleration
time_to_land = 2 * time_to_peak
horizontal_displacement = horizontal_velocity * time_to_land
print(horizontal_displacement.as_units('m'))  # 13.995918367346937m
```

#### Usage example 2 - solutions dilution
Lets say you are in a lab, and you need to perform some solution
concentration comparison. In this curernt example
you have 5 micrograms of some material, and you need to dilute
it to 20 millimolar (mM) concentration, given a molecular
mass of 544.43 grams per mol. What volume of solvent do you need
to use?

```python
from units_calculator.all import parse

dissolved_mass = parse("5mg")
target_concentration = parse("20mM")
molar_mass = parse("544.43g/mol")
dissolved_mols = dissolved_mass / molar_mass
solvent_volume = dissolved_mols / target_concentration
print(solvent_volume.as_units("ul"))    
```

### Creating dimensional quantities explicitly
```python
from units_calculator.all import Meters, Seconds

_5m = Meters(5)
_3s = Seconds(3.0)
```

## Defining custom units
TBD

## List of supported units
TBD
