
def Strongest_Extension(class_name, extensions):
    return max(extensions, key=lambda x: x[0] == class_name)