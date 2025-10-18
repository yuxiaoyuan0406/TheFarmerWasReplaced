import utils

right_of = {North:East, East:South, South:West, West:North}
left_of = {North:West, East:North, South:East, West:South}

def use_substance():
    substance = get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)
    use_item(Items.Weird_Substance, substance)

def find_treasure():
    dir = North
    while get_entity_type() == Entities.Hedge:
        if move(right_of[dir]):
            dir = right_of[dir]
            continue
        elif move(dir):
            continue
        elif move(left_of[dir]):
            dir = left_of[dir]
            continue
        else: 
            move(utils.rev_dir(dir))
            dir = utils.rev_dir(dir)
            continue

def init():
    if get_ground_type() != Grounds.Grassland:
        till()
    plant(Entities.Bush)
    use_substance()
        
def main():
    init()
    # for i in range(1):
    #     find_treasure()
    #     use_substance()
    find_treasure()
    harvest()

def multi_drone():
    def f():
        while True:
            plant(Entities.Bush)
            while use_item(Items.Weird_Substance):
                pass
            harvest()
    clear()
    for i in range(max_drones() - 1):
        spawn_drone(f)
        move(North)
    f()

def g():
    clear()
    def f():
        while get_entity_type() != Entities.Hedge and get_entity_type() != Entities.Treasure:
            pass
        while True:
            if get_entity_type() == Entities.Treasure:
                if not use_item(Items.Weird_Substance, 2):
                    harvest()
                    plant(Entities.Bush)
                    use_item(Items.Weird_Substance, 2)
    
    for n in range(4):
        utils.move_to((n // 2, n % 2))
        spawn_drone(f)
        if n==3:
            plant(Entities.Bush)
            use_item(Items.Weird_Substance, 2)
            f()

if __name__ == "__main__":
    g()
    multi_drone()
    while True:
        main()