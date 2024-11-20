import matplotlib.pyplot as plt
import serial
import re

port = "COM3"
baudrate = 115200

def update_plot():
    ser = serial.Serial(port=port, baudrate=baudrate, timeout=1)

    plt.ion()
    fig, ax = plt.subplots(figsize=(6, 6))
    
    fig.canvas.manager.set_window_title("Live Object Tracking and Positioning")
    
    fig.patch.set_facecolor('black')
    ax.set_facecolor('black')

    korban_coords = []
    dummy_coords = []

    pattern = r"(\w+) \(\d+\.\d+\) \[ x: (\d+), y: (\d+), width: (\d+), height: (\d+) \]"

    korban_scatter = ax.scatter([], [], s=200, c="red")
    dummy_scatter = ax.scatter([], [], s=200, c="yellow")

    ax.legend([korban_scatter, dummy_scatter], ['Korban', 'Dummy'], loc='upper right')

    while True:
        try:
            line = ser.readline().decode('utf-8').strip()
            if line:
                if "Predictions" in line:
                    print("\n" + line)
                elif "korban" in line:
                    print("  " + line)
                elif "dummy" in line:
                    print("  " + line)
                else :
                    print(line)

                if "Object detection bounding boxes:" in line:
                    korban_coords.clear()
                    dummy_coords.clear()

                match = re.search(pattern, line)
                if match:
                    label = match.group(1)
                    x = int(match.group(2))
                    y = int(match.group(3))

                    if label.lower() == "korban":
                        korban_coords.append((x, y))
                    elif label.lower() == "dummy":
                        dummy_coords.append((x, y))

                ax.clear()
                ax.set_xlim(0, 100)
                ax.set_ylim(0, 100)
                ax.set_xlabel("X", color='white')
                ax.set_ylabel("Y", color='white')
                ax.grid(True, color='white')
                
                ax.spines['top'].set_color('white')
                ax.spines['right'].set_color('white')
                ax.spines['bottom'].set_color('white')
                ax.spines['left'].set_color('white')
                ax.tick_params(axis='x', colors='white')
                ax.tick_params(axis='y', colors='white')

                if korban_coords:
                    ax.scatter(
                        [coord[0] for coord in korban_coords],
                        [coord[1] for coord in korban_coords],
                        s=200, c="red", label="Korban"
                    )
                if dummy_coords:
                    ax.scatter(
                        [coord[0] for coord in dummy_coords],
                        [coord[1] for coord in dummy_coords],
                        s=200, c="yellow", label="Dummy"
                    )

                ax.legend(loc='upper right')

                plt.draw()
                plt.pause(0.1)
        except KeyboardInterrupt:
            print("\nProgram dihentikan oleh pengguna.")
            break
        except Exception as e:
            print(f"Error: {e}")

    ser.close()
    plt.ioff()
    plt.show()

update_plot()