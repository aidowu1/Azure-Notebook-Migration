import os
import cPickle as pickle

class SimpleCache(object):
    def __init__(self, cache_file_folder=r'c:\temp\simple_cache', cache_name=r'data'):
        if not os.path.exists(cache_file_folder):
            os.makedirs(cache_file_folder)
        self.cache_name = '{}.pickle'.format(cache_name)
        self.cache_file_path = os.path.join(cache_file_folder, self.cache_name)
        self.cache_data = None

    def read(self):
        with open(self.cache_file_path, 'rb') as f:
            # The protocol version used is detected automatically, so we do not
            # have to specify it.
            self.cache_data = pickle.load(f)
        return self.cache_data

    def write(self, data):
        with open(self.cache_file_path, 'wb') as f:
            self.cache_data = data
            # Pickle the 'data' dictionary using the highest protocol available.
            pickle.dump(self.cache_data, f, pickle.HIGHEST_PROTOCOL)


def testSimpleCache():
    data = data = {
    'a': [1, 2.0, 3, 4+6j],
    'b': ("character string", b"byte string"),
    'c': {None, True, False}
    } 

    cache = SimpleCache()
    cache.write(data)
    cache_data = cache.read()
    print("Cached data: \n{}".format(cache_data))

if __name__ == "__main__":
    testSimpleCache()