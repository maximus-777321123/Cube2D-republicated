import sys

def run_game(mode):
    if mode == "3D":
        from Scripts import world_3d
        world_3d.run()
    elif mode == "2D":
        from Scripts import world_2d
        world_2d.run()
    else:
        print("Неизвестный режим:", mode)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        run_game(sys.argv[1])
    else:
        print("Укажите режим: 3D или 2D")
