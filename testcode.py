import hashlib
import os
import platform
import socket
import uuid

def get_machine_id():
    # Lấy UUID phần cứng (chạy tốt trên Linux, Termux, Cloud Shell)
    try:
        with open("/var/lib/dbus/machine-id", "r") as f:
            machine_uuid = f.read().strip()
    except FileNotFoundError:
        try:
            with open("/etc/machine-id", "r") as f:
                machine_uuid = f.read().strip()
        except FileNotFoundError:
            machine_uuid = str(uuid.getnode())  # Dùng địa chỉ MAC nếu không có machine-id

    # Lấy hostname của máy
    hostname = socket.gethostname()

    # Lấy hệ điều hành
    os_name = platform.system()

    # Kết hợp các thông tin
    raw_id = f"{machine_uuid}-{hostname}-{os_name}"

    # Mã hóa SHA256 để tạo mã máy chuẩn
    machine_id = hashlib.sha256(raw_id.encode()).hexdigest().upper()

    return machine_id

print(get_machine_id())