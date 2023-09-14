import argparse
import connector
from rich.console import Console
from rich.table import Table

def print_table(todos):
    table = Table(title="Todo List :D", title_justify="left")
    table.add_column("task", justify="left", style="green", no_wrap=True)
    table.add_column("status", justify="left", style="yellow", no_wrap=True)
    table.add_column("date", justify="left", style="red", no_wrap=True)

    for doc in todos:
        table.add_row(doc['task'], doc['status'], doc['date'])
    
    console = Console()
    console.print(table)

def delete_result(result):
    if result == 0:
        pass
    else:
        pass

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="CLI Todo", usage="CLI Todo application making use of MongoDB")
    parser.add_argument('--add', type=str, help='add a todo', required=False)
    parser.add_argument('--rm', type=str, help ='remove a todo', required=False)
    parser.add_argument('--display', help='print todos', required=False, action="store_true")
    parser.add_argument('--test', help='test if the connection to databseworks', required=False, action="store_true")
    parser.add_argument('--done', type=str, help='update a todo to done', required=False)


    args = parser.parse_args()
    c = connector.Connetion()

    if args.add:
        c.post_todo(args.add)
    
    if args.rm:
       count =  c.delete_todo(args.rm)
       delete_result(count)

    if args.display:
        print_table(c.get_todos())

    if args.done:
        c.upsert_todo(args.done)

    if args.test:
        c.test()



