Python 3.12.1 (v3.12.1:2305ca5144, Dec  7 2023, 17:23:38) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> #A: Joining Strings
>>> 
>>> "-".join("cat")
'c-a-t'
>>> 
>>> #it separated the word cat.
>>> 
>>> lines = ["Haiku frogs in snow",
...          "A limerick came from Nantucket",
...          "Tetrametric drum-beats thrumming, Hiawathianic rhythm."]
>>> 
>>> def breakify(lines):
...     return '<br>'.join(lines)
... 
>>> print(lines)
['Haiku frogs in snow', 'A limerick came from Nantucket', 'Tetrametric drum-beats thrumming, Hiawathianic rhythm.']
>>> #T. Burns and V. Antimo
>>> 
