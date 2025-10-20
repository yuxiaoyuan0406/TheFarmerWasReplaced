import utils
import pumpkin

def farm_0():
    utils.harvest_if_able(Entities.Tree)
    def tree_sellector():
        a = [4,2,0,-2,-4]
        return get_pos_x() - get_pos_y() in a
    if tree_sellector():
        plant(Entities.Tree)
        use_item(Items.Water)

def farm_1():
    # Farm 1 grows grass, trees and carrots
    utils.harvest_if_able()
    def carrot_sellector():
        # a = [4,2,0,-2,-4]
        # return get_pos_x() - get_pos_y() in a
        return (get_pos_x() + get_pos_y()) % 2 == 0
    def tree_sellector():
        x,y = utils.get_coor()
        return x+y == utils.world_size - 1 or x+y == utils.world_size + 1 or x+y == utils.world_size - 3
    if carrot_sellector():
        if get_ground_type() != Grounds.Soil:
            till()
        plant(Entities.Carrot)
        utils.water()
    elif tree_sellector():
        plant(Entities.Tree)
        utils.water()
    else:
        if get_ground_type() != Grounds.Grassland:
            till()

def farm_2():
    # Farm 2 grows carrots.
    # need all land to be tilled
    utils.harvest_if_able()
    plant(Entities.Carrot)
    utils.water()

def farm_3():
    # Farm 3 grows pumpkins.
    utils.multi_drone_mission(pumpkin.__plant)

    pumpkin.check_for_dead()
    harvest()
    # utils.move_to_origin()

if __name__ == "__main__":
    # utils.harvest_everything()
    utils.move_to_origin()
    while True:
        # utils.move_through_farm(farm_0)
        farm_3()