## Introduction

The following is a description on how we used two RST parsers and two PDTB parsers 

For our specific parsing, download the [ICNALE](https://language.sakura.ne.jp/icnale/download.html) and [CROW](https://crow.corporaproject.org/) datasets. ICNALE requires registration, while CROW requires permission from the corpus owners. Alternatively, this can be run on your own dataset.

## RST Parser based on "Fast Rhetorical Structure Theory Discourse Parsing" by "Michael Heilman, Kenji Sagae"

Original code from https://github.com/EducationalTestingService/rstfinder

As mentioned in this parser's README, the treebanks used to train this model are not freely available and can only be accessed via a personal/academic/institutional subscription to the Linguistic Data Consortium (LDC). This means that we cannot make our RSTFinder parser models publicly available. Therefore, the first step must be to download and train the parser from its orignal source.

1. Run the following to download the parser, and follow the guide to train the models:

	```bash
	git clone https://github.com/EducationalTestingService/rstfinder.git
	```

2. As the README in this file only allows for running on one file at a time, we created runonessays.bash to run recursively on every file in a given folder.

	```bash
	bash runonessays.bash
	```
	
Replace ```ICNALE/*.txt``` with your folder containing the raw text files and ```segmentation_model.C0.5``` with the regularization parameter provided by the parser.

3. Remove metadata from CROW essays with ```python Remove_CROW_Extras.py```
