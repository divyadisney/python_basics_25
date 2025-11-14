import pickle
users=[{"username":"admin","password":"admin123"},{"username":"teacher","password":"teacher123"}]
with open("auth_file","wb") as authen_file:
    pickle.dump(users,authen_file)
