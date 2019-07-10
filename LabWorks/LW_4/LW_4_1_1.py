orbital_year = {'Mercury': 0.24,
                'Venus': 0.62,
                'Earth': 1,
                'Mars': 1.88,
                'Jupiter': 11.86,
                'Saturn': 29.46,
                'Uranus': 84,
                'Neptune': 165,
                'Pluto': 247.7}

orbital_radius = {'Mercury': 0.39,
                  'Venus': 0.72,
                  'Earth': 1,
                  'Mars': 1.52,
                  'Jupiter': 5.2,
                  'Saturn': 9.54,
                  'Uranus': 19.2,
                  'Neptune': 30,
                  'Pluto': 39.4}

orbital_speed = {'Mercury': 47.8,
                 'Venus': 35.0,
                 'Earth': 29.8,
                 'Mars': 24.0,
                 'Jupiter': 13.0,
                 'Saturn': 9.6,
                 'Uranus': 6.8,
                 'Neptune': 5.4,
                 'Pluto': 4.7}


def calc_days_year(orb_year):
    return orb_year * 365


def get_min_value(**x):
    # сортируем по значению и получаем список
    sorted_x = sorted(x.items(), key=lambda kv: kv[1])
    # print(sorted_x)
    key_value = sorted_x[0]

    # print(key_value)
    return key_value


def get_max_value(**x):
    sorted_x = sorted(x.items(), key=lambda kv: kv[1], reverse=True)
    # print(sorted_x)
    key_value = sorted_x[0]
    # print(key_value)
    return key_value

def get_inform(num_planet):
    try:
        planet = planets_dic[num_planet]
        print(' Your choiсe is {} :'.format(planet.upper()))
        print('=' * 25)
        orb_year_days = int(calc_days_year(orbital_year[planet]))
        print('* orbit year is {} days'.format(orb_year_days))
        orb_radius = orbital_radius[planet]
        print('* orbit radius is {} a.e'.format(orb_radius))
        orb_speed = orbital_speed[planet]
        print('* orbit speed is {} km/h'.format(orb_speed))
    except:
        print('You enter uncorrect number')



planets = orbital_year.keys()
# print(planets)
n = 0
planets_dic = {}
n = 1
for i in planets:
    planets_dic[n] = i
    n += 1
# print(planets_dic)

# pl_txt = ', '.join(planets)
# print('PLANETS: ', pl_txt)
keys_planets = planets_dic.keys()
print('PLANETS:')
for i in keys_planets:
    print('{}. {}'.format(i, planets_dic[i]))

print('='*25)
minYear = get_min_value(**orbital_year)
print('The shortest year has a {} - {} days'.format(minYear[0], calc_days_year(minYear[1])))

maxYear = get_max_value(**orbital_year)
print('The longest year has a {} - {} days'.format(maxYear[0], calc_days_year(maxYear[1])))

min_orbit_radius = get_min_value(**orbital_radius)
print('The closest planet to Sun is {} - {} a.e'.format(min_orbit_radius[0], min_orbit_radius[1]))

max_orbit_radius = get_max_value(**orbital_radius)
print('The further planet to Sun is {} - {} a.e'.format(max_orbit_radius[0], max_orbit_radius[1]))

min_speed = get_min_value(**orbital_speed)
print('The slowest planet is {} - {} km/h'.format(min_speed[0], min_speed[1]))

max_speed = get_max_value(**orbital_speed)
print('The fastest planet is {} - {} km/h'.format(max_speed[0], max_speed[1]))
#
print('='*25)
anser_1 = input('Do you want to know about of some planet? Y or N ')

try:
    if anser_1.lower() == 'y':
        num_planet = int(input('Input number of planet - '))
        try:
            get_inform(num_planet)

        except ValueError:
            print('You input not number')
    else:
        print('Thank you! Good luck!')

except:
    print('Thank you!')


