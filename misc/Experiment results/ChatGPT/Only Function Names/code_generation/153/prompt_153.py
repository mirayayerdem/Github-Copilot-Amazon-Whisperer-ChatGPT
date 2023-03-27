def Strongest_Extension(class_name, extensions):
    strongest_extension = ""
    max_strength = 0
    for ext in extensions:
        if ext["class_name"] == class_name and ext["strength"] > max_strength:
            max_strength = ext["strength"]
            strongest_extension = ext["extension_name"]
    return strongest_extension
