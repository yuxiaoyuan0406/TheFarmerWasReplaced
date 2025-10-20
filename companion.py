import utils

comp_list = [Entities.Grass, Entities.Bush, Entities.Tree, Entities.Carrot]

def __random_entity():
    return comp_list[random() * len(comp_list) // 1]

def plant_at(entity, coor):
    _coor = utils.get_coor()
    utils.move_to(coor)
    if entity == get_entity_type():
        utils.move_to(_coor)
        return
    if get_entity_type() != None:
        harvest()
    __plant(entity)
    utils.move_to(_coor)

def __plant(entity):
    if entity == Entities.Grass or entity == Entities.Bush:
        if get_ground_type() != Grounds.Grassland:
            till()
    if entity == Entities.Carrot:
        if get_ground_type() != Grounds.Soil:
            till()
    
    if entity != Entities.Grass:
        plant(entity)

    utils.water()

def main():
    # utils.harvest_everything()
    # utils.till_everything()
    utils.move_to_origin()
    companion_coors = []
    is_companion = []
    for i in range(get_world_size()):
        companion_coors.append([])
        is_companion.append([])
        for j in range(get_world_size()):
            companion_coors[i].append(None)
            is_companion[i].append(False)

    def f():
        entity = get_entity_type()
        x,y = utils.get_coor()
        if entity == Entities.Carrot:
            if utils.harvest_if_able():
                companion_coor = companion_coors[x][y]
                is_companion[companion_coor[0]][companion_coor[1]] = False
                companion_coors[x][y] = None
        else:
            harvest()
            if get_ground_type() != Grounds.Soil:
                till()
            plant(Entities.Carrot)
            companion_type, companion_coor = get_companion()
            plant_at(companion_type, companion_coor)
            companion_coors[x][y] = utils.get_coor()
            is_companion[companion_coor[0]][companion_coor[1]] = True

    while True:
        utils.move_through_farm(f)

def sub_main():
    # utils.harvest_everything()
    # utils.till_everything()
    utils.move_to_origin()

    def f():
        # go through every block
        entity = get_entity_type()
        quick_print(utils.get_coor())

        # Three conditions: Entities.Carrot, None, else
        if entity == Entities.Carrot:
            # On a carrot block
            # Plant its companion
            # Harvest the carrot
            # Plant new carrot
            companion_type, companion_coor = get_companion()
            plant_at(companion_type, companion_coor)
            utils.harvest_if_able()
            utils.water()
            plant(Entities.Carrot)
            # use_item(Items.Fertilizer)

        
        elif entity == None:
            # On an empty block
            # Plant carrot
            if get_ground_type() != Grounds.Soil:
                till()
            utils.water()
            plant(Entities.Carrot)
            # use_item(Items.Fertilizer)
        
        else:
            # On a non-carrot and non-empty block
            # harvest
            use_item(Items.Weird_Substance)
            utils.harvest_if_able()
            utils.water()
            plant(Entities.Carrot)
            use_item(Items.Fertilizer)
    

    while True:
        utils.move_through_farm(f)

def plant_companion():
    comp_type, comp_coor = get_companion()
    # _coor = utils.get_coor()
    utils.move_to(comp_coor)
    if get_entity_type() == comp_type:
        pass
    elif can_harvest():
            harvest()
    else:
        pass

    __plant(comp_type)

def plant_with_companion(entity):
    utils.water()
    __plant(entity)
    plant_companion()

def minimum_centering_companion(entity, center_coor):
    utils.move_to(center_coor)
    plant_with_companion(entity)

def single_block_companion_mission(entity, coor, width, height):
    plant_point_list = []
    for i in range(width // 8):
        for j in range(height // 8):
            plant_point_list.append((coor[0] + i * 8 + 3, coor[1] + j * 8 + 3))
            plant_point_list.append((coor[0] + i * 8 + 7, coor[1] + j * 8 + 7))

    for center in plant_point_list:
        utils.move_to(center)
        if can_harvest():
            plant_companion()
            utils.move_to(center)
            harvest()
        __plant(entity)
        if entity == Entities.Tree:
            use_item(Items.Fertilizer)

def multi_drone(entity=None):
    def f(coor, width, height):
        __entity = entity
        if __entity == None:
            __entity = __random_entity()
        single_block_companion_mission(__entity, coor, width, height)
    utils.__multi_drone_mission(f)


if __name__ == "__main__":
    # utils.harvest_everything()
    clear()
    while True:
        multi_drone(Entities.Carrot)

    # world_size = get_world_size()
    # center_list = []
    # for i in range(world_size // 7):
    #     for j in range(world_size // 7):
    #         center_list.append((i*7+3, j*7+3))

    # while True:
    #     for coor in center_list:
    #         utils.move_to(coor)
    #         if can_harvest():
    #             plant_companion()
    #             utils.move_to(coor)
    #             harvest()
