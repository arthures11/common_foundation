## example program results for given data.txt file:

```
Ivana Moura, ivana.moura@example.com, Brazil
Scarlett Kumar, scarlett.kumar@example.com, New Zealand
Natan Flø, natan.flo@example.com, Norway
Brankica Radanović, brankica.radanovic@example.com, Serbia
Adem Erkekli, adem.erkekli@example.com, Turkey
Darin Bøhler, darin.bohler@example.com, Norway
Bradley Mason, bradley.mason@example.com, United Kingdom
Alexis Roy, alexis.roy@example.com, Canada
Yashika Babu, yashika.babu@example.com, India
Jasmin Nicolas, jasmin.nicolas@example.com, Switzerland
```



example result using `python main.py`:

output:
```
Total lines: 10
[2025-02-17 00:41:44] Task Counting lines completed in 0.000225 seconds.
```

example result using `python main.py -s iv` or `python main.py --search iv`:

output:
```
1: Ivana Moura, ivana.moura@example.com, Brazil
[2025-02-17 00:41:34] Task Searching for 'iv' completed in 0.000330 seconds.
```

example result using `python main.py -p` or `python main.py --populate`:

output:

```
File 'data.txt' has been populated with 10 random users.
[2025-02-17 00:46:37] Task Populating new data to file 'data.txt' completed in 0.194287 seconds.
```


for tests, run: `pytest -v` or `pytest`, example output:
```
plugins: mock-3.14.0
collected 6 items

tests/test_api_client.py::test_fetch_random_users_success PASSED
tests/test_api_client.py::test_fetch_random_users_failure PASSED
tests/test_file_manager.py::test_count_lines PASSED
tests/test_file_manager.py::test_search_keyword_found PASSED 
tests/test_file_manager.py::test_search_keyword_not_found PASSED
tests/test_file_manager.py::test_write_data PASSED   
```