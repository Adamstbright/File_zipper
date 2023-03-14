import PySimpleGUI as sg

sg.theme("DarkBlack1")

label1 = sg.Text("Select file to compress:")
input1 = sg.InputText(tooltip="Enter file")
Choose_button1 = sg.FilesBrowse("Choose")

label2 = sg.Text("Select destination folder:")
input2 = sg.InputText(tooltip="Enter Zip file name")
Choose_button2 = sg.FolderBrowse("Choose")

Compress_button = sg.Button("Compress")

window = sg.Window("File Zipper", layout=[[label1, input1, Choose_button1],
                                          [label2, input2, Choose_button2],
                                          [Compress_button]])

window.read()
window.close()
