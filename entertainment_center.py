import media
import fresh_tomatoes
# initializing objects from the movie class
toy = media.Movie("Toy story",
                  "http://www.rotoscopers.com/wp-content/uploads/2013/10/"
                  "Toy-Story-Poster.jpg",
                  "https://www.youtube.com/watch?v=KYz2wyBy3kc")
thor = media.Movie("Thor",
                  "http://images.wookmark.com/100251_thor_ver5_xxlg.jpg",
                  "https://www.youtube.com/watch?v=JOddp-nlNvQ")
panda = media.Movie("Kung Fu Panda",
                  "https://s-media-cache-ak0.pinimg.com/originals/08/4d/31"
                  "/084d31f5cf591007d7878a7cbdb2d47c.jpg",
                  "https://www.youtube.com/watch?v=PXi3Mv6KMzY")
tangled = media.Movie("Tangled",
                  "https://i0.wp.com/www.stunningmesh.com/wp-content/uploads/2011/05"
                  "/stunningmesh-3d-movie-poster-76.jpg?w=1320",
                  "https://www.youtube.com/watch?v=2f516ZLyC6U")
iron_man = media.Movie("Iron Man",
                  "https://s-media-cache-ak0.pinimg.com/236x/a8/63/be/a863beaf5413786"
                  "0699352f35e6c5052.jpg",
                  "https://www.youtube.com/watch?v=8hYlB38asDY")
ted = media.Movie("Ted",
                  "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQK7HRLEe2od8AMS"
                  "gZqs4PXTt9ei_sNhwmKg0UNtVvhFg1qMbWLKg",
                  "https://www.youtube.com/watch?v=9fbo_pQvU7M")
movies = [toy,thor,panda,tangled,iron_man,ted]  # array containing the 6 movies
fresh_tomatoes.open_movies_page(movies)  # calling fresh_tomatoes
