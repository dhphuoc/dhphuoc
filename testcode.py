import platform
import socket
import uuid

try:
    with open("/var/lib/dbus/machine-id", "r") as f:
        machine_uuid = f.read().strip()
except FileNotFoundError:
    try:
        with open("/etc/machine-id", "r") as f:
            machine_uuid = f.read().strip()
    except FileNotFoundError:
        machine_uuid = str(uuid.getnode())  # Dùng MAC nếu không có machine-id

hostname = socket.gethostname()
os_name = platform.system()

print("Machine UUID:", machine_uuid)
print("Hostname:", hostname)
print("OS Name:", os_name)