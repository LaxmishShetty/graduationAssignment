import sys

class Graduation():
    def __init__(self, days):
        self.days = days
        # total number of ways a student can attend classes
        self.total_no_of_ways = self.no_of_ways_to_attend_class()
        # no of ways which a student is not eligible to attend classes
        self.incorrect_ways = self.get_incorrect_ways_of_attending_classes(self.total_no_of_ways)

    def calculate_ways(self, days, pattern, ways):
        """
        recursive function that calculates the no of ways a student can attend classes
        param days: current day
        param pattern: a valid way for the current day
        param ways: total number of ways at this day
        """
        if days == 0:
            ways.append(pattern)
            return
        # at any given day, a student will have only 2 choices to make, either
        # attend a class or not.
        self.calculate_ways(days - 1, pattern + "P", ways)
        self.calculate_ways(days - 1, pattern + "A", ways)
   
    def get_incorrect_ways_of_attending_classes(self, total_ways):
        """
        param total_ways: Total no of ways calculated 
        """
        incorrect_ways = 0
        for way in total_ways:
            # if a student has skipped classes continuously for 4 days,
            # then that is an invalid one.
            if "AAAA" in way:
                incorrect_ways += 1
        return incorrect_ways
   
    def get_no_of_ways_to_attend_class(self):
        # return valid no of ways a student can attend classes over N days
        return len(self.total_no_of_ways) - self.get_incorrect_ways_of_attending_classes(self.total_no_of_ways)
   
    def no_of_ways_to_attend_class(self):
        # base function which calls the recursive function
        total_no_of_ways = []
        pattern = ""
        self.calculate_ways(self.days, pattern, total_no_of_ways)
        return total_no_of_ways
       
    def get_probability_of_missing_graduation_ceremony(self):
        absent_on_last_day = 0
        # a student might have missed only 3 consecutive days as max until the graduation
        # day , but if he is not present on the Nth day ( which is a graduation day ), then 
        # it means he has missed the graduation day, so the current way is an invalid one.
        # So, adding this to incorrect ways calculated earlier which gives the correct
        # probability of a student missing his graduation day.
        for way in self.total_no_of_ways:
            if way[-1] == "A" and "AAAA" not in way[:-1]:
                absent_on_last_day = absent_on_last_day + 1
       
        total_incorrect_ways = self.incorrect_ways + absent_on_last_day
       
        return len(self.total_no_of_ways) -  total_incorrect_ways
   

if __name__ == "__main__":
    days = int(sys.argv[1])
    if days < 4:
        raise Exception("No of days cannot be less than 4 according to given problem statement")
  
    obj = Graduation(days)
    
    print(f"The solution is: {obj.get_probability_of_missing_graduation_ceremony()}/{obj.get_no_of_ways_to_attend_class()}")
