usernames = ['Victor', 'Trump','Biden']
passwords = ('password', 'abcd1234','12345')
loginMethod = ['mobile','gmail', 'password']
users = (zip(usernames, passwords, loginMethod))
users1 = dict(zip(usernames, passwords))
print(type (users))
print(users1)