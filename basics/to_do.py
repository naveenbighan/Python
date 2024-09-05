def task():
    tasks=[]
    try:
      total_task=int(input("enter a number of task you want= " ))
      for i in range(1,total_task+1):
          task_name=input(f"Enter a task name{i}= " ) 
          tasks.append(task_name)
          print(f"{tasks}")
    except ValueError:
       print("invalid input")
           
            
    while True:
      try:
        operation=int(input("1-add\n2-update\n3-delete\n4-show\n5-Exit" ))
        
        if operation==1:
            add=input("enter a task you want to add= " ).split(',')
            tasks.extend([task for task in add])
            print(f"new task added={add}")
        elif operation==2:
            update=input("enter a task you want to update= " )
            if update in tasks:
                update_task=input("Enter a new taks to update= " )
                ind= tasks.index(update)
                tasks[ind]=update_task
                print(f"task updated{update_task}")
            else:
                print("task not found")
        
        elif operation==3:
            delete=input("enter a task you wanted to delete= " )
            if delete in tasks:
                ind=tasks.remove(delete)
                print(f"task {delete} succesfully deleted")
            else:print("task not found")
            
        elif operation==4:
            print(f"your task={tasks}")
            
        elif operation==5:
            print("Exit the program" )
            break
      except:
            print("invalid task")

task()
            
         
    
  