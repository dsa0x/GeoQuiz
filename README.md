# Geo References 

This repository houses a basis geoquiz written in Python. From a dictionary file listing a tuple for every capital, country, subregion on the planet, the quiz code generates a random tuple for posing the "what capital belongs to this country" question. The code then generates a tuple of four possible answers, including the correct one. These answers are based on the subregion of the country - so the alternative answers for say Netherlands (Amsterdam) would be Brussels, Berlin, London --- and not e.g. Bogota, Beijing, Brasilia. This to make it a little harder to figure out the proper answer.

For every question answered correct, one gets a point. For every wrong answer, one loses a point. No points left means game over.
