from fabric.api import local
import json

def create_dirs(dir_file, dir_name):

    # load in dir config file
    with open(dir_file) as f:
        dirs = json.load(f)

    # function that will recursively iterate over a dict
    # and make a corresponding directory structure
    def mkdirs(top_level_dir, data):

        # json gets read in as unicode
        if isinstance(data, unicode):
            tld = '/'.join((top_level_dir, data))
            # actually make the directory!
            local('mkdir -p {p}'.format(p=tld))

        elif isinstance(data, dict):
            for k, v in data.iteritems():
                # make a dir for the dict key even if
                # its corresponding value is empty
                mkdirs(top_level_dir, k)

                # then mkdir for its value
                tld = '/'.join((top_level_dir, k))
                mkdirs(tld, v)

        elif isinstance(data, list):
            for i in data:
                mkdirs(top_level_dir, i)

    # make the directories!
    mkdirs(dir_name, dirs)

