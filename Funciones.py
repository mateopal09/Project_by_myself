"""
Author: Mateo Palomá Quila
8 de septiembre 2022

"""

class operaciones: #I created a class called operaciones is where I saved all the program 
    """
    The function saludo does all the presentation of the programm
    the variable name saved the name of the user
    if the user wants to do an mathematic operation they'll say yes
    and the function saludo called the function number_register
    if the answer is no, the programm finishes and exit  
    """
    def saludo(self):
        print("Bienvenido, ¿Cuál es tú nombre? ")
        nombre = input()
        print("Hola", nombre)
        print("Vas a hacer una operación? ")
        print("Responde Si o No ")
        answer1 = input()
        if answer1 == "Si" or answer1 == "si":
            self.number_register()
        else:
            print("Adiós")
            exit()
    """
    The function menu displayed the principal menu to the user, and they can
    choose one of the option:
    -Variable option saves the number that user will choose
    if option is equal to 1, it will call suma function
    if option is equal to 2, it will call resta function
    if option is equal to 3, it will call multiplicacion function
    if option is equal to 4, it will call dividir function
    if option is equal to 5 or another number, the programm will finish
    """
    def menu(self):
        print("Ahora vas a escoger que deseas hacer, nuestro menú es el siguiente:")

        menu = [
        ['Menú de opciones'],
        ['1. Suma'],
        ['2. Resta'],
        ['3. Multiplicación'],
        ['4. División'],
        ['5. Salir']
        ]


        for value in range(6):#this will display the menu above in order 
            print(menu[value][0])

        option = int(input("Escoger la opción que usarás: "))

        if option == 1:
            self.suma()
        elif option == 2:
            self.resta()
        elif option ==3:
            self.multiplicacion()
        elif option == 4:
            self.dividir()
        else:
            print("Gracias por utilizarme, bye...")
            exit()
        self.menu()
        """
        As soon as the user chooses an option, 
        the operation will be made and it returns to menu for continuing and displaying 
        others operations, so the user can see another results 

        """

        
    """
    The function number_register saved the numbers
    that the user wants to use in the program
    self.numero1 and self.numero2 are information from user, it'll be the numbers to use in the ma
    mathematics operations 

    Then it will be divided in the maximum and minimum of the numbers typed for the user
    and return those numbers  
    """
    def number_register(self):
        print("Hola, necesitamos registrar el primer número")
        self.numero1 = int (input("Digite el primer valor: "))
        print("Ahora el segundo número ")
        self.numero2 = int(input("Digite el segundo valor:  "))

        if self.numero1 > self.numero2:
            self.maxnumero = self.numero1
            self.minnumero = self.numero2
        else:
            self.maxnumero = self.numero2
            self.minnumero = self.numero1

            return self.maxnumero,self.minnumero

    #addition of numbers
    def suma(self):
        sumares = self.maxnumero + self.minnumero
        print("La suma de ", self.maxnumero ,"y",self.minnumero,"es ", sumares )

    #Substraction of numbers
    def resta(self):
        restanumbers = self.maxnumero-self.minnumero
        print("La resta de ", self.maxnumero, "y", self.minnumero, "es:" , restanumbers)

    #Multiplication of numbers
    def multiplicacion (self):
        multi = self.minnumero * self.maxnumero
        print("La multiplicación de ", self.minnumero, "pr", self.maxnumero, "es:" , multi)

    #Division of numbers
    def dividir(self):
        divi = self.minnumero / self.maxnumero
        print("La división de ", self.minnumero, "y", self.maxnumero, "es:" , divi)





