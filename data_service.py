graves = []


# get all graves
def get_all_graves():
    return graves


# create a grave
def create_grave(grave):
    graves.append(grave)


# search by id
def search_grave_by_id(grave_id):
    for grave in graves:
        if grave.id == grave_id:
            return grave
    return


# search by name (like query)
def search_grave_by_name(name_part):
    name_matched = []
    for grave in graves:
        if grave.name.startswith(name_part):
            name_matched.append(grave)
    return name_matched


# update grave
def update_grave(grave_id, grave_updated):
    for grave in graves:
        if grave.id == grave_id:
            grave.name = grave_updated.name
            grave.slot_number = grave_updated.slot_number
            return
    return


# delete grave
def delete_grave(grave_id):
    for grave in graves:
        if grave.id == grave_id:
            graves.remove(grave)
            return
