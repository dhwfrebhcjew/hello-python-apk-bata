[app]

# 应用基本信息
title = Hello Python APK
package.name = hellopythonapk
package.domain = com.example
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,txt

# 版本信息
version = 1.0
version.regex = __version__ = ['"](.*)['"]
version.filename = %(source.dir)s/main.py

# 应用要求
requirements = python3,kivy==2.1.0
orientation = portrait
fullscreen = 0

# 支持的安卓版本
android.minapi = 21
android.ndk = 23b
android.sdk = 30
android.ndk_api = 21

# 权限配置（最基本的权限）
android.permissions = INTERNET

# 图标配置（可自行替换）
# icon.filename = icon.png

# 启动画面配置（可自行替换）
# presplash.filename = presplash.png
# presplash.color = #FFFFFF

# 适配现代安卓屏幕
android.allow_backup = true
android.meta_data = android.allow_backup=true

# 只构建64位版本减小体积
android.arch = arm64-v8a

# Buildozer配置
[buildozer]
log_level = 2
warn_on_root = 1

# 如需发布版本，取消下面的注释并设置密钥
# [app:release]
# android.keystore = /path/to/your.keystore
# android.keystore_passwd = PASSWORD
# android.keyalias = ALIAS
# android.keyalias_passwd = PASSWORD
