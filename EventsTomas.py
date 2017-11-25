
#The action to choose the car I think need to be when you are offline. Because when you are online I believe that you cannot change the car. I am not sure.
#In that case you need to have a car_selection event separated for the event Go_Online

   @task(8)
    def driver_car_selection(self):
        user = random.choice(users) #Drivers instaed of Users?
        self.create_event("car_selection", {
            "car_id": car_id_generator()# The driver can choose a Car. 
        })


   @task(8)
    def driver_go_online(self):
        user = random.choice(users) #Drivers instaed of Users?
        self.create_event("go_online", {
            "timezone": fake.timezone(),
            'address': fake.address(),
            "car_id": car_id_generator()# In the case that we can do this action Online.
            #Can we join with the table car_properties or we need to put the properties in the event?

            "car_category": category_generator(), 
            "car_model": car_model_generator(),
            "car_year": car_year_generator(),
            "car_license_plate": car_license_plate_generator(),
            "car_color": car_color_generator(),
            "car_inspection_expire_Date": car_inspection_expire_date_generator(),
            'Insurance': car_insurance()
        })


#The company maybe want to see. Some KPIS
#How many cars of Model 2018 are in this ZIP Code?
#How many cars are near to the expire date by ZIP_ZONE
#How many cars of category Deluxe are on Average per day in Manhatan?



#In one of the application you can see a list of cars near you.
#So, maybe the action view car could be useful
#So then you could have some KPI comparing how many time the user select one category instead of other category when you have different possibilities
#Other KPI could be: When the user has two different options with the same wait_time_minutes is chosing the cheaper category or the best category?

    @task(17)
    def user_view_cars(self):
        self.create_event("view_product", {
            "car_id": car_id_generator(),
            "car_category": car_category_generator(),
            "estimation_wait_time": estimation_time_generator(), #Minutes  
        })


    @task(17)
    def user_request_car(self):
        self.create_event("user_request_car", {
            "car_id": car_id_generator(),
        })




