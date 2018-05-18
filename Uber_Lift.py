import numpy as np
from scipy import stats as st


class sim:
    def __init__(self, type_car):
        """
        The constructor function of the Sim class, initialize the instance of the
        Sim class.
        """
        self.type_car = type_car

        
    def Distribution_day(self, day):

        """
        Compute the distribution of a given day
        :param day: input is the day, ex. Monday =0, Tuesday = 1
        :return: return an array of distribution of trafic time during the day
        """
        if day == 0:
            return np.sort(np.random.normal(140, 20, 250).astype(np.int))
        elif day== 1:
            return np.sort(np.random.normal(140, 30, 250).astype(np.int))
        elif day== 2:
            return np.sort(np.random.normal(140, 30, 250).astype(np.int))
        elif day== 3:
            return np.sort(np.random.normal(140, 30, 250).astype(np.int))
        elif day== 4:
            return np.sort(np.random.normal(140, 30, 250).astype(np.int))
        elif day== 5:
            return np.sort(np.random.normal(120, 20, 250).astype(np.int))
        elif day == 6:
            return np.sort(np.random.normal(120, 20, 250).astype(np.int))
        
    def Distribution_car(self, type_car):
        """
        Compute the distribution of the car that customer books
        :param type car: input is the given by user 
        :return: return an array of distribution of time the car takes to pick the customer
        """
        if type_car == "Pool":
            return np.sort(np.random.normal(120,40, 250).astype(np.int))
        if type_car == "X":
            return np.sort(np.random.normal(60, 40, 250).astype(np.int))
        if type_car == "XL":
            return np.sort(np.random.normal(60, 40, 250).astype(np.int))
    
            
    def trip_booking_hours(self, day, trip_time):
        """
        Compute the distribution of the trip time it takes during daily hours
        :param day and trip time: input is the day and trip time which comes through random number generator
        :return: return an array of distribution of time hour wise
        """
        
        if day <= 5: 
            if 1 <= trip_time <= 8:
                return np.sort(np.random.normal(120, 20, 250).astype(np.int))
            elif 8 <= trip_time <= 11:
                return np.sort(np.random.normal(90, 20, 250).astype(np.int))
            elif 11 <= trip_time <= 13:
                return np.sort(np.random.normal(90, 20, 250).astype(np.int))
            elif 13 <= trip_time <= 17:
                return np.sort(np.random.normal(90, 20, 250).astype(np.int))
            elif 17 <= trip_time <= 20:
                return np.sort(np.random.normal(90, 20, 250).astype(np.int))
            elif 20 <= trip_time <= 22:
                return np.sort(np.random.normal(120, 20, 250).astype(np.int))
            elif 22 <= trip_time <= 24:
                return np.sort(np.random.normal(120, 20, 250).astype(np.int))
        else:
            if 1 <= trip_time <= 8:
                return np.sort(np.random.normal(120, 30, 250).astype(np.int))
            elif 8 <= trip_time <= 11:
                return np.sort(np.random.normal(90, 20, 250).astype(np.int))
            elif 11 <= trip_time <= 13:
                return np.sort(np.random.normal(90, 20, 250).astype(np.int))
            elif 13 <= trip_time <= 17:
                return np.sort(np.random.normal(90, 25, 250).astype(np.int))
            elif 17 <= trip_time <= 20:
                return np.sort(np.random.normal(90, 20, 250).astype(np.int))
            elif 20 <= trip_time <= 22:
                return np.sort(np.random.normal(100, 30, 250).astype(np.int))
            elif 22 <= trip_time <= 24:
                return np.sort(np.random.normal(120, 30, 250).astype(np.int))

    def user_type(self):
        user_t = np.random.randint(10)
        if(user_t == 0 or user_t ==1):
            user_tp = 1
            return user_tp
        else:
            user_tp = 2
            return user_tp
    
    def booking_time(self,user):
        """
        Compute the distribution of the time taken by user to book the trip 
        :param user: input is the day and trip time which comes through random number generator
        :return: return an array of distribution of time taken by user
        """
        
        if user == 1:
            return np.sort(np.random.normal(20, 5, 250).astype(np.int))
        elif user == 2:
            return np.sort(np.random.normal(10, 3, 250).astype(np.int))

def takes():
    
    takes = np.random.randint(10)
    if(takes > 7):
        return False
    else:
        return True
    
def driver_time():
    """
        Compute the distribution of the time taken by driver to accept the trip 
        :param: input is the output of the function takes
        :return: return an array of distribution of time taken by the driver to accept the trip
        """
        
    dtime = np.sort(np.random.normal(5, 2, 250).astype(np.int))
    driver_takes_duty = takes()

    if(driver_takes_duty == True):
        return dtime
    
    while(driver_takes_duty == False):
        dtime += 10
        driver_takes_duty= takes()
    return dtime  


while True:
    type_of_car = input('What car you wanna book? (Pool, X, XL)\n')
    try:        
        if (type_of_car !='Pool' and type_of_car !='X' and type_of_car != 'XL'):
            print("Please choose from the option")
        else:
            break

    except:
        print("Please select a valid car")

  days = np.random.randint(7)
trip_time = np.random.randint(1,25)





final_arrival_time = np.random.choice(x.Distribution_day(days))+np.random.choice(x.Distribution_car(type_of_car))+np.random.choice(x.trip_booking_hours(days, trip_time))+ np.random.choice(x.booking_time(x.user_type()))+driver_time()

print("The average waiting time is", np.mean(final_arrival_time), 'seconds')
print("The minimum waiting time is",np.min(final_arrival_time), 'seconds')
print("The maximum waiting time is",np.max(final_arrival_time), 'seconds')
