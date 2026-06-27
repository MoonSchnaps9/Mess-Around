capital = {
    "France": "Paris",
    "Germany": "Berlin"
}

#Nested List in Dictionary

travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Stuttgart", "Berlin"]
}

#How to print Lille
print(travel_log["France"][1])

nested_list = ["A", "B", ["C", "D"]]

#How to print D
print(nested_list[2][1])

#List nested inside a dictionary nested inside another dictionary 

travel_log_nested = {
    "France": {
        "num_times-visited": 8,
        "cities_visited": ["Paris", "Lille", "Dijon"],
    },
    "Germany": {
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5,
    },   
}

#How to print out Stuttgart?
print(travel_log_nested["Germany"]["cities_visited"][2])