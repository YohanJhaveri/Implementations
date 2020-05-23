STEP 1: To run the program, enter the following command in the CLI in the hw2 directory:

$ python3 hw2.py <input filename> <support threshold> <output filename>

Example: python3 hw2.py T10I4D100K.txt 500 result500.txt



STEP 2: Now, sort the output file using the command

$ sort <output filename> -nk1 -k 2 -o <output filename>

Example: sort result500.txt -nk1 -k 2 -k 3 -o result500.txt


STEP 3: Now, run the diff checker to find differences in the files
