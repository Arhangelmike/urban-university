import inspect, sys
def introspection(obj):

    obj_type = type(obj).__name__
    # print(obj_type)
    attributes = [attribute for attribute in dir(obj) if not callable(getattr(obj, attribute))]
    # print(attributes)
    methods = [method for method in dir(obj) if callable(getattr(obj, method)) and not method.startswith("__")]
    # print(methods)
    module = obj.__class__.__module__
    # module = sys.argv[0]
    # print(f'{module}')
    info = {'type': obj_type, 'attributes': attributes, 'methods': methods, 'module': module}
    return info


number_info = introspection(42)
print(number_info)
string_info = introspection('Hi all')
print(string_info)
list_info = introspection(['sting', 4, 7.5])
print(list_info)
