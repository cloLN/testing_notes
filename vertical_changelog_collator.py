import pandas as pd

file1 = open('C:\\Testing\\ScriptForChangelogs\\community_9.2.102-1_fulllog.html')
file1_contents = file1.readlines()[6:]
file1.close()

file2 = open('C:\\Testing\\ScriptForChangelogs\\community_9.4.76-1_fulllog.html')
file2_contents = file2.readlines()[6:]
file2.close()

file3 = open('C:\\Testing\\ScriptForChangelogs\\community_9.6.28-1_fulllog.html')
file3_contents = file3.readlines()[6:]
file3.close()   


#print(file1_contents)


def remove_items_from_list(existing_list, items_to_remove):
    new_list = [item for item in existing_list if item not in items_to_remove]
    return new_list
cleanedlist2 = remove_items_from_list(file2_contents, file1_contents)

cleanedlist3a = remove_items_from_list(file3_contents, file1_contents)
cleanedlist3b = remove_items_from_list(cleanedlist3a, cleanedlist2)



#table formatting
table_html_open = "<style> table {border-collapse: collapse;  th, td {border: 1px solid black; font-family: 'Calibri', Helvetica, Arial, sans-serif; padding: 10px;text-align: left;vertical-align: top} </style><table>\n"

table_html_open += "<tr><td><th>Changelogs</th></tr>\n"
table_html_open += "<tr><th>9.6.26-1</th></td><td>"
table_html_middle1 = "</tr><tr><th>9.4.74-1</th><td>"
table_html_middle2 = "</tr><tr><th>9.2.100-1</th><td>"
table_html_close = "</td></td></tr></table>"


# Print or save the HTML table
#print(table_html_open )
# Save the HTML table to a file
n_file1 = ["{}<br>".format(i) for i in file1_contents]
n_file2 = ["{}<br>".format(j) for j in cleanedlist2]
n_file3 = ["{}<br>".format(k) for k in cleanedlist3b]
open('C:\\Testing\\ScriptForChangelogs\\verticaltable.html', 'w').close()
with open('C:\\Testing\\ScriptForChangelogs\\verticaltable.html', 'w') as file:
    file.write(table_html_open)
    file.writelines(n_file3)
    file.write(table_html_middle1)  
    file.writelines(n_file2)
    file.write(table_html_middle2)
    file.writelines(n_file1)
    file.write(table_html_close)

file.close()   