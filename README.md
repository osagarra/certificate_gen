Certificate_gen
===============

## Short description

This is a certificate generator for a congress, in case you need to generate multiple certificates with different names and contributions.

This is a program to do event-like certificates at an "industrial" pace

## Dependencies

	- PDFlatex (if you have another latex compiler change the lines in the code as specified).
	- Python


## Making it work...

The program needs as input:
	
	- Name list: names.txt (in format as in example names.txt)
	- List of contributions: posters.txt
	- .tex DOcument with the spot where "name" field should appear marked as NNAMEE and the contribution name (poster field) as PPOSTERR. Place the doc at the same folder
	- Output files are created in folder output	
	- Images can be added to the .tex doc: Put them in './fig'

To run the script: 

```
$> ./python certificate_gen.py'
```


## Examples

There are figures added for your convenience as example. To run the example, just type at the shell: 

```
$> ./python certificate_gen.py'
```

## Known issues and bugs and license and so on...

You may use this program at your convenience. Please report any bugs you detect at "osagarra@ub.edu". Obviously, no warranty is provided or whatsoever.
If you run it under windows, see the comments directly on the code to make appropriate changes...

