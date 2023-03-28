
def check_dict_case(dict):
    if dict['case'] == 'lower':
        return dict['lower']
    elif dict['case'] == 'upper':
        return dict['upper']
    elif dict['case'] == 'title':
        return dict['title']
    else:
        return dict['default']