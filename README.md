# 3D打印机状态监控与通知工具 / 3D Printer Status Monitoring & Notification Tool

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)

## 🌐 中文文档

### 📖 项目简介
这是一个通过Obico（原The Spaghetti Detective）服务监控3D打印机状态，并通过Bark应用推送iPhone通知的Python工具。当打印机状态发生变化时（如开始打印、完成打印、发生错误等），自动发送中文通知到您的iPhone。

### 🚀 主要功能
- 实时监控打印机事件状态
- 支持多种事件类型：
  - 打印任务开始/结束/取消
  - 打印机错误警报
  - 打印暂停/恢复
  - 故障检测警报
- 自动翻译原始状态信息
- 通过Bark推送即时通知
- 支持自定义打印机名称和图标

### ⚙️ 安装配置

#### 前置要求
- Python 3.8+
- Obico账户和服务（自托管或官方云服务）
- Bark应用（iOS设备）

#### 安装步骤
1. 克隆仓库：
```bash
git clone https://github.com/haha44444/3d-printer-notifications.git
cd 3d-printer-notifications
```
2. 安装依赖：
```bash
pip install -r requirements.txt
```
3. 修改配置：
```python
# 在代码的"Start Settings"部分设置：
printer_name = "你的打印机名称"  # 显示在通知标题中的名称
bark_api_iphone = "https://api.day.app/你的Bark密钥"  # Bark提供的API地址（自托管用户需修改）
obico_url = "https://app.obico.io"  # Obico服务器地址（自托管用户需修改）
obico_token = "你的Obico认证令牌"  # 在Obico后台创建并获取
```
### 🎮 使用方法
运行监控脚本：
```bash
python printer_monitor.py
```
保持长期运行：(linux)
```bash
nohup python printer_monitor.py > monitor.log 2>&1 &
```

### 感谢以下项目做出的贡献：

[Bark](https://github.com/Finb/Bark)

[Obico](https://github.com/TheSpaghettiDetective)
