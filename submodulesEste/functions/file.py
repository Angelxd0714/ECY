import os



def create_directory():
    """
    crea el directorio de uploads si no existe
    :return: 
    
    """
    dictory="uploads"
    if not os.path.exists(dictory):
        os.makedirs(dictory)    
    else:
        print("ya existe")


# def file_pass_save(password)->str:
#     name_file="pass.txt"

#     with open(name_file,'w') as file:
#             file.write(password)

# def file_pass_read()->str:
#     name_file="pass.txt"
#     if os.path.exists(name_file):
#         with open(name_file,'r') as file:
#             mode=file.read()
#         return mode
#     else:
#         return "0"

