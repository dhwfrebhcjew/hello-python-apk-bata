[app]
title = Hello Python APK
package.name = hellopythonapk
package.domain = com.example

# 源代码配置
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,txt

# 版本配置 - 只使用 version，不要 version.regex
version = 1.0.0

# 依赖包
requirements = python3,kivy==2.1.0

# 应用设置
orientation = portrait
fullscreen = 0

# Android 配置
android.minapi = 21
android.sdk = 30
android.permissions = INTERNET
android.arch = arm64-v8a

# 如需发布版本，取消注释并填写以下信息
# [app:release]
# android.keystore = /path/to/your.keystore
# android.keystore_passwd = YOUR_PASSWORD
# android.keyalias = myapp
# android.keyalias_passwd = YOUR_PASSWORD

[buildozer]
log_level = 2
warn_on_root = 1
