from collections import defaultdict, Counter

def merge_with_defaultdict(*dicts: dict):
    '''
    Merges multiple dictionaries by summing values with the same keys.
    Uses defaultdict to handle missing keys.

    Args:
    ----
    dicts: Any number of dictionaries to merge.

    Returns:
    -------
    merge_dict: A merged dictionary with summed values.
    '''
    merge_dict = defaultdict(int)
    for d in dicts:
        for key, value in d.items():
            merge_dict[key] += value
    
    return dict(merge_dict)

def merge_with_counter(*dicts):
    '''
    Merges multiple dictionaries by summing values with the same keys.
    Uses Counter to handle missing keys and merge dictionaries efficiently.

    Args:
    ----
    dicts: Any number of dictionaries to merge.

    Returns:
    -------
    merge_dict: A merged dictionary with summed values.
    '''
    merge_dict = Counter()
    for d in dicts:
        merge_dict.update(d)

    return dict(merge_dict)