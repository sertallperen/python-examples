class Country:
    def __init__(self, name, population):
        self.name = name
        self.population = population

cnt_1 = Country('Poland', '20,000,000')
cnt_2 = Country('Turkey', '80,000,000')

def versus_country (cnt_1, cnt_2):
    if(cnt_1.population > cnt_2.population):
        print("Poland has more population ")

    else:
        print("Turkey has more population ")

#create ghost country_3 for changing the population. 
cnt_3.population = int(input("Enter the change amount. "))
def change_population (cnt_1, cnt_2):
    cnt_1.population = cnt_3.population
    cnt_2.population = cnt_1.population
    cnt_3.population = cnt_2.population

