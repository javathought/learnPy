#language: fr
# -- FILE: features/example.feature
Fonctionnalité: Kaprekars Constant

  Have the function KaprekarsConstant(num) take the num parameter being passed which will be a 4-digit number with at
  least two distinct digits. Your program should perform the following routine on the number: Arrange the digits in
  descending order and in ascending order (adding zeroes to fit it to a 4-digit number), and subtract the smaller
  number from the bigger number. Then repeat the previous step. Performing this routine will always cause you to reach
  a fixed number: 6174. Then performing the routine on 6174 will always give you 6174 (7641 - 1467 = 6174). Your
  program should return the number of times this routine must be performed until 6174 is reached. For example: if
  num is 3524 your program should return 3 because of the following steps: (1) 5432 - 2345 = 3087, (2) 8730 - 0378 = 83
  52, (3) 8532 - 2358 = 6174.

  Scénario: 0 itération pour 6174
    Etant donné Le nombre 6174
    Quand on appelle la fonction KaprekarsConstant
    Alors le nombre d'itérations est 0

  Scénario: 1 itération pour 8532
    Etant donné Le nombre 8532
    Quand on appelle la fonction KaprekarsConstant
    Alors le nombre d'itérations est 1

  Scénario: 7 itérations pour 9831
    Etant donné Le nombre 9831
    Quand on appelle la fonction KaprekarsConstant
    Alors le nombre d'itérations est 7

  Scénario: 5 itérations pour 2111
    Etant donné Le nombre 2111
    Quand on appelle la fonction KaprekarsConstant
    Alors le nombre d'itérations est 5

