import tkinter as tk
from tkinter import filedialog, messagebox
from google import genai
import pandas as pd
import os

client = genai.Client(api_key="AIzaSyB9L3RcJuQ-sof6khCzSvj__Zoli-Y1m-I")

def select_csv_file():
    root = tk.Tk()
    root.title("CSV Cleaner")
    root.geometry("500x550")

    file_label = tk.Label(root, text="No file selected", wraplength=480)
    file_label.pack(pady=5)

    output_label = tk.Label(root, text="No output file selected", wraplength=480)
    output_label.pack(pady=5)

    chunk_size_label = tk.Label(root, text="Enter chunk size:")
    chunk_size_label.pack()
    chunk_size_entry = tk.Entry(root)
    chunk_size_entry.pack()

    start_row_label = tk.Label(root, text="Enter starting row:")
    start_row_label.pack()
    start_row_entry = tk.Entry(root)
    start_row_entry.pack()

    clean_button = tk.Button(root, text="Clean Data!", state=tk.DISABLED)
    clean_button.pack(pady=10)

    def open_file():
        file_path = filedialog.askopenfilename(
            title="Select a CSV File",
            filetypes=[("CSV Files", "*.csv")]
        )
        if file_path:
            file_label.config(text=f"Selected: {file_path}")
            clean_button.config(state=tk.NORMAL)
        else:
            file_label.config(text="No file selected")
            clean_button.config(state=tk.DISABLED)
    
    def select_output_file():
        output_path = filedialog.asksaveasfilename(
            title="Select Output CSV File",
            filetypes=[("CSV Files", "*.csv")],
            defaultextension=".csv"
        )
        if output_path:
            output_label.config(text=f"Output: {output_path}")
        else:
            output_label.config(text="No output file selected")
    
    def read_csv_chunk(file_path, chunk_size, start_row):
        try:
            chunk = pd.read_csv(file_path, skiprows=range(1, start_row+1), nrows=chunk_size)
            return chunk.to_csv(index=False)
        except Exception as e:
            print(f"Error reading CSV: {e}")
            return ""
    
    def clean_data():
        prompt = prompt_textbox.get("1.0", tk.END).strip()
        file_path = file_label.cget("text").replace("Selected: ", "").strip()
        output_path = output_label.cget("text").replace("Output: ", "").strip()
        
        if not prompt or not file_path or not output_path:
            return
        
        chunk_size = int(chunk_size_entry.get()) if chunk_size_entry.get().isdigit() else 5
        start_row = int(start_row_entry.get()) if start_row_entry.get().isdigit() else 0
        
        if os.path.exists(output_path):
            overwrite = messagebox.askyesno("File Exists", "The output file already exists. Overwrite?")
            if not overwrite:
                return
            open(output_path, 'w').close()
        
        for chunk in pd.read_csv(file_path, skiprows=range(1, start_row+1), chunksize=chunk_size):
            chunk_data = chunk.to_csv(index=False)
            final_prompt = f"{prompt}\n\nHere is a sample of the data:\n{chunk_data}"
            
            response = client.models.generate_content(
                model="gemini-2.0-flash", contents=final_prompt
            )
            
            with open(output_path, 'a', encoding='utf-8') as f:
                f.write(response.text + "\n")
        
        messagebox.showinfo("Success", "Data cleaning complete!")
    
    button = tk.Button(root, text="Select CSV File", command=open_file)
    button.pack(pady=5)
    
    output_button = tk.Button(root, text="Select Output File", command=select_output_file)
    output_button.pack(pady=5)
    
    prompt_textbox = tk.Text(root, height=5, width=60)
    prompt_textbox.pack(pady=10)
    prompt_textbox.insert("1.0", "Enter your cleaning instructions here...")
    
    clean_button.config(command=clean_data)
    
    response_label = tk.Label(root, text="LLM Response:")
    response_label.pack(pady=5)
    
    response_textbox = tk.Text(root, height=5, width=60, state=tk.DISABLED)
    response_textbox.pack(pady=10)
    
    root.mainloop()

select_csv_file()