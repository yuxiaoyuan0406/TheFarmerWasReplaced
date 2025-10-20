import utils
import farm
import companion
import cactus
import pumpkin
import bones

def condition(item):
    return utils.item_counter[item] < (get_world_size() ** 2 * 1000)

def exit_condition(item):
    return utils.item_counter[item] > (get_world_size() ** 2 * 10000)

GRASS = -2
WOOD = -1
CARROT = 0
PUMPKIN = 1
CACTUS = 2
BONES = 3

system_state = CARROT
state_changing = True

def change_state(state):
    global system_state
    global state_changing
    if system_state != state:
        system_state = state
        state_changing = True
    

def state_slector():
    global system_state
    global state_changing

    if condition(Items.Hay):
        change_state(GRASS)
        return
    elif not exit_condition(Items.Hay):
        change_state(GRASS)
        return

    if condition(Items.Wood):
        change_state(WOOD)
        return
    elif not exit_condition(Items.Wood):
        change_state(WOOD)
        return

    if condition(Items.Carrot):
        change_state(CARROT)
        return
    elif not exit_condition(Items.Carrot):
        change_state(CARROT)
        return

    if condition(Items.Pumpkin):
        change_state(PUMPKIN)
        return
    elif not exit_condition(Items.Pumpkin):
        change_state(PUMPKIN)
        return

    if condition(Items.Cactus):
        change_state(CACTUS)
        return
    elif not exit_condition(Items.Cactus):
        change_state(CACTUS)
        return

    change_state(BONES)

def sub_drone_mission(coor, width, height):
    global system_state
    global state_changing
    
    while True:
        utils.update_counter()
        state_slector()

        if state_changing:
            return

        # Farm
        # utils.move_to(coor)
        if system_state == GRASS:
            companion.single_block_companion_mission(Entities.Grass, coor, width, height)
        elif system_state == WOOD:
            companion.single_block_companion_mission(Entities.Tree, coor, width, height)
        elif system_state == CARROT:
            companion.single_block_companion_mission(Entities.Carrot, coor, width, height)
        elif system_state == PUMPKIN:
            utils.move_through_area(pumpkin.__plant, coor, width, height)
            pumpkin.__check_for_dead(coor, width, height)
            return
        elif system_state == CACTUS:
            return
        elif system_state == BONES:
            return
        else:
            return

def pumpkin_harvester():
    utils.move_to_origin()
    while get_entity_type() != Entities.Pumpkin:
        pass
    while measure() != measure(West):
        pass
    harvest()


def main():
    global system_state
    global state_changing

    while True:
        utils.update_counter()
        state_slector()

        if state_changing:
            # utils.harvest_everything()
            while num_drones() != 1:
                pass
            state_changing = False

        # Farm
        if system_state == GRASS:
            utils.__multi_drone_mission(sub_drone_mission)
        elif system_state == WOOD:
            utils.__multi_drone_mission(sub_drone_mission)
        elif system_state == CARROT:
            utils.__multi_drone_mission(sub_drone_mission)
        elif system_state == PUMPKIN:
            spawn_drone(pumpkin_harvester)
            utils.__multi_drone_mission(sub_drone_mission)
        elif system_state == CACTUS:
            cactus.fill_cactus()
            cactus.sort()
            harvest()
        elif system_state == BONES:
            clear()
            change_hat(Hats.Dinosaur_Hat)
            next = measure()
            while bones.move_to(next):
                next = measure()
            change_hat(Hats.Gold_Hat)




if __name__ == "__main__":
    clear()
    main()
