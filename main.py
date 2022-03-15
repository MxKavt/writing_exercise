from user_resources import UsersBase

users_db = UsersBase()
welcome_message = "Welcome to Writing Exercise! Please register first!"

print(welcome_message)
new_user_n = users_db.user_printer()
print(type(new_user_n))
new_user_n.choosing_plot()
new_user_n.choosing_mc()
