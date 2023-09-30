import tkinter as tk
from tkinter import font


class Calculator:
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.expression = ""
        self.equation = tk.StringVar()
        self.log = tk.StringVar()

        self.root.title("Calculator")
        self.root.configure(background="#434343")
        self.root.geometry("+800+300")
        self._set_display()

    def run(self) -> None:
        self.root.mainloop()

    def _clear(self) -> None:
        self.expression = ""
        self.equation.set("")
        self.log.set("")

    def _equal(self) -> None:
        try:
            ans = str(eval(self.expression))
            self.equation.set(ans)
            self.log.set(self.log.get() + f"\n{self.expression} = {ans}")
            self.expression = ""
        except SyntaxError:
            self.equation.set("Error")
            self.expression = ""

    def _press(self, num: str) -> None:
        if not self.expression and not num.isdigit():
            self.expression = self.equation.get() + num
        else:
            self.expression = self.expression + num
        self.equation.set(self.expression)

    def _set_display(self) -> None:
        label = tk.Label(
            self.root,
            anchor="se",
            textvariable=self.log,
            fg="#DEDEDE",
            bg="#434343",
            height=5,
            justify="right",
            font=font.Font(size=15),
        )
        expression_field = tk.Entry(
            self.root,
            fg="#DEDEDE",
            bg="#434343",
            textvariable=self.equation,
        )
        btn_0 = tk.Button(
            self.root,
            command=lambda: self._press("0"),
            fg="#DEDEDE",
            bg="#606060",
            text="0",
            padx=20,
            pady=10,
        )
        btn_1 = tk.Button(
            self.root,
            command=lambda: self._press("1"),
            fg="#DEDEDE",
            bg="#606060",
            text="1",
            padx=20,
            pady=10,
        )
        btn_2 = tk.Button(
            self.root,
            command=lambda: self._press("2"),
            fg="#DEDEDE",
            bg="#606060",
            text="2",
            padx=20,
            pady=10,
        )
        btn_3 = tk.Button(
            self.root,
            command=lambda: self._press("3"),
            fg="#DEDEDE",
            bg="#606060",
            text="3",
            padx=20,
            pady=10,
        )
        btn_4 = tk.Button(
            self.root,
            command=lambda: self._press("4"),
            fg="#DEDEDE",
            bg="#606060",
            text="4",
            padx=20,
            pady=10,
        )
        btn_5 = tk.Button(
            self.root,
            command=lambda: self._press("5"),
            fg="#DEDEDE",
            bg="#606060",
            text="5",
            padx=20,
            pady=10,
        )
        btn_6 = tk.Button(
            self.root,
            command=lambda: self._press("6"),
            fg="#DEDEDE",
            bg="#606060",
            text="6",
            padx=20,
            pady=10,
        )
        btn_7 = tk.Button(
            self.root,
            command=lambda: self._press("7"),
            fg="#DEDEDE",
            bg="#606060",
            text="7",
            padx=20,
            pady=10,
        )
        btn_8 = tk.Button(
            self.root,
            command=lambda: self._press("8"),
            fg="#DEDEDE",
            bg="#606060",
            text="8",
            padx=20,
            pady=10,
        )
        btn_9 = tk.Button(
            self.root,
            command=lambda: self._press("9"),
            fg="#DEDEDE",
            bg="#606060",
            text="9",
            padx=20,
            pady=10,
        )

        btn_clear = tk.Button(
            self.root,
            command=lambda: self._clear(),
            fg="#DEDEDE",
            bg="#606060",
            text="C",
            padx=20,
            pady=10,
        )
        btn_plus = tk.Button(
            self.root,
            command=lambda: self._press("+"),
            fg="#DEDEDE",
            bg="#606060",
            text=" + ",
            padx=20,
            pady=10,
        )
        btn_minus = tk.Button(
            self.root,
            command=lambda: self._press(" - "),
            fg="#DEDEDE",
            bg="#606060",
            text="-",
            padx=20,
            pady=10,
        )
        btn_multiply = tk.Button(
            self.root,
            command=lambda: self._press(" * "),
            fg="#DEDEDE",
            bg="#606060",
            text="*",
            padx=20,
            pady=10,
        )
        btn_divide = tk.Button(
            self.root,
            command=lambda: self._press(" / "),
            fg="#DEDEDE",
            bg="#606060",
            text="/",
            padx=20,
            pady=10,
        )
        btn_dot = tk.Button(
            self.root,
            command=lambda: self._press("."),
            fg="#DEDEDE",
            bg="#606060",
            text=".",
            padx=20,
            pady=10,
        )
        btn_equal = tk.Button(
            self.root,
            command=lambda: self._equal(),
            fg="#DEDEDE",
            bg="#606060",
            text="=",
            padx=20,
            pady=10,
        )

        # label.pack(fill=tk.BOTH, expand=True)
        label.grid(row=0, column=0, columnspan=4)
        expression_field.grid(row=1, columnspan=4, ipadx=70, padx=3, pady=3)
        btn_plus.grid(row=2, column=0, sticky=tk.N + tk.E + tk.W + tk.S, padx=3, pady=3)
        btn_minus.grid(
            row=2, column=1, sticky=tk.N + tk.E + tk.W + tk.S, padx=3, pady=3
        )
        btn_multiply.grid(
            row=2, column=2, sticky=tk.N + tk.E + tk.W + tk.S, padx=3, pady=3
        )
        btn_divide.grid(
            row=2, column=3, sticky=tk.N + tk.E + tk.W + tk.S, padx=3, pady=3
        )
        btn_7.grid(row=3, column=0, sticky=tk.N + tk.E + tk.W + tk.S, padx=3, pady=3)
        btn_8.grid(row=3, column=1, sticky=tk.N + tk.E + tk.W + tk.S, padx=3, pady=3)
        btn_9.grid(row=3, column=2, sticky=tk.N + tk.E + tk.W + tk.S, padx=3, pady=3)
        btn_clear.grid(
            row=3, column=3, sticky=tk.N + tk.E + tk.W + tk.S, padx=3, pady=3
        )
        btn_4.grid(row=4, column=0, sticky=tk.N + tk.E + tk.W + tk.S, padx=3, pady=3)
        btn_5.grid(row=4, column=1, sticky=tk.N + tk.E + tk.W + tk.S, padx=3, pady=3)
        btn_6.grid(row=4, column=2, sticky=tk.N + tk.E + tk.W + tk.S, padx=3, pady=3)
        btn_equal.grid(
            row=4, column=3, rowspan=3, sticky=tk.N + tk.E + tk.W + tk.S, padx=3, pady=3
        )
        btn_1.grid(row=5, column=0, sticky=tk.N + tk.E + tk.W + tk.S, padx=3, pady=3)
        btn_2.grid(row=5, column=1, sticky=tk.N + tk.E + tk.W + tk.S, padx=3, pady=3)
        btn_3.grid(row=5, column=2, sticky=tk.N + tk.E + tk.W + tk.S, padx=3, pady=3)
        btn_0.grid(
            row=6,
            column=0,
            columnspan=2,
            sticky=tk.N + tk.E + tk.W + tk.S,
            padx=1,
            pady=1,
        )
        btn_dot.grid(row=6, column=2, sticky=tk.N + tk.E + tk.W + tk.S, padx=3, pady=3)

        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_rowconfigure(2, weight=1)
        self.root.grid_columnconfigure(2, weight=1)
        self.root.grid_rowconfigure(3, weight=1)
        self.root.grid_columnconfigure(3, weight=1)
        self.root.grid_rowconfigure(4, weight=1)
        self.root.grid_rowconfigure(5, weight=1)
        self.root.grid_rowconfigure(6, weight=1)
