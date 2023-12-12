import tkinter as tk
from tkinter import scrolledtext

class GptChatView:
    def __init__(self, title, queryModel):
        self.controller = queryModel
        self.window = tk.Tk()
        self.window.title(title)

        font = ("맑은 고딕", 10)
        self.conversation = scrolledtext.ScrolledText(self.window, wrap=tk.WORD, bg='#f0f0f0', font=font)
        # width, height를 없애고 배경색 지정하기(2)
        self.conversation.tag_configure("user", background="#c9daf8")
        # 태그별로 다르게 배경색 지정하기(3)
        self.conversation.tag_configure("assistant", background="#e4e4e4")
        # 태그별로 다르게 배경색 지정하기(3)
        self.conversation.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        # 창의 폭에 맞추어 크기 조정하기(4)

        self.input_frame = tk.Frame(self.window)  # user_entry와 send_button을 담는 frame(5)
        self.input_frame.pack(fill=tk.X, padx=10, pady=10)  # 창의 크기에 맞추어 조절하기(5)

        self.user_entry = tk.Entry(self.input_frame)
        self.user_entry.pack(fill=tk.X, side=tk.LEFT, expand=True)

        self.send_button = tk.Button(self.input_frame, text="Send", command=self.on_send)
        self.send_button.pack(side=tk.RIGHT)

        self.window.bind('<Return>', lambda event: self.on_send())
        self.window.mainloop()

    def show_popup_message(self, window, message):
        popup = tk.Toplevel(window)
        popup.title("")

        # 팝업 창의 내용
        label = tk.Label(popup, text=message, font=("맑은 고딕", 12))
        label.pack(expand=True, fill=tk.BOTH)

        # 팝업 창의 크기 조절하기
        window.update_idletasks()
        popup_width = label.winfo_reqwidth() + 20
        popup_height = label.winfo_reqheight() + 20
        popup.geometry(f"{popup_width}x{popup_height}")

        # 팝업 창의 중앙에 위치하기
        window_x = window.winfo_x()
        window_y = window.winfo_y()
        window_width = window.winfo_width()
        window_height = window.winfo_height()

        popup_x = window_x + window_width // 2 - popup_width // 2
        popup_y = window_y + window_height // 2 - popup_height // 2
        popup.geometry(f"+{popup_x}+{popup_y}")

        popup.transient(window)
        popup.attributes('-topmost', True)

        popup.update()
        return popup

    def on_send(self):
        user_input = self.user_entry.get()
        self.user_entry.delete(0, tk.END)

        if user_input.lower() == "quit":
            self.window.destroy()
            return

        self.conversation.config(state=tk.NORMAL)  # 이동
        self.conversation.insert(tk.END, f"You: {user_input}\n", "user")  # 이동
        thinking_popup = self.show_popup_message(self.window, "처리중...")
        self.window.update_idletasks()
        # '생각 중...' 팝업 창이 반드시 화면에 나타나도록 강제로 설정하기
        response = self.controller.query(user_input)
        thinking_popup.destroy()

        # 태그를 추가한 부분(1)
        self.conversation.insert(tk.END, f"gpt assistant: {response}\n", "assistant")
        self.conversation.config(state=tk.DISABLED)
        # conversation을 수정하지 못하게 설정하기
        self.conversation.see(tk.END)