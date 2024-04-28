from errorfordict import *
class DictStrInt:
    def __init__(self, dic=None):
        self._d={}
        if isinstance(dic, dict):
            for i, j in enumerate(self._d):
                if type(i) != str:
                    raise DictStrIntError(i, j, 0)
                if type(j) != int:
                    raise DictStrIntError(i, j, 1)
                self._d[i]=j
    def __setitem__(self, key, value):
        if type(key) != str:
            raise DictStrIntError(key, value, 0)
        if type(value) != int:
            raise DictStrIntError(key, value, 1)
        self._d[key]=value
    def __getitem__(self, item):
        if type(item) != str:
            raise DictStrIntError(item, 1, 0)
        return self._d[item]
    def __str__(self):
        return self._d.__str__()
if __name__=="__main__":
    d=DictStrInt()
    d['a']=1
    d['b']=2
    try:
        d[1]=1
    except:
        try:
            d['w]+'] = 'q'
        except:
            print("Nothing")
    print(d)