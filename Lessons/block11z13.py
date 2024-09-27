def introspection(obj):
    obj_type = type(obj).__name__

    attributes = [attribute for attribute in dir(obj)
                  if not callable(getattr(obj, attribute))]

    methods = [method for method in attributes if callable(getattr(obj, method))]

    module = obj.__class__.__module__

    info = {'type': obj_type, 'attributes': attributes, 'methods': methods, 'module': module}

    return info

number_info = introspection(42)
print(number_info)

string_info = introspection('Hi all')
print(string_info)

list_info = introspection(['sting', 4, 7.5])
print(list_info)


for attribute in dir(callable):
    print(attribute, getattr(callable, attribute))
