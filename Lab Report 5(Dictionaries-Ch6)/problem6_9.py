favorite_places={
    'Sidrat':['bandarban','bhatiary','rangamati'],
    'Muntaha':['mirsharai','sajek valley','sylhet'],
    'Arian':['cox-s bazar','saint martin']
}
for name, places in favorite_places.items():
    print(f"\nFavorite palces of {name.title()}'s are : ")
    for  place in places:
        print(f"{place.title()}")