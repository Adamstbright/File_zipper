import PySimpleGUI as sg
from zip_creator import make_archive


sg.theme("DarkBlack1")

label1 = sg.Text("Select file to compress:")
input1 = sg.InputText(tooltip="Enter file")
Choose_button1 = sg.FilesBrowse("Choose", key='files')

label2 = sg.Text("Select destination folder:")
input2 = sg.InputText(tooltip="Enter Zip file name")
Choose_button2 = sg.FolderBrowse("Choose", key='folder')
Compress_button = sg.Button("Compress")
output_label = sg.Text(key='output', text_color='blue')

window = sg.Window("File Zipper", layout=[[label1, input1, Choose_button1],
                                          [label2, input2, Choose_button2],
                                          [Compress_button, output_label]])

while True:
    try:
        event, values = window.read()
        print(event, values)
        filepath = values['files'].split(';')
        folder = values['folder']
        make_archive(filepath, folder)
        window['output'].update(value="Compression Completed")
    except TypeError:
        break


window.close()
