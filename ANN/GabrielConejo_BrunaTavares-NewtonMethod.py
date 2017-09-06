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
funcao = 1
# funcao = 2

# Funcao 5 da lista (Bruna Tavares na chamada)
def f1(x):
    return (2 ** mt.cos(x)) - (x/2)

# Derivada da funcao 5 da lista (Bruna Tavares na chamada)
def df1(x):
    return (mt.log(2,10)*mt.sin(x)*(-2**mt.cos(x))) - (1/2)

# Funcao 11 da lista (Gabriel Conejo na chamada)
def f2(x):
    return (4*x) - (mt.sqrt(mt.e**x))

# Derivada da funcao 11 da lista (Gabriel Conejo na chamada)
def df2(x):
    return 4 - ((mt.sqrt(mt.e**x))/2)

# Metodo de Newton
def newton(func,deriv,xk,error):
    if funcao == 1:
        newError = abs(0-f1(xk))
        while error < newError:
            xk = xk - f1(xk)/df1(xk)
            newError = abs(0-f1(xk))
        return xk
    else:
        newError = abs(0-f1(xk))
        while error < newError:
            xk = xk - f2(xk)/df2(xk)
            newError = abs(0-f2(xk))
        return xk

def main():
    xk = 0
    error = 1e-5
    if funcao == 1:
        xn = newton(f1,df1,xk,error)
        print ('Xk resultante = ', xn)
        print ('f1(x) resultante = ', f1(xn))
    else:
        xn = newton(f2,df2,xk,error)
        print ('Xk resultante = ', xn)
        print ('f2(x) resultante = ', f2(xn))

if __name__ == '__main__':
    main()
