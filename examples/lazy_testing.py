from spencer_funcs.lazy import LazyObject, lazy_init


class A(object):
    def __init__(self, val):
        print(f"A init {val}")
        self.val = val

    def func(self, arg, kwarg="default"):
        print(f"A.func(arg='{arg}' kwarg='{kwarg}') -> val = '{self.val}'")
        return "asdf"

    def __getitem__(self, item):
        return item + 5

    def __call__(self, *args, **kwargs):
        print("callin me")
        return "call result"

    def __str__(self):
        return "A(object)"

def main():
    obj = lazy_init(A, 8)
    print("Not loaded")
    print(f"First {obj.func(9)}")
    print(f"Second {obj.func(10, kwarg='ggg')}")
    print(f"GetItem {obj[5]}")
    print(obj())
    print(obj)

    pass

if __name__ == "__main__":
    main()

