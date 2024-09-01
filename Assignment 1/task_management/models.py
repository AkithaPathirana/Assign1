class Task:
    task_counter = 1
    tasks = []

    def __init__(self, title, description):
        self.id = Task.task_counter
        self.title = title
        self.description = description
        Task.task_counter += 1

    @classmethod
    def add_task(cls, task):
        cls.tasks.append(task)

    @classmethod
    def get_task(cls, task_id):
        return next((task for task in cls.tasks if task.id == task_id), None)

    @classmethod
    def update_task(cls, task_id, title, description):
        task = cls.get_task(task_id)
        if task:
            task.title = title
            task.description = description
            return True
        return False

    @classmethod
    def delete_task(cls, task_id):
        task = cls.get_task(task_id)
        if task:
            cls.tasks.remove(task)
            return True
        return False

    @classmethod
    def get_all_tasks(cls):
        return cls.tasks
