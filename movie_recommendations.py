#movie_recommendations
movies_a={"Superman","Stranger things","Kuruthi"}
movies_b={"Superman","Strangers at sea","500 days of summer"}

movie_both_watched = movies_a.intersection(movies_b)
print(movie_both_watched)
movies_unique_a = movies_a.difference(movies_b)
print(movies_unique_a)
movies_sugg_a=movies_b.difference(movies_a)
print(movies_sugg_a)
