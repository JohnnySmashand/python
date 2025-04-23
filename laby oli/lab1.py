''' 
Otwieram git basha i pisze tak:
cd "ścieżka do mojego folderu" (tworze se nowy)
git init
git remote add origin https://github.com/JohnnySmashand/test.git (tutaj bedzie inny, tworze nowe repozytorium na github)
git add nazwa_pliku istniejacego w folderze
git commit -m "cos tam"
git push -u origin master/main (wrzuca mi na github)



git init: Zakłada zeszyt (repozytorium) w Twoim folderze. Czyli: „Od teraz śledzimy zmiany w tym folderze”.

git status: Pokazuje Ci, co się zmieniło. Co zostało zmodyfikowane, co nie jest zapisane itp.

git add nazwa_pliku: Wkładasz konkretny plik do „szuflady”, żeby powiedzieć: „Hej Git, ten plik chcę zapisać”.

git commit -m "opis": Robisz zdjęcie aktualnego stanu plików i dodajesz komentarz, np. „Zrobiłem nową stronę”. (zapis)

git log: Pokazuje historię zdjęć (czyli commitów). Możesz podejrzeć, co było robione wcześniej.

git branch nazwa_pliku: Tworzy nową „gałąź” — np. chcesz coś testować, ale nie psuć głównej wersji.

git checkout nazwa_pliku: Przełączasz się między gałęziami.

git merge nazwa_pliku: Scalanie gałęzi — czyli wrzucasz zmiany z jednej gałęzi do drugiej (np. z testowej do głównej).


'''