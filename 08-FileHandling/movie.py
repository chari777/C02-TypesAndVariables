# Program zapisujący dane filmu do pliku tekstowego

# Zmienne z danymi filmu
movie_title = "Inception"
director = "Christopher Nolan"
lead_actor = "Leonardo DiCaprio"

# Nazwa pliku, do którego zapisujemy dane
file_name = 'movie_details.txt'

# Tryb 'w' (write) tworzy plik lub nadpisuje go, jeśli już istnieje
with open(file_name, 'w', encoding='utf-8') as file:
    file.write(f"Movie Title: {movie_title}\n")
    file.write(f"Director: {director}\n")
    file.write(f"Lead Actor: {lead_actor}\n")

print(f"Movie details have been written to {file_name}.")
