import utils

def g(dir):
    for i in range(32):
        swap_count = 0
        for j in range(31):
            if measure() > measure(dir):
                swap(dir)
                swap_count += 1
            move(dir)
        if swap_count == 0:
            return
        move(dir)

def fill_cactus():
    def _():
        if get_ground_type() != Grounds.Soil:
            if get_entity_type() != Entities.Cactus:
                till()
            else:
                return
        else:
            if get_entity_type() != Entities.Cactus:
                harvest()
                if get_entity_type() != None:
                    till()
                    till()
            else:
                return

        plant(Entities.Cactus)
    utils.multi_drone_mission(_)

def farm():
    fill_cactus()
    utils.move_to_origin()
    def h():
        g(North)
    for i in range(32):
        if not spawn_drone(h):
            h()
        move(East)
    while num_drones()!=1:
        pass
    utils.move_to_origin()
    def h():
        g(East)
    for i in range(32):
        if not spawn_drone(h):
            h()
        move(North)
    while num_drones()!=1:
        pass
    harvest()

if __name__ == "__main__":
    farm()