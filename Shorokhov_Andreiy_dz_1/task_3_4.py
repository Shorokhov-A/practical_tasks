def dict_sort(unsorted_dict):
    keys_list = []
    sorted_dict = {}
    for key in unsorted_dict.keys():
        keys_list.append(key)
    keys_list.sort()
    for key in keys_list:
        sorted_dict[key] = unsorted_dict[key]
    return sorted_dict


def thesaurus_adv(*args):
    names_dict_adv = {}
    for lastname in args:
        lastnames_temp = []
        lastname = str(lastname).split()[-1].lower()
        lastnames_filtered = filter(lambda el:
                                    el.split()[-1].lower().startswith(lastname[0]),
                                    args)
        lastnames_temp.extend(list(lastnames_filtered))
        names_dict = {}
        for name in lastnames_temp:
            names_temp = []
            name = str(name).split()[0].lower()
            names_filtered = filter(lambda el:
                                    el.split()[0].lower().startswith(name[0]),
                                    lastnames_temp)
            names_temp.extend(list(names_filtered))
            names_dict[name[0].upper()] = names_temp
            names_dict_adv[lastname[0].upper()] = dict_sort(names_dict)
    return dict_sort(names_dict_adv)


print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"))
