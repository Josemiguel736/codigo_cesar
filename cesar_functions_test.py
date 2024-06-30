"""
Test funciones codigo cesar
"""
from cesar_functions import *

def test_to_list():
    assert to_list("hola")==["h","o","l","a"]
    

def test_index_list_strings():
    assert index_list_strings(["a"],[[1,2,3],["a","b","c"]])==[[1,0]]

    assert index_list_strings(["4"],[[1,2,3],["a","b","c"]])==[]

def test_move_index():
    assert move_index([[0,0],[1,2]],3)==[[0,3],[1,5]]

def test_recompose_list_string():
    assert recompose_list_string([[0,1],[1,5]],list_of_variables)==["b","u"]
    assert recompose_list_string([[0,27],[3,5]],list_of_variables)==["z","5"]
    assert recompose_list_string([[0,-1],[3,5]],list_of_variables)==["z","5"]
    assert recompose_list_string([[0,28],[3,5]],list_of_variables)==["a","5"]
    assert recompose_list_string([[0,-28],[3,5]],list_of_variables)==["z","5"]

def test_concatenate_list():
    assert concatenate_list(["h","o","l","a"])=="hola"


