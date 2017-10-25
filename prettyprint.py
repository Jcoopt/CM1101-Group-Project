"""to do:
normalise inventory lists
        -split on space first and then normalise
normalise task lists
"""

to_reduce="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam volutpat pellentesque lorem, at dictum nunc" \
          " tincidunt sit amet. Duis gravida velit vestibulum tincidunt hendrerit. Pellentesque habitant morbi " \
          "tristique senectus"

ui_template="""
_______________ ___________________________________  _____________________\n
|   Inventory   |                                     |       Tasks       |\n
|               |                                     |                   |\n
| 1234567890123 | 12345678901234567890123456789012345 |                   |\n
|               |                                     |                   |\n
|               |                                     |                   |\n
|               |                                     |                   |\n
|               |                                     |                   |\n
|               |                                     |                   |\n
|               |                                     |                   |\n
|               |                                     |                   |\n
|               |                                     |                   |\n
|               |                                     |                   |\n
|               |                                     |                   |\n
|               |                                     |                   |\n
|               |                                     |                   |\n
|               |                                     |                   |\n
|               |                                     |                   |\n
|               |                                     |                   |\n
|               |                                     |                   |\n
-----------------------------------------------------------------------\n
               >
"""
#print(string)

print_buffer=[]

def reduce_text(input_text):
    """takes a string (a long one in normally use, and reduces it down for use with the UI, i.e 35 characters"""
    reduced_string=""
    ch_pos=1
    for ch in input_text:
        if ch_pos%34==0:
            reduced_string = "{0}{1}".format(reduced_string, "\n")
        reduced_string="{0}{1}".format(reduced_string,ch)
        ch_pos+=1

    return reduced_string
def reduce_to_lines(reduced_text):
    """takes a string that has been reduced down to fit on screen, and splits it line by line to a list"""
    text_line=reduced_text.split("\n")
    return text_line



inv= ["Id","credit Card","lunch", "a stupidly long string that wil, not fit"]
task_list=["steal manager credit card","disable cameras","give lunch coupon"]

def create_slice_point(text,position):
    """takes a string that does not fit on screen and puts 'n\' where a newline is needed, as indicated by position
     . This can then be used to splice the string into line by line lists"""

    pos=1
    slice_ready_text=""
    for ch in text:
        if pos%(position-1)==0:
            if ch ==" ":
                slice_ready_text = "{0}\n".format(slice_ready_text)
            else:
                slice_ready_text="{0}\n".format(slice_ready_text)
        slice_ready_text = "{0}{1}".format(slice_ready_text,ch)
        pos+=1
    return slice_ready_text

def reduce_inv(inv):
    """takes an inventory list and reduces it to fit in the box"""

    reduced_inv_list=[]
    for item in inv:
        slice_ready=create_slice_point(item,13)
        reduced_inv_list.append(slice_ready.split("\n"))
        reduced_inv_list.append("             ")
    return reduced_inv_list

def pad_inv(inv_item):
    front_pad=((13-len(inv_item))//2)
    back_pad= (13-front_pad-len(inv_item))
    return "{0}{1}{2}".format(" "*front_pad,inv_item," "*back_pad)

def pad_output(ui_text_lis):
    pass

def print_UI(inv_text_list,ui_text_list,task_text_list):
    print("____________________________________________________________________________________")
    print("|   Inventory   |                                     |            Tasks            |")
    print("|               |                                     |                             |")

    for line_pos in range(0,len(ui_text_list)):
        if line_pos < len(inv_text_list)*2:
            if line_pos<len(task_list)*2:

                line="| {0} | {1} |{2}|".format(pad_inv(inv_text_list[line_pos]),ui_text_list[line_pos],task_text_list[line_pos])
            else:
                line = "|{0}| {1} |                           |".format(inv_text_list[line_pos], ui_text_list[line_pos])
        elif line_pos<len(task_list)*2:
            line = "|             | {0} | {1} |".format(ui_text_list[line_pos], task_text_list[line_pos])

        elif line_pos<len(ui_text_list):
            line = "|             | {0} |                           |".format(ui_text_list[line_pos],
                                                                              ui_text_list[line_pos])
        else:
            line= "--------------------------------------------------"
        print(line)


def text_into_box(text):
    pass

print(reduce_inv(inv))


#print(reduce_to_lines(reduce_text(to_reduce)))
#print(print_UI(reduce_to_lines(ui_template)))
print_UI(inv,reduce_to_lines(create_slice_point(to_reduce,35)),task_list)
