import argparse
from scipy import misc

max_iter = 10000

def f(x):
  return eval(args.function)

def newton_method(x0, epsilon, step, max_iter):   
    x = x0
    for i in range(max_iter):
        x0 = x - f(x) / misc.derivative(f, x) * step
        if abs(x0 - x) < epsilon:
            return x0
        x = x0
    return None
  

parser = argparse.ArgumentParser(description='Newton\'s method for finding roots of a function.')
parser.add_argument('-function', type=str, required=True, help='Function to find roots of')
parser.add_argument('-start', type=int, required=False, help='Starting point')
parser.add_argument('-step', type=float, required=False, help='Step size')
parser.add_argument('-max_iter', type=int, required=False, help='Number of iterations')
parser.add_argument('-eps', type=float, required=False, help='Epsilon')
args = parser.parse_args()

x = 1
if args.start:
  x = args.start

step = 0.6
if args.step:
  step= args.step

max_iter = 100
if args.max_iter:
  max_iter = args.max_iter

epsilon = 0.0001
if args.eps:
  epsilon = args.eps

print(newton_method(x, epsilon, step, max_iter))