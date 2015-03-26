# pybook
My ipython notebook setup, collection of notebooks and their html exports.

### Installation

Clone the repo and run `python setup/install.py`

After cloning, remember to change the password. Use the following snippet to generate the encrypted password.

```
In [1]: from IPython.lib import passwd
In [2]: passwd()
Enter password:
Verify password:
Out[2]: 'sha1:67c9e60bb8b6:9ffede0825894254b2e042ea597d771089e11aed'
```

Copy paste this value into `ipython_notebook_config.py` file located in the `.ipython/profile_pybook/` folder.

