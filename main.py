"""
Hello World APK - 最简单的Python安卓应用
点击按钮显示Hello World
"""

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window

# 设置窗口背景颜色为白色
Window.clearcolor = (1, 1, 1, 1)  # RGBA白色

class HelloApp(App):
    def build(self):
        self.title = "Hello Python APK"
        
        # 创建主布局（垂直排列）
        layout = BoxLayout(orientation='vertical', 
                          spacing=20,
                          padding=50)
        
        # 标题标签
        self.title_label = Label(
            text="欢迎使用Python APK",
            font_size='24sp',
            color=(0, 0, 0, 1),  # 黑色文字
            bold=True
        )
        
        # 显示消息的标签（初始为空）
        self.message_label = Label(
            text="点击下方按钮",
            font_size='20sp',
            color=(0.2, 0.2, 0.2, 1)  # 深灰色
        )
        
        # 按钮
        self.hello_button = Button(
            text="点击显示Hello World",
            font_size='20sp',
            size_hint=(0.8, 0.3),
            pos_hint={'center_x': 0.5},
            background_color=(0.1, 0.5, 0.9, 1),  # 蓝色按钮
            color=(1, 1, 1, 1)  # 白色文字
        )
        self.hello_button.bind(on_press=self.show_hello)
        
        # 清除按钮
        self.clear_button = Button(
            text="清除消息",
            font_size='18sp',
            size_hint=(0.6, 0.2),
            pos_hint={'center_x': 0.5},
            background_color=(0.9, 0.3, 0.3, 1),  # 红色按钮
            color=(1, 1, 1, 1)
        )
        self.clear_button.bind(on_press=self.clear_message)
        
        # 添加所有控件到布局
        layout.add_widget(self.title_label)
        layout.add_widget(self.message_label)
        layout.add_widget(self.hello_button)
        layout.add_widget(self.clear_button)
        
        return layout
    
    def show_hello(self, instance):
        """显示Hello World消息"""
        self.message_label.text = "🎉 Hello World from Python APK!"
        self.message_label.color = (0, 0.5, 0, 1)  # 绿色
        self.hello_button.text = "再次点击！"
    
    def clear_message(self, instance):
        """清除消息"""
        self.message_label.text = "消息已清除"
        self.message_label.color = (0.5, 0.5, 0.5, 1)  # 灰色
        self.hello_button.text = "点击显示Hello World"

if __name__ == '__main__':
    # 启动应用
    HelloApp().run()
