def trans(a):
    return ''.join(x for x in a.lstrip('\\').split('\\'))
