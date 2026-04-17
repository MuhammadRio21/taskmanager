# File: task_manager.py

# Menggunakan konstanta untuk menghindari Magic Numbers
STATUS_COMPLETED = 1
STATUS_PENDING = 2

def get_status_label(status_code):
    """Mengubah kode status menjadi teks yang bisa dibaca."""
    status_map = {
        STATUS_COMPLETED: "Selesai",
        STATUS_PENDING: "Pending"
    }
    return status_map.get(status_code, "Unknown")

def display_tasks(tasks):
    """Menampilkan daftar tugas ke konsol."""
    for task in tasks:
        label = get_status_label(task['status'])
        print(f"Tugas: {task['name']} | Status: {label}")

def count_completed_tasks(tasks):
    """Menghitung jumlah tugas yang sudah selesai."""
    return sum(1 for task in tasks if task['status'] == STATUS_COMPLETED)

# Data lebih deskriptif
task_list = [
    {'name': 'Beli Susu', 'status': STATUS_COMPLETED},
    {'name': 'Belajar Clean Code', 'status': STATUS_PENDING}
]

# Eksekusi
display_tasks(task_list)
print(f"Total Selesai: {count_completed_tasks(task_list)}")