with open('IP.ASN.China.list', 'r') as f, open('IP.ASN.China.txt', 'w') as o:
    lines = f.readlines()
    for line in lines:
        line = line.strip()  
        if ":" in line:
            new_line = "IP-CIDR6," + line + "\n"
        else:
            new_line = "IP-CIDR," + line + "\n"
        o.write(new_line)
