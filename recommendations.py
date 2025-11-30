# This app provide same restaurants in differently categories in Rome Italy

from dataset import restaurants, categories



# Recommendation app class that takes the dataset data as parameters: categories and elements for each category
class Recommadations:
    def __init__(self, categories, items):
        self.categories = categories
        self.items = items
        

    # returns a list of categories starting from an initial letter choiced by user
    def get_categories(self):
        letter = self.choice_category_by_user()
        while letter == "":
            letter = self.choice_category_by_user()
        return [element for element in self.categories if element.startswith(letter)]

    # returns a list of element lists for each category inserted
    def get_iems(self, category):
        return [self.items[category] for category in self.items]    

    # asks the user to enter a letter to search for categories
    def choice_category_by_user(self):
        print("\nWhat type of food do you like to eat?")
        letter = input("Enter the beginning letters of the categories of food you want to choose: \n")
        return letter.capitalize()

    def start_use(self):
        self.greet()
        while True:
            results = self.get_categories()
            if len(results) > 1:
                print(f"\nThis is all categories in database with your beginning letters.")
                for item in results:
                    print(f"---> {item}")
            elif len(results) > 0:
                print(f"The only option with those beginning letters is {results[0]}.")
                choice = input(f"Do you want to look a {results[0]} restaurants? Enter 'y' for yes and 'n' for no:\n")
                if choice == "y":
                    # print(self.items[results[0]])
                    print("\nThe best 5 restaurants in Rome for your choice are:\n")
                    self.show_all_items(results[0].lower())
                    again = input("\nDo you want find other restaurants? Enter 'y' for yes and 'n' for no:\n")
                else:
                    again = input("\nDo you want find other restaurants? Enter 'y' for yes and 'n' for no:\n")

                if again == 'n':
                    break
            else:
                print("I'm sorry...there is not categories with this letter on the database.!")

    def show_all_items(self, key):
        
        for item in self.items[key]:
            print("\n*********************************************************\n")
            print("Name: {0}".format(item[0]))
            print("Rating: {0}".format(item[1]))
            print("Price:   {0}".format(item[2]))
            print("Address:  {0}".format(item[3]))
            
    # it simply welcomes the user who is using the app
    def greet(self):
        print("*********************************************************")
        print("* Welcome to our restaurat's recommadatios app for Rome *")
        print("*********************************************************")


app = Recommadations(categories, restaurants)
app.start_use()
