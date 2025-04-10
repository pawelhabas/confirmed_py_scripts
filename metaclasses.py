# Metaclasses

def example1():
    class AutoMethodMetaclass(type):
        def __new__(cls, name, bases, dct):
            def hello(self):
                print(f"Hello from instance of {self.__class__.__name__}!")

            dct['hello'] = hello  # add method to class dictionary

            # Clreate the class using the superclass (type)
            return super().__new__(cls, name, bases, dct)

    # This class now automatically has a 'hello' method
    class MyClass(metaclass=AutoMethodMetaclass):
        def __init__(self, value):
            self.value = value

    obj = MyClass(3)
    obj.hello()


def example2():
    class PluginMeta(type):
        registry = {}

        def __new__(cls, name, bases, attrs):
            new_class = super().__new__(cls, name, bases, attrs)

            # Avoid registering the base class itself
            if bases != ():
                PluginMeta.registry[name] = new_class
                print(f"Registered plugin: {name}")

            return new_class

    class Plugin(metaclass=PluginMeta):
        def run(self):
            raise NotImplementedError

    class AnalyticPlugin(Plugin):
        def run(self):
            print("Running analytics plugin.")

    class SecurityPlugin(Plugin):
        def run(self):
            print("Running security plugin.")

    print("Available plugins:", PluginMeta.registry)

    for plugin_name, plugin_class in PluginMeta.registry.items():
        print(f"Instantiating {plugin_name}...")
        plugin = plugin_class()
        plugin.run()


if __name__ == '__main__':
    pass
