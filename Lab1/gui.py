import tkinter
from tkinter import Tk
from tkinter import ttk
from tkinter import filedialog
import variant
import random
import setop
import os

class MainWindow:
	def __init__(self):	
		#Vars
		self.set_A = []
		self.set_B = []
		self.set_C = []
		self.set_U = []
		self.source_set_result = []
		self.simplified_set_result = []
		self.set_Z = []
		self.state_manual_entries = 'disabled'
		self.state_automate_entries = 'normal'
		self.state_unvrsl_entries = 'normal'
		self.state_windowed_buttons = ['disabled']
		self.input_mode_automate = 'automate'
		self.input_mode_manual = 'manual'
		self.input_mode = tkinter.StringVar(value=self.input_mode_automate)
		#Entry
		self.manual_A_entry = tkinter.Entry(state=self.state_manual_entries)
		self.manual_B_entry = tkinter.Entry(state=self.state_manual_entries)
		self.manual_C_entry = tkinter.Entry(state=self.state_manual_entries)
		self.power_A_entry = tkinter.Entry(state=self.state_automate_entries)
		self.power_B_entry = tkinter.Entry(state=self.state_automate_entries)
		self.power_C_entry = tkinter.Entry(state=self.state_automate_entries)
		self.universal_range_from_entry = tkinter.Entry(state=self.state_unvrsl_entries)
		self.universal_range_to_entry = tkinter.Entry(state=self.state_unvrsl_entries)
		#RadioButtons
		self.set_automate_input_radiobutton = ttk.Radiobutton(text='Згенерувати множини', value=self.input_mode_automate, variable=self.input_mode, command=self.input_mode_event)
		self.set_manual_input_radiobutton = ttk.Radiobutton(text='Ввести множини вручну', value=self.input_mode_manual, variable=self.input_mode, command=self.input_mode_event)
		#Buttons
		self.generate_ALL_button = tkinter.Button(root, width=25, height=1, text='Згенерувати множини', font=('Arial', '12'), bg='grey', command=self.generate_ALL_button_event)
		self.button1 = tkinter.Button(root, width=10, height=2, text='Вікно №2', state=self.state_windowed_buttons, command=self.button1_event)
		self.button2 = tkinter.Button(root, width=10, height=2, text='Вікно №3', state=self.state_windowed_buttons, command=self.button2_event)	
		self.button3 = tkinter.Button(root, width=10, height=2, text='Вікно №4', state=self.state_windowed_buttons, command=self.button3_event)
		self.button4 = tkinter.Button(root, width=10, height=2, text='Вікно №5', state=self.state_windowed_buttons, command=self.button4_event)
		#Labels
		self.universal_range_label = tkinter.Label(text='Задати універсальну множину U', font=('Arial', 10))
		self.label1 = tkinter.Label(text='Студент: first and last name', font=('Arial', 12))
		self.label2 = tkinter.Label(text='Група: number', font=('Arial', 12))
		self.label3 = tkinter.Label(text='Номер у списку: number', font=('Arial', 12))
		self.label4 = tkinter.Label(text=variant.show_variant(), font=('Arial', 12))
		#Set-Labels
		self.label_A = tkinter.Label(text='Потужність множини: A', font=('Arial', 10))
		self.label_B = tkinter.Label(text='Потужність множини: B', font=('Arial', 10))
		self.label_C = tkinter.Label(text='Потужність множини: C', font=('Arial', 10))
		#Entry-labels
		self.universal_range_from_label = tkinter.Label(text='від', font=('Arial', 8))
		self.universal_range_to_label = tkinter.Label(text='до', font=('Arial', 8))
		self.entry_label_A = tkinter.Label(text='Введіть множину: A', font=('Arial', 10))
		self.entry_label_B = tkinter.Label(text='Введіть множину: B', font=('Arial', 10))
		self.entry_label_C = tkinter.Label(text='Введіть множину: C', font=('Arial', 10))
		#pack labels
		self.label1.pack(anchor='nw')
		self.label2.pack(anchor='nw')
		self.label3.pack(anchor='nw')
		self.label4.pack(anchor='nw')
		#place buttons
		self.button1.place(x=400, y=10)
		self.button2.place(x=500, y=10)
		self.button3.place(x=600, y=10)
		self.button4.place(x=700, y=10)
		self.generate_ALL_button.place(x=5, y=510)
		#place labels and entries
		self.label_A.place(x=5, y=250)
		self.power_A_entry.place(x=5, y=270)
		self.label_B.place(x=5, y=300)
		self.power_B_entry.place(x=5, y=320)
		self.label_C.place(x=5, y=350)
		self.power_C_entry.place(x=5, y=370)
		#pack manual_entries with entry_labels
		self.entry_label_A.pack(anchor='sw')
		self.manual_A_entry.pack(anchor='sw')
		self.entry_label_B.pack(anchor='sw')
		self.manual_B_entry.pack(anchor='sw')
		self.entry_label_C.pack(anchor='sw')
		self.manual_C_entry.pack(anchor='sw')
		#place universal_range_entry with universal_range_*labels
		self.universal_range_label.place(x=5, y=400)
		self.universal_range_from_label.place(x=5, y=430)
		self.universal_range_from_entry.place(x=30, y=430)
		self.universal_range_to_label.place(x=5, y=470)
		self.universal_range_to_entry.place(x=30, y=470)
		#place radiobuttons
		self.set_automate_input_radiobutton.place(x=200, y=100)
		self.set_manual_input_radiobutton.place(x=200, y=120)

	def button1_event(self):
		window2 = Window2(self.set_A, self.set_B, self.set_C, self.set_U)

	def button2_event(self):
		window3 = Window3(self.set_A, self.set_B, self.set_C, self.set_U)

	def button3_event(self):
		window4 = Window4(self.set_A, self.set_B, self.set_C, self.set_U)

	def button4_event(self):
		window5 = Window5(self.source_set_result, self.simplified_set_result, self.set_Z, self.set_Z_off)

	def generate_ALL_button_event(self):
		self.set_A = list(self.set_A)
		self.set_A.clear()
		self.set_B = list(self.set_B)
		self.set_B.clear()
		self.set_C = list(self.set_C)
		self.set_C.clear()
		self.set_U = list(self.set_U)
		self.set_U.clear()
		unvrsl_from = int(self.universal_range_from_entry.get())
		unvrsl_to = int(self.universal_range_to_entry.get())
		if self.input_mode.get() == 'automate':	
			power_A = int(self.power_A_entry.get())
			power_B = int(self.power_B_entry.get())
			power_C = int(self.power_C_entry.get())	
			for i in range(power_A):
				self.set_A.append(random.randint(unvrsl_from, unvrsl_to))
			for i in range(power_B):
				self.set_B.append(random.randint(unvrsl_from, unvrsl_to))
			for i in range(power_C):
				self.set_C.append(random.randint(unvrsl_from, unvrsl_to))
			self.set_A = set(self.set_A)
			self.set_B = set(self.set_B)
			self.set_C = set(self.set_C)
		else:
			self.set_A = set(map(int, self.manual_A_entry.get().split(',')))
			self.set_B = set(map(int, self.manual_B_entry.get().split(',')))
			self.set_C = set(map(int, self.manual_C_entry.get().split(',')))


		for i in range(unvrsl_from, unvrsl_to +1):
			self.set_U.append(i)
		self.set_U = set(self.set_U)
		self.source_set_result = str(setop.set_not(setop.set_intersection(setop.set_union(setop.set_not(self.set_A, self.set_U), setop.set_not(self.set_B, self.set_U)), setop.set_union(setop.set_not(self.set_B, self.set_U), setop.set_not(self.set_C, self.set_U))), self.set_U))
		self.simplified_set_result = str(setop.set_intersection(self.set_B, setop.set_union(self.set_A, self.set_C)))
		self.set_X = setop.set_not(self.set_A, self.set_U)
		self.set_Y = self.set_C.copy()
		self.set_Z = str(setop.set_symmetric_difference(self.set_X, self.set_Y))
		self.set_Z_off = str(self.set_X.symmetric_difference(self.set_Y))
		if self.state_windowed_buttons == ['disabled']:
			self.state_windowed_buttons = ['normal']
			self.button1['state'] = self.state_windowed_buttons
			self.button2['state'] = self.state_windowed_buttons
			self.button3['state'] = self.state_windowed_buttons
			self.button4['state'] = self.state_windowed_buttons
	def input_mode_event(self):
		if self.state_manual_entries == 'disabled' and self.state_automate_entries == 'normal' and self.input_mode.get() == 'manual':
			self.state_manual_entries = 'normal'
			self.state_automate_entries = 'disabled'
			self.power_A_entry['state'] = self.state_automate_entries
			self.power_B_entry['state'] = self.state_automate_entries
			self.power_C_entry['state'] = self.state_automate_entries
			self.manual_A_entry['state'] = self.state_manual_entries
			self.manual_B_entry['state'] = self.state_manual_entries
			self.manual_C_entry['state'] = self.state_manual_entries
		elif self.state_manual_entries == 'normal' and self.state_automate_entries == 'disabled' and self.input_mode.get() == 'automate':
			self.state_manual_entries = 'disabled'
			self.state_automate_entries = 'normal'
			self.power_A_entry['state'] = self.state_automate_entries
			self.power_B_entry['state'] = self.state_automate_entries
			self.power_C_entry['state'] = self.state_automate_entries
			self.manual_A_entry['state'] = self.state_manual_entries
			self.manual_B_entry['state'] = self.state_manual_entries
			self.manual_C_entry['state'] = self.state_manual_entries

class Window2(Tk):
	def __init__(self, set_A, set_B, set_C, set_U):
		#Vars
		self.set_A = set_A
		self.set_B = set_B
		self.set_C = set_C
		self.set_U = set_U
		super().__init__()
		#Settings
		self.geometry("800x800+250+0")
		self.title('Вікно №2 - Початковий вираз')
		#Vars 
		self.active_result_performance_text = False
		#Buttons
		self.save_step_performance_button = tkinter.Button(self, text='Зберегти у файл', width=20, height=2, command=self.save_step_performance_button_event)
		self.step_performance_button = tkinter.Button(self, text='Покрокове виконання', width=20, height=2, command=self.step_performance_button_event)
		#Labels
		self.frst_line_expression_label = tkinter.Label(self, text='1) (not(A) v not(B)) = ' + str(setop.set_union(setop.set_not(self.set_A, self.set_U), setop.set_not(self.set_B, self.set_U))), font=('Arial', 12))
		self.scnd_line_expression_label = tkinter.Label(self, text='2) (not(B) v not(C)) = '+ str(setop.set_union(setop.set_not(self.set_B, self.set_U), setop.set_not(self.set_C, self.set_U))), font=('Arial', 12))
		self.thrd_line_expression_label = tkinter.Label(self, text='3) (not(A) v not(B)) ^ (not(B) v not(C)) = ' + str(setop.set_intersection(setop.set_union(setop.set_not(self.set_A, self.set_U), setop.set_not(self.set_B, self.set_U)), setop.set_union(setop.set_not(self.set_B, self.set_U), setop.set_not(self.set_C, self.set_U)))), font=('Arial', 12))
		self.frth_line_expression_label = tkinter.Label(self, text='4) not((not(A) v not(B)) ^ (not(B) v not(C))) = ' + str(setop.set_not(setop.set_intersection(setop.set_union(setop.set_not(self.set_A, self.set_U), setop.set_not(self.set_B, self.set_U)), setop.set_union(setop.set_not(self.set_B, self.set_U), setop.set_not(self.set_C, self.set_U))), self.set_U)), font=('Arial', 12))
		self.last_line_expression_label = tkinter.Label(self, text='Відповідь: ' + str(setop.set_not(setop.set_intersection(setop.set_union(setop.set_not(self.set_A, self.set_U), setop.set_not(self.set_B, self.set_U)), setop.set_union(setop.set_not(self.set_B, self.set_U), setop.set_not(self.set_C, self.set_U))), self.set_U)), font=('Arial', 12))

		self.source_expression_label = tkinter.Label(self, font=('Arial', 12, 'bold'))
		self.source_expression_label['text'] = ('Заданий вираз: D = not((not(A) v not(B)) ^ (not(B) v not(C)))')
		self.show_A_label = tkinter.Label(self, text='Множина А: ' + str(self.set_A), font=('Arial', 10))
		self.show_B_label = tkinter.Label(self, text='Множина B: ' + str(self.set_B), font=('Arial', 10))
		self.show_C_label = tkinter.Label(self, text='Множина C: ' + str(self.set_C), font=('Arial', 10))
		#place labels and place source_expression label
		self.show_A_label.place(x=0, y=0)
		self.show_B_label.place(x=0, y=50)
		self.show_C_label.place(x=0, y=100)
		self.source_expression_label.place(x=0, y=150)
		#place buttons
		self.step_performance_button.place(x=0, y=200)
		self.save_step_performance_button.place(x=500, y=200)

	def step_performance_button_event(self):
		if self.active_result_performance_text == False:
			self.frst_line_expression_label.place(x=0, y=300)
			self.scnd_line_expression_label.place(x=0, y=350)
			self.thrd_line_expression_label.place(x=0, y=400)
			self.frth_line_expression_label.place(x=0, y=450)
			self.last_line_expression_label.place(x=0, y=500)
			self.active_result_performance_text = True
		else:
			self.frst_line_expression_label.place_forget()
			self.scnd_line_expression_label.place_forget()
			self.thrd_line_expression_label.place_forget()
			self.frth_line_expression_label.place_forget()
			self.last_line_expression_label.place_forget()
			self.active_result_performance_text = False

	def save_step_performance_button_event(self):
		path_long = 'C:\\Users\\' + str(os.getlogin()) +'\\OneDrive\\Рабочий стол\\save_result_long.txt'
		path_short = 'C:\\Users\\' + str(os.getlogin()) +'\\OneDrive\\Рабочий стол\\save_result_short.txt'
		if self.frth_line_expression_label['text'] == '':
			with open(path_short, 'w') as f:
				f.write(self.source_expression_label['text'] + str('\n'))
				f.write(self.frst_line_expression_label['text'] + str('\n'))
				f.write(self.scnd_line_expression_label['text'] + str('\n'))
				f.write(self.thrd_line_expression_label['text'] + str('\n'))
		else:
			with open(path_long, 'w') as f:
				f.write(self.source_expression_label['text'] + str('\n'))
				f.write(self.frst_line_expression_label['text'] + str('\n'))
				f.write(self.scnd_line_expression_label['text'] + str('\n'))
				f.write(self.thrd_line_expression_label['text'] + str('\n'))
				f.write(self.frth_line_expression_label['text'] + str('\n'))
				f.write(self.last_line_expression_label['text'] + str('\n'))

class Window3(Window2):
	def __init__(self, set_A, set_B, set_C, set_U):
		#Vars
		self.set_A = set_A
		self.set_B = set_B
		self.set_C = set_C
		self.set_U = set_U
		self.result_set = str(setop.set_intersection(self.set_B, setop.set_union(self.set_A, self.set_C)))
		super().__init__(self.set_A, self.set_B, self.set_C, self.set_U)
		#Settings
		self.title('Вікно №3 - Спрощений вираз')
		#redefine labels
		self.source_expression_label['text'] = 'Спрощений вираз: D = B ^ (A v C) '
		self.frst_line_expression_label['text'] = '1) A v C = ' + str(setop.set_union(self.set_A, self.set_C))
		self.scnd_line_expression_label['text'] = '2) B ^ (A v C) = ' + str(setop.set_intersection(self.set_B, setop.set_union(self.set_A, self.set_C)))
		self.thrd_line_expression_label['text'] = 'Відповідь: ' + str(setop.set_intersection(self.set_B, setop.set_union(self.set_A, self.set_C)))
		self.frth_line_expression_label['text'] = ''
		self.last_line_expression_label['text'] = ''

class Window4(Window3):
	def __init__(self, set_A, set_B, set_C, set_U):
		#Vars
		self.set_A = set_A
		self.set_B = set_B
		self.set_C = set_C
		self.set_U = set_U
		self.set_X = setop.set_not(self.set_A, self.set_U)
		self.set_Y = self.set_C.copy()
		self.set_Z = setop.set_symmetric_difference(self.set_X, self.set_Y)
		super().__init__(self.set_A, self.set_B, self.set_C, self.set_U)
		#Settings
		self.title('Вікно №4 - Множини X та Y')
		#redefine labels
		self.show_X_label = self.show_A_label
		self.show_X_label['text'] = 'X = ' + str(self.set_X)
		self.show_Y_label = self.show_B_label
		self.show_Y_label['text'] = 'Y = ' + str(self.set_Y)
		self.show_C_label['text'] = ''
		self.source_expression_label['text'] = 'Задана операція: Z = X △ Y'
		self.frst_line_expression_label['text'] = 'Z = X △ Y = ' + str(self.set_Z)
		self.scnd_line_expression_label['text'] = 'Відповідь: ' + str(self.set_Z)
		self.thrd_line_expression_label['text'] = ''
		#replace labels
		self.show_X_label.place(x=0, y=20)
		#hide buttons
		self.save_step_performance_button.place_forget()
		# change step_performance_button text
		self.step_performance_button['text'] = 'Відповідь'

class Window5(Tk):
	def __init__(self, source_set_result, simplified_set_result, set_Z, set_offAlgo):
		#Settings
		super().__init__()
		self.title('Вікно №5 - Результати')
		self.geometry("800x800+250+0")
		#Vars
		self.hard_set_path = ''
		self.source_set_result = source_set_result
		self.simplified_set_result = simplified_set_result
		self.set_Z = set_Z
		self.set_offAlgo = set_offAlgo
		#Buttons
		self.read_from_files_button = tkinter.Button(self, text='Зчитати з файлів', width=20, height=2, command=self.ask_read_file)
		#Labels
		self.correct_results_label = tkinter.Label(self, text='Результати сходяться', font=('Arial', 14), foreground='red')
		self.correct_results_label2 = tkinter.Label(self, text='Результати сходяться', font=('Arial', 14), foreground='red')
		self.source_expression_label = tkinter.Label(self, text='D = not((not(A) v not(B)) ^ (not(B) v not(C))) = ' + self.source_set_result, font=('Arial', 14))
		self.simplified_expression_label = tkinter.Label(self, text='D = B ^ (A v C) = ' + self.simplified_set_result, font=('Arial', 14))
		self.z_expression_label = tkinter.Label(self, text='Z(авторський алгоритм) = ' + self.set_Z, font=('Arial', 14))
		self.z_expression_offAlgo_label = tkinter.Label(self, text='Z(алгоритм Python) = ' + self.set_offAlgo, font=('Arial', 14))
		#Place labels
		self.correct_results_label.place(x=20, y=80)
		self.correct_results_label2.place(x=20, y=450)
		self.source_expression_label.place(x=20, y=20)
		self.simplified_expression_label.place(x=20, y=50)
		self.z_expression_label.place(x=20, y=300)
		self.z_expression_offAlgo_label.place(x=20, y=400)
		#Place buttons
		self.read_from_files_button.place(x=500, y=20)
	def ask_read_file(self):
		self.hard_set_path = filedialog.askopenfilenames()

root = tkinter.Tk()
root.geometry("800x800+250+0")
root.title('Головне вікно')
window = MainWindow()
root.mainloop()