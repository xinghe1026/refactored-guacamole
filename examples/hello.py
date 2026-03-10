"""
示例脚本 / Example script

这个脚本演示了一个简单的 Python 程序，用于测试 Git 工作流。
This script demonstrates a simple Python program for testing Git workflows.
"""


def greet(name: str) -> str:
    """返回问候语 / Return a greeting message."""
    return f"Hello, {name}! 欢迎使用 Git 和 AI 工具。"


def main():
    print(greet("World"))
    print(greet("GitHub"))


if __name__ == "__main__":
    main()
