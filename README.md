
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
<h4/>
<p>
The data collection process involved using google maps API places to and storing restaurants in the South Yarra, Melbourne region in an xlsx file (south yarra refined data). The excel files had the following columns: Name, rating, price, category, address, suburb, available meal types, available dietary requirements and short description). This data was read from 'south yarra refined data.xlsx' using the pandas module where each column was stored as a list object. This formed the basis of restaurant data that was to be used in the program.
  </p>
