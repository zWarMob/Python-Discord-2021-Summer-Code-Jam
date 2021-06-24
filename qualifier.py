import json
import math

def rotate_90_degree_clckwise_by_zip_method(matrix):
    return list(list(x)[::-1] for x in zip(*matrix))

line_break_symbols = [
    ["┌","┬","┐\n"],
    ["├","┼","┤\n"],
    ["└","┴","┘\n"],
]

def make_table_line_break(rowSpace, lbs_index):
    line_break = line_break_symbols[lbs_index][0]

    first = True
    for space in rowSpace:
        if(not first):
            line_break += line_break_symbols[lbs_index][1]
        else:
            first = False
        line_break += "─" * space
    line_break += line_break_symbols[lbs_index][2]
    
    return line_break

def make_table_row(rowSpace, rowData, centered):
    row = "│" 
    index = 0
    for item in rowData:
        row += " "
        spacing = rowSpace[index] -2 -len(item)
        if(not centered):
            row += item + spacing * " "
        else:
            row += " " * math.floor(spacing/2) + item + " " * math.ceil(spacing/2)
        
        row += " │"
        index += 1
    row += "\n"
    return row


def make_table(rows, labels = None, centered = False):
    hasLabels = False
    if(labels!=None):
        rows.insert(0,labels)
        hasLabels = True

    rows = [[str(r) for r in row] for row in rows]
    modRows = rotate_90_degree_clckwise_by_zip_method(rows)
    rowSpace = list(map(lambda row: len(max(row, key=len))+2, modRows))
    
    table = make_table_line_break(rowSpace, 0)

    first = True
    for row in rows:
        if(first and hasLabels):
            table += make_table_row(rowSpace,row, centered)
            table += make_table_line_break(rowSpace, 1)
            first = False
        else:
            table += make_table_row(rowSpace,row, centered)

    table += make_table_line_break(rowSpace, 2)

    return table