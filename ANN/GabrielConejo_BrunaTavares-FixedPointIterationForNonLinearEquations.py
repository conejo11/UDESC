
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

import math as mt

def f1(x,y):
    return (mt.sin(x-y) - y)/8

def f2(x,y):
    return (x - mt.cos(x*y))/8

def ptoFixo(f1,f2,x,y,xk,yk,erro):
    it = 0
    print('Iteracao = ', it)
    print('X1k = ', x)
    print('X2k = ', y)
    print('f(X1k,X2k) = ', f1(x,y))
    print(' ')
    xk = f1(x,y)
    yk = f2(x,y)
    newErro = max(abs(xk-x),abs(yk-y))/max(abs(xk),abs(yk))
    print('Iteracao = ', it+1)
    print('X1k = ', xk)
    print('X2k = ', yk)
    print('f(X1k,X2k) = ', f1(xk,yk))
    print('Erro = ', newErro)
    print(' ')
    while newErro > erro:
        aux1 = xk
        aux2 = yk
        xk = f1(xk,yk)
        yk = f2(xk,yk)
        newErro = max(abs(xk-aux1),abs(yk-aux2))/max(abs(xk),abs(yk))
        it += 1
        print('Iteracao = ', it+1)
        print('X1k = ', xk)
        print('X2k = ', yk)
        print('f(X1k,X2k) = ', f1(xk,yk))
        print('Erro = ', newErro)
        print(' ')
    return xk, yk, newErro, it

if __name__ == '__main__':
    erro = 0.000001
    x0 = 1
    y0 = 1
    xk = 0
    yk = 0

    xn,yn,erroFin, it = ptoFixo(f1,f2,x0,y0,xk,yk,erro)
    print(' ')
    print(' ---------------------------------------- ')
    print(' ---------------------------------------- ')
    print ('X1k resultante = ', xn)
    print ('X2k resultante = ', yn)
    print ('f1(x1,x2) resultante = ', f1(xn,yn))
    print ('f2(x1,x2) resultante = ', f2(xn,yn))
    print ('Erro resultante = ', erroFin)
    print ('Iteracoes = ', it+1)
    print(' ---------------------------------------- ')
    print(' ---------------------------------------- ')
