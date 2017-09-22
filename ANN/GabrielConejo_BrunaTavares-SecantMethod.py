    # This program is free software: you can redistribute it and/or modify
    # it under the terms of the GNU General Public License as published by
    # the Free Software Foundation, either version 3 of the License, or
    # (at your option) any later version.
    #
    # This program is distributed in the hope that it will be useful,
    # but WITHOUT ANY WARRANTY; without even the implied warranty of
    # MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    # GNU General Public License for more details.
    #
    # You should have received a copy of the GNU General Public License
    # along with this program.  If not, see <http://www.gnu.org/licenses/>.
# -------------------------------------------------------------------------------- #
# -------------------------------------------------------------------------------- #
# -------------------------------------------------------------------------------- #
# Alunos: Gabriel Guebarra Conejo                                                  #
#         Bruna Tavares Silva                                                      #
#                                                                                  #
# Prof: Helder                                                                     #
#                                                                                  #
# Curso: Bacharelado em Ciencia da Computacao                                      #
#                                                                                  #
# Materia: ANN - Analise Numerica                                                  #
# -------------------------------------------------------------------------------- #
# -------------------------------------------------------------------------------- #
# -------------------------------------------------------------------------------- #

# -*- coding: cp1252 -*-
# import numpy as np
import math as mt

# Comente a função que não irá utilizar, tire o comentário da função que irá utilizar '1 = f1' e '2 = f2'
# Atalho para comentar/descomentar mais rápido, vá até a linha a ser comentada e pressione 'ctrl+/' (Apenas alguns editores possuem essa funcao)
# funcao = 1
funcao = 2

# Funcao 5 da lista (Bruna Tavares na chamada)
def f1(x):
    return (2 ** mt.cos(x)) - (x/2)

# Funcao 11 da lista (Gabriel Conejo na chamada)
def f2(x):
    return (4*x) - (mt.sqrt(mt.e**x))


# Metodo da Secante
def secante(func, x0, xk, error):
    it = 0
    xk_me1 = x0
    aux = 0
    if funcao == 1:
        newError = abs(0-f1(xk))
        while error < newError:
            aux = xk
            xk = xk - ((xk - xk_me1)*f1(xk))/(f1(xk) - f1(xk_me1))
            xk_me1 = aux
            newError = abs(0-f1(xk))
            it += 1
    else:
        newError = abs(0-f2(xk))
        while error < newError:
            aux = xk
            xk = xk - ((xk - xk_me1)*f2(xk))/(f2(xk) - f2(xk_me1))
            xk_me1 = aux
            newError = abs(0-f2(xk))
            it += 1

    print ('Iteracoes: ', it)
    return xk

def main():
    xk = 0
    x0 = 1
    error = 1e-5
    if funcao == 1:
        xn = secante(f1, x0, xk, error)
        print ('Funcao 1: f(x) = 2^(cos(x))-x/2')
        print ('Xk resultante = ', xn)
        print ('f1(x) resultante = ', f1(xn))
            
    else:
        xn = secante(f2, x0, xk, error)
        print ('Funcao 2: f(x) = 4*x - sqrt(e^x)')
        print ('Xk resultante = ', xn)
        print ('f1(x) resultante = ', f2(xn))

if __name__ == '__main__':
    main()
