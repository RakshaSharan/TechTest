# SkyTechTest

Goals -  Testing API using Python Behave BDD approach for the User Story below

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
We	have	2	API	endpoints	located	here:	
 
• https://5f99522350d84900163b8737.mockapi.io/tech-test/articles	-	returns	a	list	of	articles

• https://5f99522350d84900163b8737.mockapi.io/tech-test/articles/2	-	returns	a	single	article

Both	endpoints	return	data	in	JSON	format	and	only	support	HTTP	GET	methods.
Attempting	a	POST,	PUT	or	DELETE	request	on	these	endpoints	will	return	a	HTTP	404.	

	
Tasks:	
1. Using a	framework	of	your	choice,	write	a	suite	of	automated	tests	to	test	these	endpoints.
Please	note,	the	coding	language	must	either	be	Python, Java, or JavaScript.

2. Include	a	ReadMe	within	the	project	with	instructions	on	how	to	run	the	tests.	
	
3. Upload	your	project	to	GitHub	and	share	the	link

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Clone https://github.com/RakshaSharan/TechTest.git to download the files on to your local machine

Command to Run in commandline:

$git clone https://github.com/RakshaSharan/TechTest.git

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Scripting Language - Python V3.8

Libraries imported - Behave, requests

Testing Approach - BDD

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Running the code in command line for testing the features

$behave Features

#Running invdividual features

$behave Features/returnAllArticles.feature

$behave Features/returnSingleArticle.feature

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Command for allure reports 

$behave -f allure_behave.formatter:AllureFormatter -o reports/ Features

reports will be stored in .json files in reports folder

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
