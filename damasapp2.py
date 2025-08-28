import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import json
import webbrowser
import random
import textwrap

class EducationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Education Hub")
        self.root.geometry("1000x700")
        self.root.configure(bg='#f0f8ff')
        
        # Educational content
        self.content = {
            "Mathematics": {
                "Algebra": {
                    "description": "Algebra is the study of mathematical symbols and rules for manipulating these symbols. It's a unifying thread of almost all of mathematics.",
                    "examples": [
                        "Solve for x: 2x + 5 = 11 → x = 3",
                        "Quadratic formula: x = [-b ± √(b² - 4ac)] / 2a",
                        "Linear equation: y = mx + b"
                    ]
                },
                "Geometry": {
                    "description": "Geometry is a branch of mathematics concerned with questions of shape, size, relative position of figures, and properties of space.",
                    "examples": [
                        "Area of a circle = πr²",
                        "Pythagorean theorem: a² + b² = c²",
                        "Volume of a sphere = (4/3)πr³"
                    ]
                },
                "Calculus": {
                    "description": "Calculus is the mathematical study of continuous change, in the same way that geometry is the study of shape and algebra is the study of generalizations of arithmetic operations.",
                    "examples": [
                        "Derivative of x² is 2x",
                        "Integral of 2x is x² + C",
                        "Fundamental Theorem of Calculus"
                    ]
                }
            },
            "Science": {
                "Physics": {
                    "description": "Physics is the natural science that studies matter, its motion and behavior through space and time, and the related entities of energy and force.",
                    "examples": [
                        "Newton's Second Law: F = ma",
                        "Law of Gravitation: F = G(m₁m₂)/r²",
                        "Einstein's E = mc²"
                    ]
                },
                "Chemistry": {
                    "description": "Chemistry is the scientific discipline involved with elements and compounds composed of atoms, molecules and ions: their composition, structure, properties, behavior and the changes they undergo during a reaction with other substances.",
                    "examples": [
                        "Water chemical formula: H₂O",
                        "Periodic Table of Elements",
                        "Chemical reaction: 2H₂ + O₂ → 2H₂O"
                    ]
                },
                "Biology": {
                    "description": "Biology is the natural science that studies life and living organisms, including their physical structure, chemical processes, molecular interactions, physiological mechanisms, development and evolution.",
                    "examples": [
                        "Mitosis: Process of cell division",
                        "DNA structure: Double helix",
                        "Photosynthesis: 6CO₂ + 6H₂O → C₆H₁₂O₆ + 6O₂"
                    ]
                }
            },
            "Programming": {
                "Python": {
                    "description": "Python is an interpreted, high-level, general-purpose programming language. Created by Guido van Rossum and first released in 1991, Python's design philosophy emphasizes code readability with its notable use of significant whitespace.",
                    "examples": [
                        "for i in range(5):\n    print('Hello, World!')",
                        "def factorial(n):\n    return 1 if n == 0 else n * factorial(n-1)",
                        "numbers = [1, 2, 3, 4, 5]\nsquares = [x**2 for x in numbers]"
                    ]
                },
                "Data Structures": {
                    "description": "Data structures are specialized formats for organizing, processing, retrieving and storing data. There are several basic and advanced types of data structures, all designed to arrange data to suit a specific purpose.",
                    "examples": [
                        "Stack follows LIFO (Last-In-First-Out) principle",
                        "Queue follows FIFO (First-In-First-Out) principle",
                        "Binary Search Tree: left child < parent < right child"
                    ]
                },
                "Algorithms": {
                    "description": "An algorithm is a step-by-step procedure to solve a problem or accomplish some end. There are many types of algorithms including sorting, searching, graph algorithms, and more.",
                    "examples": [
                        "Binary Search algorithm has O(log n) time complexity",
                        "Bubble Sort: repeatedly swapping adjacent elements",
                        "Dijkstra's algorithm for shortest path finding"
                    ]
                }
            }
        }
        
        # Resources links
        self.resources = {
            "Mathematics": [
                {"name": "Khan Academy Math", "url": "https://www.khanacademy.org/math"},
                {"name": "Math is Fun", "url": "https://www.mathsisfun.com/"},
                {"name": "Wolfram MathWorld", "url": "https://mathworld.wolfram.com/"}
            ],
            "Science": [
                {"name": "Khan Academy Science", "url": "https://www.khanacademy.org/science"},
                {"name": "PhET Simulations", "url": "https://phet.colorado.edu/"},
                {"name": "NASA STEM Engagement", "url": "https://www.nasa.gov/stem"}
            ],
            "Programming": [
                {"name": "Codecademy", "url": "https://www.codecademy.com/"},
                {"name": "freeCodeCamp", "url": "https://www.freecodecamp.org/"},
                {"name": "W3Schools Python", "url": "https://www.w3schools.com/python/"}
            ]
        }
        
        # Quiz questions
        self.quizzes = {
            "Mathematics": [
                {"question": "What is the value of π (pi) approximately?", "options": ["3.14", "2.71", "1.62", "4.13"], "answer": "3.14"},
                {"question": "What is the derivative of x²?", "options": ["2x", "x²", "2", "x"], "answer": "2x"},
                {"question": "What is the Pythagorean theorem?", "options": ["a² + b² = c²", "E = mc²", "F = ma", "V = IR"], "answer": "a² + b² = c²"}
            ],
            "Science": [
                {"question": "What is the chemical formula for water?", "options": ["H₂O", "CO₂", "NaCl", "O₂"], "answer": "H₂O"},
                {"question": "What is Newton's Second Law?", "options": ["F = ma", "E = mc²", "PV = nRT", "V = IR"], "answer": "F = ma"},
                {"question": "What is the powerhouse of the cell?", "options": ["Mitochondria", "Nucleus", "Ribosome", "Golgi Apparatus"], "answer": "Mitochondria"}
            ],
            "Programming": [
                {"question": "Which keyword is used to define a function in Python?", "options": ["def", "function", "define", "func"], "answer": "def"},
                {"question": "Which data structure uses LIFO?", "options": ["Stack", "Queue", "Array", "Linked List"], "answer": "Stack"},
                {"question": "What does OOP stand for?", "options": ["Object-Oriented Programming", "Object-Option Programming", "Objective-Oriented Protocol", "Object-Ordered Programming"], "answer": "Object-Oriented Programming"}
            ]
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
            
        # Additional buttons
        tk.Button(left_frame, text="Take a Quiz", font=('Arial', 12), 
                 command=self.show_quiz_selection, bg='#e74c3c', fg='white', 
                 relief=tk.FLAT, width=15).pack(pady=20)
        
        tk.Button(left_frame, text="About", font=('Arial', 12), 
                 command=self.show_about, bg='#f39c12', fg='white', 
                 relief=tk.FLAT, width=15).pack(pady=5)
        
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
        
        - Detailed explanations and examples for each topic
        - Additional resources with direct links
        - Interactive quizzes to test your knowledge
        
        Click on any topic to learn more about it.
        """
        
        welcome_label = tk.Label(self.right_frame, text=welcome_text, font=('Arial', 14), 
                                bg='white', justify=tk.LEFT)
        welcome_label.pack(pady=50, padx=30)
        
        # Add some decorative elements
        quote_frame = tk.Frame(self.right_frame, bg='#e8f4f8', relief=tk.RIDGE, bd=1)
        quote_frame.pack(fill=tk.X, padx=30, pady=10)
        
        quotes = [
            "Education is the most powerful weapon which you can use to change the world. - Nelson Mandela",
            "The beautiful thing about learning is that no one can take it away from you. - B.B. King",
            "Live as if you were to die tomorrow. Learn as if you were to live forever. - Mahatma Gandhi"
        ]
        
        quote_label = tk.Label(quote_frame, text=random.choice(quotes), 
                              font=('Arial', 12, 'italic'), bg='#e8f4f8', 
                              wraplength=600, justify=tk.CENTER)
        quote_label.pack(pady=15)
        
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
        for topic, info in self.content[subject].items():
            topic_frame = tk.Frame(notebook, bg='white')
            notebook.add(topic_frame, text=topic)
            
            # Topic content with scrollbar
            canvas = tk.Canvas(topic_frame, bg='white')
            scrollbar = ttk.Scrollbar(topic_frame, orient="vertical", command=canvas.yview)
            scrollable_frame = tk.Frame(canvas, bg='white')
            
            scrollable_frame.bind(
                "<Configure>",
                lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
            )
            
            canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
            canvas.configure(yscrollcommand=scrollbar.set)
            
            # Topic description
            desc_label = tk.Label(scrollable_frame, text=info["description"], font=('Arial', 12), 
                                 bg='white', wraplength=600, justify=tk.LEFT)
            desc_label.pack(pady=20, padx=20, anchor="w")
            
            # Examples
            tk.Label(scrollable_frame, text="Examples:", font=('Arial', 14, 'bold'), 
                    bg='white').pack(pady=(20, 10), padx=20, anchor="w")
            
            for example in info["examples"]:
                example_frame = tk.Frame(scrollable_frame, bg='#f9f9f9', relief=tk.SUNKEN, bd=1)
                example_frame.pack(fill=tk.X, padx=20, pady=5)
                
                example_label = tk.Label(example_frame, text=example, font=('Courier', 11), 
                                        bg='#f9f9f9', justify=tk.LEFT, wraplength=600)
                example_label.pack(pady=10, padx=10, anchor="w")
            
            canvas.pack(side="left", fill="both", expand=True)
            scrollbar.pack(side="right", fill="y")
        
        # Resources section
        resources_frame = tk.Frame(self.right_frame, bg='white')
        resources_frame.pack(fill=tk.X, pady=20)
        
        tk.Label(resources_frame, text="Additional Resources:", font=('Arial', 14, 'bold'), 
                bg='white').pack(pady=(20, 10))
        
        for resource in self.resources[subject]:
            btn = tk.Button(resources_frame, text=resource["name"], font=('Arial', 12),
                           command=lambda r=resource: webbrowser.open(r["url"]),
                           bg='#2ecc71', fg='white', relief=tk.FLAT, width=20)
            btn.pack(pady=5)
            
    def show_quiz_selection(self):
        # Clear right frame
        for widget in self.right_frame.winfo_children():
            widget.destroy()
            
        title = tk.Label(self.right_frame, text="Select a Quiz", font=('Arial', 20, 'bold'), 
                        bg='white', fg='#2c3e50')
        title.pack(pady=20)
        
        instruction = tk.Label(self.right_frame, 
                              text="Choose a subject to test your knowledge:", 
                              font=('Arial', 14), bg='white')
        instruction.pack(pady=10)
        
        for subject in self.quizzes.keys():
            btn = tk.Button(self.right_frame, text=subject, font=('Arial', 14),
                           command=lambda s=subject: self.start_quiz(s),
                           bg='#9b59b6', fg='white', relief=tk.RAISED, width=20)
            btn.pack(pady=10)
            
    def start_quiz(self, subject):
        # Clear right frame
        for widget in self.right_frame.winfo_children():
            widget.destroy()
            
        self.quiz_subject = subject
        self.quiz_questions = self.quizzes[subject].copy()
        random.shuffle(self.quiz_questions)
        self.current_question = 0
        self.score = 0
        
        self.show_question()
        
    def show_question(self):
        # Clear right frame
        for widget in self.right_frame.winfo_children():
            widget.destroy()
            
        if self.current_question >= len(self.quiz_questions):
            self.show_quiz_results()
            return
            
        question_data = self.quiz_questions[self.current_question]
        
        # Question number
        title = tk.Label(self.right_frame, 
                        text=f"Question {self.current_question + 1} of {len(self.quiz_questions)}",
                        font=('Arial', 16), bg='white')
        title.pack(pady=10)
        
        # Question text
        question_label = tk.Label(self.right_frame, text=question_data["question"], 
                                 font=('Arial', 14), bg='white', wraplength=600)
        question_label.pack(pady=20)
        
        # Options
        self.answer_var = tk.StringVar(value="")
        for option in question_data["options"]:
            rb = tk.Radiobutton(self.right_frame, text=option, variable=self.answer_var,
                               value=option, font=('Arial', 12), bg='white')
            rb.pack(pady=5, anchor="w", padx=50)
            
        # Submit button
        submit_btn = tk.Button(self.right_frame, text="Submit Answer", 
                              font=('Arial', 12), command=self.check_answer,
                              bg='#3498db', fg='white')
        submit_btn.pack(pady=20)
        
    def check_answer(self):
        if not self.answer_var.get():
            messagebox.showwarning("No Answer", "Please select an answer.")
            return
            
        question_data = self.quiz_questions[self.current_question]
        if self.answer_var.get() == question_data["answer"]:
            self.score += 1
            messagebox.showinfo("Correct!", "Your answer is correct!")
        else:
            messagebox.showerror("Incorrect", 
                                f"Sorry, the correct answer is: {question_data['answer']}")
            
        self.current_question += 1
        self.show_question()
        
    def show_quiz_results(self):
        # Clear right frame
        for widget in self.right_frame.winfo_children():
            widget.destroy()
            
        title = tk.Label(self.right_frame, text="Quiz Results", 
                        font=('Arial', 20, 'bold'), bg='white', fg='#2c3e50')
        title.pack(pady=20)
        
        result_text = f"You scored {self.score} out of {len(self.quiz_questions)} in {self.quiz_subject}!"
        result_label = tk.Label(self.right_frame, text=result_text, 
                               font=('Arial', 16), bg='white')
        result_label.pack(pady=20)
        
        percentage = (self.score / len(self.quiz_questions)) * 100
        if percentage >= 80:
            feedback = "Excellent job! You really know your stuff!"
            color = "#2ecc71"
        elif percentage >= 60:
            feedback = "Good effort! Keep learning and improving!"
            color = "#f39c12"
        else:
            feedback = "Keep studying! You'll get better with practice."
            color = "#e74c3c"
            
        feedback_label = tk.Label(self.right_frame, text=feedback, 
                                 font=('Arial', 14), bg='white', fg=color)
        feedback_label.pack(pady=10)
        
        # Retry button
        retry_btn = tk.Button(self.right_frame, text="Take Another Quiz", 
                             font=('Arial', 12), command=self.show_quiz_selection,
                             bg='#3498db', fg='white')
        retry_btn.pack(pady=20)
        
    def show_about(self):
        # Clear right frame
        for widget in self.right_frame.winfo_children():
            widget.destroy()
            
        title = tk.Label(self.right_frame, text="About Python Education Hub", 
                        font=('Arial', 20, 'bold'), bg='white', fg='#2c3e50')
        title.pack(pady=20)
        
        about_text = """
        Python Education Hub is a comprehensive educational application built with Python and Tkinter.
        
        Features:
        - Detailed information on Mathematics, Science, and Programming
        - Interactive quizzes to test your knowledge
        - Direct links to additional online resources
        - User-friendly interface with easy navigation
        
        This application demonstrates the power of Python for creating educational tools
        and interactive learning experiences.
        
        Version: 1.0
        Developed with Python and Tkinter
        """
        
        about_label = tk.Label(self.right_frame, text=about_text, 
                              font=('Arial', 12), bg='white', justify=tk.LEFT)
        about_label.pack(pady=20, padx=30)
        
        # Close button
        close_btn = tk.Button(self.right_frame, text="Back to Home", 
                             font=('Arial', 12), command=self.show_welcome,
                             bg='#3498db', fg='white')
        close_btn.pack(pady=20)

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = EducationApp(root)
    root.mainloop()