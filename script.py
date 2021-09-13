# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# write your update damages function here:

def damages_float(damages):
    damages_list = []
    conversion = {"M": 1000000, "B": 1000000000}
    for num in damages:
        if "B" in num:
            damages_list.append(float(num.replace("B", ""))*conversion["B"])
        elif "M" in num:
            damages_list.append(float(num.replace("M", ""))*conversion["M"])
        else:
            damages_list.append(num)
    return damages_list

updated_damages = damages_float(damages)
print(updated_damages)

# write your construct hurricane dictionary function here:

def hurricanes_dict(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths):
    hurricanes_new_dict = {}
    for index in range(len(names)):
        hurricanes_new_dict[names[index]] = {"Name": names[index], "Month": months[index], "Year": years[index], "Max Sustained Wind": max_sustained_winds[index], "Areas Affected": areas_affected[index], "Damage": updated_damages[index], "Deaths": deaths[index]}
    return hurricanes_new_dict

hurricanes = hurricanes_dict(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths)
print(hurricanes)

# write your construct hurricane by year dictionary function here:

def hurricanes_by_year(hurricanes):
    year_hurricane = {}
    for name, data in hurricanes.items():
        current_year = hurricanes[name]['Year']
        current_cane = hurricanes[name]
        if current_year not in year_hurricane:
            year_hurricane[current_year] = [current_cane]
        else:
            year_hurricane[current_year].append(current_cane)
    return year_hurricane

hurricane_year = hurricanes_by_year(hurricanes)
print(hurricane_year)

# write your count affected areas function here:

def affected_by_hurricane(hurricanes):
    areas_dict = {}
    for key, dict in hurricanes.items():
        for area in dict['Areas Affected']:
            if area not in areas_dict:
                areas_dict[area] = 1
            else:
                areas_dict[area] += 1
    return areas_dict

hurricane_affected_areas = affected_by_hurricane(hurricanes)
print(hurricane_affected_areas)

# write your find most affected area function here:

def most_affected(hurricane_affected_areas):
    max_value = 0
    for key, value in hurricane_affected_areas.items():
        if value > max_value:
            max_value = value
            max_key = key
    print("Most affected area:")
    return max_key, max_value

max_affected = most_affected(hurricane_affected_areas)
print(max_affected)

# write your greatest number of deaths function here:

def most_deaths(hurricanes):
    max_mortality = 0
    for name, data in hurricanes.items():
        if data["Deaths"] > max_mortality:
            max_mortality = data["Deaths"]
            max_hurricane = name
    print("Most deaths:")
    return max_hurricane, max_mortality

max_death = most_deaths(hurricanes)
print(max_death)

# write your catgeorize by mortality function here:

def hurricanes_rating(hurricanes):
    hurricanes_by_mortality = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[]}
    mortality_scale = {0: 0, 1: 100, 2: 500, 3: 1000, 4: 10000}
    n = 0
    while n < 4:
        for name, data in hurricanes.items():
            if mortality_scale[n+1] >= data["Deaths"] > mortality_scale[n]:
                hurricanes_by_mortality[n+1].append(data)
        n += 1
    for key, value in hurricanes.items():
        if value["Deaths"] > mortality_scale[4]:
            hurricanes_by_mortality[5].append(value)

    return hurricanes_by_mortality

rating = hurricanes_rating(hurricanes)
print(rating)

# write your greatest damage function here:

def greatest_damage(hurricanes):
    max_damage = 0
    for name, data in hurricanes.items():
        if isinstance(data["Damage"], str) is False:
            if data["Damage"] > max_damage:
                max_damage = data["Damage"]
                max_dam_hurricane = name
    print("Greatest damage in dollars:")
    return max_dam_hurricane, max_damage

max_cost = greatest_damage(hurricanes)
print(max_cost)

# write your catgeorize by damage function here:

def hurricanes_damage(hurricanes):
    hurricanes_by_damage = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[], "n/a": []}
    damage_scale = {0: 0, 1: 100000000, 2: 1000000000, 3: 10000000000, 4: 50000000000}
    n = 0
    while n < 4:
        for name, data in hurricanes.items():
            if isinstance(data["Damage"], str) is False:
                if damage_scale[n+1] >= data["Damage"] > damage_scale[n]:
                    hurricanes_by_damage[n+1].append(data)
        n += 1
    for key, value in hurricanes.items():
        if isinstance(value["Damage"], str) is False:
            if value["Damage"] > damage_scale[4]:
                hurricanes_by_damage[5].append(value)
        else:
            hurricanes_by_damage["n/a"].append(value)
    return hurricanes_by_damage

rating_damage = hurricanes_damage(hurricanes)
print(rating_damage)
