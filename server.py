import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import subprocess
import uuid
import time
import os
import atexit
import sys
import signal

# 配置
MINI_ID = "mini1"  #不同机器设置为不同名字,比如mini2，3，4
DB_URL = 'https://xxxxxxxxxx.firebasedatabase.app'  # 替换为你的数据库 URL
KEY_PATH = os.path.join(os.path.dirname(__file__), 'firebase_key.json')  # 假设 json 文件在同一目录

# 初始化 Firebase
cred = credentials.Certificate(KEY_PATH)
firebase_admin.initialize_app(cred, {'databaseURL': DB_URL})

# 引用数据库路径
root_ref = db.reference('/')
mini_ref = root_ref.child('minis').child(MINI_ID)

# 清理过期的 minis
def cleanup_stale_minis():
    all_minis = root_ref.child('minis').get()
    if all_minis:
        current_time = time.time()
        for mid, data in all_minis.items():
            if 'last_update' in data and current_time - data['last_update'] > 60:
                root_ref.child('minis').child(mid).update({'status': 'offline'})

cleanup_stale_minis()

# 设置离线状态的函数
def set_offline():
    mini_ref.update({'status': 'offline', 'last_update': time.time()})

atexit.register(set_offline)

# 处理信号以确保正常关闭
def signal_handler(sig, frame):
    set_offline()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)

# 更新 Mini 状态（在线）
mini_ref.update({'status': 'online', 'last_update': time.time()})

# 监听命令
def on_command(event):
    if event.path == '/command' and event.data:
        command = event.data
        try:
            output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT).decode()
        except Exception as e:
            output = str(e)
        mini_ref.update({'output': output, 'command': None})  # 清空命令，返回输出

mini_ref.listen(on_command)

# 保持运行并在循环中定期清理
try:
    while True:
        mini_ref.update({'last_update': time.time()})
        cleanup_stale_minis()  
        time.sleep(30)
except Exception as e:
    set_offline()
    raise
