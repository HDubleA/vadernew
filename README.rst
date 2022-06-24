====================================
VADERNEW
====================================
VADERNEW starts from VADER base and aims to show how it can be improved. Vadernew is completely similar to VADER, as shown in the project, obtained better performances by working on specific topics.
It is fully open-sourced under the `[MIT License] <http://choosealicense.com/>`_ (we sincerely appreciate all attributions and readily accept most contributions, but please don't hold us liable).

* `vadernew: a vader evolution`_
* `Introduction`_
* `Installation`_
* `Package explanation`_
* `Example`_
* `Files explanation`_
* `Conclusion`_

vadernew: a vader evolution
------------------------------------
The project starts from the basic idea of overcoming the limits of Vader, which is too general and not applicable to specific contexts. 
An example of the above problem can be found in terms such as ”bull” which in everyday language means ”bull”, but in a financial context 
it means that a certain stock is destined to grow. The project will be divided into two parts, which have the aim of creating the basis for 
an articulated and cohesive system of recognition and specific analysis of topics of discussion.

The package offers specialized dictionaries for sentiment analysis on the following topics:

#. Food: food review on amazon

#. Electronics: review of electronic products on amazon

#. Disneyland: review of amusement parks on tripadvisor

#. Finance: reviews and tweets of financial topics

In addition to the VADER sentiment analysis Python module, options 3 or 4 will also download all the additional resources and datasets (described below).



The procedure and the study that led to the results obtained is explained in full in the **Project_explanation** pdf file.
In general, the noteworthy result is that working with dictionaries trained on specific lexicons always improves Vader's performance for sentiment analysis.

By reviewing all the steps of the project, from expected results, making changes in order to specialize Vader on topics of discussion leads only to improvements. In general, it is necessary to underline the result observed, according to which, regardless of the methods of assigning weights and the models used to assign them, Vader is always worse than its specialized versions. This result leads to the conclusion that despite being an innovative and extremely effective system, Vader is now easily overcome, or better said, improved.
As a conclusion, we invite you to grasp the input proposed by this project, that is the development, starting from Vader, of a system that is able to identify the topic of discussion text by text, sentence by sentence and which uses specialized dictionaries in order to have performing and accurate analyzes.
As a last note, we recommend that anyone who intends to apply textual analyzes, such as sentiment analyzes, on texts whose topic of discussion is already known at the outset, to take datasets with characteristics similar to those seen previously and to train a specialized dictionary for the subject. The resulting dictionary, used as illustrated in the project, regardless of the attention paid to the choice of models and the assignment of weights, should still be more efficient than the general one used by Vader.

In addition, we invite you to offer us your specialized dictionaries in order to increase the offer made by us.

====================================
Introduction
====================================

This README file briefly describes the proposed package:

	|  **vadernew: Overcoming Vader limits by identifying discussion topics and analyzing using specialized dictionaries**
	|  (by Vittorio Haardt, Riccardo Fossato and Luca Porcelli)  
 
 

Starting from Vader
------------------------------------

The project was developed starting from Vader, who was born thanks to cjhotto. For the operation of this fantastic tool we refer directly to the github page of the creator `[Vader] <https://github.com/cjhutto/vaderSentiment>`_ . The original article is shown below:

  **Hutto, C.J. & Gilbert, E.E. (2014). VADER: A Parsimonious Rule-based Model for Sentiment Analysis of Social Media Text. Eighth International Conference on Weblogs and Social Media (ICWSM-14). Ann Arbor, MI, June 2014.** 

====================================
Installation
====================================

To install and use vadernew you can proceed in the following way:  

Use the command line to do an installation from `[PyPI] <https://pypi.org/project/vadernew/>`_ using pip, e.g., 
    ``> pip install vadernew``


====================================
Package explanation
====================================
IT start by installing the ”vadernew” package via pip install.

The package contains the dictionaries and functions relating to the 4 topics separately, which can be imported individually.
:: 
   from vadernew imoport vader_food

   from vadernew import vader_electronic 

   from vadernew import vader_disneyland

   from vadernew import vader_finance

The package contains the dictionaries and functions relating to the 4 topics separately, which can be imported individually.
That is, two replacement functions, respectively of SentiText() which identifies the string-level properties relevant to the sentiment of the input text, and SentimentIntensityAnalyzer() which instead assigns a sentiment intensity score to the phrases. The two functions are renamed for each argument.
:: 
   from vadernew.vader_food import Food_ST, Food_SIA

   from vadernew.vader_electronic import Electronic_ST, Electronic_SIA 

   from vadernew.vader_disneyland import Disney_ST, Disney_SIA

   from vadernew.vader_finance import Finance_ST, Finance_SIA

Fortheworkingofthe STfunctions,pleaselookattheclassicVaderguideforSentiText(),astheyarenot the point of the changes made.
Now let’s see how the SIA functions work and how with one of its sub-functions we find the com- pound values. The resulting values are more accurate, as they refer to specific dictionaries. For all callable sub-functions, reference is always made to the VaderSentiment guide, remember that the operation of the vadernew package is in all respects the same as that of VaderSentiment, the only change is the specificity of the dictionaries used.

Inclusion we invite you to try and experiment the potential of the package, which, we remind you once again,
only acts as a showcase of how a specialization of VaderSentiment leads to more accurate analyzes.

====================================
Example
====================================

We now show how the package works with an example.

Code Examples
------------------------------------
::

	from vadernew.vader_finance import Finance_ST, Finance_SIA

    # --- example -------
    sentence = "Just an example"
    
    analyzer = vader_finance.Finance_SIA()
    vs = analyzer.polarity_scores(sentence) print("{:<13} {}".format(sentence, str(vs))




Output for the above example
------------------------------------
::

	Just an example {’neg’: 0.0, ’neu’: 0.286, ’pos’: 0.714, ’compound’: 0.7184}


====================================
Files explanation
====================================
#. data 

	The folder contains the datasets used for development.

		- **Completo_learing.xlsx** : dataset to train the topic classification model
		- **Cibo_learing.xlsx** : dataset to build the Food vocabulary
		- **Food.xlsx** : dataset to test the Food vocabulary
		- **Disneyland_learing.xlsx** : dataset for building the Disneyland vocabulary
		- **Disneyland.xlsx** : dataset for testing Disneyland vocabulary
		- **Electronic_learing.xlsx** : dataset to build the Electronic vocabulary
		- **Electronic.xlsx** : dataset to test the Electronic vocabulary
		- **Finance_learing.xlsx** : dataset to build the Finance vocabulary
		- **Finance.xlsx** : dataset to test the Finance vocabulary

#. dictionaries 

	The folder contains the specialized dictionaries obtained from the analyzes.

		- **Food_dic.json** : dictionary specialized on the topic of Food
		- **Disneyland_dic.json** : dictionary specialized on the topic of Disneyland
		- **Electronic_dic.json** : dictionary specialized on the topic of Electronic
		- **Finance_dic.json** : dictionary specialized on the topic of Finance

#. analysis and development

	the folder contains the python notebooks for the project's development.

		- **word_weight_evaluation.ipynb** : notebook for thecreation of the specialized dictionaries
		- **we_for_better_performance.ipynb** : notebook for the evaluation of the wordembedding in dictionaries
		- **Vader_evaluation.ipynb** : notebook for the evaluation of the specialized dictionaries
		- **Classification.ipynb** : notebook for the topic classification model
    
#. vadernew
	
	Folder that contains everiting necessary to post the package vadernew.

#. Project_explanation.pdf
	
	Pdf file that explain the project.

====================================
Conclusion
====================================

As a conclusion, we invite you to grasp the input proposed by this project, that is the development, starting from Vader, of a system that is able to identify the topic of discussion text by text, sentence by sentence and which uses specialized dictionaries in order to have performing and accurate analyzes.
As a last note, we recommend that anyone who intends to apply textual analyzes, such as sentiment analyzes, on texts whose topic of discussion is already known at the outset, to take datasets with charac- teristics similar to those seen previously and to train a specialized dictionary for the subject. The resulting dictionary, used as illustrated in the project, regardless of the attention paid to the choice of models and the assignment of weights, should still be more efficient than the general one used by Vader.

