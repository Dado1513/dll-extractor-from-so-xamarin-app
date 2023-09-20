# Extract dll from .so

### Requirements

- python2.7
- dotnet core
- ilspycmd

```
dotnet tool install ilspycmd -g 
sudo apt-get install libffi-dev
sudo apt-get install python2-dev
```

- enable virtualenv

```
virtualenv venv-python3
source venv-python3/bin/activate 
pip install virtualenv==20.21.1
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
- <https://github.com/icsharpcode/ILSpy/tree/master/ICSharpCode.ILSpyCmd>
