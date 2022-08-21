#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk


class UpdatePasswordApp:
    def __init__(self, master=None):
        # build ui
        self.UpdatePassword = tk.Tk() if master is None else tk.Toplevel(master)
        self.layoutFrame = tk.Frame(self.UpdatePassword)
        self.logoFrame = tk.Frame(self.layoutFrame)
        self.ccpLogoLabel = ttk.Label(self.logoFrame)
        self.img_ccp_logo = tk.PhotoImage(file="ccp_logo.png")
        self.ccpLogoLabel.configure(
            anchor="center",
            background="#ffffff",
            compound="center",
            image=self.img_ccp_logo,
        )
        self.ccpLogoLabel.configure(relief="flat")
        self.ccpLogoLabel.pack(side="top")
        self.logoFrame.configure(height=200, width=200)
        self.logoFrame.pack(side="top")
        self.controlFrame = tk.Frame(self.layoutFrame)
        self.pwdEntry = tk.Entry(self.controlFrame)
        self.pwdEntry.configure(
            font="{@Microsoft JhengHei} 12 {}",
            foreground="#008000",
            justify="left",
            relief="groove",
        )
        self.pwdEntry.configure(show="*", state="disabled", width=23)
        self.pwdEntry.place(relx=0.10, y=20)
        self.showPassBtn = tk.Button(self.controlFrame)
        self.img_visibility_on = tk.PhotoImage(file="visibility_on.png")
        self.showPassBtn.configure(
            cursor="arrow",
            image=self.img_visibility_on,
            relief="flat",
            state="disabled",
        )
        self.showPassBtn.place(relx=0.85, rely=0.10, x=0, y=0)
        self.showPassBtn.configure(command=self.show_pass)
        self.saveBtn = tk.Button(self.controlFrame)
        self.saveBtn.configure(
            activebackground="#008040",
            activeforeground="#ffffff",
            background="#008040",
            cursor="arrow",
        )
        self.saveBtn.configure(
            disabledforeground="#9b0a64",
            font="{@Microsoft JhengHei} 12 {}",
            foreground="#ffffff",
            justify="left",
        )
        self.saveBtn.configure(relief="flat", state="disabled", text="Save")
        self.saveBtn.place(
            height=45, relwidth=0.25, relx=0.10, rely=0.3, width=0, x=0, y=0
        )
        self.saveBtn.configure(command=self.save_pass)
        self.updatePassBtn = tk.Button(self.controlFrame)
        self.updatePassBtn.configure(
            activebackground="#008000",
            activeforeground="#ffffff",
            background="#008000",
            borderwidth=1,
        )
        self.updatePassBtn.configure(
            cursor="hand2",
            default="normal",
            disabledforeground="#9b0a64",
            font="{@Microsoft JhengHei} 12 {}",
        )
        self.updatePassBtn.configure(
            foreground="#ffffff",
            highlightbackground="#ff00ff",
            highlightthickness=1,
            overrelief="flat",
        )
        self.updatePassBtn.configure(
            relief="flat", state="normal", takefocus=True, text="Update Password"
        )
        self.updatePassBtn.place(anchor="nw", relx=0.10, rely=0.60, width=250, x=0, y=0)
        self.updatePassBtn.configure(command=self.run_batch_script)
        self.appVersionLabel = tk.Label(self.controlFrame)
        self.appVersionLabel.configure(
            background="#ffffff",
            font="{@Microsoft YaHei UI} 10 {}",
            foreground="#c5c5c5",
            text="V1.0",
        )
        self.appVersionLabel.place(anchor="nw", relx=0.45, rely=0.82, x=0, y=0)
        self.changePwdRatioBtn = tk.Radiobutton(self.controlFrame)
        self.changePwdRatioBtn.configure(
            background="#ffffff",
            compound="top",
            cursor="hand2",
            disabledforeground="#f5010a",
        )
        self.changePwdRatioBtn.configure(
            font="{@Microsoft YaHei} 9 {}",
            foreground="#008000",
            selectcolor="#ffffff",
            state="normal",
        )
        self.changePwdRatioBtn.configure(text="Change password")
        self.changePwdRatioBtn.place(anchor="nw", relx=0.52, rely=0.31, x=0, y=0)
        self.changePwdRatioBtn.configure(command=self.activate_all_btn)
        self.dontChangePwdRatioBtn = tk.Radiobutton(self.controlFrame)
        self.dontChangePwdRatioBtn.configure(
            background="#ffffff",
            compound="top",
            cursor="arrow",
            disabledforeground="#f5010a",
        )
        self.dontChangePwdRatioBtn.configure(
            font="{@Microsoft YaHei} 9 {}",
            foreground="#008000",
            state="disabled",
            text="Don't change",
        )
        self.dontChangePwdRatioBtn.place(anchor="nw", relx=0.52, rely=0.43, x=0, y=0)
        self.dontChangePwdRatioBtn.configure(command=self.deactivate_all_btn)
        self.controlFrame.configure(background="#ffffff", height=290, width=300)
        self.controlFrame.pack(side="top")
        self.layoutFrame.configure(background="#ffffff", height=290)
        self.layoutFrame.pack(side="top")
        self.img_regular = tk.PhotoImage(file="regular.png")
        self.UpdatePassword.configure(height=200, takefocus=True, width=200)
        self.UpdatePassword.geometry("370x490+400+100")
        self.UpdatePassword.iconphoto(True, self.img_regular)
        self.UpdatePassword.resizable(False, False)
        self.UpdatePassword.title("Update Password")

        # Main widget
        self.mainwindow = self.UpdatePassword

    def run(self):
        self.mainwindow.mainloop()

    def show_pass(self):
        pass

    def save_pass(self):
        pass

    def run_batch_script(self):
        pass

    def activate_all_btn(self):
        pass

    def deactivate_all_btn(self):
        pass


if __name__ == "__main__":
    app = UpdatePasswordApp()
    app.run()
