class Todo:
    def __init__(self):
        self.tasks = []
    
    # function to show the number of tasks created
    def qty(self):
        
        return len(self.tasks)
    
    # function to create a new task with title, content and default status
    def create(self, new_title, new_content):
             
        base = {}
        
        base['title'] = new_title
        base['content'] = new_content
        base['status'] = 'not done'
        
        self.tasks.append(base.copy())
        base.clear()
    
    # function to remove a task using your index
    def delete(self, index):
        self.tasks.remove(self.tasks[index])
        
    # function to pass for all tasks and show, title, content and status
    def view(self):
        
        print()
        for i, v in enumerate(self.tasks):
            
            print(f'-' * 10 + f'<{i}>' + '-' * 10)
            print(f'| Title : {v['title']}')
            print(f'| Content : {v['content']}')
            print(f'| Status: {v['status']}')
            print()
            
    def view_task(self, index):
        
            print(f'-' * 10 + f'<{self.tasks.index(self.tasks[index])}>' + '-' * 10)
            print(f'| Title : {self.tasks[index]['title']}')
            print(f'| Content : {self.tasks[index]['content']}')
            print(f'| Status: {self.tasks[index]['status']}')
            print()
            
    # function to set DONE in a task
    def done_task(self, index):
        if not self.tasks[index]['status'] == 'done':
            self.tasks[index]['status'] = 'done'

    # function to set NO DONE in a task
    def ndone_task(self, index):
        if not self.tasks[index]['status'] == 'not done':
            self.tasks[index]['status'] = 'not done'
    
    # function to show tasks with status not done
    def view_ndone(self):
        
        print()
        for i, v in enumerate(self.tasks):
            
            if v['status'] == 'not done':
                
                print(f'-' * 10 + f'<{i}>' + '-' * 10)
                print(f'| Title : {v['title']}')
                print(f'| Content : {v['content']}')
                print(f'| Status: {v['status']}')
                print()
                
    # function to show tasks with status done
    def view_done(self):
        
        print()
        for i, v in enumerate(self.tasks):
            
            if v['status'] == 'done':
                
                print(f'-' * 10 + f'<{i}>' + '-' * 10)
                print(f'| Title : {v['title']}')
                print(f'| Content : {v['content']}')
                print(f'| Status: {v['status']}')
                print()