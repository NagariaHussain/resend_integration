from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in resend_integration/__init__.py
from resend_integration import __version__ as version

setup(
	name="resend_integration",
	version=version,
	description="Resend.com Integration for Frappe",
	author="Hussain Nagaria",
	author_email="hussain@frappe.io",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
