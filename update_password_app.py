#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
from createPwd import take_and_save_pwd as save_pwd
from runScript import run_script
DRAWABLE_PATH = "res/drawable/"


class UpdatePasswordApp:
    def __init__(self, master=None):
        # build ui
        self.UpdatePassword = tk.Tk() if master is None else tk.Toplevel(master)
        self.layoutFrame = tk.Frame(self.UpdatePassword)
        self.logoFrame = tk.Frame(self.layoutFrame)
        self.ccpLogoLabel = ttk.Label(self.logoFrame)
        self.img_ccp_logo = tk.PhotoImage(file=DRAWABLE_PATH+"ccp_logo.png")
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
        self.img_visibility_on = tk.PhotoImage(file=DRAWABLE_PATH+"visibility_on.png")
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
            disabledforeground="#000000",
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
            disabledforeground="#000000",
            font="{@Microsoft JhengHei} 12 {}",
        )
        self.updatePassBtn.configure(
            foreground="#ffffff",
            overrelief="flat",
        )
        self.updatePassBtn.configure(
            relief="flat", state="normal", text="Update Password"
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
            disabledforeground="#000000",
        )
        self.changePwdRatioBtn.configure(text="Change password")
        self.changePwdRatioBtn.place(anchor="nw", relx=0.52, rely=0.31, x=0, y=0)
        self.changePwdRatioBtn.configure(command=self.activate_all_btn)
        self.dontChangePwdRatioBtn = tk.Radiobutton(self.controlFrame)
        self.dontChangePwdRatioBtn.configure(
            background="#ffffff",
            compound="top",
            cursor="arrow",
            disabledforeground="#000000",
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
        self.img_regular = tk.PhotoImage(file=DRAWABLE_PATH+"regular.png")
        self.UpdatePassword.configure(height=200, takefocus=True, width=200)
        self.UpdatePassword.geometry("370x490+400+100")
        self.UpdatePassword.iconphoto(True, self.img_regular)
        self.UpdatePassword.resizable(False, False)
        self.UpdatePassword.title("CCPros")

        # Main widget
        self.mainwindow = self.UpdatePassword
        
        # Binding the save_pass method to save button
        self.pwdEntry.bind("<Return>", self.save_pass)


    def run(self):
        self.mainwindow.mainloop()


    def hide_pass(self):
        """
        hide the password in the password entry
        """
        # hiding the password in the password entry
        self.pwdEntry.config(show="*")
        
        # re-enable the show password button
        self.showPassBtn.config(state="normal")
    
    
    def show_pass(self):
        """
        show the password in the password entry
        """
        pwd = self.pwdEntry.get()
        
        # Checking if the password is not empty
        if pwd != "":
            # first disable the show password button
            self.showPassBtn.config(state="disabled")
            
            # showing the password in the password entry
            self.pwdEntry.config(show="")
            
            # hiding the password in the password entry after 4 seconds
            self.mainwindow.after(4000, self.hide_pass)
        

    def save_pass(self, event=True):
        """
        save the password in the batch script file
        """
        
        pwd = self.pwdEntry.get()
        
        # Check if the password is empty
        if pwd == "":
            # Create tk messagebox to show the user an error
            messagebox.showinfo("Empty Password", "Password can't be empty")
        # Check is password is secure enough
        elif len(pwd) > 0:
        
            # Keeping track of the letters and digits in the password
            alpha_chars = []
            digit_chars = []
            
            # Keep track of the other characters in the password
            other_chars = []
            
            # Setting the minimum length of letters and digits in the password
            min_alpha_chars = 5
            min_digit_chars = 3
            
            # Looping through the password
            for char in pwd:
                # checking if the char is a letter
                if char.isalpha():
                    alpha_chars.append(char)
                # checking if the char is a digit
                elif char.isdigit():
                    digit_chars.append(char)
                # checking if the char is a special character
                else:
                    other_chars.append(char)
            
            # Checking is any special characters are in the password
            if len(other_chars) > 0 or len(alpha_chars) < min_alpha_chars or len(digit_chars) < min_digit_chars:
                # Create tk messagebox to show the user an error
                messagebox.showinfo("Password is not secure enough", "The password must contain at least 5 letters and 3 digits and no special characters.")

            # Ask the user to confirm the password up
            else:
                confirm_pwd = messagebox.askyesno("Confirm Password", "Are you sure you want to save the password?")
                
                # check if the user confirmed the password
                if confirm_pwd:
                    # save the password in the root.gits file
                    save_pwd(pwd)
                    # saving the password in the batch script file
                    self.run_batch_script()
                    # Inform the user that the password was saved
                    messagebox.showinfo("Password Saved", "The password was saved and updated automatically.")
                    # close the window
                    self.mainwindow.destroy()


    def run_batch_script(self):
        """
        Run the batch script to update the account password
        """
        run_script()
    
    
    def activate_all_btn(self):
        """
        Activate the following widgets:
        password entry, show password button & save button
        
        Disable the following widgets:
        change password ratio button, update password button
        """
        


        # First disable the change password button
        self.changePwdRatioBtn.config(state="disabled")

        
        # Disable update password button
        self.updatePassBtn.config(state="disabled")
        
        
        # Deciding which state the update password button is in
        match self.updatePassBtn.cget("state"):
            case "normal":
                # set cursor to hand for the update password button
                self.updatePassBtn.config(cursor="hand2")
            case "disabled":
                # set cursor to arrow for the update password button
                self.updatePassBtn.config(cursor="arrow")
        
   
        # Activating the don't change password button
        self.dontChangePwdRatioBtn.config(state="normal")
        
        
        
        # Deciding which cursor to set for change password button
        match self.changePwdRatioBtn.cget("state"):
            case "normal":
                # set cursor to hand for the change password button
                self.changePwdRatioBtn.config(cursor="hand2")
            case "disabled":
                # set cursor to arrow for the change password button
                self.changePwdRatioBtn.config(cursor="arrow")
        
        # Deciding which cursor to set for don't change password button
        match self.dontChangePwdRatioBtn.cget("state"):
            case "normal":
                # set cursor to hand for the don't change password button
                self.dontChangePwdRatioBtn.config(cursor="hand2")
                # set cursor to arrow for the don't change password button
            case "disabled":
                self.dontChangePwdRatioBtn.config(cursor="arrow")
        
        
        # Activate all widgets that was disabled before
        self.pwdEntry.config(state="normal")
        self.showPassBtn.config(state="normal")
        self.saveBtn.config(state="normal")
        
        # Set the focus on the password entry
        self.pwdEntry.focus()
        
        # Deciding which cursor to set for show password button
        match self.showPassBtn.cget("state"):
            case "normal":
                # set cursor to hand for the show password button
                self.showPassBtn.config(cursor="hand2")
            case "disabled":
                # set cursor to arrow for the show password button
                self.showPassBtn.config(cursor="arrow")
        
        # Deciding which cursor to set for save button
        match self.saveBtn.cget("state"):
            case "normal":
                # set cursor to hand for the save button
                self.saveBtn.config(cursor="hand2")
            case "disabled":
                # set cursor to arrow for the save button
                self.saveBtn.config(cursor="arrow")



    def deactivate_all_btn(self):
        """
        Disable the following widgets:
        password entry, show password button & save button
        
        Activate the following widgets:
        don't change password ratio button, update password button
        """
        

        # First disable the don't change password button
        self.dontChangePwdRatioBtn.config(state="disabled")
        
        
        # Checking if the password is not empty then clear the password entry
        if self.pwdEntry.get() != "":
            self.pwdEntry.delete(0, "end")
        
        
        # Activating the change password button
        self.changePwdRatioBtn.config(state="normal") 
        
        
        # Deciding which cursor to set for change password button
        match self.changePwdRatioBtn.cget("state"):
            case "normal":
                # set cursor to hand for the change password button
                self.changePwdRatioBtn.config(cursor="hand2")
            case "disabled":
                # set cursor to arrow for the change password button
                self.changePwdRatioBtn.config(cursor="arrow")
        
        # Deciding which cursor to set for don't change password button
        match self.dontChangePwdRatioBtn.cget("state"):
            case "normal":
                # set cursor to hand for the don't change password button
                self.dontChangePwdRatioBtn.config(cursor="hand2")
                # set cursor to arrow for the don't change password button
            case "disabled":
                self.dontChangePwdRatioBtn.config(cursor="arrow")
        
            
        
        # Activating the update password button
        self.updatePassBtn.config(state="normal")
        
        # Deciding which state the update password button is in
        match self.updatePassBtn.cget("state"):
            case "normal":
                # set cursor to hand for the update password button
                self.updatePassBtn.config(cursor="hand2")
            case "disabled":
                # set cursor to arrow for the update password button
                self.updatePassBtn.config(cursor="arrow")
        
        
        # Deactivate all widgets that was enabled before
        self.pwdEntry.config(state="disabled")
        self.showPassBtn.config(state="disabled")
        self.saveBtn.config(state="disabled")
        
        # Set the focus on the update password button
        # self.updatePassBtn.focus()


        # Deciding which cursor to set for show password button
        match self.showPassBtn.cget("state"):
            case "normal":
                # set cursor to hand for the show password button
                self.showPassBtn.config(cursor="hand2")
            case "disabled":
                # set cursor to arrow for the show password button
                self.showPassBtn.config(cursor="arrow")
                

        # Deciding which cursor to set for save button
        match self.saveBtn.cget("state"):
            case "normal":
                # set cursor to hand for the save button
                self.saveBtn.config(cursor="hand2")
            case "disabled":
                # set cursor to arrow for the save button
                self.saveBtn.config(cursor="arrow")



if __name__ == "__main__":
    app = UpdatePasswordApp()
    app.run()
