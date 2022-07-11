
<h1>
  Restaurant Recommender Program Summary
</h1>
<p>
The restaurant recommender program filters restaurant recommendations based on user inputs, of restaurant category, meal type (breakfast, lunch, dinner etc), dietary requiremet (halal, vegan, vegetarian..etc) and price point based on google categorisations of number of "$" in description.
<p>
<h3>
Restaurant Recommender Process
</h3>
<h4>
Data Collection Process
</h4>
<p>
The data collection process involved using google maps API places to and storing restaurants in the South Yarra, Melbourne region in an xlsx file (south yarra refined data). The excel files had the following columns: Name, rating, price, category, address, suburb, available meal types, available dietary requirements and short description). This data was read from 'south yarra refined data.xlsx' using the pandas module where each column was stored as a list object. This formed the basis of restaurant data that was to be used in the program.
 </p>
 
<h4>
Organising Collected data
</h4>
<p>
 Data structure selection process for storing restaurant data was chosen as a Tree Data structure, this was designed with the end in mind meaning restaurants were placed in branches that were filtered by category, meal type, dietary requirement and price point. This was used for efficiency of retrieving data for the user. Methods were constructured in the tree data structure that populate the tree with all possible requirements for each category. Methods were also constructed in the tree data structure to store restaurants in appropriate 'categories' for ease of retrieval.
 </p>

<h4>
Retrieiving Data
</h4>
<p>
The tree data structure has a key in feature for retrieval making it efficient with time complexity of O(NlogN). User is prompted to type the beginning of a category and is continuously prompted until just 1 value is remaining. This is done for each filter untill a list of possible restaurants are shown in the terminal.

</p>
  
