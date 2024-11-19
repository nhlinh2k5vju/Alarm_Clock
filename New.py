import time
import datetime
import pygame

# Danh sách các báo thức
alarms = []

# Danh sách âm thanh
sound_files = ["d:/vscode/Projects/Alarm_Aclock/2am.mp3", "d:/vscode/Projects/Alarm_Aclock/Save_Me.mp3", "d:/vscode/Projects/Alarm_Aclock/No_More_Goodbye.mp3"]

# Đặt báo thức
def set_alarm(alarm_time, sound_file, repeat=False):
    alarms.append({"time": alarm_time, "sound": sound_file, "repeat": repeat})
    print(f"Alarm set for {alarm_time} with sound {sound_file} (Repeat: {repeat})")

# Kiểm tra báo thức
def check_alarms():
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)

        for alarm in alarms[:]:
            if current_time == alarm["time"]:
                print("WAKE UP! 😴")

                pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)
                pygame.mixer.music.load(alarm["sound"])
                pygame.mixer.music.play()

                while pygame.mixer.music.get_busy():
                    time.sleep(1)

                if alarm["repeat"]:
                    set_alarm(alarm["time"], alarm["sound"], repeat=True)  # Đặt lại báo thức nếu cần
                alarms.remove(alarm)  # Xóa báo thức sau khi đã thực hiện

        time.sleep(1)

# Chế độ ngủ (Snooze)
def snooze():
    print("Snooze activated... Sleeping for 5 minutes.")
    time.sleep(5 * 60)  # Tạm dừng trong 5 phút
    print("Waking up again!")
    check_alarms()

# Hiển thị thời gian còn lại đến báo thức
def time_until_alarm(alarm_time):
    current_time = datetime.datetime.now()
    alarm_time = datetime.datetime.strptime(alarm_time, "%H:%M:%S")
    remaining_time = alarm_time - current_time

    if remaining_time.total_seconds() < 0:
        remaining_time += datetime.timedelta(days=1)  # Điều chỉnh nếu báo thức là vào ngày hôm sau

    hours, remainder = divmod(remaining_time.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    print(f"Time remaining until alarm: {hours} hours, {minutes} minutes")

# Tùy chọn âm thanh
def choose_sound():
    print("Choose an alarm sound:")
    for i, sound in enumerate(sound_files):
        print(f"{i + 1}. {sound}")
    choice = int(input("Enter the corresponding number: ")) - 1
    return sound_files[choice]

if __name__ == "__main__":
    while True:
        print("\nAvailable options:")
        print("1. Set a new alarm")
        print("2. Check alarms")
        print("3. Snooze")
        print("4. Time remaining for a specific alarm")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            alarm_time = input("Enter the alarm time (HH:MM:SS): ")
            sound = choose_sound()
            repeat = input("Do you want this alarm to repeat every day? (yes/no): ").strip().lower() == "yes"
            set_alarm(alarm_time, sound, repeat)
        elif choice == "2":
            check_alarms()
        elif choice == "3":
            snooze()
        elif choice == "4":
            alarm_time = input("Enter the alarm time (HH:MM:SS): ")
            time_until_alarm(alarm_time)
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")
