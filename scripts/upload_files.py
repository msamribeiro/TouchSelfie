import os
import config

def read_config(filename):
  config = {}
  for line in fileinput.input(filename):
    if not fileinput.isfirstline():
      key, val = line.rstrip().split(' = ')
      config[key] = val
  return config


def setup_google(config_fname, credentials_fname, username):
    try:
        # Create a client class which will make HTTP requests with Google Docs server.
        client = OAuth2Login(config_fname, credentials_fname, username)

    except KeyboardInterrupt:
        raise
    except Exception, e:
        print 'could not login to Google, check .credential file\n   %s' % e
        client = False
    return client


def googleUpload(filen):
    if custom.albumID != 'None':
        album_url ='/data/feed/api/user/%s/albumid/%s' % (config.username, custom.albumID)
        photo = client.InsertPhotoSimple(album_url,'NoVa Snap',custom.photoCaption, filen, content_type='image/jpeg')
    else:
        raise ValueError("albumID not set")



configdir = os.path.expanduser('./')
config_fname      = os.path.join(configdir, 'OpenSelfie.json')
credentials_fname = os.path.join(configdir, 'credentials.dat')

config = read_config(config_fname)

client = setup_google(config_fname, credentials_fname, 'ucreate.studio')

PROC_FILENAME = ''

try:
    googleUpload(PROC_FILENAME, config['albumid'], config['photocaption'])

except Exception, e:
    print "Upload Error", str(e)
    print  "Upload Failed:%s" % e)


