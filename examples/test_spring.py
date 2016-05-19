# -*- coding: utf-8 -*-
# ***********************************
#  Author: Pedro Jorge De Los Santos     
#  E-mail: delossantosmfq@gmail.com 
#  Web: labdls.blogspot.mx
#  License: MIT License
# ***********************************
import sys
sys.path.insert(0,'../') # Insert parent folder

from nusa.core import *
from nusa.model import *
from nusa.element import *

def test1():
    """
    Logan, D. (2007). A first course in the finite element analysis.
    Example 2.1, pp. 42.
    """
    P = 5000.0
    # Model
    m1 = SpringModel("2D Model")
    # Nodes
    n1 = Node((0,0))
    n2 = Node((0,0))
    n3 = Node((0,0))
    n4 = Node((0,0))
    # Elements
    e1 = Spring((n1,n3),1000.0)
    e2 = Spring((n3,n4),2000.0)
    e3 = Spring((n4,n2),3000.0)

    # Add elements 
    for nd in (n1,n2,n3,n4):
        m1.addNode(nd)
    for el in (e1,e2,e3):
        m1.addElement(el)

    m1.buildGlobalMatrix()
    #~ n4.fx = P
    m1.addForce(n4,(P,))
    #~ n1.ux = 0.0
    #~ n2.ux = 0.0
    m1.addConstraint(n1,ux=0)
    m1.addConstraint(n2,ux=0)
    m1.solve()
    
    for node in m1.getNodes():
        print  node.ux, node.uy, node.fx, node.fy

def test2():
    """
    Logan, D. (2007). A first course in the finite element analysis.
    Example 2.2, pp. 45.
    """
    P = 4e3
    k = 200e3
    # Model
    m2 = SpringModel("Spring Model 02")
    # Nodes
    n1 = Node((0,0),0)
    n2 = Node((0,0),1)
    n3 = Node((0,0),2)
    n4 = Node((0,0),3)
    n5 = Node((0,0),4)
    # Elements
    e1 = Spring((n1,n2),k)
    e2 = Spring((n2,n3),k)
    e3 = Spring((n3,n4),k)
    e4 = Spring((n4,n5),k)
    
    for nd in (n1,n2,n3,n4,n5):
        m2.addNode(nd)
    for el in (e1,e2,e3,e4):
        m2.addElement(el)
    
    m2.buildGlobalMatrix()
    m2.addForce(n4,(P,))
    m2.addConstraint(n1,ux=0)
    m2.addConstraint(n5,ux=0.02)
    
    m2.solve()


def test3():
    """
    Logan, D. (2007). A first course in the finite element analysis.
    Problem 2.8, pp. 62.
    """
    P = 500
    k = 500
    # Model
    m3 = SpringModel("Spring Model 03")
    # Nodes
    n1 = Node((0,0))
    n2 = Node((0,0))
    n3 = Node((0,0))
    # Elements
    e1 = Spring((n1,n2),k)
    e2 = Spring((n2,n3),k)
    
    for nd in (n1,n2,n3):
        m3.addNode(nd)
    for el in (e1,e2):
        m3.addElement(el)
    
    m3.buildGlobalMatrix()
    m3.addForce(n3,(P,))
    m3.addConstraint(n1,ux=0)
    m3.solve()
    
    for n in m3.getNodes():
        print n.ux, n.uy
        

def simple_case():
    """
    """
    P = 750
    k = 300
    # Model
    ms = SpringModel("Simple")
    # Nodes
    n1 = Node((0,0))
    n2 = Node((0,0))
    # Elements
    e1 = Spring((n1,n2),k)
    
    for nd in (n1,n2):
        ms.addNode(nd)
    ms.addElement(e1)
    
    ms.buildGlobalMatrix()
    ms.addForce(n2,(P,))
    ms.addConstraint(n1,ux=0)
    ms.solve()
    
    print("Node displacements")
    for n in ms.getNodes():
        print n.ux, n.uy
    
    print("Element stiffness matrix")
    for el in ms.getElements():
        print(el.getElementStiffness())


if __name__ == '__main__':
    #~ test1()
    #~ test3()
    simple_case()
