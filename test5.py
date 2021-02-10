def UnCommonWords(A, B): 
    un_comm = [i for i in "".join(B).split() if i not in "".join(A).split()] 
    return un_comm 

def CommonWords(A, B): 
    comm = [i for i in "".join(B).split() if i in "".join(A).split()] 
    return comm 

#Driver code 
A1 = "Python para todos" 
B1 = "Aprendiendo Python para todos en la web"
print("Common words:", CommonWords(A1, B1)) 
print("Un common words: ", UnCommonWords(A1, B1)) 

A2 = "Londres" 
B2 = "Juegos olimpicos en Londres"
print("Common words:", CommonWords(A2, B2)) 
print("Un common words: ", UnCommonWords(A2, B2))  

A3 = "Java" 
B3 = "Test of script"
print("Common words:", CommonWords(A3, B3)) 
print("Un common words: ", UnCommonWords(A3, B3)) 