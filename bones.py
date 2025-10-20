import utils

def move_to(coor):
    x,y = coor
    _x = get_pos_x()
    _y = get_pos_y()

    if not utils.move_steps(East, x-_x):
        return False
    if not utils.move_steps(North, y-_y):
        return False
    return True

def main():
    clear()
    change_hat(Hats.Dinosaur_Hat)

    while True:
        next = measure()
        if not move_to(next):
            change_hat(Hats.Gold_Hat)
            change_hat(Hats.Dinosaur_Hat)

if __name__ == "__main__":
    main()
