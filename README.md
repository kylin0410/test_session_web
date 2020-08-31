# test_session_web
How to test session based web backend (ex: .NET MVC web app) by Python unittest framework.

* Modify basic setting in config.py to specify test site and login information.

* Run all unittest in folder:

```
python -W ignore -m unittest discover -vf baseline
```

* Run single unit test:

``` 
# Single module
python -W ignore -m unittest -vf dummy.test_demo

# Single module.Class
python -W ignore -m unittest -vf dummy.test_demo.Demo

# Single module.Class.method
python -W ignore -m unittest -vf dummy.test_demo.Demo.test_func1
``` 

