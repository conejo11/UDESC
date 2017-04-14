import random
import math as mt
import randomPop as rp
import naturalSelection as ns
import crossover as crs
import fitness as fit
import mutation as mtt
import variaveis as var

def printPopulacao(matriz, pop,d):
  for i in range(pop):
    for j in range(d):
      print (matriz[i][j], end=" ")
    print()

# FUNCAO MAIN
def main():
  initPop = rp.randomPopulation(var.cod,var.pop_size,var.d_size,var.bounds)

  objective = initPop
  offspring = []
  aux = []
  while var.generations:
    if var.problem == 1:
      objective = fit.bitsAlternados(initPop,var.pop_size,var.d_size)
    if var.problem == 2:
      objective = fit.paresAlternados(initPop,var.pop_size,var.d_size)
    if var.problem == 3:
      objective = fit.maxFuncAlg(initPop, var.pop_size, var.d_size)
    

    if var.selection == 1:
      dad = ns.selectRoulette(objective,var.pop_size,var.d_size)
      mom = ns.selectRoulette(objective,var.pop_size,var.d_size)
    elif var.selection == 2:
      dad = ns.selectTournament(objective,var.pop_size,var.d_size,var.k)
      mom = ns.selectTournament(objective,var.pop_size,var.d_size,var.k)

    if crs.cross():
      if var.cover == 1:
        offspring = crs.onePointCrossover(objective,var.pop_size,var.d_size,dad,mom)
      elif var.cover == 2:
        offspring = crs.uniformCrossover(objective,var.pop_size,var.d_size,dad,mom)
      elif var.cover == 3:
        offspring = crs.blxReal(objective,var.pop_size,var.d_size,dad,mom)
      elif var.cover == 4:
        offspring = crs.uniformAverageReal(objective,var.pop_size,var.d_size,dad,mom)
      # elif cover == 5:
      #   offspring = 

    for i in range(var.pop_size):
      for j in range(var.d_size-1):
        if mtt.mut():
          if var.mutar == 1:
            offspring[i][j] = mtt.bitFlip(offspring[i][j])
            objective = offspring
          if var.mutar == 2:
            offspring[i][j] = mtt.randMutation(offspring[i][j],var.d_size)
            objective = offspring
          if var.mutar == 3:
            offspring[i][j] = mtt.deltaMutation(offspring[i][j])
            objective = offspring
          if var.mutar == 4:
            offspring[i][j] = mtt.gaussianMutation(offspring[i][j])
            objective = offspring
          if var.mutar == 5:
            aux = mtt.swapPositions(offspring,i,j,var.d_size)
            objective = aux

    var.generations -= 1
  fit.printPopulacaoEFitness(objective,var.pop_size,var.d_size)

main()
