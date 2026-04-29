river_country={
   'nile':'Egypt',
   'padma':'Bangladesh',
   'amazon':'Brazil',

}
for river,country in river_country.items():
    print(f"The {river.title()}  runs through {country.title()} .")
print(f"\nThe Rivers names included in the Dictionary are : ")
for river in river_country.keys():
    print(river.title())
print(f"\nThe countries names included in the Dictionary are : ")
for country in river_country.values():
    print(country.title())