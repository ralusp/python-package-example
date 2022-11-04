# Use as package only works with leading dot, use as script only works without
from .extended_queue import ExtendedQueue

class PackageClass:
    def __init__(self):
        print('Constructing.')
        myq = ExtendedQueue()
        myq.blah()

if __name__ == '__main__':
    _testobj = PackageClass()
    print('Unit Test Exiting.')
