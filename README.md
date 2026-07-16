# Beyond-the-Paycheck-An-Empirical-Assessment-of-Worker-Economic-Well-being-in-a-Changing-Labor-Market
This repository contains the computational model, research paper, data, and final conclusions I used in my submission to the National Science Research Institute's One week Research Hackathon. In this study, I investigated factors that contribute to economic well-being among workers &amp; how employment conditions influence financial resilience.

## Research Question

What factors contribute to economic well-being among U.S. workers, and how do employment conditions influence financial resilience?

## Datasets

Raw datasets are not included because of file size.
This project uses:
- Federal Reserve SHED 2025 Dataset
  Download: https://www.federalreserve.gov/consumerscommunities/shed_data.htm

## Methodology

To fully determine what factors contribute to economic well-being among U.S. workers, I analyzed ~ 18 research papers, particularly "Quality of Work Life Components: A literature Review" by Nanjundeswaraswamy and Sandhya (2016). With the quantative data given by that specific piece of literature, accompanied with the other articles I read through, I found a number of variables. These factors consist of: Income Adequacy, Access to Benefits, Job Flexibility, Income Stability, and Financial Resillience. 

Through further inspection and with the numbers established in the previously referred to article, I composed the Economic Security Index, a score 0-100 that quantifies the economic well-being among all workers in the United States. I found that each individual dimension affected the Economic Security Index as so:

*Income Adequacy: 50%*
*Benefits Access: 11.2%*
*Job Flexibility: 11.2%*
*Income Stability: 13.8%*
*Financial Resilience: 13.8%*

My next step, collect data on these dimsnesions using the Federal Reserve SHED 2025 Dataset, where I quantified each variable that goes into each dimension (This idea is further elaborated on in the Variable Dictionary Document).

This methodology allowed me to create various diagrams to show the effects of each dimension on overall economic well-being, as shown in the Outputs repository.

## Repository Structure

data/
  - cleaned_data.csv
  - variable_dictionary.md

src/ 
  - data_cleaning.py
  - preprocessing.py
  - scoring.py
  - visualizations.py
    
output/
  - dimension_averages.png
  - economic_security_index_histograms.png
  - economic_security_index_weights.png
  - flexibility_vs_economic_security_index.png

paper/
  - Beyond the Paycheck: An Empirical Assessment of Worker Economic Well-being in a Changing Labor Market.pdf

## How to Run

1. Install dependencies
2. Download datasets
3. Run preprocessing
4. Generate figures
