import user_interface as ui
import file_creator as fc
import logger as log
import dictionary_create as dc
def changes():
    type = ui.choice()
    if type[0] == 0:
        fc.file_creator()
        log.logger()
    elif type[0] == 1:
        print(dc.create_dict()[type[1]])
        log.logger()
    elif type[0] == 2:
        log.logger()
        dc.create_dict()[type[1]] = type[3]
        log.logger()
        fc.file_creator()
    elif type[0] == 3:
        log.logger()
        old = type[3]
        new = type[4]
        dc.create_dict()[type[1]] = dc.create_dict()[type[1]].replace(old, new)
        log.logger()
        fc.file_creator()
    else:
        del dc.create_dict()[type[1]]
        log.logger()
        fc.file_creator()
