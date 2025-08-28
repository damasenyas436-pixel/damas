import tkinter as tk
from tkinter import ttk, messagebox
import json
import webbrowser

class EducationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Education Hub")
        self.root.geometry("900x600")
        self.root.configure(bg='#f0f8ff')
        
        # Educational content
        self.content = {
            "Mathematics": {
                "Algebra": "Algebra is the study of mathematical symbols and rules for manipulating these symbols. It's a unifying thread of almost all of mathematics.",
                "Geometry": "Geometry is a branch of mathematics concerned with questions of shape, size, relative position of figures, and properties of space.",
                "Calculus": "Calculus is the mathematical study of continuous change, in the same way that geometry is the study of shape and algebra is the study of generalizations of arithmetic operations."
            },
            "Science": {
                "Physics": "Physics is the natural science that studies matter, its motion and behavior through space and time, and the related entities of energy and force.",
                "Chemistry": "Chemistry is the scientific discipline involved with elements and compounds composed of atoms, molecules and ions: their composition, structure, properties, behavior and the changes they undergo during a reaction with other substances.",
                "Biology": "Biology is the natural science that studies life and living organisms, including their physical structure, chemical processes, molecular interactions, physiological mechanisms, development and evolution."
            },
            "Programming": {
                "Python": "Python is an interpreted, high-level, general-purpose programming language. Created by Guido van Rossum and first released in 1991, Python's design philosophy emphasizes code readability with its notable use of significant whitespace.",
                "Data Structures": "Data structures are specialized formats for organizing, processing, retrieving and storing data. There are several basic and advanced types of data structures, all designed to arrange data to suit a specific purpose.",
                "Algorithms": "An algorithm is a step-by-step procedure to solve a problem or accomplish some end. There are many types of algorithms including sorting, searching, graph algorithms, and more."
            }
        }
        
        # Resources links
        self.resources = {
            "Mathematics": ["https://www.khanacademy.org/math", "https://www.mathsisfun.com/"],
            "Science": ["https://www.khanacademy.org/science", "https://phet.colorado.edu/"],
            "Programming": ["https://www.codecademy.com/", "https://www.freecodecamp.org/"]
        }
        
        self.setup_ui()
        
    def setup_ui(self):
        # Header
        header = tk.Frame(self.root, bg='#2c3e50', height=80)
        header.pack(fill=tk.X)
        
        title = tk.Label(header, text="Python Education Hub", font=('Arial', 24, 'bold'), 
                        fg='white', bg='#2c3e50')
        title.pack(pady=20)
        
        # Main content area
        main_frame = tk.Frame(self.root, bg='#f0f8ff')
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Left sidebar for categories
        left_frame = tk.Frame(main_frame, bg='#34495e', width=200)
        left_frame.pack(side=tk.LEFT, fill=tk.Y, padx=(0, 10))
        left_frame.pack_propagate(False)
        
        tk.Label(left_frame, text="Subjects", font=('Arial', 16, 'bold'), 
                fg='white', bg='#34495e').pack(pady=20)
        
        # Subject buttons
        for subject in self.content.keys():
            btn = tk.Button(left_frame, text=subject, font=('Arial', 12), 
                           command=lambda s=subject: self.show_subject(s),
                           bg='#3498db', fg='white', relief=tk.FLAT, width=15)
            btn.pack(pady=5)
        
        # Right content area
        self.right_frame = tk.Frame(main_frame, bg='white')
        self.right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        
        # Initial content
        self.show_welcome()
        
    def show_welcome(self):
        # Clear right frame
        for widget in self.right_frame.winfo_children():
            widget.destroy()
        
        # Welcome message
        welcome_text = """
        Welcome to the Python Education Hub!
        
        This application provides educational information on various subjects.
        
        Select a subject from the left sidebar to explore topics and resources.
        
        Features:
        - Mathematics: Algebra, Geometry, Calculus
        - Science: Physics, Chemistry, Biology
        - Programming: Python, Data Structures, Algorithms
        
        Click on any topic to learn more about it.
        """
        
        welcome_label = tk.Label(self.right_frame, text=welcome_text, font=('Arial', 14), 
                                bg='white', justify=tk.LEFT)
        welcome_label.pack(pady=50, padx=30)
        
    def show_subject(self, subject):
        # Clear right frame
        for widget in self.right_frame.winfo_children():
            widget.destroy()
        
        # Subject title
        title = tk.Label(self.right_frame, text=subject, font=('Arial', 20, 'bold'), 
                        bg='white', fg='#2c3e50')
        title.pack(pady=20)
        
        # Topics notebook
        notebook = ttk.Notebook(self.right_frame)
        notebook.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        # Add tabs for each topic
        for topic, description in self.content[subject].items():
            topic_frame = tk.Frame(notebook, bg='white')
            notebook.add(topic_frame, text=topic)
            
            # Topic content
            desc_label = tk.Label(topic_frame, text=description, font=('Arial', 12), 
                                 bg='white', wraplength=600, justify=tk.LEFT)
            desc_label.pack(pady=20, padx=20)
            
            # Example or additional information based on topic
            if subject == "Mathematics":
                if topic == "Algebra":
                    example = "Example: Solve for x: 2x + 5 = 11\nSolution: x = 3"
                elif topic == "Geometry":
                    example = "Example: Area of a circle = πr²\nWhere r is the radius of the circle"
                else:
                    example = "Example: Derivative of x² is 2x\nIntegral of 2x is x² + C"
            elif subject == "Science":
                if topic == "Physics":
                    example = "Newton's Second Law: F = ma\nForce equals mass times acceleration"
                elif topic == "Chemistry":
                    example = "Water chemical formula: H₂O\nTwo hydrogen atoms bonded to one oxygen atom"
                else:
                    example = "Mitosis: Process of cell division that results in two genetically identical daughter cells"
            else:
                if topic == "Python":
                    example = "Example Python code:\n\nfor i in range(5):\n    print('Hello, World!')"
                elif topic == "Data Structures":
                    example = "Example: Stack follows LIFO (Last-In-First-Out) principle"
                else:
                    example = "Example: Binary Search algorithm has O(log n) time complexity"
            
            example_label = tk.Label(topic_frame, text=example, font=('Courier', 11), 
                                    bg='#f9f9f9', relief=tk.SUNKEN, wraplength=600, justify=tk.LEFT)
            example_label.pack(pady=10, padx=20)
        
        # Resources section
        resources_frame = tk.Frame(self.right_frame, bg='white')
        resources_frame.pack(fill=tk.X, pady=20)
        
        tk.Label(resources_frame, text="Additional Resources:", font=('Arial', 14, 'bold'), 
                bg='white').pack(pady=(20, 10))
        
        for i, resource in enumerate(self.resources[subject]):
            btn = tk.Button(resources_frame, text=f"Resource {i+1}", font=('Arial', 12),
                           command=lambda r=resource: webbrowser.open(r),
                           bg='#2ecc71', fg='white', relief=tk.FLAT)
            btn.pack(pady=5)

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = EducationApp(root)
    root.mainloop()