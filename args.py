import argparse
import connector

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="CLI Todo", usage="CLi todo application making use of MongoDB")
    parser.add_argument('--add', type=str, help='add a todo', required=False)
    parser.add_argument('--rm', type=str, help ='remove a todo', required=False)
    parser.add_argument('--display', help='print todos', required=False, action="store_true")

    args = parser.parse_args()
    c = connector.Connetion()

    if args.add:
        c.post_todo(args.add)
        print(args.add)
    
    if args.rm:
        c.delete_todo(args.rm)

    if args.display:
        c.get_todos()


