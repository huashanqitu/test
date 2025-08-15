import tkinter as tk


def center_window(window: tk.Tk, width: int, height: int) -> None:
    window.update_idletasks()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    window.geometry(f"{width}x{height}+{x}+{y}")


def main() -> None:
    root = tk.Tk()
    root.title("柔宝专用")
    root.configure(bg="#ffffff")

    # 固定窗口尺寸并居中
    window_width, window_height = 520, 340
    center_window(root, window_width, window_height)
    root.resizable(False, False)

    # 容器
    container = tk.Frame(root, bg="#ffffff")
    container.pack(expand=True, fill="both")

    # 文本标签
    text_label = tk.Label(
        container,
        text="柔宝就是一头猪",
        font=("Microsoft YaHei", 26, "bold"),
        fg="#222222",
        bg="#ffffff",
        wraplength=window_width - 80,
    )
    text_label.pack(pady=(40, 10))

    # 猪头标签（初始不显示）
    pig_label = tk.Label(
        container,
        text="🐷",
        font=("Segoe UI Emoji", 110),
        bg="#ffffff",
    )

    def show_pig() -> None:
        pig_label.pack(pady=(10, 30))

    # 1 秒后显示猪头
    root.after(1000, show_pig)

    root.mainloop()


if __name__ == "__main__":
    main()