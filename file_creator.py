import dictionary_create as dc

def file_creator():
    with open('database.csv', 'w') as file:
        for i in dc.create_dict():
            file.write(f'{i} {dc.create_dict()[i]}\n')

