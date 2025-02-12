Summary:

“Onboarding to Crypto Chatbot”

* The user can ask about how to get started in crypto.
* The chatbot tells the user about three promising and unique crypto coins in February 2024. The user has to ask by name to be told a summary about the coins. 
* The user can ask which marketplaces are currently performing the most volume for each of the three coins.
* The user can ask for a guide of how to buy each of these coins. 
* The chatbot also can tell you the live price of bitcoin and bitcoin’s top exchanges.


Solutions to known issues:
* Adding to stories.yml instead of just rules.yml.
* Implementing standardized coding conventions instead of such repetitive code.
* Filling in the test stories. 
* Addressing in-line execution warnings.

Minor improvements:
* Get marketcap data for coins.
* Get recent performance history for coins. 
* Implement error handling. 

Big-picture improvements:
* It would be sweet to be able to execute trades from the Chatbot. 
* It would be sweet to have more access to more on-chain data through the Chatbot. 
* It would be sweet to be able to live-query all sorts of coins without hardcoding them. 
* Deploy the Chatbot outside of a shell development environment.

Notes on usage:
* You’ll need to run “rasa run actions” in a separate terminal window. 
* Should work out of the box with “rasa shell”.
