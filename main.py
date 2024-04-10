import customtkinter
from logic import listContent

# AJUSTES BÁSICOS
customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk() # Root element
root.title("Igualador de carpetas")
root.geometry("600x400")
#customtkinter.set_widget_scaling(1)  # widget dimensions and text size

def comparativeResults(content, frame):
    docs, folders = content
    # Creamos el ScrollableFrame
    resultf = customtkinter.CTkScrollableFrame(master=frame, label_text="Le falta:")
    resultf.pack(pady=12, padx=10)
    if docs:  # Si hay documentos diferentes
        label = customtkinter.CTkLabel(master=resultf, text="🗎 Documentos")
        label.pack(pady=6, padx=10)
        for doc in docs:
            label = customtkinter.CTkLabel(master=resultf, text=doc)
            label.pack(pady=6, padx=10)
    if folders:  # Si hay carpetas diferentes
        label = customtkinter.CTkLabel(master=resultf, text="🗀 Carpetas")
        label.pack(pady=6, padx=10)
        for fold in folders:
            label = customtkinter.CTkLabel(master=resultf, text=fold)
            label.pack(pady=6, padx=10)

def main():
    dir1 = entry1.get()
    dir2 = entry2.get()
    print("test")
    #print(docs1)
    #print(fold1)
    comparativeResults(listContent(dir1), frame1)
    comparativeResults(listContent(dir2), frame2) 

# F R A M E  1
frame1 = customtkinter.CTkFrame(master=root)
frame1.pack(side="left", fill="both", expand=True)
#frame1.pack(pady=20, padx=20, fill="both", expand=True)

label1 = customtkinter.CTkLabel(master=frame1, text="Directorio 1")
label1.pack(pady=12,padx=10)

entry1 = customtkinter.CTkEntry(master=frame1, placeholder_text="Directorio 2")
entry1.pack(pady=12, padx=10)

# F R A M E  2
frame2 = customtkinter.CTkFrame(master=root)
frame2.pack(side="left", fill="both", expand=True)

label2 = customtkinter.CTkLabel(master=frame2, text="Carpeta 1")
label2.pack(pady=12,padx=10)

entry2 = customtkinter.CTkEntry(master=frame2, placeholder_text="Ruta 2")
entry2.pack(pady=12, padx=10)

# M E N Ú
button = customtkinter.CTkButton(master=root, text="Comparar", command=main)
button.pack(pady=12, padx=10)

checkbox_a = customtkinter.CTkCheckBox(master=root, text="Comparar archivos")
checkbox_a.pack(pady=12, padx=10)

checkbox_b = customtkinter.CTkCheckBox(master=root, text="Comparar carpetas")
checkbox_b.pack(pady=12, padx=10)

checkbox_c = customtkinter.CTkCheckBox(master=root, text="Realizar igualación")
checkbox_c.pack(pady=12, padx=10)

root.mainloop()
