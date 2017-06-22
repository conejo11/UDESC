import random
import math as mt
import matplotlib.pyplot as plt
import numpy as np
import randomPop as rp
import naturalSelection as ns
import crossover as crs
import fitness as fit
import mutation as mtt
import variaveis as var
import plotPram as pp
import diversityManagement as dm
import copy

def printPopulacao(matriz, pop,d):
  for i in range(pop):
    for j in range(d):
      print (matriz[i][j], end=" ")
    print()

def newPop(matriz,pop,d):
  popula = []
  for i in range(pop):
      popula.append([matriz[i][j] for j in range(d)])
  return popula

# FUNCAO MAIN
if  __name__ =='__main__':
  initPop = rp.randomPopulation(var.cod,var.pop_size,var.d_size,var.bounds)
  objective = initPop
  offspring = []
  aux = []
  bestFit = []
  averageFit = []
  divers = []
  divers1 = 0
  worst = 0
  ce = 1.2
  inc = 0.8/var.generations

  if var.genGap:
    gGap = int((var.genGapPercent/100)*var.pop_size)
    gapMat = []

  if var.problem == 1:
    objective = fit.bitsAlternados(initPop,var.pop_size,var.d_size)
  if var.problem == 2:
    objective = fit.paresAlternados(initPop,var.pop_size,var.d_size)
  if var.problem == 3:
    objective = fit.sphere(initPop, var.pop_size, var.d_size)
  if var.problem == 4:
    objective = fit.radio(initPop, var.pop_size, var.d_size)
  if var.problem == 5:
    objective = fit.pattern(initPop, var.pop_size, var.d_size)
  if var.problem == 6:
    objective = fit.nQueens(initPop, var.pop_size, var.d_size)  
  if var.problem == 7:
    objective = fit.f3(initPop, var.pop_size, var.d_size)  
  if var.problem == 8:
    objective = fit.f3s(initPop, var.pop_size, var.d_size)


  while var.generations:
    if var.genGap:
      gapMat = dm.getGap(objective,gGap,var.pop_size,var.d_size)

    if var.share:
      dm.sharing(objective,var.pop_size,var.d_size)

    if var.elitism:
      elected = ns.elit(objective,var.pop_size,var.d_size)

    newGen = []
    while len(newGen)!= var.pop_size:
      if var.selection == 1:
        if var.linearScaling == True:
          dad = ns.selectRouletteLinearScaling(objective,var.pop_size,var.d_size,ce)
          mom = ns.selectRouletteLinearScaling(objective,var.pop_size,var.d_size,ce)
          ce += inc
        else:
          dad = ns.selectRoulette(objective,var.pop_size,var.d_size)
          mom = ns.selectRoulette(objective,var.pop_size,var.d_size)
      elif var.selection == 2:
        dad = ns.selectTournament(objective,var.pop_size,var.d_size,var.k)
        mom = ns.selectTournament(objective,var.pop_size,var.d_size,var.k)
        
      if crs.cross():
        if var.cover == 1:
          child1,child2 = crs.onePointCrossover(objective,var.pop_size,var.d_size,dad,mom)
          newGen.append(child1)
          newGen.append(child2)
        elif var.cover == 2:
          child1,child2 = crs.uniformCrossover(objective,var.pop_size,var.d_size,dad,mom)
          newGen.append(child1)
          newGen.append(child2)
        elif var.cover == 3:
          child1,child2 = crs.blxReal(objective,var.pop_size,var.d_size,dad,mom)
          newGen.append(child1)
          newGen.append(child2)
        elif var.cover == 4:
          child1,child2 = crs.uniformAverageReal(objective,var.pop_size,var.d_size,dad,mom)
          newGen.append(child1)
          newGen.append(child2)
        elif var.cover == 5:
          child1,child2 = crs.pmxPerm(objective,var.pop_size,var.d_size,dad,mom)
          newGen.append(child1)
          newGen.append(child2)

    if var.crowd:
      place = placeholder

    for i in range(var.pop_size):
      for j in range(var.d_size):
        if mtt.mut():
          if var.mutar == 1:
            newGen[i][j] = mtt.bitFlip(newGen[i][j])
          if var.mutar == 2:
            newGen[i][j] = mtt.randMutation(newGen[i][j],var.d_size)
          if var.mutar == 3:
            newGen[i][j] = mtt.deltaMutation(newGen[i][j])
          if var.mutar == 4:
            newGen[i][j] = mtt.gaussianMutation(newGen[i][j])
          if var.mutar == 5:
            aux = mtt.swapPositions(newGen,i,j,var.d_size)
            newGen = aux

    newPopu = newPop(newGen,var.pop_size,var.d_size)

    if var.genGap:
      for i in range(gGap):
        random.shuffle(newPopu)
        newPopu[i] = gapMat[i]

    if var.elitism:
      randIndex = random.randint(0,(var.d_size-1))
      newPopu[randIndex] = elected

    if var.problem == 1:
      objective = fit.bitsAlternados(newPopu,var.pop_size,var.d_size)
    if var.problem == 2:
      objective = fit.paresAlternados(newPopu,var.pop_size,var.d_size)
    if var.problem == 3:
      objective = fit.sphere(newPopu, var.pop_size, var.d_size)
    if var.problem == 4:
      objective = fit.radio(newPopu, var.pop_size, var.d_size)
    if var.problem == 5:
      objective = fit.pattern(newPopu, var.pop_size, var.d_size)
    if var.problem == 6:
      objective = fit.nQueens(newPopu, var.pop_size, var.d_size)
    if var.problem == 7:
      objective = fit.f3(newPopu, var.pop_size, var.d_size)    
    if var.problem == 8:
      objective = fit.f3s(newPopu, var.pop_size, var.d_size)

    bestFit.append(pp.getBest(objective,var.pop_size,var.d_size))
    averageFit.append(pp.averageInd(objective,var.pop_size,var.d_size))
    if type(var.cod) is not float:
      divers.append(pp.diversityHam(objective,var.pop_size,var.d_size))
    else:
      divers.append(pp.diversityMeasure(objective,var.pop_size,var.d_size))
    var.generations -= 1

  best = pp.bestInd(objective,var.pop_size,var.d_size)
  plt.plot(bestFit,label = 'Best')
  plt.plot(averageFit, label = 'Average')
  plt.legend()
  plt.ylabel('Fitness')
  plt.xlabel('Generations')
  plt.savefig("best_average.png")

  plt.clf()
  plt.plot(divers,label = 'Diversity')
  plt.legend()
  plt.ylabel('Diversity')
  plt.xlabel('Generations')
  plt.savefig("diversity.png")

  print(best)
