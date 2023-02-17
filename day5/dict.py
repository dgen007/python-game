student = {"name":"Ibrahim",
           "location":"Manchester",
           "height": 185,
           "food":("Cheese","Chicken"),
           "favourite_colour":["blue","green",
                               {"shade_of_colour":"teal",
                                "type":"Primary"},
                               {"faded":True}],
           "address":{"street":"123 Generation Street",
                      "post_code":"GH2 345",
                      "city":"Manchester"}}


for key,val in student.items():
    print(key,"<<item",val,"<<value")
