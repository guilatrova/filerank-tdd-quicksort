# Akuaro Test

Thanks for the opportunity :)

## Installation / First Setup

You're going to need both `python`, `pip` and `virtualenv` to install test dependencies in an isolated environment.

```bash
virtualenv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Test it

Just running following should be enough:

```bash
pytest tests
```

Note we have a single simple integration test.
We use this only to make sure we're expecting a proper output, which can be forgotten and uncosidered if we just mock stuff around,
Otherwise it may lead to annoying and weird errors in future. (e.g. All my tests are passing, why is my user experiencing such errors!?).

## Run it

It should be as easy as invoking the `main.py` with your directory.
This application expects all the calls and inputs to be sane, so there's no validation if you insert an invalid directory (or no directory at all) nor invalid unreadable files.

```bash
python main.py yourdirectory
```

### Example usage

There's a `testfolder` to help you testing some basic stuff.
Here's some output examples:

**All 100% path**
```bash
(.venv) latrova@guilherme-ubuntu:~/personal/akuaro$ python main.py testfolder
4 files read in directory testfolder
What would you like to search for: content

=== Results ===
file4.txt - 100.00%
file1.txt - 100.00%
file3.txt - 100.00%
file2.txt - 100.00%
```

**

**100%/50% path**
```bash
(.venv) latrova@guilherme-ubuntu:~/personal/akuaro$ python main.py testfolder
4 files read in directory testfolder
What would you like to search for: content

=== Results ===
file4.txt - 100.00%
file1.txt - 100.00%
file3.txt - 100.00%
file2.txt - 100.00%
```

**100%/0% path**
```bash
(.venv) latrova@guilherme-ubuntu:~/personal/akuaro$ python main.py testfolder
4 files read in directory testfolder
What would you like to search for: file

=== Results ===
file1.txt - 100.00%
file2.txt - 100.00%
file3.txt - 0.00%
file4.txt - 0.00%
```

**Long, repetitive words path**
```bash
(.venv) latrova@guilherme-ubuntu:~/personal/akuaro$ python main.py testfolder
4 files read in directory testfolder
What would you like to search for: a long long long search with repetitive words and no content that matters not even a single one

=== Results ===
file4.txt - 13.33%
file1.txt - 6.67%
file3.txt - 6.67%
file2.txt - 6.67%
```
