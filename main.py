import utils
import farm

def carrot_condition():
    # return True
    return utils.item_counter[Items.Carrot] < (get_world_size() ** 2 * 100)

def exit_carrot_condition():
    return utils.item_counter[Items.Carrot] > (get_world_size() ** 2 * 1000)

CARROT = 0
PUMPKIN = 1

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
            utils.multi_drone_mission(farm.farm_1)
        elif system_state == PUMPKIN:
            farm.farm_3()



if __name__ == "__main__":
    clear()
    main()