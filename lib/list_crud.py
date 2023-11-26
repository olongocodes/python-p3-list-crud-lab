def create_an_empty_list():
    return []
    return None

def create_a_list():
    return["Kevin", "Geophrey", "Monica", "Denis"]
    return None

def add_element_to_end_of_list(l, element):
    l.append(element)
    return l
    return None

def add_element_to_start_of_list(l, element):
    l.insert(0, element)
    return l 
    return None

def remove_element_from_end_of_list(l):
    l.pop()
    return l
    return None

def remove_element_from_start_of_list(l):
    del l[0]
    return l
    return None

def retrieve_first_element_from_list(l):
    return l[0]
    return None

def retrieve_element_from_index(l, index):
    return l[index]
    return None

def retrieve_last_element_from_list(l):
    return l[-1]
    return None
