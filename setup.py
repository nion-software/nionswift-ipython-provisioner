from setuptools import setup

if __name__ == "__main__":
    setup()

    # This does not work with pip + pyproject.toml distributions, because pip uses an isolated environment to build
    # the package. Therefore the package cannot be imported at build time.
    # We need to import the provisioner module here so that the kernel specs file gets written to disk. Without this,
    # jupyter will not be able to find our kernel.
    # from nionswift_kernel_provisioner import kernel_provisioner
