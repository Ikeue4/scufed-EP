import subprocess
import tkinter as tk

__name__ = '__main__'

class TerminalUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Python Terminal")
        
        self.input_box = tk.Entry(self.root, width=50)
        self.input_box.pack(side=tk.LEFT, padx=10, pady=10)
        
        self.submit_button = tk.Button(self.root, text="Submit", command=self.submit_command)
        self.submit_button.pack(side=tk.LEFT, padx=10, pady=10)
        
        self.output_box = tk.Text(self.root, width=50, height=10)
        self.output_box.pack(side=tk.LEFT, padx=10, pady=10)
        
        self.process = None
        
    def run_script(self, script_path):
        print("Running script: ", script_path)
        self.process = subprocess.Popen(["python", script_path], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        self.read_stdout()
        
    def read_stdout(self):
        while self.process and self.process.poll() is None:
            output = self.process.stdout.readline()
            if output:
                self.output_box.insert(tk.END, output.decode())
        self.stop_process()
        
    def stop_process(self):
        if self.process:
            self.process.kill()
            self.process = None
        
    def submit_command(self):
        command = self.input_box.get()
        self.process.stdin.write((command + "\n").encode())
        self.process.stdin.flush()
        
    def run(self):
        self.root.mainloop()

print (__name__)
if __name__ == '__main__':
    try:
        terminal_ui = TerminalUI()
        script_path = "d:/source control/beta/auto quiz.py"
        terminal_ui.run_script(script_path)
        terminal_ui.run()
    except Exception as e:
        print("An error occurred:", e)

