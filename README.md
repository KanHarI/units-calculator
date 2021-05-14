# units-calculator
Simple units python calculator optimized for convenience over performance.

## Basic usage
### Parsing units from free text:
```python
from units_calculator.all import parse

distance = parse("5m")  # 5 meters
time = parse("500ms")  # 500ms = 0.5 seconds
velocity = distance / time  # should be 10 m/s
assert velocity == parse("1e1m/s")
print(velocity)  # 0.01m*ms^(-1) - as we used milliseconds, this is a preferred unit
assert velocity > parse("1.0m/s")
distance_over_1_min = parse("60s") * velocity
assert distance_over_1_min == parse("0.6km")
assert distance_over_1_min ** 2 == parse("0.36km^2")
assert str(parse("1s^2") + time**2) == "1.25s^2"
```

### Creating dimensional quantities explicitly
```python
from units_calculator.all import Meters, Seconds

_5m = Meters(5)
_3s = Seconds(3.0)
```

### Defining your own units
TBD
