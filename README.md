# homework
This is the homework assignment with the following instructions:

Here is the HW for the Python Tools Engineer role:
 
1) Write a python program to rotate integer array elements by shift (user-input). Do this without using another array or without moving any element of the input array multiple times.
e.g. python array_rotate.py <shift_size> <csv_int_array)
python array_rotate.py 3 10,11,14,15
This should produce output : 11,14,15,10

2) Write a python program to read input json from : http://mysafeinfo.com/api/data?list=englishmonarchs&format=json
and create list of uniq 'nm' by 'cty' and 'hse'.
e.g. Output json should look like :
{
"United Kingdom" : {
"House of Blois" : ["Stephen"],
...
}
...
}

3) Write a python program to read input json from http://mysafeinfo.com/api/data?list=englishmonarchs&format=json
and write the data to local file called "/tmp/converter_input.json" Then create another file called ?/tmp/converter_input.csv" to dump the data in csv file format.
Don?t use python CSV modules.

4) Write a shell script to sum the sizes of all files in input dir.
- Must be shell (no python)
- Only include regular files (no directly, don?t follow any symlinks)
- Print the size in bytes as well as human readable format

 
