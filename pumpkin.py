import utils

def is_grown_pumpkin():
    return get_entity_type() == Entities.Pumpkin and can_harvest()

def __plant():
    if get_ground_type() != Grounds.Soil:
        till()
    elif get_entity_type() != None:
        harvest()
        if get_entity_type() != None:
            till()
            till()
    plant(Entities.Pumpkin)

def __check_for_dead(coor, width, height):
    dead_pk_coor = []
    def f():
        if not is_grown_pumpkin():
            dead_pk_coor.append(utils.get_coor())
            plant(Entities.Pumpkin)

    utils.move_through_area(f, coor, width, height)
        
    while len(dead_pk_coor):
        new_coors = []
        for i in range(len(dead_pk_coor)):
            utils.move_to(dead_pk_coor[i])
            if not is_grown_pumpkin():
                new_coors.append(utils.get_coor())
                plant(Entities.Pumpkin)
                utils.water()
        # if 0 < len(new_coors) and len(new_coors) <= 4:
            # utils.wait_s(2)
            # pass
        dead_pk_coor = list(new_coors)

def check_for_dead():
    utils.__multi_drone_mission(__check_for_dead)
