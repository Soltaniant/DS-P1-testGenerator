# DS-P1-testGenerator

what is this?
-------------
This is an automated test generator for the first phase of DS project(Dr Safarnejad Boroujeni).
It will:
- show the missing words which your code doesn't find
- show the approximate execution time for each query

How to use it?
-------------
To use, you need to have a function(e.g `find()`) which returns the list of words that matches with the query.
This list will be used to assert your result correctness.
steps:
1. Add your code including classes and functions (except driver codes!)
2. In the last loop, assign your final answer(the list which returned by your find method) to `myResult` variable.
NOTICE: `query` is a list containing 2 srtings. the first one includes `.*` which is used in `findByRegex()` and the second one is whcih we should use(uses `\S*` instead)
3. Run the program! it will hopefully accept your answer! if not, you may need to think more :)

How does it work?
-------------
It generally uses Regex module to find the correct answer of each query and check the result with the answer generated by your code.
As inputs, it uses a text file(included in "texts" folder) to generate a query by randomly choosing a word and converting it to a regex-like string.

Find a bug?
-------------
let [me](mailto:s.soltaniant@gmail.com) know :)
