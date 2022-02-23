# In this exercise we are going to create a whole project called "To-do List". We are going to create the project step-by-step starting with the project structure:
#
# Please, create separate file for each class as shown above. You are tasked to create two classes: a Task class and a Section class.
# The Task class should receive a name (string), and a due_date (str) upon initialization. The Task also has two attributes: comments (empty list) and completed set to False by default.
# The Task class should also have five methods:
#     • change_name(new_name: str)
#         ◦ Change the name of the task and return the new name.
#         ◦ If the new name is the same as the current name, return "Name cannot be the same."
#     • change_due_date(new_date: str)
#         ◦ Change the due date of the task and return the new date.
#         ◦ If the new date is the same as the current date, return "Date cannot be the same."
#     • add_comment(comment: str)
#         ◦ Add a comment to the task.
#     • edit_comment(comment_number: int, new_comment: str)
#         ◦ The comment number value represents the index of the comment we want to edit. You should change the comment and return all the comments, separated by comma and space (", ")
#         ◦ If the comment number is out of range, return "Cannot find comment."
#     • details()
#         ◦ Return the task's details in this format:
# "Name: {task_name} - Due Date: {due_date}"
# The Section class should receive a name (string) upon initialization. The Task also has one instance attribute: tasks (empty list)
# The Section class should also have four methods:
#     • add_task(new_task: Task)
#         ◦ Add a new task to the collection. Return "Task {task details} is added to the section"
#         ◦ If the task is in the collection, return "Task is already in the section {section_name}"
#     • complete_task(task_name: str)
#         ◦ Change the task to completed (True). Return "Completed task {task_name}"
#         ◦ If the task is not found, return "Could not find task with the name {task_name}"
#     • clean_section()
#         ◦ Removes all the completed tasks and returns "Cleared {amount of removed tasks} tasks."
#     • view_section()
#         ◦ Return information about the section and its tasks in this format:
#     "Section {section_name}:
#      {details of the first task}
#      {details of the second task}
#      ...
#      {details of the n task}"



from project import task


class Section:
    def __init__(self, name: str):
        self.name = name
        self.tasks = []


    def add_task(self, new_task):
        if not new_task in self.tasks:
            self.tasks.append(new_task)
            return f"Task {new_task.details()} is added to the section"
        else:
            return f"Task is already in the section {self.name}"

    def complete_task(self, task_name: str):
        for ts in self.tasks:
            if task_name == ts.name:
                ts.completed = True
                return f"Completed task {ts.name}"
        else:
            return f"Could not find task with the name {task_name}"

    def clean_section(self):
        counter = 0
        for ts in self.tasks:
            if ts.completed:
                self.tasks.remove(ts)
                counter += 1
        if counter > 0:
            return f"Cleared {counter} tasks."
        if counter == 0:
            return "Cleared 0 tasks."


    def view_section(self):
        result = ""
        result += f"Section {self.name}:\n"
        for ts in self.tasks:
            result += f"{ts.details()}\n"
        return result


