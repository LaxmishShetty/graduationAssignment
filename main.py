import sys

class Graduation():
    def __init__(self, days):
        if days < 5:
            raise Exception("No of days can not be less than 5.")
        self.days = days
        self.total_no_of_ways = self.no_of_ways_to_attend_class()
        self.incorrect_ways = self.get_incorrect_ways_of_attending_classes(self.total_no_of_ways)

    def calculate_ways(self, days, pattern, ways):
        if days == 0:
            ways.append(pattern)
            return
        self.calculate_ways(days - 1, pattern + "P", ways)
        self.calculate_ways(days - 1, pattern + "A", ways)
   
    def get_incorrect_ways_of_attending_classes(self, total_ways):
        incorrect_ways = 0
        for way in total_ways:
            if "AAAA" in way:
                incorrect_ways += 1
        return incorrect_ways
   
    def get_no_of_ways_to_attend_class(self):
        return len(self.total_no_of_ways) - self.get_incorrect_ways_of_attending_classes(self.total_no_of_ways)
   
    def no_of_ways_to_attend_class(self):
        total_no_of_ways = []
        pattern = ""
        self.calculate_ways(self.days, pattern, total_no_of_ways)
        return total_no_of_ways
       
    def get_probability_of_missing_graduation_ceremony(self):
        absent_on_last_day = 0
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
    print(obj.get_probability_of_missing_graduation_ceremony())
    print(obj.get_no_of_ways_to_attend_class())