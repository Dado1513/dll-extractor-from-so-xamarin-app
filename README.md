# Extract dll from .so

### Requirements

- python2.7

```
sudo apt-get install libffi-dev
sudo apt-get install python2-dev
```

- enable virtualenv

```
virtualenv -p /usr/bin/python2.7  .venv-python2 
```

- install requirements.txt

```
pyelftools==0.28
yara-python==4.2.0
```

### References

- <https://securitygrind.com/reverse-engineering-a-xamarin-application/>
- <https://github.com/maldroid/maldrolyzer/blob/master/plugins/z3core.py>
