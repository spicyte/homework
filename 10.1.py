def oops(name):
    return name

try:
    print(oops(name="one"))
except IndexError:
    print(f"error", {oops})


try:
    def opps(name):
        print(opps("two"))
except KeyError:
    print(f"error, {opps(name)}")
