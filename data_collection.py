# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 18:01:01 2020

@author: itxab
"""

import glassdoor_scraper as gs
import pandas as pd 
path = "C:/Users/itxab/Documents/ds_salary_proj/chromedriver"

df= gs.get_jobs('Data Scientist', 1000, False, path, 20)

df.to_csv('glassdoor_jobs.csv', index=False)
