FCC Clustering Algorithm
========================

*Fraction of Common Contacts Clustering Algorithm for Protein Models from Structure Prediction Methods*


Requirements
------------

* Python 2.6+
* C/C++ Compiler

Installation
------------

Navigate to the src/ folder and issue 'make' to compile the contact programs.
Edit the Makefile if necessary (e.g. different compiler, optimization level).

Usage
------------

All scripts produce usage documentation if called without any arguments. Further,
the '-h' option produces (for Python scripts) a more detailed help with descriptions
of all available options.

For most cases, the following setup is enough:

    # Make a file list with all your PDB files
    ls *pdb > pdb.list
    
    # Ensure all PDB models have segID identifiers
    # Convert chainIDs to segIDs if necessary using scripts/pdb_chainxseg.py
    for pdb in $( cat pdb.list ); do pdb_chainxseg.py $pdb > temp; mv temp $pdb; done

    # Generate contact files for all PDB files in pdb.list
    # using 4 cores on this machine.
    python2.6 make_contacts.py -f pdb.list -n 4

    # Create a file listing the names of the contact files
    # Use file.list to maintain order in the cluster output
    sed -e 's/pdb/contacts/' pdb.list | sed -e '/^$/d' > pdb.contacts

    # Calculate the similarity matrix
    python2.6 calc_fcc_matrix.py -f pdb.contacts -o fcc_matrix.out

    # Cluster the similarity matrix using a threshold of 0.75 (75% contacts in common)
    python2.6 cluster_fcc.py fcc_matrix.out 0.75 -o clusters_0.75.out

    # Use ppretty_clusters.py to output meaningful names instead of model indexes
    python2.6 ppretty_clusters.py clusters_0.75.out pdb.list



