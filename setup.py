from setuptools import setup

if __name__ == "__main__":
    setup()

    # We need to import the provisioner module here so that the kernel specs file gets written to disk. Without this,
    # jupyter will not be able to find our kernel.
    from nionswift_kernel_provisioner import kernel_provisioner
