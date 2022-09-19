# Type_II_PKS_Project
 
1. AlphaFold_models
  + The AlphaFold outputs for the three chosen sequences as well as the 6 sequence mutated models
  + For Model 1-6, there are additional files containing the structures with altered rotamers
2. CASTp
  + The folders contain [CASTp](http://sts.bioe.uic.edu/castp/calculation.html) data, all using 1.1 as the radius
  + There is also a jupyter notebook along with two .csv files to generate some plots
3. Chen_et_al_SI.xlsx
  + The SI from [here](https://onlinelibrary.wiley.com/doi/10.1002/anie.202202286)
  + Contains data for all type II PKS with known sequences and products (as of 6/4/22)
4. ConSurf
  + Contains ConSurf runs for the three clades, as well as for the entire dataset, each with the correct reference sequence
  + To visualise colours on one of the proteins, run @color_def.txt in the PyMol command line
  + Open one of the three AlphaFold models and run the corresponding _clade_color.txt in the same way
  + consurf_conservation_analysis.py contains the script to produce these text files
5. model_comparison.pse --> get correct AF in there
  + A PyMol session containing all the AlphaFold models aligned and their CLRs shown
6. MSAs
  + The MSAs generated in fasta format
  + msa_1 contains all 155 (there are some duplicate sequences in the Chen db) original sequences
  + msa_2 contains 148 sequences, the 7 outliers have been removed
7. phylogenetic_trees
  + as above in terms of nomenclature
  + present as .treefiles
  
