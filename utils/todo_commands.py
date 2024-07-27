from classes.todo_class import Todo
from info import *

# instanciate class
core = Todo()

def show_info():
    print(f'{info['name']} [version: {info['version']}]')
    print()

# function to write command and assign to variable in that function was assigned
def write_commands():
    
    cmd = input('=> ')
    
    return cmd

# todo new
def new_task():
    
    print()
    print('The title is MANDATORY!')
    
    new_title = input(' - new title: ')
    new_content = input(' - new content: ')
    
    if not new_title == '':
        
        core.create(new_title, new_content)
        print()
        print(f'The task "{new_title}" was CREATED!')
        print()
        
        return
    
    
    print('TODO [ERROR] - The title is MANDATORY!')
    print()
    
    return
    
# todo remove
def remove_task():
    
    if not core.qty() == 0:
        
        try:  
              
            print()
            print('The index is MANDATORY!')
            index = int(input(' - Index: '))

                    
            print(f'The task "{core.tasks[index]['title']}" was REMOVED!')
            print()
            core.delete(index)
            
            return
              
        except Exception as err:
            
            print()
            print(f'TODO [ERROR] - {err}')
            print()
            
            return
        

    print()
    print('No has tasks to remove')
    print()
    
    return

# todo done
def done_task():
    
    if not core.qty() == 0:
        try:
        
            print()
            print('The index is MANDATORY!')
            index = int(input(' - Index: '))

            if not core.tasks[index]['status'] == 'done':
                
                print(f'The task "{core.tasks[index]['title']}" now is DONE!')
                print()
                core.done_task(index)
            
                return   
            
            print()
            print(f'The task "{core.tasks[index]['status']}" is DONE!')     
            print()
            return
        
        except Exception as err:
            
            print()
            print(f'TODO [ERROR] - {err}')
            print()
            
            return
        
    print()
    print('No has tasks to remove')
    print()
    
    return

# todo ndone
def nodone_task():
    
    if not core.qty() == 0:
        
        try:
        
            print()
            print('The index is MANDATORY!')
            index = int(input(' - Index: '))

                    
            if not core.tasks[index]['status'] == 'not done':
                
                print(f'The task "{core.tasks[index]['title']}" now is NOT DONE!')
                print()
                core.ndone_task(index)
            
                return   
            
            print()
            print(f'The task "{core.tasks[index]['status']}" is NOT DONE!')     
            print()
            
            return
        
        except Exception as err:
            
            print()
            print(f'TODO [ERROR] - {err}')
            print()
            
            return

    print()
    print('No has tasks to remove')
    print()
    
    return

# todo view
def todo_view():
    
    if not core.qty() == 0:
        
        core.view()
        
        return
    
    print()
    print('No has element to show')
    print('Create a task with command "todo new"')
    print()
    
    return

# todo view -t
def todo_view_task():
    
    if not core.qty() == 0:
        
        try:  
              
            print()
            print('The index is MANDATORY!')
            index = int(input(' - Index: '))

                    
            print(f'The task "{core.tasks[index]['title']}" was FOUNDED!')
            print()
            core.view_task(index)
            
            return
              
        except Exception as err:
            
            print()
            print(f'TODO [ERROR] - {err}')
            print()
            
            return
        

    print()
    print('No has tasks to show')
    print()
    
    return  

# todo view -d
def todo_view_d():
    core.view_done()

# todo view -nd
def todo_view_nd():
    core.view_ndone()

# todo creator
def todo_creator():
    print('by Gabriel Xavier')

# todo -V
def todo_version():
    print(f'TodoCli {info['version']}')

# todo quit - function to leave the program
def todo_quit():
    
    return

# todo help
def todo_help():
    
    print()
    for k, v in all_commands.items():
        print(f'< {k} >  - {v}')
        print()
    
    return

# todo help -cmd
def todo_help_cmd():
    
    cmd = input(' - Cmd: ')
    
    print()
    print(all_commands[cmd])
    print()
    
    return




# This function go verify the command writed and execute the function, else, it is return a error
def compilator(cmd):
    
    n_cmd = cmd.lower()
    
    match n_cmd:
        
        case 'todo new':
            new_task()
            
        case 'todo remove':
            remove_task()
            
        case 'todo quit':
            todo_quit()
            
        case 'todo view':
            todo_view() 
        
        case 'todo done':
            done_task()       
        
        case 'todo ndone':
            nodone_task()
        
        case 'todo view -d':
            todo_view_d()
            
        case 'todo view -nd':
            todo_view_nd()
        
        case 'todo -V':
            todo_version()
            
        case 'todo creator':
            todo_creator()
        
        case 'todo view -t':
            todo_view_task()
        
        case 'todo help':
            todo_help()
        
        case 'todo help -cmd':
            todo_help_cmd()
        
        case _:
            print('TODO [ERROR] - This command not exist')