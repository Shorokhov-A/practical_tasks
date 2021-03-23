with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    tuples_list = []
    for line in f:
        remote_addr = line.split(' - -')[0]
        request_type = line.split(' /')[0].split(' "')[1]
        requested_resource = line.split('" ')[0].rsplit(' ', 2)[1]
        result = remote_addr, request_type, requested_resource
        tuples_list.append(result)

print(tuples_list)
