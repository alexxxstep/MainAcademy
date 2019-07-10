domains = {'Ukraine': 'UA', 'Belarus': 'BY', 'Finland': 'FI', 'USA': 'US', 'Germany': 'D'}

capitals = {'Ukraine': 'Kyiv', 'Belarus': 'Minsk', 'Finland': 'Helsinki', 'USA': 'Washington', 'Germany': 'Berlin'}

d_keys = domains.keys()
print(d_keys)

for key in d_keys:
    print('Domain for {} is {}'.format(key, domains[key]))

cap_keys = capitals.keys()

for key in cap_keys:
    print('The capital of {} is {}'.format(key, capitals[key]))

cap_keys = capitals.keys()

for key in cap_keys:
    print('The capital of {} is {}. Domain for {} is {}'.format(key, capitals[key], key, domains[key]))

cap_keys = capitals.keys()

for key in cap_keys:
    domains[key] = 'GOV.' + domains[key]
    # print(domains[key])

for key in d_keys:
    print('domain of {} is {} '.format(key, domains[key]))
