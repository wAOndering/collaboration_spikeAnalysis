# collaboration_spikeAnalysis
This repository keeps track of the progress of a collaboration and resources used with Lorenzon Fontolan for the spike analysis of Syngap1 project.

# Objective
## general principles
* perform CCA (canonical correlation analysis) and latent subspace manifold features and comparison 
* perfom coherency analysis  
## relevant litterature
* Functional causal flow [paper](https://www.biorxiv.org/content/10.1101/2020.11.23.394916v2)
* Lorenzo's speech information processing [paper](https://www.nature.com/articles/ncomms5694)
* Manifold work 
	* [Perspective](https://doi.org/10.1016/j.neuron.2017.05.025)
	* [Cortical population and behavior](https://doi.org/10.1038/s41593-019-0555-4)
	* [Manifold stability](https://doi.org/10.1038/s41467-018-06560-z)

# Frame work
__Hypothesis:__ Evidence of sensory motor processing by comparing coherency / cross correlogram during events (potentially model event amplitude) and quite wakefulness (when no running, no whiksing, no touch *need to filter out the data*)
* doc to follow up the progress and frame work
* analysis of all spikes 
	* during touch
	* during whisk 
	* during quiet wakefullness
* check out work from Mark Churchland and John Cunningham (Columbia)

# Data
## spikes
* DataFrame
	* n files: 1
	* format: csv
	* dimensions: 254,419,892 x 13
	* size: 24 Gb
	* info: see [example](/allDataSample.csv)
* npy arrays
	* spike times for 1 brain region 1 animal (20Mb)
	* spike cluster for 1 brain region 1 animal (10Mb)
	* overall size: 2.4 Gb

## behavior
* npy arrays
	* whisking onset
	* touch onset
	* running onset
	* quiet wakefulness (to be defined by substracting the other epochs)
	* layer multicomponent of touch / whisking / running (establish kmeans state transition analysis)


# Future plan 
## CCG 
Consider performing CCG may be similar to CCA mentioned earlier see [paper](https://doi.org/10.1016/j.neuron.2022.01.027) and associated [repo](https://github.com/jiaxx/modular_network). The potential drawback of this approach is that if there is no clear pattern in the matrices that can be difficult to perform the analysis. One way this could be accomplished would be to just plot the matrices and then determined if further analysis need to be perfromed.


## Whisking regularity 
Some interesting ways of looking at the data in this [paper](https://doi.org/10.1038/
s41586-022-05144-8) and [code]()

## Other papers and analyses relevant to spiking
* Deisseroth Fig4 [paper](https://doi.org/10.1126/science.aav3932)
* Margrie [paper](https://doi.org/10.1016/j.neuron.2021.10.031)
* Helmchen [paper](https://www.biorxiv.org/content/10.1101/2020.07.08.193334v1)


