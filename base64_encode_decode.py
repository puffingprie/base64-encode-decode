import base64 as b64
import tkinter as tk


def encode_string(b_string, count):
    if count < 1:
        return b_string.decode()
    return encode_string(b64.urlsafe_b64encode(b_string), count - 1)


def decode_string(str, count):
    if count < 1:
        return str
    decoded_b_string = b64.urlsafe_b64decode(str)
    return decode_string(decoded_b_string.decode(), count - 1)


def on_focus_in(event, entry, placeholder):
    if entry.get() == placeholder:
        entry.delete(0, "end")
        entry.config(fg='black')


def on_focus_out(event, entry, placeholder):
    if entry.get() == '':
        entry.insert(0, placeholder)
        entry.config(fg='gray')


def set_result_label(string, type='encode'):
    if type == 'encode':
        encode_result_label.delete("1.0", "end")
        encode_result_label.insert("1.0", string)
    # elif type == 'decode':


root = tk.Tk()
root.title("Base64 Encode Decode")
root.geometry("600x600")

# create widgets
encode_placeholder = 'Enter a string to encode'
encode_input = tk.Entry(root, textvariable=tk.StringVar(
    value=encode_placeholder), fg='gray')
encode_input.bind("<FocusIn>", lambda event: on_focus_in(
    event, encode_input, encode_placeholder))
encode_input.bind("<FocusOut>", lambda event: on_focus_out(
    event, encode_input, encode_placeholder))
encode_count_placeholder = 'Enter the amount of times to encode'
encode_count_input = tk.Entry(root, textvariable=tk.StringVar(
    value=encode_count_placeholder), fg='gray')
encode_count_input.bind(
    "<FocusIn>", lambda event: on_focus_in(event, encode_count_input, encode_count_placeholder))
encode_count_input.bind("<FocusOut>", lambda event: on_focus_out(
    event, encode_count_input, encode_count_placeholder))
encode_button = tk.Button(
    root, text="Encode", command=lambda: set_result_label(encode_string(str(encode_input.get()).encode(), int(encode_count_input.get()))))

decode_placeholder = 'Enter a string to decode'
decode_input = tk.Entry(root, textvariable=tk.StringVar(
    value=decode_placeholder), fg='gray')
decode_input.bind("<FocusIn>", lambda event: on_focus_in(
    event, decode_input, decode_placeholder))
decode_input.bind("<FocusOut>", lambda event: on_focus_out(
    event, decode_input, decode_placeholder))
decode_count_placeholder = 'Enter the amount of times to decode'
decode_count_input = tk.Entry(root, textvariable=tk.StringVar(
    value=decode_count_placeholder), fg='gray')
decode_count_input.bind("<FocusIn>", lambda event: on_focus_in(
    event, decode_count_input, decode_count_placeholder))
decode_count_input.bind("<FocusOut>", lambda event: on_focus_out(
    event, decode_count_input, decode_count_placeholder))
decode_button = tk.Button(
    root, text="Decode", command=lambda: set_result_label(decode_string(str(decode_input.get()), int(decode_count_input.get()))))
encode_result_frame = tk.Frame(root, height=150, width=450)
encode_result_scrollbar = tk.Scrollbar(encode_result_frame)
encode_result_label = tk.Text(
    encode_result_frame, height=5, width=20, yscrollcommand=encode_result_scrollbar.set)

# pack widgets
encode_input.pack()
encode_count_input.pack()
encode_button.pack()
decode_input.pack()
decode_count_input.pack()
decode_button.pack()
encode_result_frame.pack()
encode_result_scrollbar.pack(side='right', fill='y')
encode_result_label.pack()

root.mainloop()
