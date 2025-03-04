import tkinter as tk
import kociemba

class RubikSolverApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Rubik's Cube Solver")

        self.colors = ["white", "yellow", "blue", "green", "red", "orange"]
        self.color_codes = {'white': 'W', 'yellow': 'Y', 'blue': 'B', 'green': 'G', 'red': 'R', 'orange': 'O'}
        self.current_color_index = 0
        self.faces = ['U', 'R', 'F', 'D', 'L', 'B']
        self.current_face_index = 0
        self.buttons = []
        self.cube_state = [['W'] * 9 for _ in range(6)]

        self.create_widgets()

    def create_widgets(self):
        self.cube_frame = tk.Frame(self.root)
        self.cube_frame.pack()

        self.buttons_face = []
        for j in range(9):
            button = tk.Button(self.cube_frame, bg=self.colors[self.current_color_index], width=4, height=2, relief="raised", borderwidth=2)
            button.config(command=lambda b=button, i=j: self.change_color(b, i))
            button.grid(row=j//3, column=j%3, padx=3, pady=3)
            self.buttons_face.append(button)

        self.face_label = tk.Label(self.root, text=f"Face: {self.faces[self.current_face_index]}", font=("Arial", 14))
        self.face_label.pack(pady=10)

        self.change_face_button = tk.Button(self.root, text="Change Face", command=self.change_face, font=("Arial", 12), bg="lightgray")
        self.change_face_button.pack(pady=5)

        self.solve_button = tk.Button(self.root, text="Solve", command=self.solve, font=("Arial", 12), bg="lightgray")
        self.solve_button.pack(pady=10)

        self.solution_label = tk.Label(self.root, text="", wraplength=300, font=("Arial", 12))
        self.solution_label.pack()

        self.steps_text = tk.Text(self.root, height=10, width=50, font=("Arial", 12), wrap='word')
        self.steps_text.pack(pady=10)

        self.update_buttons()

    def change_color(self, button, index):
        self.current_color_index = (self.current_color_index + 1) % len(self.colors)
        button.config(bg=self.colors[self.current_color_index])
        self.cube_state[self.current_face_index][index] = self.color_codes[self.colors[self.current_color_index]]

    def change_face(self):
        self.current_face_index = (self.current_face_index + 1) % len(self.faces)
        self.face_label.config(text=f"Face: {self.faces[self.current_face_index]}")
        self.update_buttons()

    def update_buttons(self):
        for i, button in enumerate(self.buttons_face):
            color_code = self.cube_state[self.current_face_index][i]
            color_name = [k for k, v in self.color_codes.items() if v == color_code][0]
            button.config(bg=color_name)

    def solve(self):
        cube_state = ''.join([''.join(face) for face in self.cube_state])
        try:
            solution = kociemba.solve(cube_state)
            self.solution_label.config(text="Solution found! See steps below.")
            self.steps_text.delete(1.0, tk.END)
            self.steps_text.insert(tk.END, f"Steps to solve the cube:\n{solution}")
        except:
            self.solution_label.config(text="Invalid cube state!")

if __name__ == "__main__":
    root = tk.Tk()
    app = RubikSolverApp(root)
    root.mainloop()
