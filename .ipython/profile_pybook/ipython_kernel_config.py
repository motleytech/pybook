# Configuration file for ipython-kernel.

c = get_config()

#------------------------------------------------------------------------------
# IPKernelApp configuration
#------------------------------------------------------------------------------

# IPython: an enhanced interactive Python shell.

# IPKernelApp will inherit config from: BaseIPythonApplication, Application,
# InteractiveShellApp, ConnectionFileMixin

# Run the file referenced by the PYTHONSTARTUP environment variable at IPython
# startup.
# c.IPKernelApp.exec_PYTHONSTARTUP = True

# The importstring for the DisplayHook factory
# c.IPKernelApp.displayhook_class = 'IPython.kernel.zmq.displayhook.ZMQDisplayHook'

# Set the kernel's IP address [default localhost]. If the IP address is
# something other than localhost, then Consoles on other machines will be able
# to connect to the Kernel, so be careful!
# c.IPKernelApp.ip = u''

# Pre-load matplotlib and numpy for interactive use, selecting a particular
# matplotlib backend and loop integration.
# c.IPKernelApp.pylab = None

# Create a massive crash report when IPython encounters what may be an internal
# error.  The default is to append a short message to the usual traceback
# c.IPKernelApp.verbose_crash = False

# The Kernel subclass to be used.
# 
# This should allow easy re-use of the IPKernelApp entry point to configure and
# launch kernels other than IPython's own.
# c.IPKernelApp.kernel_class = <class 'IPython.kernel.zmq.ipkernel.IPythonKernel'>

# Run the module as a script.
# c.IPKernelApp.module_to_run = ''

# The date format used by logging formatters for %(asctime)s
# c.IPKernelApp.log_datefmt = '%Y-%m-%d %H:%M:%S'

# set the shell (ROUTER) port [default: random]
# c.IPKernelApp.shell_port = 0

# set the control (ROUTER) port [default: random]
# c.IPKernelApp.control_port = 0

# Whether to overwrite existing config files when copying
# c.IPKernelApp.overwrite = False

# Execute the given command string.
# c.IPKernelApp.code_to_run = ''

# set the stdin (ROUTER) port [default: random]
# c.IPKernelApp.stdin_port = 0

# Set the log level by value or name.
# c.IPKernelApp.log_level = 30

# lines of code to run at IPython startup.
# c.IPKernelApp.exec_lines = []

# Path to an extra config file to load.
# 
# If specified, load this config file in addition to any other IPython config.
# c.IPKernelApp.extra_config_file = u''

# The importstring for the OutStream factory
# c.IPKernelApp.outstream_class = 'IPython.kernel.zmq.iostream.OutStream'

# Whether to create profile dir if it doesn't exist
# c.IPKernelApp.auto_create = False

# set the heartbeat port [default: random]
# c.IPKernelApp.hb_port = 0

# 
# c.IPKernelApp.transport = 'tcp'

# redirect stdout to the null device
# c.IPKernelApp.no_stdout = False

# Should variables loaded at startup (by startup files, exec_lines, etc.) be
# hidden from tools like %who?
# c.IPKernelApp.hide_initial_ns = True

# dotted module name of an IPython extension to load.
# c.IPKernelApp.extra_extension = ''

# A file to be run
# c.IPKernelApp.file_to_run = ''

# The IPython profile to use.
# c.IPKernelApp.profile = u'default'

# kill this process if its parent dies.  On Windows, the argument specifies the
# HANDLE of the parent process, otherwise it is simply boolean.
# c.IPKernelApp.parent_handle = 0

# JSON file in which to store connection info [default: kernel-<pid>.json]
# 
# This file will contain the IP, ports, and authentication key needed to connect
# clients to this kernel. By default, this file will be created in the security
# dir of the current profile, but can be specified by absolute path.
# c.IPKernelApp.connection_file = ''

# If true, IPython will populate the user namespace with numpy, pylab, etc. and
# an ``import *`` is done from numpy and pylab, when using pylab mode.
# 
# When False, pylab mode should not import any names into the user namespace.
# c.IPKernelApp.pylab_import_all = True

# The name of the IPython directory. This directory is used for logging
# configuration (through profiles), history storage, etc. The default is usually
# $HOME/.ipython. This option can also be specified through the environment
# variable IPYTHONDIR.
# c.IPKernelApp.ipython_dir = u''

# Configure matplotlib for interactive use with the default matplotlib backend.
# c.IPKernelApp.matplotlib = None

# ONLY USED ON WINDOWS Interrupt this process when the parent is signaled.
# c.IPKernelApp.interrupt = 0

# Whether to install the default config files into the profile dir. If a new
# profile is being created, and IPython contains config files for that profile,
# then they will be staged into the new directory.  Otherwise, default config
# files will be automatically generated.
# c.IPKernelApp.copy_config_files = False

# List of files to run at IPython startup.
# c.IPKernelApp.exec_files = []

# Enable GUI event loop integration with any of ('glut', 'gtk', 'gtk3', 'osx',
# 'pyglet', 'qt', 'qt5', 'tk', 'wx').
# c.IPKernelApp.gui = None

# A list of dotted module names of IPython extensions to load.
# c.IPKernelApp.extensions = []

# redirect stderr to the null device
# c.IPKernelApp.no_stderr = False

# The Logging format template
# c.IPKernelApp.log_format = '[%(name)s]%(highlevel)s %(message)s'

# set the iopub (PUB) port [default: random]
# c.IPKernelApp.iopub_port = 0

#------------------------------------------------------------------------------
# IPythonKernel configuration
#------------------------------------------------------------------------------

# IPythonKernel will inherit config from: Kernel

# Whether to use appnope for compatiblity with OS X App Nap.
# 
# Only affects OS X >= 10.9.
# c.IPythonKernel._darwin_app_nap = True

# 
# c.IPythonKernel._execute_sleep = 0.0005

# 
# c.IPythonKernel._poll_interval = 0.05

#------------------------------------------------------------------------------
# ZMQInteractiveShell configuration
#------------------------------------------------------------------------------

# A subclass of InteractiveShell for ZMQ.

# ZMQInteractiveShell will inherit config from: InteractiveShell

# Use colors for displaying information about objects. Because this information
# is passed through a pager (like 'less'), and some pagers get confused with
# color codes, this capability can be turned off.
# c.ZMQInteractiveShell.color_info = True

# A list of ast.NodeTransformer subclass instances, which will be applied to
# user input before code is run.
# c.ZMQInteractiveShell.ast_transformers = []

# 
# c.ZMQInteractiveShell.history_length = 10000

# Don't call post-execute functions that have failed in the past.
# c.ZMQInteractiveShell.disable_failing_post_execute = False

# Show rewritten input, e.g. for autocall.
# c.ZMQInteractiveShell.show_rewritten_input = True

# Set the color scheme (NoColor, Linux, or LightBG).
# c.ZMQInteractiveShell.colors = 'Linux'

# If True, anything that would be passed to the pager will be displayed as
# regular output instead.
# c.ZMQInteractiveShell.display_page = False

# 
# c.ZMQInteractiveShell.separate_in = '\n'

# Enable magic commands to be called without the leading %.
# c.ZMQInteractiveShell.automagic = True

# Deprecated, use PromptManager.in2_template
# c.ZMQInteractiveShell.prompt_in2 = '   .\\D.: '

# 
# c.ZMQInteractiveShell.separate_out = ''

# Deprecated, use PromptManager.in_template
# c.ZMQInteractiveShell.prompt_in1 = 'In [\\#]: '

# Enable deep (recursive) reloading by default. IPython can use the deep_reload
# module which reloads changes in modules recursively (it replaces the reload()
# function, so you don't need to change anything to use it). deep_reload()
# forces a full reload of modules whose code may have changed, which the default
# reload() function does not.  When deep_reload is off, IPython will use the
# normal reload(), but deep_reload will still be available as dreload().
# c.ZMQInteractiveShell.deep_reload = False

# Make IPython automatically call any callable object even if you didn't type
# explicit parentheses. For example, 'str 43' becomes 'str(43)' automatically.
# The value can be '0' to disable the feature, '1' for 'smart' autocall, where
# it is not applied if there are no more arguments on the line, and '2' for
# 'full' autocall, where all callable objects are automatically called (even if
# no arguments are present).
# c.ZMQInteractiveShell.autocall = 0

# 
# c.ZMQInteractiveShell.separate_out2 = ''

# Deprecated, use PromptManager.justify
# c.ZMQInteractiveShell.prompts_pad_left = True

# The part of the banner to be printed before the profile
# c.ZMQInteractiveShell.banner1 = 'Python 2.7.3 (default, Dec 18 2014, 19:10:20) \nType "copyright", "credits" or "license" for more information.\n\nIPython 3.0.0 -- An enhanced Interactive Python.\n?         -> Introduction and overview of IPython\'s features.\n%quickref -> Quick reference.\nhelp      -> Python\'s own help system.\nobject?   -> Details about \'object\', use \'object??\' for extra details.\n'

# 
# c.ZMQInteractiveShell.readline_parse_and_bind = ['tab: complete', '"\\C-l": clear-screen', 'set show-all-if-ambiguous on', '"\\C-o": tab-insert', '"\\C-r": reverse-search-history', '"\\C-s": forward-search-history', '"\\C-p": history-search-backward', '"\\C-n": history-search-forward', '"\\e[A": history-search-backward', '"\\e[B": history-search-forward', '"\\C-k": kill-line', '"\\C-u": unix-line-discard']

# The part of the banner to be printed after the profile
# c.ZMQInteractiveShell.banner2 = ''

# 
# c.ZMQInteractiveShell.debug = False

# 
# c.ZMQInteractiveShell.object_info_string_level = 0

# 
# c.ZMQInteractiveShell.ipython_dir = ''

# 
# c.ZMQInteractiveShell.readline_remove_delims = '-/~'

# Start logging to the default log file.
# c.ZMQInteractiveShell.logstart = False

# The name of the logfile to use.
# c.ZMQInteractiveShell.logfile = ''

# 
# c.ZMQInteractiveShell.wildcards_case_sensitive = True

# Save multi-line entries as one entry in readline history
# c.ZMQInteractiveShell.multiline_history = True

# Start logging to the given file in append mode.
# c.ZMQInteractiveShell.logappend = ''

# 
# c.ZMQInteractiveShell.xmode = 'Context'

# 
# c.ZMQInteractiveShell.quiet = False

# Deprecated, use PromptManager.out_template
# c.ZMQInteractiveShell.prompt_out = 'Out[\\#]: '

# Set the size of the output cache.  The default is 1000, you can change it
# permanently in your config file.  Setting it to 0 completely disables the
# caching system, and the minimum value accepted is 20 (if you provide a value
# less than 20, it is reset to 0 and a warning is issued).  This limit is
# defined because otherwise you'll spend more time re-flushing a too small cache
# than working
# c.ZMQInteractiveShell.cache_size = 1000

# 'all', 'last', 'last_expr' or 'none', specifying which nodes should be run
# interactively (displaying output from expressions).
# c.ZMQInteractiveShell.ast_node_interactivity = 'last_expr'

# Automatically call the pdb debugger after every exception.
# c.ZMQInteractiveShell.pdb = False

#------------------------------------------------------------------------------
# ProfileDir configuration
#------------------------------------------------------------------------------

# An object to manage the profile directory and its resources.
# 
# The profile directory is used by all IPython applications, to manage
# configuration, logging and security.
# 
# This object knows how to find, create and manage these directories. This
# should be used by any code that wants to handle profiles.

# Set the profile location directly. This overrides the logic used by the
# `profile` option.
# c.ProfileDir.location = u''

#------------------------------------------------------------------------------
# Session configuration
#------------------------------------------------------------------------------

# Object for handling serialization and sending of messages.
# 
# The Session object handles building messages and sending them with ZMQ sockets
# or ZMQStream objects.  Objects can communicate with each other over the
# network via Session objects, and only need to work with the dict-based IPython
# message spec. The Session will handle serialization/deserialization, security,
# and metadata.
# 
# Sessions support configurable serialization via packer/unpacker traits, and
# signing with HMAC digests via the key/keyfile traits.
# 
# Parameters ----------
# 
# debug : bool
#     whether to trigger extra debugging statements
# packer/unpacker : str : 'json', 'pickle' or import_string
#     importstrings for methods to serialize message parts.  If just
#     'json' or 'pickle', predefined JSON and pickle packers will be used.
#     Otherwise, the entire importstring must be used.
# 
#     The functions must accept at least valid JSON input, and output *bytes*.
# 
#     For example, to use msgpack:
#     packer = 'msgpack.packb', unpacker='msgpack.unpackb'
# pack/unpack : callables
#     You can also set the pack/unpack callables for serialization directly.
# session : bytes
#     the ID of this Session object.  The default is to generate a new UUID.
# username : unicode
#     username added to message headers.  The default is to ask the OS.
# key : bytes
#     The key used to initialize an HMAC signature.  If unset, messages
#     will not be signed or checked.
# keyfile : filepath
#     The file containing a key.  If this is set, `key` will be initialized
#     to the contents of the file.

# Username for the Session. Default is your system username.
# c.Session.username = u'motley'

# The name of the unpacker for unserializing messages. Only used with custom
# functions for `packer`.
# c.Session.unpacker = 'json'

# Threshold (in bytes) beyond which a buffer should be sent without copying.
# c.Session.copy_threshold = 65536

# The name of the packer for serializing messages. Should be one of 'json',
# 'pickle', or an import name for a custom callable serializer.
# c.Session.packer = 'json'

# The maximum number of digests to remember.
# 
# The digest history will be culled when it exceeds this value.
# c.Session.digest_history_size = 65536

# The UUID identifying this session.
# c.Session.session = u''

# The digest scheme used to construct the message signatures. Must have the form
# 'hmac-HASH'.
# c.Session.signature_scheme = 'hmac-sha256'

# execution key, for extra authentication.
# c.Session.key = ''

# Debug output in the Session
# c.Session.debug = False

# The maximum number of items for a container to be introspected for custom
# serialization. Containers larger than this are pickled outright.
# c.Session.item_threshold = 64

# path to file containing execution key.
# c.Session.keyfile = ''

# Threshold (in bytes) beyond which an object's buffer should be extracted to
# avoid pickling.
# c.Session.buffer_threshold = 1024

# Metadata dictionary, which serves as the default top-level metadata dict for
# each message.
# c.Session.metadata = {}
