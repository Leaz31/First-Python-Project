Créer un notebook : `intro-python-exercies.ipynb`

# Exercice - Somme

Créer une fonction sum qui prend deux paramètres et retourne leur somme.

Exemple :

- sum(1,8) => 9

# Exercice - Somme de liste

Créer une fonction sum_list qui prend en paramètre une liste et qui renvoit la somme de ses éléments.

Exemple :

- sum_list([1, 3, 8]) => 12

# Exercice - is_string

Créer une fonction is_string qui prend un paramètre et qui renvoit un booléan disant si c'est une chaîne de caractères.

Exemple :

- is_string(3) => False
- is_string("Salut toi") => True
- is_string(None) => False

# Exercice - has_string

Créer une fonction has_string qui prend un paramètre une liste et qui renvoit True si au moins un élément est de type string, sinon False.

Exemple :

- has_string([1, 3]) => False
- has_string([1, "Salut"]) => True

# Exercice - has_only_string

Créer une fonction has_only_string qui prend un paramètre une liste et qui renvoit True si tous les éléments sont des chaînes de caractères, sinon False.

Exemple :

- has_only_string([1, "Salut"]) => False
- has_only_string(["Bonjour", "Salut"]) => True

# Exercice - FizzBuzz

- Créer une fonction fizzbuzz. Elle prend un paramètre : number.
- Si ce paramètre est un multiple de 3, la fonction renvoie "Fizz".
- Si ce paramètre est un multiple de 5, la fonction renvoie "Buzz".
- Si ce paramètre est un multiple de 3 et un multiple de 5, la fonction renvoie "FizzBuzz".
- Sinon, elle renvoit le paramètre.

Exemple :

- fizzbuzz(1) => 1
- fizzbuzz(2) => 2
- fizzbuzz(3) => "Fizz"
- fizzbuzz(5) => "Buzz"
- fizzbuzz(6) => "Fizz"
- fizzbuzz(15) => "FizzBuzz"
- fizzbuzz(20) => "Buzz"
- fizzbuzz(22) => 22

# Exercice - POO

## Part 1

- Créer une classe Car dans le fichier Car.py
- Ajouter les attributs : color, nb_wheels, brand, position
- Dans le constructeur, mettre les valeurs par défaut : "black", 4, "Tesla", 0
- Ajouter tous les setters et tous les getters
- Ajouter la méthode `move` qui ajoute 1 à la position

## Part 2

- Dans un fichier main.py
- Instancier deux objets Car
- Modifier la seconde pour qu'elle soit "yellow", de marque "Ford"
- Faites bouger la 2nde pour qu'elle soit en position 4

# Exercice - Calculette

- Add a class Calculator (calculator.py)
- Its constructor take one argument 'base_nb'
- Add these methods :
  - add(nb)
  - subtract(nb)
  - multiply(nb)
  - divide(nb)
    - throws an error if nb = 0
  - power(nb, power)
  - isMultipleOf(nb)
  - isInList(list)
  - getResult()
  - reset()
  - getQuotientAndRemainderBy(nb)
  - getInferiorIntegers()

Your code must work as follows:

```
myCalc = new Calculator(10)
myCalc.getResult() # => 10

myCalc.add(3)
myCalc.getResult() # => 13

myCalc.multiply(2)
myCalc.getResult() # => 26

myCalc.subtract(6)
myCalc.getResult() # => 20

myCalc.reset()
myCalc.getResult() # => 0

myCalc.add(10)
myCalc.getResult() # => 10

myCalc.isMultipleOf(3) # => False
myCalc.isMultipleOf(5) # => True

myCalc.power(2)
myCalc.getResult() # => 100

myCalc.divide(2)
myCalc.getResult() # => 50

myCalc.isInList([1, 2, 3]) # => False
myCalc.isInList([1, 2, 50]) # => True

myCalc.getQuotientAndRemainderBy(5) # => (10, 0)
myCalc.getQuotientAndRemainderBy(4) # => (12, 2)
myCalc.getQuotientAndRemainderBy(11) # => (4, 6)

myCalc.reset(7)
myCalc.getResult() # => 7
myCalc.getInferiorIntegers() # => [1, 2, 3, 4, 5, 6]

```

# Contraintes
