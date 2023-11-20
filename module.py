import random
import PySimpleGUI as sg

def guess_the_number():
    secret_number = random.randint(1, 100)
    attempts = 0

    layout = [
        [sg.Text("Welcome to the Guess the Number game!", size=(30, 1))],
        [sg.Text("I'm thinking of a number between 1 and 100.")],
        [sg.Text("Take a guess:"), sg.InputText(key='-GUESS-')],
        [sg.Button('Guess'), sg.Button('Exit')],
        [sg.Text(size=(40, 1), key='-OUTPUT-')]
    ]

    window = sg.Window('Guess the Number', layout, element_justification='c')

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED or event == 'Exit':
            break

        if event == 'Guess':
            try:
                guess = int(values['-GUESS-'])
            except ValueError:
                window['-OUTPUT-'].update('Invalid input. Please enter a number.')
                continue

            attempts += 1

            if guess < secret_number:
                window['-OUTPUT-'].update('Too low. Try again.')
            elif guess > secret_number:
                window['-OUTPUT-'].update('Too high. Try again.')
            else:
                window['-OUTPUT-'].update(f"Congratulations! You guessed the number in {attempts} attempts.")
                break

    window.close()
