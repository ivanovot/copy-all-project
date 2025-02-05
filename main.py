import os

def read_files_in_directory(directory, extensions=None):
    if not os.path.isdir(directory):
        print("Указанная папка не существует.")
        return
    
    for root, _, files in os.walk(directory):
        for filename in files:
            if extensions and not any(filename.lower().endswith(ext) for ext in extensions):
                continue
            
            file_path = os.path.join(root, filename)
            print(f"Файл: {file_path.replace(directory, '')}")
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()
                    print("Содержимое:")
                    print(content)
            except Exception as e:
                print(f"Ошибка чтения файла {filename}: {e}")
            print("-" * 3)

directory = input("Введите путь к папке: ")
extensions = input("Введите расширения файлов через запятую (оставьте пустым для всех файлов): ")
extensions = [ext.strip().lower() for ext in extensions.split(',')] if extensions else None

read_files_in_directory(directory, extensions)
