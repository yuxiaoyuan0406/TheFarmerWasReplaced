import utils
import farm

def carrot_condition():
    # return True
    return utils.item_counter[Items.Carrot] < (get_world_size() ** 2 * 50)

def exit_carrot_condition():
    return utils.item_counter[Items.Carrot] > (get_world_size() ** 2 * 100)

CARROT = 0
PUMPKIN = 1

system_state = PUMPKIN
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
    if carrot_condition():
        change_state(CARROT)
        return
    elif exit_carrot_condition():
        change_state(PUMPKIN)
        return

    

def main():
    global system_state
    global state_changing

    while True:
        utils.update_counter()
        state_slector()

        if state_changing:
            # utils.harvest_everything()
            if system_state == CARROT:
                # utils.untill_everything()
                pass
            elif system_state == PUMPKIN:
                # utils.till_everything()
                pass
            state_changing = False

        # Farm
        if system_state == CARROT:
            # utils.move_through_farm(farm.farm_1)
            for n in range(4):
                def farm_carrot():
                    utils.move_through_area(
                        farm.farm_1,
                        ((n // 2) * get_world_size() / 2, (n % 2) * get_world_size() / 2),
                        get_world_size() / 2, get_world_size() / 2)
                if spawn_drone(farm_carrot):
                    pass
                else:
                    farm_carrot()
                    while num_drones() != 1:
                        pass
        elif system_state == PUMPKIN:
            farm.farm_3()



if __name__ == "__main__":
    clear()
    main()