# Danh sách để lưu các công việc
tasks = [
    {"name": "Học bài Git", "completed": False},
    {"name": "Làm bài tập Python", "completed": False}
]

# Hàm thêm công việc
def add_task(task_name):
    task = {"name": task_name, "completed": False}
    tasks.append(task)
    print(f" Đã thêm công việc: {task_name}")

# Hàm hiển thị danh sách công việc
def list_tasks():
    if not tasks:
        print(" Danh sách công việc trống.")
        return
    print(" Danh sách công việc:")
    for i, task in enumerate(tasks):
        status = "[x]" if task["completed"] else "[ ]"
        print(f"{i}. {status} {task['name']}")

# Hàm đánh dấu hoàn thành công việc
def complete_task(task_index):
    if 0 <= task_index < len(tasks):
        tasks[task_index]["completed"] = True
        print(f"V Đã đánh dấu hoàn thành: {tasks[task_index]['name']}")
    else:
        print(" Không tìm thấy công việc với chỉ số này.")

#  Hàm xóa công việc
def delete_task(task_index):
    if 0 <= task_index < len(tasks):
        deleted_task = tasks.pop(task_index)
        print(f" Đã xóa công việc: {deleted_task['name']}")
        return True
    else:
        print("X Lỗi: Chỉ số không hợp lệ!")
        return False

if __name__ == "__main__":
    print(" Chào mừng đến với ứng dụng To-Do List!")
    list_tasks()

    add_task("Học bài Git và GitHub")
    add_task("Làm bài tập thực hành ở nhà")
    list_tasks()

    complete_task(0)
    list_tasks()

    delete_task(1)
    list_tasks()