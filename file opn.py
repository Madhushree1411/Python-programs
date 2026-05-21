import os
import platform
import subprocess

def open_file_automatically(file_path):
    """
    Automatically opens a file using the default application 
    of the user's operating system (Windows, macOS, or Linux).
    """
    if not os.path.exists(file_path):
        print(f"❌ Error: The file '{file_path}' does not exist.")
        return
    current_os = platform.system()
    try:
        if current_os == 'Windows':
            os.startfile(file_path)
            print(f"✅ Automatically opened '{file_path}' in Windows.")
        elif current_os == 'Darwin':  
            subprocess.call(('open', file_path))
            print(f"✅ Automatically opened '{file_path}' in macOS.")
        elif current_os == 'Linux':
            subprocess.call(('xdg-open', file_path))
            print(f"✅ Automatically opened '{file_path}' in Linux.")
        else:
            print(f"⚠️ OS '{current_os}' is not supported in this script.")
            
    except Exception as e:
        print(f"❌ An error occurred: {e}")
if __name__ == "__main__":
    test_filename = "auto_open_test.txt"
    print("Creating a test file...")
    with open(test_filename, "w") as f:
        f.write("Hello! Your Python script successfully opened this file automatically.\n")
        f.write("You can close this window now.")
    print("Attempting to open the file automatically...")
    open_file_automatically(test_filename)
