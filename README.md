# MacWebManager
说明：这是一个自动上线的MAC网页管理器，类似于早期的自动连接木马。

在mac和ubuntu测试正常。后面打算做成一个完善的管理器。

## 1.设置 Firebase 项目
访问 firebase.google.com，登录 Google 账户，创建新项目。

在 Firebase 控制台，选择“Realtime Database”

点击“创建数据库”，选择“测试模式”（允许读写，后续可加规则限制访问）。数据库 URL 会显示（如 https://your-project-default-rtdb.firebaseio.com）。
<img width="1794" height="866" alt="image" src="https://github.com/user-attachments/assets/a2a21976-c2c9-4374-a0c2-ba1909db3493" />

生成服务账户密钥（用于 Python）：控制台 > 项目设置 > 服务账户 > 生成新私钥（下载 JSON 文件，如 firebase_key.json）。

设置数据库规则（在控制台 > Realtime Database > 规则）：简单规则如：

{
  "rules": {
    ".read": "auth != true",
    ".write": "auth != true"
  }
}

如下图：

<img width="1582" height="794" alt="image" src="https://github.com/user-attachments/assets/856928c4-4fd6-4ea0-b219-4a47909de4bf" />

## 2. 在每台 Mac Mini 上安装 Python 服务（自动连接 Firebase）

安装 Firebase Admin SDK：

    pip install firebase-admin

将步骤 1 下载的 firebase_key.json 复制到 Mini 上 跟server.py放在一起。并如下运行：

    python server.py

运行如下图所示：

<img width="1140" height="494" alt="image" src="https://github.com/user-attachments/assets/01b2e031-d9a8-4084-b0a6-0c8e85c53445" />

## 3: 修改网页管理器参数

需要修改参数如下图
<img width="1136" height="396" alt="image" src="https://github.com/user-attachments/assets/e7bd5804-b50a-4bd7-b0db-98070c95f92d" />

对应参数在Firebase 配置（从控制台 > 项目设置 > 你的应用 > SDK 设置），如下图
<img width="2626" height="1180" alt="image" src="https://github.com/user-attachments/assets/6050cd9e-59a9-44cb-a9c7-e3aeb2cd9383" />

## 4 运行

双击打开index.html，自动显示上线的机器。并可以直接非交互式命令。比如ls,mkdir，git clone等

分别输入上线的id，及执行命令。如下图所示

<img width="1140" height="844" alt="image" src="https://github.com/user-attachments/assets/49705b13-c807-4476-b4db-de82aefe5395" />


## 5 后续

目前只能执行非交互式命令，待后面完善。






