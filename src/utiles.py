def trans(a):
    return ''.join(x for x in a.lstrip('\\').split('\\'))


print(trans("\u0412\u044b\u0441\u0448\u0435\u0435"))
