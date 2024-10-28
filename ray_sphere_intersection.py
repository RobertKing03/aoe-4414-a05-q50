# ray_sphere_intersection.py
#
# Usage: python3 ray_sphere_intersection.py d_l_x d_l_y d_l_z c_l_x c_l_y c_l_z c_s_x c_s_y c_s_z r_s
#
# Input:
#  d_l_x: x coordinate of origin referecned ray unt vector
#  d_l_y: y coordinate of origin referecned ray unt vector
#  d_l_z: z coordinate of origin referecned ray unt vector
#  c_l_x: x coordinate of the ray origin offset
#  c_l_y: y coordinate of the ray origin offset
#  c_l_z: z coordinate of the ray origin offset
#  c_s_x: x coordinate of the sphere offset origin
#  c_s_y: y coordinate of the sphere offset origin
#  c_s_z: z coordinate of the sphere offset origin
#  r_s: radius of the sphere
# Output:
#  Prints the x, y, and z coordinates of the intersection (if it exists)
#
# Written by Robert King
# Other contributors: None
#
# Optional license statement, e.g., See the LICENSE file for the license.

# import Python modules
import math # math module
import sys # argv

# helper functions

## vector magnitude
def mag(v):
  sum_of_squares = 0.0
  for i  in range(0,len(v)):
    sum_of_squares += v[i]**2
  return math.sqrt(sum_of_squares)

## scalar multiplication
def smul(s,v):
  return [s*e for e in v]

## vector addition
def add(v1,v2):
  if len(v1)!=len(v2):
    return None
  else:
    v3 = []
    for i in range(0,len(v1)):
        v3.append(v1[i]+v2[i])
  return v3

## vector subtraction
def sub(v1,v2):
  if len(v1)!=len(v2):
    return None
  else:
    v3 = []
    for i in range(0,len(v1)):
      v3.append(v1[i]-v2[i])
    return v3

## dot product
def dot(v1,v2):
  if len(v1)!=len(v2):
    return float('nan')
  else:
    dp = 0.0
    for i in range(0,len(v1)):
      dp += v1[i]*v2[i]
    return dp

if len(sys.argv)==7:
    d_l_x= float(sys.argv[1]) # x coordinate of origin referecned ray unt vector
    d_l_y= float(sys.argv[2]) # y coordinate of origin referecned ray unt vector
    d_l_z= float(sys.argv[3]) # z coordinate of origin referecned ray unt vector
    c_l_x= float(sys.argv[4]) # x coordinate of the ray origin offset
    c_l_y= float(sys.argv[5]) # y coordinate of the ray origin offset
    c_l_z= float(sys.argv[6]) # z coordinate of the ray origin offset
else:
    print(
    'Usage: '\
    'python3 ray_sphere_intersection.py d_l_x d_l_y d_l_z c_l_x c_l_y c_l_z c_s_x c_s_y c_s_z r_s'\
   )
exit()

## setup vectors
d_l = [d_l_x, d_l_y, d_l_z]
c_l = [c_l_x, c_l_y, c_l_z]
c_s = [0.0,0.0,0.0]
r_s = 6378.105

## discriminant
cl_m_cs = sub(c_l,c_s)
a = dot(d_l,d_l)
b = 2.0*dot(d_l,cl_m_cs)
c = dot(cl_m_cs,cl_m_cs)-r_s
discr = b*b-4.0*a*c

## solution
if discr>=0.0:
  d = (-b-math.sqrt(discr))/(2*a)
  if d<0.0:
    d = (-b+math.sqrt(discr))/(2*a)
  if d>=0.0:
    l_d = add(smul(d,d_l),c_l)
  print(l_d[0])
  print(l_d[1])
  print(l_d[2])