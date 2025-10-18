WATER_THRESHOLD = 0.6

world_size = get_world_size()
item_counter = dict()

rev_of = {North: South, East: West, South: North, West: East}

def update_counter(item=None):
    if item == None:
        for item in Items:
            item_counter[item] = num_items(item)
    item_counter[item] = num_items(item)

update_counter()

def water():
    if num_items(Items.Water) < 10:
        return
    while get_water() <= WATER_THRESHOLD:
        use_item(Items.Water)

def harvest_if_able(entity_type=None):
    if can_harvest():
        if entity_type == None or get_entity_type() == entity_type:
            return harvest()
        else:
            return False
    return False

def wait_s(n):
    for i in range(n):
        do_a_flip()

def rev_dir(dir):
    if dir == North:
        return South
    if dir == South:
        return North
    if dir == East:
        return West
    if dir == West:
        return East

def move_steps(dir, steps):
    if steps < 0:
        steps = - steps
        dir = rev_of[dir]
    for i in range(steps):
        move(dir)

def get_coor():
    return get_pos_x(), get_pos_y()

def move_to(coor):
    x,y = coor
    _x = get_pos_x()
    _y = get_pos_y()

    def f(dir, z, _z):
        dir = dir
        diff = 0
        if _z == z:
            pass
        elif _z < z:
            diff = z - _z
        else:
            diff = _z - z
            dir = rev_of[dir]
        if diff >= get_world_size() / 2:
            diff = diff - get_world_size()
        return dir, diff
    
    dir, diff = f(East, x, _x)
    move_steps(dir, diff)
    dir, diff = f(North, y, _y)
    move_steps(dir, diff)

def move_to_origin():
    move_to((0,0))

def move_through_area(func, coor, width, height):
    move_to(coor)
    dir = North
    for i in range(width):
        for j in range(height):
            func()
            if j + 1 != height:
                move(dir)
            else:
                dir = rev_of[dir]
        if i + 1 != width:
            move(East)

def move_through_farm(func):
    for i in range(get_world_size()):
        for j in range(get_world_size()):
            func()
            move(North)
        move(East)

def till_everything():
    def f():
        if get_ground_type() != Grounds.Soil:
            till()
    multi_drone_mission(f)

def untill_everything():
    def f():
        if get_ground_type() == Grounds.Soil:
            till()
    multi_drone_mission(f)

def harvest_everything():
    def f():
        if get_entity_type() != Entities.Grass:
            while get_entity_type() != None and get_entity_type() != Entities.Grass:
                harvest()
    # move_to_origin()
    multi_drone_mission(harvest)
    # move_to_origin()

def multi_drone_mission(func):
    for n in range(4):
        def f():
            move_through_area(func, ((n//2) * world_size / 2, (n % 2) * world_size / 2), world_size / 2, world_size / 2)
        if n == 3:
            f()
        else:
            spawn_drone(f)
    while num_drones() != 1:
        pass

def __multi_drone_mission(func):
    for n in range(4):
        def f():
            func(((n//2) * world_size / 2, (n % 2) * world_size / 2), world_size / 2, world_size / 2)
        if n == 3:
            f()
        else:
            spawn_drone(f)
    while num_drones() != 1:
        pass

if __name__ == "__main__":
    quick_print(item_counter)