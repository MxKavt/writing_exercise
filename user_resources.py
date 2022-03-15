from plot_resources import Plot, MainCharacter

random_plot = Plot()
random_character = MainCharacter()


class User:
    def __init__(self, _id, username, email, password):
        self._id = _id
        self.username = username
        self.email = email
        self.password = password
        self.content = []

    def __repr__(self):
        return f'User stats: {self._id} - {self.username} - {self.email}'

    def choosing_plot(self):
        plot_choice = input("Please type Y to choose the plot: ")
        while plot_choice.capitalize() != 'Y':
            plot_choice = input("Please type the correct response: ")
        else:
            plot_genre = random_plot.working_genre()
            plot_ending = random_plot.working_ending()
            plot_chars = random_plot.working_characters()
            print(f'You will be working with the genres: {plot_genre}, with a {plot_ending} ending, '
                  f'{plot_chars} characters!')
            return plot_genre, plot_ending, plot_chars

    def choosing_mc(self):
        char_choice = input("Please type Y to start choosing main character stats: ")
        while char_choice.capitalize() != 'Y':
            char_choice = input("Please type the correct response: ")
        else:
            char_age = random_character.mc_age()
            char_type = random_character.mc_type()
            occupation_choice = input(f'MC age: {char_age}. MC type: {char_type}. '
                                      f'Would you like to randomize character occupation? '
                                      f'Type Y for Yes, N for No: ')
            while occupation_choice.capitalize() not in ('Y', 'N'):
                occupation_choice = input("Please type the correct response: ")
            if occupation_choice.capitalize() == 'Y':
                char_occupation = random_character.mc_occupation()
                print(f'Character stats: {char_age} years old; {char_type} of the story, {char_occupation}')
                return char_age, char_type, char_occupation
            elif occupation_choice.capitalize() != 'Y':
                print(f'Character stats: {char_age} years old, {char_type} of the story.')
                return char_age, char_type


class UsersBase:
    def __init__(self):
        self.database = []

    def user_registration(self):
        user_data = {}
        user_id = input('Please type the ID: ')
        while user_id.isdigit() is False:
            user_id = input('Make sure to type the numbers only: ')
        else:
            user_name = input('Please type your username: ')
            user_email = input('Please type your email: ')
            user_pass = input('Please type your password: ')
            user_data.update({"_id": user_id,
                             "username": user_name,
                             "email": user_email,
                             "password": user_pass
                             })
            for e in [user_data]:
                self.database.append(User(**e))
            return user_data

    def user_printer(self):
        user_data = self.user_registration()
        for e in self.database:
            if user_data['_id'] == e._id:
                print(e)
                return e


