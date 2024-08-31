import json
import csv
import operator
import itertools
from SPARQLWrapper import SPARQLWrapper, JSON
import time
import re
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"
from pandasql import sqldf


import Metric
import warnings



class Predicate():
    def construct(self, dict_pre_label):
        self.pre_label = dict_pre_label
    
    def __init__(self):
        self.pre_label = dict()

predicate = Predicate()




def current_milli_time():
    return round(time.time() * 1000)



def inputFile(input_config):
    with open(input_config, "r") as input_file_descriptor:
        input_data = json.load(input_file_descriptor)
    prefix = input_data['prefix']
    path = './'+ input_data['KG']
    endpoint = input_data['endpoint']
    path_result = 'Results/' + input_data['KG'] + "_NewTriples/" + ".nt"
    predicate = input_data['predicate']

    return endpoint, prefix, rules, path, predicate, path_result


def query_generation(endpoint, prefix, pre1, pre2, pre3):
    prex1 = []
    pattern = r'\?([A-Za-z])'
    for item in pre2:
        new_item = re.sub(pattern, r'?\g<1>1', item, count=1)
        prex1.append(new_item)
    print(prex1)
    
    sparql_query_template = """
        PREFIX wd: <http://www.wikidata.org/entity/>
        PREFIX wdt: <http://www.wikidata.org/prop/direct/>
        SELECT (MIN(xsd:float(?Instances))/MAX(xsd:float(?Instances)) AS ?overlap) WHERE {
          {
          SELECT (COUNT(DISTINCT *) AS ?Instances) WHERE {
              SELECT ?o1 WHERE {
              subject pre1 ?o1.
              }
              }      
            }
        UNION 
        {
          SELECT (COUNT(DISTINCT *) AS ?Instances) WHERE {
             SELECT ?o2 WHERE {
               subject pre2 ?o2.
              }
             }      
           } 
          }
        """
    
    if len(pre2) != len(pre3):
        print("Both lists should have the same length.")
        return
    
    overlaps = []  # Store the overlap values for all queries
    
    for elem2, elemx1 in zip(pre2, prex1, pre3):
        sparql_query = sparql_query_template.replace("subject", pre1).replace("pre1", elem2).replace("pre2", elemx1)

        # print(sparql_query)
        
        sparql = SPARQLWrapper(endpoint)
        sparql.setQuery(sparql_query)
        sparql.setReturnFormat(JSON)

        # Execute the query and print the results
        results = sparql.query().convert()
        
        for result in results["results"]["bindings"]:
            overlap = result["overlap"]["value"]
            
            overlaps.append(overlap)

    return overlap
        
        




if __name__ == '__main__':
    start_time = time.time()
    input_config = 'input-SynScore.json'
    endpoint, prefix, path, predicate, path_result = inputFile(input_config)
    score = query_generation(endpoint, prefix, predicate, preB1, preB2)
    

    end_time = time.time()
    execution_time = end_time - start_time

    print('Execution time', execution_time)
