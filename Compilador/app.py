import tkinter as tk
from lexer import Lexer, Resul
from parser import Parser
from parser import *
import subprocess
import os

script_dir = os.path.dirname(os.path.abspath(__file__))

def generador_codigo_c(tokens):
    c_code = "#include <stdio.h>\n\nint main() {\n"
    c_code += '  printf("Resultado: ");\n'
    inside_block = False
    variables = {}  # Diccionario para almacenar variables
    
    i = 0
    while i < len(tokens):
        token = tokens[i]

        if token == 'inicio':
            c_code += "  {\n"
            inside_block = True

        elif token == 'fin':
            for var in variables:
                c_code += f'    printf("{var}: %d\\n", {variables[var]});\n' if isinstance(variables[var], int) else f'    printf("{var}: %f\\n", {variables[var]});\n'
            c_code += "  }\n"
            inside_block = False

        elif token == 'definir':
            i += 1
            var_name = tokens[i]
            i += 2  
            if tokens[i] == 'entero':
                variables[var_name] = 0  # Inicializar variable entera en 0
            else:
                variables[var_name] = 0.0  # Inicializar variable real en 0.0

        elif token == ':=':  # Asignación de valor a variable
            var_name = tokens[i - 1]  # El nombre de la variable está antes de :=
            i += 1
            expr = ''
            while i < len(tokens) and tokens[i] != ';':
                expr += tokens[i]
                i += 1
            try:
                expr_as_number = eval(expr)
                variables[var_name] = expr_as_number
            except:
                pass  # Ignorar asignaciones no evaluables
            
        elif token == 'escribir':
            expr = ''
            i += 1
            while i < len(tokens) and tokens[i] != ';':
                if tokens[i].startswith('"') and tokens[i].endswith('"'):
                    expr += tokens[i][1:-1]
                else:
                    expr += tokens[i]
                i += 1

            try:
                expr_as_number = eval(expr)
                c_code += f"  printf(\"%d\\n\", {expr_as_number});\n" if not inside_block else f"    printf(\"%d\\n\", {expr_as_number});\n"
            except:
                indentation = '    ' if inside_block else '  '
                c_code += f'{indentation}printf("{expr}\\n");\n'

        i += 1
    c_code += "  getchar();\n"
    c_code += "  return 0;\n}\n"

    return c_code


def crear_archivo_c(c_code):
    file_path = os.path.join(script_dir, "cintermedio.c")
    with open(file_path, "w") as file:
        file.write(c_code)
        print(f"Código en C generado correctamente en '{file_path}'")

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Compilador')

        frame = tk.Frame(self)
        frame.pack(padx=10, pady=10)

        # Cuadro de texto para ingresar la expresión a analizar
        self.label = tk.Label(frame, text="Ingrese una expresión:")
        self.label.grid(row=0, column=0, sticky="w")
        self.code_text = tk.Text(frame, width=50, height=20, bd=5)
        self.code_text.grid(row=1, column=0, padx=5, pady=5)

        # Cuadro de texto para mostrar los tokens encontrados
        self.tokens_label = tk.Label(frame, text="Analizador Léxico:")
        self.tokens_label.grid(row=0, column=1, sticky="w")
        self.tokens_text = tk.Text(frame, width=50, height=20, bd=5, state="disabled")
        self.tokens_text.grid(row=1, column=1, padx=5, pady=5)

        # Cuadro de texto para mostrar el resultado del análisis
        self.sin_label = tk.Label(frame, text="Analizador Sintáctico:")
        self.sin_label.grid(row=2, column=0, sticky="w")
        self.sin_text = tk.Text(frame, height=5, width=50, bd=5, state="disabled")
        self.sin_text.grid(row=3, column=0, padx=5, pady=5)

        # Agregar "inicio" y "fin" al cuadro de texto
        self.code_text.insert('end', 'inicio\n  \nfin')

        # Contenedor para los botones
        button_frame = tk.Frame(frame)
        button_frame.grid(row=4, column=0, columnspan=2)

        # Botón para compilar
        self.compile_button = tk.Button(button_frame, text='Compilar', command=self.compile_code)
        self.compile_button.pack(side='left', padx=5)

        # Botón para optimizar
        self.optimize_button = tk.Button(button_frame, text='Optimizar', command=self.optimize_code)
        self.optimize_button.pack(side='left', padx=5)

        # Botón para crear ejecutable
        self.create_executable_button = tk.Button(button_frame, text='Crear Ejecutable', command=self.create_executable)
        self.create_executable_button.pack(side='left', padx=5)

        # Cuadro de texto para mostrar el resultado de la compilación
        self.result_label = tk.Label(frame, text="Resultado:")
        self.result_label.grid(row=2, column=1, sticky="w")
        self.result_text = tk.Text(frame, height=5, width=50, bd=5)
        self.result_text.grid(row=3, column=1, padx=5, pady=5)

    def codigo_objeto(self):
        try:
            c_file_path = os.path.join(script_dir, "cintermedio.c")
            obj_file_path = os.path.join(script_dir, "cobjeto.o")

            subprocess.Popen(["gcc", "-c", c_file_path, "-o", obj_file_path], cwd=script_dir)

        except subprocess.CalledProcessError as e:
            self.handle_compilation_error(e)

    def create_executable(self):
        code = self.code_text.get('1.0', 'end-1c')
        lexer = Resul()

        try:
            tokens = lexer.tokenize(code)

            codigo_c = generador_codigo_c(tokens)
            crear_archivo_c(codigo_c)
            self.codigo_objeto()

            self.compile_to_executable()

        except Exception as e:
            self.handle_compilation_error(e)

    def compile_to_executable(self):
        try:
            c_file_path = os.path.join(script_dir, "cintermedio.c")
            subprocess.Popen(["gcc", c_file_path, "-o", "Aplicacion"], cwd=script_dir)

            self.result_text.delete('1.0', 'end')
            self.result_text.insert('end', f"¡Ejecutable creado correctamente como 'Aplicacion'!")

        except subprocess.CalledProcessError as e:
            self.handle_compilation_error(e)

    def compile_code(self):
        code = self.code_text.get('1.0', 'end-1c')
        lexer = Resul()
        parser = Parser()

        try:
            tokens = lexer.tokenize(code)
            ast = parser.parse(tokens)

            if ast is None:
                self.handle_syntax_error()
            else:
                self.handle_compilation_success(ast)
                self.print_tokens()

        except Exception as e:
            self.handle_compilation_error(e)

    def show_message(self, message):
        self.result_text.configure(state='normal')
        self.result_text.delete('1.0', 'end')
        self.result_text.insert('1.0', message)
        self.result_text.configure(state='disabled')

    def optimize_code(self):
        code = self.code_text.get('1.0', 'end-1c')
        lexer = Resul()

        try:
            tokens = lexer.tokenize(code)
            optimized_tokens = self.optimize_constants(tokens)
            optimized_code = ' '.join(optimized_tokens).replace(';', ';\n')
            optimized_code = optimized_code.replace('inicio', 'inicio\n')

            self.code_text.delete('1.0', 'end')
            self.code_text.insert('end', optimized_code)

            self.print_tokens()

        except Exception as e:
            self.handle_optimization_error(e)

    def optimize_constants(self, tokens):
        optimized_tokens = []
        i = 0
        while i < len(tokens):
            if i + 2 < len(tokens) and tokens[i + 1] == '+' and tokens[i + 2].isdigit():
                result = int(tokens[i]) + int(tokens[i + 2])
                optimized_tokens.append(str(result))
                i += 3
            elif i + 2 < len(tokens) and tokens[i + 1] == '-' and tokens[i + 2].isdigit():
                result = int(tokens[i]) - int(tokens[i + 2])
                optimized_tokens.append(str(result))
                i += 3
            elif i + 2 < len(tokens) and tokens[i + 1] == '*' and tokens[i + 2].isdigit():
                result = int(tokens[i]) * int(tokens[i + 2])
                optimized_tokens.append(str(result))
                i += 3
            else:
                optimized_tokens.append(tokens[i])
                i += 1
        return optimized_tokens

    def handle_syntax_error(self):
        self.sin_text.config(state="normal")
        self.sin_text.delete("1.0", "end")
        self.sin_text.insert("1.0", "Error de sintaxis.")
        self.sin_text.config(state="disabled")

        self.result_text.delete('1.0', 'end')
        self.result_text.insert('end', "Error de compilación: Error de sintaxis\n")

    def handle_compilation_success(self, ast):
        self.result_text.delete('1.0', 'end')
        self.result_text.insert('end', f'Compilación exitosa!\nResultado: {str(ast)}\n')

        self.sin_text.config(state="normal")
        self.sin_text.delete("1.0", "end")
        self.sin_text.insert("1.0", "Programa analizado correctamente.")
        self.sin_text.config(state="disabled")

    def handle_compilation_error(self, e):
        error_message = f"Error de compilación: {e}"
        self.sin_text.config(state="normal")
        self.sin_text.delete("1.0", "end")
        self.sin_text.insert("1.0", error_message)
        self.sin_text.config(state="disabled")

        self.result_text.delete('1.0', 'end')
        self.result_text.insert('end', error_message + "\n")

    def handle_optimization_error(self, e):
        self.result_text.delete('1.0', 'end')
        self.result_text.insert('end', f'Error de optimización: {e}\n')

    def print_tokens(self):
        code = self.code_text.get('1.0', 'end-1c')

        lexer = Lexer()
        tokens = lexer.tokenize(code)

        self.tokens_text.config(state="normal")
        self.tokens_text.delete('1.0', 'end')
        self.tokens_text.insert("1.0", "\n".join(tokens))
        self.tokens_text.config(state="disabled")

if __name__ == '__main__':
    app = App()
    app.mainloop()