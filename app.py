# Danh sách để lưu các công việc
tasks = []
def add_task(task_name):
    task = {"name": task_name, "completed": False}
    tasks.append(task)
    print(f"Đã thêm công việc: {task_name}")
if __name__ == "__main__":
 print("Chào mừng đến với ứng dụng To-Do List!")
 add_task("Học bài Git và GitHub")
 add_task("Làm bài tập thực hành ở nhà")

tasks = [
    {"name": "Học bài Git", "completed": False},
    {"name": "Làm bài tập", "completed": False}
]
def list_tasks():
    if not tasks:
        print("Danh sách công việc trống.")
        return
    print("\nDanh sách công việc:")
    for i, task in enumerate(tasks):
        status = "[x]" if task["completed"] else "[ ]"
        print(f"{i}. {status} {task['name']}")
if __name__ == "__main__":
 list_tasks()
def complete_task(task_index):
    if 0 <= task_index < len(tasks):
        tasks[task_index]["completed"] = True
        print(f"V Đã đánh dấu hoàn thành: {tasks[task_index]['name']}")
    else:
        print("X Không tìm thấy công việc với chỉ số này.")

complete_task(0)
list_tasks()