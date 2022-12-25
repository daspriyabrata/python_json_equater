#Steps to run
- install the requirements using "pip3 install -r requirements.txt"
- run the automation suite using "python3 test.py"

#Solution Approach:
-First Part was to be able to make api calls which was handled using requests library.
-The Second part was to figure out a way to compare the response json body. FOr the same the best approach was to sort the same. Normally response json can come in two formats i.e. list or dictionary, hence I needed a centralised approach to tackle the same and created a Diff Comparator.
-Third part was to figure out a way to run the same in multi-threading.