import subprocess

def run(cmd):
    print(f"\n>> Running: {cmd}")
    subprocess.run(cmd, shell=True)

def main():
    print("=== AutoArch Installer ===")
    print("1. Update system")
    print("2. Exit")

    choice = input("Select option: ")

    if choice == "1":
        run("sudo pacman -Sy")
    elif choice == "2":
        print("Exiting...")
    else:
        print("Invalid option")

if __name__ == "__main__":
    main()