<h1>Instructions</h1>

<h3>1. Getting The File In The System</h3>

<p>One Way To Get The File In The System</p>
<p>Create a python file (.py) in the home directory.</p>
<p>❗️Make Sure That It Isn't Your Home Directory It Should Be The One That All Users Share❗️</p>

<h3>Setting Up File For Execution</h3>
<p>Within The Code Locate Line Number 26</p>
<p>It should look something like this</p>

```python
UsersDel=filterUsers('''Line You Change''')
```
<p>Within the triple quotes paste the user names seperated by commas (It doesnt matter if the usernames have spaces or are multiline)</p>
<p>It Could Look Something Like This</p>

```python
UsersDel=filterUsers('''the_coder_in_the_corner,
bob, walter, badperson''')
```

<p>After That Locate Line 65</p>
<p>It Should Look Something Like This</p>

```python
if(i != ""): #YOU PUT IN YOUR NAME
```

<p>Within the quotes add your ubuntu name</p>

```python
if(i != "the_coder_in_the_corner"): #YOU PUT IN YOUR NAME
```

<h3>Running The Script</h3>
<p>Once In The Home Directory Type In The Following</p>

```bash
sudo python3 ./automation.py
```

<p>❗️Pay Attention To The Output❗️</p>
