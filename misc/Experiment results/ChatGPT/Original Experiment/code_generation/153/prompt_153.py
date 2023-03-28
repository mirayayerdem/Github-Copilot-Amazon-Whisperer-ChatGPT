def Strongest_Extension(class_name, extensions):
    extension_strength = [(ext, (sum(c.isupper() for c in ext)-sum(c.islower() for c in ext))) for ext in extensions]
    strongest_ext = max(extension_strength, key=lambda x: x[1])
    return f"{class_name}.{strongest_ext[0]}"