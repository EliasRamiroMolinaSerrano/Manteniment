import os
import json
from datetime import datetime
#ayudaaaaaaaaaaaaaaaaaaaaaaaaaaaa   prueba de fixed cosas
#otorios
class TaskManager:
    def __init__(self):
        self.tasks = []
        self.file_name = "tasks.json"
        self.load_tasks()
    
    def load_tasks(self):
        if os.path.exists(self.file_name):
            try:
                with open(self.file_name, "r") as file:
                    self.tasks = json.load(file)
            except:
                print("Error loading task data. Starting with empty task list.  ")
                self.tasks = []
    
    def save_tasks(self):
        with open(self.file_name, "w") as file:
            json.dump(self.tasks, file)
    
    def add_task(self, title, description):
        task = {
            "id": len(self.tasks) + 1,
            "title": title,
            "description": description,
            "status": "Pending",
            "created_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.tasks.append(task)
        self.save_tasks()
        print(f"Task '{title}' added successfully!")

    #New function were added to edit tasks
    def edit_task(self, task_id, new_title, new_description):
        for task in self.tasks:
            if task["id"] == task_id:
                task["title"] = new_title
                task["description"] = new_description
                self.save_tasks()
                print(f"Task ID {task_id} updated successfully!")
                return
        print(f"Task with ID {task_id} not found.")

    
    def list_tasks(self):
        if not self.tasks:
            print("No tasks found.")
            return
        
        print("\n" + "=" * 80)
        print(f"{'ID':<5} {'TITLE':<20} {'STATUS':<10} {'CREATED DATE':<20} {'DESCRIPTION':<30}")
        print("-" * 80)
        
        for task in self.tasks:
            print(f"{task['id']:<5} {task['title'][:18]:<20} {task['status']:<10} {task['created_date']:<20} {task['description'][:28]:<30}")
        
        print("=" * 80 + "\n")
    
    def mark_complete(self, task_id):
        for task in self.tasks:
            if task["id"] == task_id:
                task["status"] = "Completed"
                self.save_tasks()
                print(f"Task '{task['title']}' marked as completed!")
                return
        print(f"Task with ID {task_id} not found.")
    
    def delete_task(self, task_id):
        for i, task in enumerate(self.tasks):
            if task["id"] == task_id:
                removed = self.tasks.pop(i)
                self.save_tasks()
                print(f"Task '{removed['title']}' deleted successfully!")
                return
        print(f"Task with ID {task_id} not found.")


def main():
    task_manager = TaskManager()
    #added 6 for edit task option
    while True:
        print("\nTASK MANAGER")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Mark Task as Complete")
        print("4. Delete Task")
        print("5. Exit")
        print("6. Edit Task")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            task_manager.add_task(title, description)
        
        elif choice == "2":
            task_manager.list_tasks()
        
        elif choice == "3":
            task_id = int(input("Enter task ID to mark as complete: "))
            task_manager.mark_complete(task_id)
        
        elif choice == "4":
            task_id = int(input("Enter task ID to delete: "))
            task_manager.delete_task(task_id)
        
        elif choice == "5":
            print("Exiting Task Manager. Goodbye!")
            break
        
            #ESTE es la nueva opcion para editar tareas 
        elif choice == "6":
            task_manager.list_tasks()
            task_id = int(input("Enter task ID to edit: "))
            new_title = input("Enter new title: ")
            new_description = input("Enter new description: ")
            task_manager.edit_task(task_id, new_title, new_description)
    
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()