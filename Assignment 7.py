def fileHandling(file):
    print("Function of File Handling")

    file_ex = open(file,"a+")
    print("File opened successfully...")
    try:
        name=input("Enter your name :")
        rollno=input("Enter your rollno :")
        dept=input("Enter your department :")
        file_ex.writelines(rollno)
        file_ex.writelines(name)
        file_ex.writelines(dept)
        print("Writed successfully in the file")
    except IOError:
        print("IO exceptions are handled here!!")
    finally:
        print("No exception present now is present now!!")


    file_ex.seek(0)               #will point the cursor to the first index of the file!
    file_context=file_ex.readlines()
    print("File Contents:")
    print(file_context)           #will print the contents of the file!!
    print("Successfully Readed!!")

    file_ex.close()
    print("File closed successfully")

fileHandling("abc.txt")    #Calling the function by passing parameter as file name!!
