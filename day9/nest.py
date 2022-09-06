#nesting
capitals = {
    "france":"paris",
    "Germany":"Berlin",
}

#nesting list in  dict
travel_log={
    "france":["paris","lille","dijon"],
    "Germany":["paris","lille","dijon","Berlin"],
}

#nesting dict in a dict
travel_log={
    "france":{"cities_visited":["paris","lille","dijon"], "total_visits":12},
    "Germany":["paris","lille","dijon","Berlin"],
}

#nesting dict in a list.
travel_log=[
    {
    "country":"france",
    "cities_visited":["paris","lille","dijon"], 
    "total_visits":12
    },
    {
    "country":"Germany", 
    "countries_visited":["paris","lille","dijon","Berlin"],
    "total_visits":5
    },
]


