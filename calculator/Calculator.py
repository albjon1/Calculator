import os
import tkinter as tk

# Using absolute icon path eventually for exe file
abs_icon_path = os.path.abspath('icon.png')

# Window configuration
window = tk.Tk()
window.title('Calculator')
window.geometry('255x440')
window.iconphoto(False, tk.PhotoImage(file=abs_icon_path))
window.resizable(width=False, height=False)
window.configure(bg='grey12')

# Functions


def key_press(key_stroke):
    '''displays button press and
       concatonates new button press with old
    '''
    entry = entry_box.get()
    entry_box.delete(0, 'end')
    entry_box.insert(0, str(entry) + str(key_stroke))


def evaluation():
    '''Will get expression from entry widget
       and evaluate the expression. Will also
       handle common errors and display them in
       entry widget
    '''
    try:
        result = entry_box.get()
        entry_box.delete(0, 'end')
        entry_box.insert(0, eval(result))

    except ZeroDivisionError:
        entry_box.delete(0, 'end')
        entry_box.insert(0, 'Error:Div 0')

    except NameError:
        entry_box.delete(0, 'end')
        entry_box.insert(0, 'Error:Letter')

    except SyntaxError:
        entry_box.delete(0, 'end')
        entry_box.insert(0, 'Invalid')


def clear():
    '''Clears entry widget
    '''
    entry_box.delete(0, 'end')


def dark():
    '''Configures all UI widgets to dark theme
    '''
    entry_box.config(bg='grey12',
                     fg='#C8C8C8',
                     selectbackground='#C8C8C8',
                     insertbackground='grey12')
    one_button.config(bg='grey12', fg='#C8C8C8')
    two_button.config(bg='grey12', fg='#C8C8C8')
    three_button.config(bg='grey12', fg='#C8C8C8')
    four_button.config(bg='grey12', fg='#C8C8C8')
    five_button.config(bg='grey12', fg='#C8C8C8')
    six_button.config(bg='grey12', fg='#C8C8C8')
    seven_button.config(bg='grey12', fg='#C8C8C8')
    eight_button.config(bg='grey12', fg='#C8C8C8')
    nine_button.config(bg='grey12', fg='#C8C8C8')
    zero_button.config(bg='grey12', fg='#C8C8C8')
    decimal_button.config(bg='grey12', fg='#C8C8C8')
    equals_button.config(bg='grey12', fg='#C8C8C8')
    divide_button.config(bg='grey12', fg='#C8C8C8')
    multiply_button.config(bg='grey12', fg='#C8C8C8')
    subtract_button.config(bg='grey12', fg='#C8C8C8')
    add_button.config(bg='grey12', fg='#C8C8C8')
    clear_button.config(bg='grey12', fg='#C8C8C8')
    left_bracket_button.config(bg='grey12', fg='#C8C8C8')
    right_bracket_button.config(bg='grey12', fg='#C8C8C8')
    power_button.config(bg='grey12', fg='#C8C8C8')
    dark_button.config(bg='grey12', fg='grey')
    light_button.config(bg='grey12', fg='white')


def light():
    '''Configures all UI widgets to light theme
    '''
    entry_box.config(bg='#F9F9F9',
                     fg='black',
                     selectbackground='black',
                     insertbackground='#F9F9F9')
    one_button.config(bg='#F9F9F9', fg='black')
    two_button.config(bg='#F9F9F9', fg='black')
    three_button.config(bg='#F9F9F9', fg='black')
    four_button.config(bg='#F9F9F9', fg='black')
    five_button.config(bg='#F9F9F9', fg='black')
    six_button.config(bg='#F9F9F9', fg='black')
    seven_button.config(bg='#F9F9F9', fg='black')
    eight_button.config(bg='#F9F9F9', fg='black')
    nine_button.config(bg='#F9F9F9', fg='black')
    zero_button.config(bg='#F9F9F9', fg='black')
    decimal_button.config(bg='#F9F9F9', fg='black')
    equals_button.config(bg='#F9F9F9', fg='black')
    divide_button.config(bg='#F9F9F9', fg='black')
    multiply_button.config(bg='#F9F9F9', fg='black')
    subtract_button.config(bg='#F9F9F9', fg='black')
    add_button.config(bg='#F9F9F9', fg='black')
    clear_button.config(bg='#F9F9F9', fg='black')
    left_bracket_button.config(bg='#F9F9F9', fg='black')
    right_bracket_button.config(bg='#F9F9F9', fg='black')
    power_button.config(bg='#F9F9F9', fg='black')
    dark_button.config(bg='#F9F9F9', fg='black')
    light_button.config(bg='#F9F9F9', fg='grey')


# User Interface
entry_box = tk.Entry(
 window,
 bg='grey12',
 fg='#C8C8C8',
 selectbackground='#C8C8C8',
 insertbackground='grey12',
 width=12,
 font=('consolas', 29))
entry_box.pack()


one_button = tk.Button(
 window,
 text='1',
 bg='grey12',
 fg='#C8C8C8',
 height=3,
 width=6,
 font=3,
 command=lambda: key_press(1))
one_button.place(x=0, y=118)

two_button = tk.Button(
 window,
 text='2',
 bg='grey12',
 fg='#C8C8C8',
 height=3,
 width=6,
 font=3,
 command=lambda: key_press(2))
two_button.place(x=64, y=118)

three_button = tk.Button(
 window,
 text='3',
 bg='grey12',
 fg='#C8C8C8',
 height=3,
 width=6,
 font=3,
 command=lambda: key_press(3))
three_button.place(x=128, y=118)

four_button = tk.Button(
 window,
 text='4',
 bg='grey12',
 fg='#C8C8C8',
 height=3,
 width=6,
 font=3,
 command=lambda: key_press(4))
four_button.place(x=0, y=186)

five_button = tk.Button(
 window,
 text='5',
 bg='grey12',
 fg='#C8C8C8',
 height=3,
 width=6,
 font=3,
 command=lambda: key_press(5))
five_button.place(x=64, y=186)

six_button = tk.Button(
 window,
 text='6',
 bg='grey12',
 fg='#C8C8C8',
 height=3,
 width=6,
 font=3,
 command=lambda: key_press(6))
six_button.place(x=128, y=186)

seven_button = tk.Button(
 window,
 text='7',
 bg='grey12',
 fg='#C8C8C8',
 height=3,
 width=6,
 font=3,
 command=lambda: key_press(7))
seven_button.place(x=0, y=254)

eight_button = tk.Button(
 window,
 text='8',
 bg='grey12',
 fg='#C8C8C8',
 height=3,
 width=6,
 font=3,
 command=lambda: key_press(8))
eight_button.place(x=64, y=254)

nine_button = tk.Button(
 window,
 text='9',
 bg='grey12',
 fg='#C8C8C8',
 height=3,
 width=6,
 font=3,
 command=lambda: key_press(9))
nine_button.place(x=128, y=254)

zero_button = tk.Button(
 window,
 text='0',
 bg='grey12',
 fg='#C8C8C8',
 height=3,
 width=6,
 font=3,
 command=lambda: key_press(0))
zero_button.place(x=0, y=322)

decimal_button = tk.Button(
 window,
 text='•',
 bg='grey12',
 fg='#C8C8C8',
 height=3,
 width=6,
 font=3,
 command=lambda: key_press('.'))
decimal_button.place(x=64, y=322)

equals_button = tk.Button(
 window,
 text='=',
 bg='grey12',
 fg='#C8C8C8',
 height=3,
 width=6,
 font=3,
 command=evaluation)
equals_button.place(x=128, y=322)

divide_button = tk.Button(
 window,
 text='➗',
 bg='grey12',
 fg='#C8C8C8',
 height=3,
 width=6,
 font=3,
 command=lambda: key_press('/'))
divide_button.place(x=192, y=118)

multiply_button = tk.Button(
 window,
 text='✖️',
 bg='grey12',
 fg='#C8C8C8',
 height=3,
 width=6,
 font=3,
 command=lambda: key_press('*'))
multiply_button.place(x=192, y=186)

subtract_button = tk.Button(
 window,
 text='➖',
 bg='grey12',
 fg='#C8C8C8',
 height=3,
 width=6,
 font=3,
 command=lambda: key_press('-'))
subtract_button.place(x=192, y=254)

add_button = tk.Button(
 window,
 text='➕',
 bg='grey12',
 fg='#C8C8C8',
 height=3,
 width=6,
 font=3,
 command=lambda: key_press('+'))
add_button.place(x=192, y=322)

clear_button = tk.Button(
 window,
 text='C',
 bg='grey12',
 fg='#C8C8C8',
 height=3,
 width=6,
 font=3,
 command=clear)
clear_button.place(x=192, y=50)

left_bracket_button = tk.Button(
 window,
 text='(',
 bg='grey12',
 fg='#C8C8C8',
 height=3,
 width=6,
 font=3,
 command=lambda: key_press('('))
left_bracket_button.place(x=0, y=50)

right_bracket_button = tk.Button(
 window,
 text=')',
 bg='grey12',
 fg='#C8C8C8',
 height=3,
 width=6,
 font=3,
 command=lambda: key_press(')'))
right_bracket_button.place(x=64, y=50)

power_button = tk.Button(
 window,
 text='yˣ',
 bg='grey12',
 fg='#C8C8C8',
 height=3,
 width=6,
 font=3,
 command=lambda: key_press('**'))
power_button.place(x=128, y=50)

dark_button = tk.Button(
 window,
 text='🌑',
 bg='grey12',
 fg='grey',
 height=2,
 width=13,
 font=3,
 command=dark)
dark_button.place(x=0, y=390)

light_button = tk.Button(
 window,
 text='🌑',
 bg='grey12',
 fg='white',
 height=2,
 width=13,
 font=3,
 command=light)
light_button.place(x=128, y=390)

print('built by albjon')

window.mainloop()
