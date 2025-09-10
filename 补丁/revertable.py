import random
class RevertableList(list):
    pass
class RevertableDict(dict):
    pass
class RevertableDefaultDict(RevertableDict):
    pass
class RevertableSet(set):
    pass
class RevertableObject(object):
    pass
class MultiRevertable(object):
    pass
class RollbackRandom(random.Random):
    pass
class DetRandom(random.Random):
    pass