import csv
import random

class QuizGame:
    def __init__(self):
        self.categories = ['Marvel','Anime','Tamil Cinema','General Knowledge', 'Engineering','Science','Medical Science','Technology','Hollywood','History']
        self.selected_category = None
        self.quiz_data = {}

    def load_quiz_data(self, file_path):
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            self.quiz_data = {category: [] for category in self.categories}

            for row in reader:
                row['options'] = row['options'].replace('\n', ' ').split(', ')  # Replace newlines with spaces
                self.quiz_data[row['category']].append(row)

    def select_category(self):
        print("Choose a category:")
        for i, category in enumerate(self.categories, start=1):
            print(f"{i}. {category}")

        choice = int(input("Enter the number of your choice (0 to exit): "))
        if choice == 0:
            print("Exiting.Goodbye!,I hope your returns")
            exit()
        elif 1 <= choice <= len(self.categories):
            self.selected_category = self.categories[choice - 1]
            print(f"Selected category: {self.selected_category}")
        else:
            print("Invalid choice. Exiting.")
            exit()

    def run_quiz(self):
        if not self.selected_category:
            print("Please select a category first.")
            return

        category_data = self.quiz_data.get(self.selected_category, [])
        if not category_data:
            print(f"No questions available for the selected category: {self.selected_category}. Exiting.")
            exit()

        random.shuffle(category_data)
        score = 0

        for question in category_data:
            print(question['question'])
            for i, option in enumerate(question['options'], start=1):
                print(f"{chr(64 + i)}. {option}")

            user_answer = input("Your answer: ").upper()

            if user_answer == question['correct_answer']:
                print("Correct!\n")
                score += 1
            else:
                print(f"Wrong! The correct answer is {question['correct_answer']}.\n")

            change_category = input("Do you want to change the category? (yes/no): ").lower()
            if change_category == 'yes':
                self.selected_category = None
                return

        print(f"You scored {score}/{len(category_data)} on the {self.selected_category} category.")

def main():
    quiz_game = QuizGame()
    print("Welcome to the Global Guru!!!")

    file_path = 'quiz_data_with_categories.csv'  # Replace with your file path
    quiz_game.load_quiz_data(file_path)

    while True:
        quiz_game.select_category()
        quiz_game.run_quiz()

if __name__ == "__main__":
    main()
