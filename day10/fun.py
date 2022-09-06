#functions with outputs

def format_name(f_name,l_name):
    # name=f_name + " "+l_name
    # name.title()
    if f_name =="" or l_name=="":
        return "You didn't provide valid inputs."
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()

    return f"{formated_f_name}  {formated_l_name}"
    

formated_string = format_name(input("what is your first name?"),input("what is your last name"))
print(formated_string)