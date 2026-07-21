relays = [
    {"name": "R1", "pickup": 1000, "bus": 1},
    {"name": "R2", "pickup": 2700, "bus": 2},
    {"name": "R3", "pickup": 1300, "bus": 3},
]
fault_current = 2400
def calc_margin(pickup, fault_current):
  return fault_current - pickup

def is_tripped(pickup, fault_current):
  margin = calc_margin(pickup, fault_current)
  if margin > 0:
    return True
  else:
    return False


for relay in relays:
    margin = calc_margin(relay["pickup"], fault_current)
    tripped = is_tripped(relay["pickup"], fault_current)
    print(f"{relay['name']} (Bus {relay['bus']}): margin = {margin} amps, tripped = {tripped}")
