# File: task_manager.py

def p(d):
    # fungsi untuk memproses data tugas
    for x in d:
        if x['s'] == 1:
            st = "Selesai"
        elif x['s'] == 2:
            st = "Pending"
        
        # Print format tugas
        print("Tugas: " + x['n'] + " | Status: " + st)

    # Duplikasi logika untuk menghitung total (Melanggar DRY)
    c = 0
    for x in d:
        if x['s'] == 1:
            c += 1
    print("Total Selesai: " + str(c))

data = [{'n': 'Beli Susu', 's': 1}, {'n': 'Belajar Clean Code', 's': 2}]
p(data)