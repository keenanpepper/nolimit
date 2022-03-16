#!/usr/bin/env python3

from math import log, sqrt

def isprime(n):
  if n < 2: return False
  for d in range(2, int(sqrt(n)+1)):
    if n % d == 0: return False
  return True

def primesupto(n):
  for i in range(n+1):
    if isprime(i): yield i

def firstnprimes(n):
  yielded = 0
  i = 0
  while yielded < n:
    i += 1
    if isprime(i):
      yield i
      yielded += 1

def gpv(stepsperoct, maxprime):
  return [round(stepsperoct * log(p,2)) for p in primesupto(maxprime)]

def top(val):
  dim = len(val)
  primes = list(firstnprimes(dim))
  v = [val[i]/log(primes[i]) for i in range(dim)]
  index_min = min(range(len(v)), key=v.__getitem__)
  index_max = max(range(len(v)), key=v.__getitem__)
  p1 = primes[index_min]
  s1 = val[index_min]
  p2 = primes[index_max]
  s2 = val[index_max]
  edo = (s1 * log(p2,2) + s2 * log(p1,2)) / (2 * log(p1,2) * log(p2,2))
  damage = abs((s1 / edo) / log(p1,2) - 1)
  return (edo, damage, index_min)

def fixedpoint(v):
  vlast = None
  while v != vlast:
    vlast = v
    edo, damage, index_min = top(v)
    pmax = min(1000, int(2 ** (0.5/(damage*edo)) + 2)) # hackery
    print('EDO', edo, 'damage', damage, 'index_min', index_min, 'pmax', pmax)
    v = gpv(edo, pmax)
  return edo, v, index_min

def nolimit():
  v = [1,1]
  while True:
    edo, v, index_min = fixedpoint(v)
    yield (edo, v)
    v[index_min] += 1
