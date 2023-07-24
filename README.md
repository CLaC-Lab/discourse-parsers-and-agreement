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

## PDTB Parser from "A Refined End-to-End Discourse Parser" by Jianxiang Wang, Man Lan

Original code from https://github.com/lanmanok/conll2015_discourse

1. Run the following to download the parser and follow the instructions in the original README, don't forget to install [ETE](http://etetoolkit.org/download/).

 	```bash
	git clone https://github.com/lanmanok/conll2015_discourse.git
	```

Note that this is written for python 2.7, for an update to python 3 try
	```bash
	git clone https://github.com/bxh9261/conll2015_discourse
	```
	
2. Install [Mallet](https://mallet.cs.umass.edu/download.php), [Stanford Parser](https://nlp.stanford.edu/software/lex-parser.shtml#Download), and [Berkeley Parser](https://github.com/slavpetrov/berkeleyparser). Place the parser jar files into a folder called "bin". (This will already be done in our fork)

3. If using the original python 2 version, download [txt2json.sh](https://github.com/bxh9261/conll2015_discourse/blob/master/txt2json.sh), which is a modified version of a file provided by https://github.com/esrel/DP

4. Replace "input_dir" in txt2json.sh with the dataset folder, and run to produce pdtb_parses.json:

	```bash
	bash txt2json.sh
	```
	
5. Finally, run

	```bash
	python $input_dataset $input_run $output_dir
	```
with dataset containing both the raw text folder and the pdtb_parses.json. This will generate a file in data/output.json

6. In our PDTB_Wang_utils directory, download json_to_csv.py and replace json_file_path with the data/output.json file. This will turn the output data into a readable csv.

	```bash
	python json_to_csv.py
	```

## PDTB Parser based on "A PDTB-Styled End-to-End Discourse Parser" from Ziheng Lin, Hwee Tou Ng, Min-Yen Kan

Original code from https://github.com/WING-NUS/pdtb-parser

1. Follow the instructions in the "Usage" section of https://github.com/WING-NUS/pdtb-parser/blob/master/README.md . Requires Java 1.7+.

2. For example, to run on every .txt file in the directory and all subdirectories of an ICNALE folder run:

	```bash
	java -jar parser.jar ICNALE/
	```
	
3. Run ```python Extract_PDTB_Data_ICNALE.py``` on the ICNALE directory (containing the parsed .pipe files) and ```python Extract_PDTB_Data_CROW.py``` on the CROW directory to extract the percentage of PDTB level relations in each individual essay into a csv file. The data folder provides some of our files.

## RST Parser Agreement

1. In Extract_EDU.py, replace lines 7 and 89 with your directories containing the parser output files. Line 90 will also require the directory containing your .EDU files generated by CoreNLP for the Wang RST parser.

2. Run this file to generate a csv file with every matching EDU.

	```bash
	python Extract_EDU.py
	```

3. See [our Google Sheets file](https://docs.google.com/spreadsheets/d/1JMQXnRybiZoi_rOcJExeoIrW31a4lLgpyr8aPCrMBms/edit?usp=sharing) to see how the contingency table was created.

