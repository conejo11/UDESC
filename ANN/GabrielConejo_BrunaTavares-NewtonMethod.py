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


# Caso queira colocar mais opcoes de funcao da pra ir colocando sem apagar as outras
funcao = 1

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

# Verificação do critério de convergência Newton
def convergeNewton(func,deriv, segDeriv, xk):
    result = -1 # -1 nao garante a convergencia; 1 garante convergencia
    if funcao == 1:
        print ('passou no 1 criterio')
        (a, b) = intervalo(f1, df1, xk)
        # primeiro criterio: f(a) * f1(b) < 0 (converge)
        if f1(a)*f1(b) <= 0 :
            print ('passou no 2 criterio')
            # segundo critério: f'(a) * f1(b) > 0   
            if df1(xk) != 0:
                # terceiro critério: f"(a) * f"(b) > 0
                print ('passou no 3 criterio')
                if ddf1(xk) > 0 or ddf1(xk) < 0:
                    if ((abs(f1(a)/df1(a)) < abs(a-b)) and (abs(f1(a)/df1(a)) < abs(a-b))) or ((f1(x0)*ddf1(xk)) >=0):
                        result = 1
                else:
                    print ('teste a: ', a, ' b: ', b, 'f(a): ', f1(a), ' f(b): ', f1(b), '\nf\'\'(a): ', ddf1(a), ' f\'\'(b): ', ddf1(b))
    return result

# Define intervalo (a, b)
def intervalo(func, deriv, xk):
    if funcao == 1:
        a = xk - f1(xk)/df1(xk)
        b = a - f1(a)/df1(a)
    if b > a:
        return (a, b)
    else:
        return (b, a)

# Metodo de Newton
def newton(func,deriv,xk,error):
    it = 0
    if funcao == 1:
        newError = abs(0-f1(xk))
        while error < newError:
            aux = xk
            xk = xk - f1(xk)/df1(xk)
            newError = abs(aux-xk)
            it += 1
            print('Iteracao = ', it)
            print('Xk = ', xk)
            print('f(Xk) = ', f1(xk))
            print('Erro = ', newError)
            print(' ')
    print(' ---------------------------------------- ')
    print(' ---------------------------------------- ')
    print('RESULTADO FINAL')
    print ('Iteracoes: ', it)
    return xk, newError

def main():
    xk = 0
    x0 = 1
    error = 1e-5
    if funcao == 1:
        #verifica criterio convergencia
        result = convergeNewton(f1, df1, ddf1, xk)
        if result == -1:
            print ('Nao atende aos criterios de convergencia\n')
            pass
        xn, erro = newton(f1,df1,xk,error)
        print ('Funcao 1: f(x) = 2^(cos(x))-x/2')
        print ('Xk resultante = ', xn)
        print ('f1(x) resultante = ', f1(xn))
        print ('Erro resultante = ', erro)
        print(' ---------------------------------------- ')
        print(' ---------------------------------------- ')

if __name__ == '__main__':
    main()
