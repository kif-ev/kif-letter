'''
    Helper functions for strings
    @author: tbach, slau
'''


def get_part_between(string, start, end):
    ''' returns the part between <start> and <end> in <string>'''
    # avoid regexp for various reasons
    index_start = string.find(start) + len(start)
    index_end = string.find(end, index_start)
    return string[index_start: index_end]


def get_part_between_n_occurrences(string, start, end, startcount):
    '''returns the part betweend <start> and <end> in <string> after the nth occurence of start'''
    str = string[:]
    index_start = str.find(start) + len(start)
    if index_start == -1:
        return ""
    count_start_found = 1

    while index_start != -1 and count_start_found < startcount:
        str = str[index_start:]
        count_start_found += 1
        index_start = str.find(start, index_start) + len(start)
    #str = str[index_start:]
    return get_part_between(str, start, end)


def get_part_between_after(string, start, end, after):
    ''' returns part_between start after <after>'''
    # avoid regexp for various reasons
    index_start = string.find(after) + len(after)
    return get_part_between(string[index_start:], start, end)
