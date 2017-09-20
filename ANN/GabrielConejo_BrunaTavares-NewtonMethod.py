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

# Segunda Derivada da funcao 5 da lista (Bruna Tavares na chamada)
def ddf1(x):
    return (mt.log(2,10)*(2 ** mt.cos(x))*(mt.log(2,10)*mt.sin(x)**2 - mt.cos(x)))

# onde df1 = 0
def anulaDf1():
    return (1.75797380969997)

# Funcao 11 da lista (Gabriel Conejo na chamada)
def f2(x):
    return (4*x) - (mt.sqrt(mt.e**x))

# Derivada da funcao 11 da lista (Gabriel Conejo na chamada)
def df2(x):
    return 4 - ((mt.sqrt(mt.e**x))/2)

# onde df2 = 0
def anulaDf2():
    return ((mt.e**(x**2))/8)

# Segunda Derivada da funcao 11 da lista (Gabriel Conejo na chamada)
def ddf2(x):
    return - ((mt.sqrt(mt.e**x))/8)

# Verificação do critério de convergência Newton
def convergeNewton(func,deriv, segDeriv, xk):
    ncvg = -1 # nao garante a convergencia
    if funcao == 1:
        (a, b) = intervalo(f1, df1, xk)
        # primeiro criterio: raiz de f no intervalo [a, b]
        if f1(a)*f1(b) > 0 :
            print ('parou no 1 criterio')
            return ncvg
        # segundo critério: f'(x) != 0 | x E [a, b]
        if anulaDf1() == a:
            print ('parou no 2 criterio')
            return ncvg
        if anulaDf1() == b:
            print ('parou no 2b criterio')
            return ncvg
        if anulaDf1() > a:
            print ('parou no 2c criterio')
            return ncvg
        if anulaDf1() < b:
            print ('parou no 2d criterio')
            return ncvg
        # terceiro critério: f"(a) * f"(b) > 0
        if ddf1(a)*ddf1(b) == 0:
            print ('parou no 3a criterio')
            return ncvg
        if ddf1(a)*ddf1(b) > 0:
            print ('parou no 3b criterio')
            return ncvg
        # quarto critério: x0 é a ou b | f(x0)*f"(x0) > 0

        if func(a)*ddf1(a) > 0:
            return a
        else:
            if func(b)*ddf1(b) > 0:
                return b
            else:
                print ('parou no 4 criterio func(b): ', func(b), ' ddf1(b): ', ddf1(b))
                return ncvg
# fazer as mesmas coisas para a funcao b, só trocando td pelos respectivos da f2

# Define intervalo (a, b)
def intervalo(func, deriv, xk):
    if funcao == 1:
        a = xk - f1(xk)/df1(xk)
        b = a - f1(a)/df1(a)
    else:
        a = xk - f2(xk)/df1(xk)
        b = a - f2(a)/df1(a)
    if b > a:
        return (a, b)
    else:
        return (a, b)

# Metodo de Newton
def newton(func,deriv,xk,error):
    it = 0
    if funcao == 1:
        newError = abs(0-f1(xk))
        while error < newError:
            xk = xk - f1(xk)/df1(xk)
            newError = abs(0-f1(xk))
            it += 1
        print ('Iteracoes: ', it)
        return xk
    else:
        newError = abs(0-f1(xk))
        while error < newError:
            xk = xk - f2(xk)/df2(xk)
            newError = abs(0-f2(xk))
            it += 1
        print ('Iteracoes: ', it)
        return xk

def main():
    xk = 0
    error = 1e-5
    if funcao == 1:
        #verifica criterio convergencia
        result = convergeNewton(f1, df1, ddf1, xk)
        if result == -1:
            print ('Nao atende aos criterios de convergencia')
        else:
            xn = newton(f1,df1,xk,error)
            print ('Xk resultante = ', xn)
            print ('f1(x) resultante = ', f1(xn))
    else:
        xn = newton(f2,df2,xk,error)
        print ('Xk resultante = ', xn)
        print ('f2(x) resultante = ', f2(xn))

if __name__ == '__main__':
    main()
