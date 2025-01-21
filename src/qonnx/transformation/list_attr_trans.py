# Work around for storing list attributes.
# This is because onnxruntime-extensions does not support list attributes,
# however string attributes are supported

def list_to_string(lst, delimiter=",", fn=str): 
    return delimiter.join(fn(x) for x in lst)


def string_to_list(string, delimiter=",", fn=int):
    return list(map(int, string.split(delimiter)))
