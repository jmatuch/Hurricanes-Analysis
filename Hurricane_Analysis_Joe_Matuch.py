#!/usr/bin/env python
# coding: utf-8

# In[119]:


# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']


# In[120]:


# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']


# In[121]:


# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]


# In[122]:


# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]


# In[123]:


# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]


# In[124]:


# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']


# In[125]:


# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]


# In[126]:


# write your update damages function here:
updated_damages = []
def update_damages(damages):
    for item in damages:
        if item == 'Damages not recorded':
            updated_damages.append(item)
        elif item[-1] == 'B':
            updated_damages.append(1000000000*float(item.strip('B')))
        else:
            updated_damages.append(1000000*float(item.strip('M')))

    return updated_damages
print(update_damages(damages))


# In[127]:


# write your construct hurricane dictionary function here:
hurricanes = {}
for i in range(len(names)):
    hurricanes[names[i]] = {'Name':names[i], 'Month':months[i], 'Year':years[i], 'Max Sustained Wind':max_sustained_winds[i], 'Areas Affected':areas_affected[i], 'Damage':updated_damages[i], 'Death':deaths[i]}
print(hurricanes['Tampico']['Damage'])
print(len(hurricanes))


# In[128]:


# write your construct hurricane by year dictionary function here:
hurricanes_by_year = {}
for keys,values in hurricanes.items():
    current_year = values['Year']
    current_cane = values
    if hurricanes_by_year.get(current_year):
        hurricanes_by_year[current_year].append(values)
    else:
        hurricanes_by_year[current_year] = [current_cane]


# In[129]:


# write your count affected areas function here:
areas_affected_count = {}
for item in areas_affected:
    for place in item:
        if place in areas_affected_count:
            areas_affected_count[place] += 1
        else:
            areas_affected_count[place] = 1
print(areas_affected_count)


# In[130]:


# write your find most affected area function here:
most_affected_area = {}
count = 0
for key,value in areas_affected_count.items():    
    if value > count:
        count = value
        most_affected_area = {}
        most_affected_area[key] = value
    elif value == count:
        most_affected_area.update({key:value})
    else:
        continue
print(most_affected_area)


# In[131]:


# write your greatest number of deaths function here:
most_deaths = 0
most_deaths_hurricane = []
for i in range(len(deaths)):
    if deaths[i] > most_deaths:
        most_deaths = deaths[i]
        most_deaths_hurricane = []
        most_deaths_hurricane.append(names[i])
    elif deaths[i] == most_deaths:
        most_deaths_hurricane.append(names[i])
    else:
        continue
most_deaths_result = {most_deaths: most_deaths_hurricane}
print(most_deaths_result)


# In[132]:


# write your catgeorize by mortality function here:
mortality_scale = {0: 0, 1: 100, 2: 500, 3: 1000, 4: 10000}
mortality_rates = {0:[], 1:[], 2:[], 3:[], 4:[]}
for keys,values in hurricanes.items():
    current_deaths = values['Death']
    current_cane = values
    if current_deaths > 10000:
        mortality_rates[4].append(values)
    elif current_deaths > 1000:
        mortality_rates[3].append(values)
    elif current_deaths > 500:
        mortality_rates[2].append(values)
    elif current_deaths > 100:
        mortality_rates[1].append(values)
    else:
        mortality_rates[0].append(values)
print(mortality_rates[3])


# In[133]:


# write your greatest damage function here:
most_damage = 0
for i in range(len(updated_damages)):
    if type(updated_damages[i]) is str:
        continue
    elif updated_damages[i] > most_damage:
        most_damage = updated_damages[i]
        most_damage_hurricane = {}
        most_damage_hurricane[names[i]] = updated_damages[i]
    else:
        continue
print(most_damage_hurricane)


# In[134]:


# write your catgeorize by damage function here:
damage_scale = {0: 0, 1: 100000000, 2: 1000000000, 3: 10000000000, 4: 50000000000}
damage_ratings = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[]}
for keys,values in hurricanes.items():
    current_damages = values['Damage']
    current_cane = values
    if type(current_damages) is str:
        damage_ratings[0].append(values)
    else:
        current_damages = float(values['Damage'])
        if current_damages > 50000000000:
            damage_ratings[5].append(values)
        elif current_damages > 10000000000:
            damage_ratings[4].append(values)
        elif current_damages > 1000000000:
            damage_ratings[3].append(values)
        elif current_damages > 100000000:
            damage_ratings[2].append(values)
        else:
            damage_ratings[1].append(values)
print(damage_ratings[0])


# In[ ]:




