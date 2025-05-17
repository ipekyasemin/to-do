# main.py
from core.todo_manager import ToDoManager
from ui.menu import print_menu
from ui.cli import get_input
from utils.helpers import format_task

def main():
    manager = ToDoManager()

    while True:
        print_menu()
        choice = get_input("Seçiminiz: ")

        if choice == "1":
            tasks = manager.list_tasks()
            if not tasks:
                print("Hiç görev yok.")
            else:
                for i, task in enumerate(tasks):
                    print(format_task(task, i))

        elif choice == "2":
            title = get_input("Görev başlığı: ")
            date = get_input("Tarih (opsiyonel, örn: 2025-05-20): ")
            manager.add_task(title, date if date else None)
            print("Görev eklendi.")

        elif choice == "3":
            index = int(get_input("Tamamlanacak görev numarası: ")) - 1
            manager.complete_task(index)
            print("Görev tamamlandı.")

        elif choice == "4":
            index = int(get_input("Silinecek görev numarası: ")) - 1
            manager.delete_task(index)
            print("Görev silindi.")

        elif choice == "5":
            print("Çıkılıyor...")
            break

        else:
            print("Geçersiz seçim!")

if __name__ == "__main__":
    main()
