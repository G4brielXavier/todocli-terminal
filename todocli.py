from utils.todo_commands import *

wr_command = ''

show_info()

while not wr_command == 'todo quit':
    
    wr_command = write_commands()
    compilator(wr_command)