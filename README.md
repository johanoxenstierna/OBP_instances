#Readme for the 1_1v3 tsplibs
In the root path there are 6 instance type names. 

## TSPLIB modified instances and memory reduction
 Instead of providing full descriptors for each instance as in standard TSPLIB, this repository divides the instance
descriptors into two parts: 1. Within each instance type directory there is a tsplib 
 "parent" description file in .txt and 
.json format which gives info on all locations and obstacles of the digital model of a warehouse. 
2. Within each instance type directory
there is then a directory "instances", with folders with all remaining necessary information to 
   reconstruct the TSPLIB instance for a specific warehouse. 
   This cut was done to make it easier to reconstruct instances and to prevent the majority of instance data to be redundant: Only a small subset 
   of all locations in a warehouse is used in a specific instance and the visit locations for each 
   instance use locations provided in the parent tsplib. 

##Pictures
The solution folders include pictures. The red and blue diamonds denote destination and origin locations respectively
. The dots denote product and their colors denote the order which the products belong to. Note colors are picked
 randomly from a list so it is often the case that two orders share the same color. In most cases there is one .png
  per batch , but in some
 cases all batches are
 shown in a single .png (to reduce memory usage). In the latter case it is usually very difficult to make out one
  batch from another.

