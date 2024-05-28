import tkinter as tk
from AVLTree import AVLTree
import winsound


class BinaryTreeGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Arvore AVL")
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()

        window_width = 800
        window_height = 600

        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        self.master.geometry(f"{window_width}x{window_height}+{x}+{y}")

        self.tree = AVLTree()

        self.label = tk.Label(
            self.master, text="Informe valor para inserir:", font=("Poppins", 12))
        self.label.pack()

        self.entry = tk.Entry(self.master, font=("Poppins", 12))
        self.entry.pack()

        self.button_frame = tk.Frame(self.master)
        self.button_frame.pack(side=tk.BOTTOM, pady=20)

        self.insert_button = tk.Button(self.button_frame, text="Inserir", font=(
            "Poppins", 12), command=self.insert_value)
        self.insert_button.pack(side=tk.LEFT, padx=10)

        self.delete_button = tk.Button(self.button_frame, text="Remover", font=(
            "Poppins", 12), command=self.delete_value)
        self.delete_button.pack(side=tk.LEFT, padx=10)
        self.preorder_button = tk.Button(self.button_frame, text="PreOrdem", font=(
            "Poppins", 12), command=self.preorder_traversal)
        self.preorder_button.pack(side=tk.LEFT, padx=10)
        self.inorder_button = tk.Button(self.button_frame, text="EmOrdem", font=(
            "Poppins", 12), command=self.inorder_traversal)
        self.inorder_button.pack(side=tk.LEFT, padx=10)

        self.postorder_button = tk.Button(self.button_frame, text="PosOrdem", font=(
            "Poppins", 12), command=self.postorder_traversal)
        self.postorder_button.pack(side=tk.LEFT, padx=10)

        self.reset_button = tk.Button(self.button_frame, text="Resetar", font=(
            "Poppins", 12), command=self.reset_tree)
        self.reset_button.pack(side=tk.LEFT, padx=10)

        self.canvas = tk.Canvas(self.master, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.root = None

    def insert_value(self):
        try:
            value = int(self.entry.get())
            if self.tree.search(self.root, value):
                self.entry.delete(0, tk.END)
            else:
                self.root = self.tree.insert(self.root, value)
                self.canvas.delete("all")
                self.draw_tree(
                    self.root, self.master.winfo_width() // 2, 50, 150)
                winsound.PlaySound("SystemAsterisk", winsound.SND_ALIAS)
                self.entry.delete(0, tk.END)
        except ValueError:
            pass

    def delete_value(self):
        try:
            value = int(self.entry.get())
            if not self.tree.search(self.root, value):
                self.entry.delete(0, tk.END)
            else:
                self.root = self.tree.delete(self.root, value)
                self.canvas.delete("all")
                self.draw_tree(
                    self.root, self.master.winfo_width() // 2, 50, 150)
                winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
                self.entry.delete(0, tk.END)
        except ValueError:
            pass

    def draw_tree(self, node, x, y, step):
        if node:
            self.canvas.create_oval(
                x-15, y-15, x+15, y+15, fill="white", outline="black")
            self.canvas.create_text(x, y, text=str(
                node.key), font=("Poppins", 12))
            if node.left:
                self.canvas.create_line(x, y, x-step, y+50, arrow=tk.LAST)
                self.draw_tree(node.left, x-step, y+50, step/2)
            if node.right:
                self.canvas.create_line(x, y, x+step, y+50, arrow=tk.LAST)
                self.draw_tree(node.right, x+step, y+50, step/2)

    def inorder_traversal(self):
        self.canvas.delete("all")
        self.tree.inorder_traversal(self.root)
        self.draw_tree(self.root, self.master.winfo_width() // 2, 50, 150)

    def preorder_traversal(self):
        self.canvas.delete("all")
        self.tree.preorder_traversal(self.root)
        self.draw_tree(self.root, self.master.winfo_width() // 2, 50, 150)

    def postorder_traversal(self):
        self.canvas.delete("all")
        self.tree.postorder_traversal(self.root)
        self.draw_tree(self.root, self.master.winfo_width() // 2, 50, 150)

    def reset_tree(self):
        self.canvas.delete("all")
