# Code For CAM ANALYSIS

In this repository, we demonstrate the capabilities of CAMs as a data gathering tool. 

The first step is to clean your data. We have provided here a basic cleaning tool called `Clean_CAMS.py` which will handle any multiple line issues that you may run into. 

Once you have your cleaned data, you can move immediately to the main analysis which is in the jupyter notebook `Full_Clean_CAM.ipynb`. 

This notebook has seven (7) steps:
1 - Read Data into pandas appropriate format

2 - Build Network Graphs from CAM information

3 - Calculate Network Measures:

	- Proportion of positive and negative nodes
	- Proportion of solid and dashed lines
	- Probability of each node type
	- Diversity measure
	- Density measure
	- Longest Path
	- Transitivity
	- Max degree 
	- Eigenvector Centrality
	- Betweeness Centrality

4 - Summary information for CAM measures

5 - Simulate probability of randomly generating graphs using Bayesian approach

6 - Combine CAM and Survey info (assuming you have a complimentary survey)

7 - Calculation fo summary statistics including correlation matrix



If you would like to see any other statistics implemented, please contact Carter Rhea at carterrhea93@gmail.com.
