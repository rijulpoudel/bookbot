def word_count(filepath):
    with open(filepath) as f:
        file_contents = f.read()

    array =  file_contents.split()
    return len(array)

def number_character(filepath):
    with open(filepath) as f:
        file_contents = f.read()

    
    letter_count = {}
    for letter in file_contents.lower():
        if letter not in letter_count:
            letter_count[letter] = 1
        else:
            letter_count[letter] += 1
    
    return letter_count

def sorted_list(dict1):
    new_list = []

    def sort_on(item):
        return item["num"]
    

    for k in dict1:
        new_dict = {}
        new_dict["char"] = k
        new_dict['num'] = dict1[k]
        new_list.append(new_dict)


    new_list.sort(reverse=True, key=sort_on) 

    for d in new_list[:]:
        if not d["char"].isalpha():
            new_list.remove(d)
    
    for dicts in new_list:
        print (f"{dicts['char']}: {dicts['num']}")
    


