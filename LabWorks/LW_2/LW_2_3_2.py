
with open('app.log','r') as f:

    f_content = f.readlines()

    err = '[ERROR]'

    err_list = []
    for line in f_content:
        if err in line:
            # print(line)
            err_list.append(line)
        else:
            continue


for er_val in err_list[:11]:
    l_s = er_val.split()
    # print(l_s)
    ip = l_s[0]
    date_ = l_s[1]
    time_ = l_s[2]
    error_ = l_s[6:]
    error_new = ' '.join(error_)

    print('IP: {}; DATE: {} , TIME: {}; ERROR: {};'.format(ip, date_, time_, error_new))

