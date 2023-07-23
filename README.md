## Introduction

The following is a description on how we used two RST parsers and two PDTB parsers 

For our specific parsing, download the [ICNALE](https://language.sakura.ne.jp/icnale/download.html) and [CROW](https://crow.corporaproject.org/) datasets. ICNALE requires registration, while CROW requires permission from the corpus owners. Alternatively, this can be run on your own dataset.

After downloading CROW, remove metadata from CROW essays with ```python Remove_CROW_Extras.py```

## RST Parser based on "Fast Rhetorical Structure Theory Discourse Parsing" by Michael Heilman, Kenji Sagae

Original code from https://github.com/EducationalTestingService/rstfinder

As mentioned in this parser's README, the treebanks used to train this model are not freely available and can only be accessed via a personal/academic/institutional subscription to the Linguistic Data Consortium (LDC). This means that we cannot make our RSTFinder parser models publicly available. Therefore, the first step must be to download and train the parser from its orignal source.

1. Run the following to download the parser, and follow the guide to train the models:

	```bash
	git clone https://github.com/EducationalTestingService/rstfinder.git
	```

2. As the README in this file only allows for running on one file at a time, we created runonessays.bash to run recursively on every file in a given folder. In this file, replace ```ICNALE/*.txt``` with your folder containing the raw text files and ```segmentation_model.C0.5``` with the regularization parameter provided by the parser.

	```bash
	bash runonessays.bash
	```

3. Run ```python Extract_RST_Data_ICNALE.py``` on the ICNALE directory (containing the parsed .pipe files) and ```python Extract_RST_Data_CROW.py``` on the CROW directory to extract the percentage of RST relations in each individual essay into a csv file. The data folder provides some of our files.

## RST Parser based on "A Two-stage Parsing Method for Text-level Discourse Analysis" by Yizhong Wang, Sujian Li, Houfeng Wang

Original code from https://github.com/yizhongw/StageDP

1. Run the following to download the parser, and follow the guide to train the models, don't forget to download [CoreNLP](https://stanfordnlp.github.io/CoreNLP/index.html) and ensure you've installed the appropriate [requirements](https://github.com/yizhongw/StageDP/blob/master/requirements.txt).

	```bash
	git clone https://github.com/yizhongw/StageDP.git
	```
	
2. From the terminal in the CoreNLP folder, run 

	```bash
	java -mx4g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer
	```

Keep this process running during the two next steps.
	
3. Add ```eduizer.py``` to the src folder and run it on the raw txt files using 
	
	```bash
	python eduizer.py --edu_file_dir ICNALE --output_dir ICNALE_OUTPUT
	```

4. Run ```parse.py``` on the generated .edu files using
	
	```bash
	python parse.py --edu_file_dir ICNALE --output_dir ICNALE_OUTPUT
	```

5. Run ```python Extract_RST_Data_ICNALE.py``` on the ICNALE directory (containing the parsed .pipe files) and ```python Extract_RST_Data_CROW.py``` on the CROW directory to extract the percentage of RST relations in each individual essay into a csv file. The data folder provides some of our files.


