import csv


def csv2json(datafile, delimiters=[';','\t',','] ):
    """
    Parse a csv and convert it to json
    We can modify the delimiters
    
    :param datafile: (str) path to csv 
    :param delimiters: (list) optional - list of delimiters in csv file
    :returns: a dict object
    """
    data = []
    
    with open(datafile, 'rb') as csvfile :
        dialect = csv.Sniffer().sniff(csvfile.read(1024), delimiters=delimiters)
        csvfile.seek(0)
        reader = csv.reader(csvfile, dialect)
        for line in reader:
            if line:
                data.append(line)
    data = [dict(zip(data[0],row)) for row in data]
    data.pop(0) 
    return data


