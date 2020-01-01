import configparser


config = configparser.ConfigParser()
config['Default'] = {
    'ServerAliveInterval' : '45', 
    'Compression' : 'yes', 
    'CompressionLevel' : 9
}

config['bitbucket.org'] = {}
config['bitbucket.org']['User'] = 'hg'
config['topsecret.server.com'] = {}

topsecret = config['topsecret.server.com']
topsecret['Port'] = '50022'
topsecret['ForwardX11'] = 'yes'
config['Default']['ForwardX11'] = 'yes'  # adding to the original Default configuration

with open('example.ini', 'w') as configfile:
    config.write(configfile)


# source for configparser: https://docs.python.org/3/library/configparser.html
# sources for tmpdir for pytest:
# └> https://code-maven.com/temporary-files-and-directory-for-pytest
# └> https://pytest.readthedocs.io/en/2.7.3/tmpdir.html
