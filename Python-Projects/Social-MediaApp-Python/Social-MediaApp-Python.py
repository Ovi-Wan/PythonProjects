import cv2
from tkinter import Tk, Label, Button, Entry, Text, StringVar, Frame, PhotoImage
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk

class SocialMediaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Social Media Basic")
        self.root.geometry("500x700")
        self.root.config(bg="#f0f0f0")
        self.users = {}
        self.posts = []
        self.current_user = None
        self.profile_image = None
        self.create_login_screen()

    def create_login_screen(self):
        self.clear_screen()
        Label(self.root, text="Social Media", font=("Arial", 24, "bold"), bg="#ffffff", fg="#333333").pack(pady=20)
        Label(self.root, text="Username:", font=("Arial", 14), bg="#f0f0f0", fg="#333333").pack(pady=5)
        self.username_entry = Entry(self.root, font=("Arial", 14), bd=0, relief="flat", highlightthickness=0)
        self.username_entry.pack(pady=5, padx=20, fill="x")
        Label(self.root, text="Password:", font=("Arial", 14), bg="#f0f0f0", fg="#333333").pack(pady=5)
        self.password_entry = Entry(self.root, show="*", font=("Arial", 14), bd=0, relief="flat", highlightthickness=0)
        self.password_entry.pack(pady=5, padx=20, fill="x")
        login_button = Button(self.root, text="Login", font=("Arial", 14, "bold"), bg="#3498db", fg="#ffffff",
                              command=self.login, relief="flat", width=20, height=2)
        login_button.pack(pady=20)
        register_button = Button(self.root, text="Create Account", font=("Arial", 14),
                                 command=self.create_account_screen, relief="flat", width=20, height=2, bg="#2ecc71",
                                 fg="#ffffff")
        register_button.pack(pady=10)

    def create_account_screen(self):
        self.clear_screen()
        Label(self.root, text="Create Account", font=("Arial", 24, "bold"), bg="#ffffff", fg="#333333").pack(pady=20)
        Label(self.root, text="Username:", font=("Arial", 14), bg="#f0f0f0", fg="#333333").pack(pady=5)
        self.new_username_entry = Entry(self.root, font=("Arial", 14), bd=0, relief="flat", highlightthickness=0)
        self.new_username_entry.pack(pady=5, padx=20, fill="x")
        Label(self.root, text="Password:", font=("Arial", 14), bg="#f0f0f0", fg="#333333").pack(pady=5)
        self.new_password_entry = Entry(self.root, show="*", font=("Arial", 14), bd=0, relief="flat",
                                        highlightthickness=0)
        self.new_password_entry.pack(pady=5, padx=20, fill="x")
        create_button = Button(self.root, text="Create Account", font=("Arial", 14), command=self.create_account,
                               relief="flat", width=20, height=2, bg="#e74c3c", fg="#ffffff")
        create_button.pack(pady=20)
        back_button = Button(self.root, text="Back to Login", font=("Arial", 14), command=self.create_login_screen,
                             relief="flat", width=20, height=2, bg="#f39c12", fg="#ffffff")
        back_button.pack(pady=10)

    def create_account(self):
        username = self.new_username_entry.get()
        password = self.new_password_entry.get()
        if username and password:
            if username not in self.users:
                self.users[username] = {"password": password, "profile_image": None, "profile_description": "",
                                        "posts": []}
                self.create_login_screen()
                self.show_message("Account created successfully!")
            else:
                self.show_message("Username already exists!")
        else:
            self.show_message("Please fill in all fields!")

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if username in self.users and self.users[username]["password"] == password:
            self.current_user = username
            self.create_home_screen()
        else:
            self.show_message("Invalid username or password!")

    def create_home_screen(self):
        self.clear_screen()
        Label(self.root, text=f"Welcome, {self.current_user}!", font=("Arial", 24), bg="#ffffff", fg="#333333").pack(pady=20)
        post_label = Label(self.root, text="Post a message", font=("Arial", 14), bg="#f0f0f0", fg="#333333")
        post_label.pack(pady=10)
        self.post_entry = Text(self.root, height=4, width=50, font=("Arial", 14), bd=0, relief="flat",
                               highlightthickness=0)
        self.post_entry.pack(pady=5, padx=20)
        self.image_to_post = None
        post_image_button = Button(self.root, text="Add Image to Post", font=("Arial", 14),
                                   command=self.select_image_for_post, relief="flat", bg="#f39c12", fg="#ffffff")
        post_image_button.pack(pady=10)
        post_button = Button(self.root, text="Post", font=("Arial", 14, "bold"), bg="#3498db", fg="#ffffff",
                             command=self.create_post, relief="flat", width=20, height=2)
        post_button.pack(pady=10)
        feed_button = Button(self.root, text="View Feed", font=("Arial", 14), command=self.view_feed, relief="flat",
                             width=20, height=2, bg="#2ecc71", fg="#ffffff")
        feed_button.pack(pady=10)
        logout_button = Button(self.root, text="Logout", font=("Arial", 14), command=self.logout, relief="flat",
                               width=20, height=2, bg="#e74c3c", fg="#ffffff")
        logout_button.pack(pady=10)
        self.create_bottom_nav()

    def create_bottom_nav(self):
        bottom_nav = Frame(self.root, bg="#ffffff")
        bottom_nav.pack(side="bottom", fill="x", pady=20)
        home_icon = Button(bottom_nav, text="🏠", font=("Arial", 24), relief="flat", bg="#ffffff",
                           command=self.create_home_screen)
        home_icon.pack(side="left", padx=20)
        search_icon = Button(bottom_nav, text="🔍", font=("Arial", 24), relief="flat", bg="#ffffff")
        search_icon.pack(side="left", padx=20)
        add_icon = Button(bottom_nav, text="➕", font=("Arial", 24), relief="flat", bg="#ffffff")
        add_icon.pack(side="left", padx=20)
        profile_icon = Button(bottom_nav, text="👤", font=("Arial", 24), relief="flat", bg="#ffffff",
                              command=self.view_profile)
        profile_icon.pack(side="left", padx=20)

    def select_image_for_post(self):
        file_path = askopenfilename(filetypes=[("Image files", "*.jpg *.png *.jpeg")])
        if file_path:
            image = Image.open(file_path)
            image = image.resize((100, 100))
            self.image_to_post = ImageTk.PhotoImage(image)
            self.show_message("Image selected for post!")

    def create_post(self):
        post_content = self.post_entry.get("1.0", "end-1c").strip()
        if post_content or self.image_to_post:
            post = {"content": post_content, "image": self.image_to_post}
            self.users[self.current_user]["posts"].append(post)
            self.show_message("Post created successfully!")
            self.post_entry.delete("1.0", "end")
            self.image_to_post = None
        else:
            self.show_message("Post cannot be empty!")

    def view_feed(self):
        self.clear_screen()
        Label(self.root, text="Feed", font=("Arial", 24), bg="#ffffff", fg="#333333").pack(pady=20)
        if self.users[self.current_user]["posts"]:
            for post in reversed(self.users[self.current_user]["posts"]):
                post_frame = Frame(self.root, bg="#f9f9f9")
                post_frame.pack(fill="both", padx=20, pady=10, anchor="w")
                if post["content"]:
                    post_content_label = Label(post_frame, text=post["content"], font=("Arial", 14), wraplength=450,
                                               bg="#f9f9f9", fg="#34495e")
                    post_content_label.pack(anchor="w")
                if post["image"]:
                    post_image_label = Label(post_frame, image=post["image"])
                    post_image_label.pack(pady=5)
        else:
            Label(self.root, text="No posts yet.", font=("Arial", 14), bg="#f0f0f0", fg="#333333").pack(pady=20)
        back_button = Button(self.root, text="Back to Home", font=("Arial", 14), command=self.create_home_screen,
                             relief="flat", width=20, height=2, bg="#f39c12", fg="#ffffff")
        back_button.pack(pady=10)

    def view_profile(self):
        self.clear_screen()
        Label(self.root, text=f"Profile of {self.current_user}", font=("Arial", 24), bg="#ffffff", fg="#333333").pack(pady=20)
        if "profile_image" in self.users[self.current_user]:
            profile_image_label = Label(self.root, image=self.users[self.current_user]["profile_image"])
            profile_image_label.pack(pady=10)
        else:
            Label(self.root, text="No profile picture.", font=("Arial", 14), bg="#f0f0f0", fg="#333333").pack(pady=10)
        change_picture_button = Button(self.root, text="Change Profile Picture", font=("Arial", 14),
                                       command=self.change_profile_picture, relief="flat", bg="#2ecc71", fg="#ffffff")
        change_picture_button.pack(pady=10)
        if self.posts:
            user_posts = [post for user, post in self.posts if user == self.current_user]
            if user_posts:
                for post in user_posts:
                    post_frame = Frame(self.root, bg="#f9f9f9")
                    post_frame.pack(fill="both", padx=20, pady=10, anchor="w")
                    post_user_label = Label(post_frame, text=f"{self.current_user} says:", font=("Arial", 16, "bold"),
                                            bg="#f9f9f9", fg="#2c3e50")
                    post_user_label.pack(anchor="w")
                    post_content_label = Label(post_frame, text=post, font=("Arial", 14), wraplength=450, bg="#f9f9f9",
                                               fg="#34495e")
                    post_content_label.pack(anchor="w")
            else:
                Label(self.root, text="No posts yet.", font=("Arial", 14), bg="#f0f0f0", fg="#333333").pack(pady=20)
        else:
            Label(self.root, text="No posts yet.", font=("Arial", 14), bg="#f0f0f0", fg="#333333").pack(pady=20)
        back_button = Button(self.root, text="Back to Home", font=("Arial", 14), command=self.create_home_screen,
                             relief="flat", width=20, height=2, bg="#f39c12", fg="#ffffff")
        back_button.pack(pady=10)

    def logout(self):
        self.current_user = None
        self.create_login_screen()

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def show_message(self, message):
        message_label = Label(self.root, text=message, font=("Arial", 14), fg="red", bg="#ffffff")
        message_label.pack(pady=5)

    def change_profile_picture(self):
        file_path = askopenfilename(filetypes=[("Image files", "*.jpg *.png *.jpeg")])
        if file_path:
            image = Image.open(file_path)
            image = image.resize((150, 150))
        self.users[self.current_user]["profile_image"] = ImageTk.PhotoImage(image)
        self.show_message("Profile picture updated successfully!")
        self.view_profile()

root = Tk()
app = SocialMediaApp(root)
root.mainloop()
