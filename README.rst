nionswift-ipython-provisioner
=============================

This is an `ipython kernel provisioner <https://jupyter-client.readthedocs.io/en/latest/provisioning.html>`_ for
``nionswift-ipython-kernel``.
It is required for connecting a jupyter notebook to ipython kernel running in Nion Swift, since there is no "--exisiting"
option for notebooks.

Simply install this package in the environment you want to use to run the jupyter notebook and select "Nion Swift" as
the kernel for the notebook.
This requires that Nion Swift is running and that ``nionswift-ipython-kernel`` is installed in the environment used to
run Nion Swift.
