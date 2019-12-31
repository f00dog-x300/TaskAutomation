import configparser


config = configparser.ConfigParser()
config.read('example.ini')

# prints ['Default', 'bitbucket.org', 'topsecret.server.com']
print(config.sections())

# prints true
print('bitbucket.org' in config)

# prints User value = hg
print(config['bitbucket.org']['User'])

for key, value in config['Default'].items():
    print(key, value)

# change yes/no to boolean
# so that I don't have to keep typing config['blah']
topsecret = config['topsecret.server.com']
print(topsecret.getboolean('ForwardX11'))       # returns true

# using dictionary's get() method as fallback
print(topsecret.get('Port'))    # prints 50022

# have to explicitly convert types
print(type(topsecret.get('Port')))          # like a json, initially a String
print(type(int(topsecret.get('Port'))))     # forcefully turning into an Int
