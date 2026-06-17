import os
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from collections import Counter
import struct
import time

# ==========================================
# CORE COMPRESSION LOGIC (RLE + Bit Packing)
# ==========================================

class Compressor:
    """
    Implements Run-Length Encoding (RLE) with bit-packing optimization.
    Instead of storing (char, count) as two bytes, we pack them tightly.
    """
    
    def __init__(self):
        pass

    def compress_data(self, raw_bytes):
        if not raw_bytes:
            return b''

        compressed = bytearray()
        
        current_byte = raw_bytes[0]
        count = 1
        
        for i in range(1, len(raw_bytes)):
            if raw_bytes[i] == current_byte and count < 127: 
                count += 1
            else:
                while count > 0:
                    chunk = min(count, 255)
                    compressed.append(current_byte)
                    compressed.append(chunk)
                    count -= chunk
                
                if i < len(raw_bytes):
                    current_byte = raw_bytes[i]
                    count = 1
                continue
                
        while count > 0:
            chunk = min(count, 255)
            compressed.append(current_byte)
            compressed.append(chunk)
            count -= chunk
            
        return bytes(compressed)

    def decompress_data(self, compressed_bytes):
        if not compressed_bytes:
            return b''

        decompressed = bytearray()
        
        for i in range(0, len(compressed_bytes), 2):
            if i + 1 >= len(compressed_bytes):
                break 
            
            byte_val = compressed_bytes[i]
            run_count = compressed_bytes[i+1]
            
            decompressed.extend([byte_val] * run_count)
            
        return bytes(decompressed)

# ==========================================
# FILE MANAGEMENT & DIRECTORY ZIPPING
# ==========================================

class FileZipperSystem:
    def __init__(self):
        self.compressor = Compressor()
        self.header_magic = b'LUMOZIP' 

    def zip_directory(self, source_path, output_path):
        """
        Zips a directory by walking all files, compressing them individually,
        and writing them into a single container with metadata.
        """
        try:
            total_original_size = 0
            total_compressed_size = 0
            file_entries = []

            # Walk directory
            for root, _, files in os.walk(source_path):
                for filename in files:
                    full_path = os.path.join(root, filename)
                    relative_path = os.path.relpath(full_path, source_path)
                    
                    try:
                        with open(full_path, 'rb') as f:
                            original_data = f.read()
                        
                        total_original_size += len(original_data)
                        compressed_data = self.compressor.compress_data(original_data)
                        total_compressed_size += len(compressed_data)
                        
                        path_bytes = relative_path.encode('utf-8')
                        
                        file_entries.append({
                            'path': path_bytes,
                            'original_len': len(original_data),
                            'data': compressed_data
                        })
                        
                    except Exception as e:
                        print(f"Error processing {full_path}: {e}")

            
            archive_data = bytearray()
            
            
            archive_data.extend(self.header_magic)
            archive_data.append(len(file_entries)) 
            
           
            index_offset_start = 0
            current_data_offset = 0
            
            
            for entry in file_entries:
                path_len = len(entry['path'])
                archive_data.extend(struct.pack('<H', path_len))
                archive_data.extend(entry['path'])
                archive_data.extend(struct.pack('<I', entry['original_len']))
                archive_data.extend(struct.pack('<I', len(entry['data'])))
                archive_data.extend(entry['data'])
            
            with open(output_path, 'wb') as f_out:
                f_out.write(archive_data)
            
            return {
                'original': total_original_size,
                'compressed': total_compressed_size,
                'files': len(file_entries)
            }

        except Exception as e:
            raise Exception(f"Zipping failed: {str(e)}")

    def unzip_directory(self, input_path, extract_to):
        """
        Extracts files from the custom archive.
        """
        try:
            with open(input_path, 'rb') as f:
                data = f.read()
            
            if not data.startswith(self.header_magic):
                raise ValueError("Invalid archive format")
            
            offset = len(self.header_magic)
            num_files = data[offset]
            offset += 1
            
            extracted_count = 0
            
            for _ in range(num_files):
                path_len = struct.unpack('<H', data[offset:offset+2])[0]
                offset += 2
                path_bytes = data[offset:offset+path_len]
                offset += path_len
                
                orig_len = struct.unpack('<I', data[offset:offset+4])[0]
                offset += 4
                comp_len = struct.unpack('<I', data[offset:offset+4])[0]
                offset += 4
                
                compressed_segment = data[offset:offset+comp_len]
                offset += comp_len
                
                original_data = self.compressor.decompress_data(compressed_segment)
                
                target_path = os.path.join(extract_to, path_bytes.decode('utf-8'))
                os.makedirs(os.path.dirname(target_path), exist_ok=True)
                
                with open(target_path, 'wb') as f_out:
                    f_out.write(original_data)
                
                extracted_count += 1
            
            return {'files': extracted_count}

        except Exception as e:
            raise Exception(f"Unzipping failed: {str(e)}")

# ==========================================
# GUI INTERFACE (Tkinter)
# ==========================================

class ZipperApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lumo File Zipper (RLE)")
        self.root.geometry("500x400")
        
        self.system = FileZipperSystem()
        
        frame = ttk.Frame(root, padding="20")
        frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        ttk.Label(frame, text="Source Folder/File:").grid(row=0, column=0, pady=5, sticky=tk.W)
        self.source_var = tk.StringVar()
        self.source_entry = ttk.Entry(frame, textvariable=self.source_var, width=40)
        self.source_entry.grid(row=0, column=1, pady=5, padx=5)
        ttk.Button(frame, text="Browse...", command=self.browse_source).grid(row=0, column=2)
        
        ttk.Label(frame, text="Output .lzp File:").grid(row=1, column=0, pady=5, sticky=tk.W)
        self.output_var = tk.StringVar()
        self.output_entry = ttk.Entry(frame, textvariable=self.output_var, width=40)
        self.output_entry.grid(row=1, column=1, pady=5, padx=5)
        ttk.Button(frame, text="Save As...", command=self.browse_output).grid(row=1, column=2)
        
        self.mode_var = tk.StringVar(value="zip")
        ttk.Radiobutton(frame, text="Compress (Zip)", variable=self.mode_var, value="zip").grid(row=2, column=0, sticky=tk.W, pady=10)
        ttk.Radiobutton(frame, text="Decompress (Unzip)", variable=self.mode_var, value="unzip").grid(row=2, column=1, sticky=tk.W)
        
        self.action_btn = ttk.Button(frame, text="Start Process", command=self.run_process)
        self.action_btn.grid(row=3, column=0, columnspan=3, pady=20)
        
        self.log_text = tk.Text(frame, height=8, width=50, state='disabled')
        self.log_text.grid(row=4, column=0, columnspan=3, pady=5, sticky=(tk.W, tk.E))
        
        self.log("Ready to compress or decompress files.")

    def log(self, message):
        self.log_text.configure(state='normal')
        self.log_text.insert(tk.END, f"{message}\n")
        self.log_text.see(tk.END)
        self.log_text.configure(state='disabled')

    def browse_source(self):
        folder = filedialog.askdirectory()
        if folder:
            self.source_var.set(folder)

    def browse_output(self):
        default_ext = ".lzp" if self.mode_var.get() == "zip" else ""
        file_type = [("Lumo Zip Files", "*.lzp")] if self.mode_var.get() == "zip" else [("Any Files", "*.*")]
        
        path = filedialog.asksaveasfilename(defaultextension=default_ext, filetypes=file_type)
        if path:
            self.output_var.set(path)

    def run_process(self):
        source = self.source_var.get()
        output = self.output_var.get()
        mode = self.mode_var.get()
        
        if not source or not output:
            messagebox.showerror("Error", "Please select both source and destination paths.")
            return

        self.action_btn.config(state='disabled')
        self.log(f"Starting {mode} process...")
        
        start_time = time.time()
        
        try:
            if mode == "zip":
                stats = self.system.zip_directory(source, output)
                elapsed = time.time() - start_time
                
                ratio = (1 - (stats['compressed'] / max(stats['original'], 1))) * 100
                
                self.log(f"Compression Complete!")
                self.log(f"Original Size: {stats['original']} bytes")
                self.log(f"Compressed Size: {stats['compressed']} bytes")
                self.log(f"Compression Ratio: {ratio:.1f}%")
                self.log(f"Files processed: {stats['files']}")
                self.log(f"Time taken: {elapsed:.2f}s")
                
            else:
                dest_folder = filedialog.askdirectory(title="Select Extraction Destination")
                if not dest_folder:
                    self.log("Extraction cancelled by user.")
                    return
                    
                stats = self.system.unzip_directory(source, dest_folder)
                self.log(f"Decompression Complete!")
                self.log(f"Extracted {stats['files']} files to: {dest_folder}")
                
        except Exception as e:
            self.log(f"ERROR: {str(e)}")
            messagebox.showerror("Process Failed", str(e))
        
        finally:
            self.action_btn.config(state='normal')

if __name__ == "__main__":
    root = tk.Tk()
    app = ZipperApp(root)
    root.mainloop()
