user_dict = {'john@example.com': 'John Doe', 'mary@example.com': 'Mary Smith'}


def find_user_by_email(email):
    if email in user_dict:
        return user_dict[email]
    else:
        return None


user_name = find_user_by_email('john@example.com')
print(user_name)
