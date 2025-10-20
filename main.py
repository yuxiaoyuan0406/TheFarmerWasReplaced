import utils
import farm
import companion
import cactus

def carrot_condition():
    # return True
    return utils.item_counter[Items.Carrot] < (get_world_size() ** 2 * 1000)

def exit_carrot_condition():
    return utils.item_counter[Items.Carrot] > (get_world_size() ** 2 * 10000)

def condition(item):
    return utils.item_counter[item] < (get_world_size() ** 2 * 1000)

def exit_condition(item):
    return utils.item_counter[item] > (get_world_size() ** 2 * 10000)

GRASS = -2
WOOD = -1
CARROT = 0
PUMPKIN = 1
CACTUS = 2

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
        return

    if condition(Items.Wood):
        change_state(WOOD)
        return
    elif not exit_condition(Items.Wood):
        return

    if condition(Items.Carrot):
        change_state(CARROT)
        return
    elif not exit_condition(Items.Carrot):
        return

    if condition(Items.Pumpkin):
        change_state(PUMPKIN)
        return
    elif not exit_condition(Items.Pumpkin):
        return

    if condition(Items.Cactus):
        change_state(CACTUS)
        return


    

def main():
    global system_state
    global state_changing

    while True:
        utils.update_counter()
        state_slector()

        if state_changing:
            # utils.harvest_everything()
            if system_state == GRASS:
                pass
            elif system_state == WOOD:
                pass
            elif system_state == CARROT:
                # utils.untill_everything()
                pass
            elif system_state == PUMPKIN:
                # utils.till_everything()
                pass
            elif system_state == CACTUS:
                pass
            state_changing = False

        # Farm
        if system_state == GRASS:
            companion.multi_drone(Entities.Grass)
        elif system_state == WOOD:
            companion.multi_drone(Entities.Tree)
        elif system_state == CARROT:
            companion.multi_drone(Entities.Carrot)
        elif system_state == PUMPKIN:
            farm.farm_3()
        elif system_state == CACTUS:
            cactus.farm()




if __name__ == "__main__":
    clear()
    main()