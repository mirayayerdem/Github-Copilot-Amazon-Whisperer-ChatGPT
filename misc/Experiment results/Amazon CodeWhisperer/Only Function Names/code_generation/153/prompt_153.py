
def Strongest_Extension(class_name, extensions):
    """
    :param class_name:
    :param extensions:
    :return:
    """
    return [x for x in extensions if x.startswith(class_name)]
