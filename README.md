# MacWebManager
MAC网页管理器

## 1.设置 Firebase 项目
访问 firebase.google.com，登录 Google 账户，创建新项目（免费计划即可）。

在 Firebase 控制台，选择“Realtime Database”（而非 Firestore，因为它更适合简单实时同步）。

点击“创建数据库”，选择“测试模式”（允许读写，后续可加规则限制访问）。数据库 URL 会显示（如 https://your-project-default-rtdb.firebaseio.com）。

配置认证（可选但推荐安全）：在控制台 > Authentication > 启用“匿名”或“Email/Password”方法。

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

    pip install firebase-admin。

将步骤 1 下载的 firebase_key.json 复制到 Mini 上 跟server.py放在一起。并如下运行：

    python server.py

运行如下图所示：

<img width="1140" height="494" alt="image" src="https://github.com/user-attachments/assets/01b2e031-d9a8-4084-b0a6-0c8e85c53445" />



