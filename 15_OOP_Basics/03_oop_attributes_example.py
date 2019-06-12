
class Demo:
    class_attribute = 'class attribute'  # This is some constant-like stuff

    def __init__(self, instance_attribute_external):
        self.instance_attribute_external = instance_attribute_external  # instance attribute, value assigned at instantiation
        self.instance_attribute_internal = 'internal'

    def do_something(self):

        print(self.class_attribute)  # the instance gets a pointer to class_attribute for reading
        # ==> class attribute

        print(self.instance_attribute_external)  # == > external
        print(self.instance_attribute_internal)  # == > internal

        self.instance_attribute_external = 'modified external'
        self.instance_attribute_internal = 'modified internal'

        print(self.instance_attribute_external)  # ==> 'modified external'
        print(self.instance_attribute_internal)  # ==> 'modified internal'

    @classmethod
    def class_method(cls):
        cls.class_attribute = 'modified class attribute'  # class methods can access class attributes
        print(cls.class_attribute)  # ==> 'modified class attribute'


my_demo = Demo('external')
my_demo.do_something()
my_demo.class_method()

print(my_demo.class_attribute)  # ==> 'modified class attribute'  The instance can read it via the pointer
