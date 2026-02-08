import os

def analyze_repository(root="."):
    total_files = 0
    total_lines = 0

    for foldername, subfolders, filenames in os.walk(root):
        for file in filenames:
            if file.endswith((".py", ".md", ".yml")):
                total_files += 1
                file_path = os.path.join(foldername, file)
                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        total_lines += len(f.readlines())
                except:
                    pass

    print("Repository Analysis Report")
    print("---------------------------")
    print(f"Total relevant files: {total_files}")
    print(f"Total lines of code: {total_lines}")

if __name__ == "__main__":
    analyze_repository()
