from setuptools import setup

try:
    long_description = open("README.rst").read()
except IOError:
    long_description = ""

setup(
    name="django-fsm",
    version="5.2.5",
    description="Django friendly finite state machine support.",
    author="Mikhail Podgurskiy",
    author_email="kmmbvnr@gmail.com",
    url="http://github.com/kmmbvnr/django-fsm",
    keywords="django",
    packages=["django_fsm", "django_fsm.management", "django_fsm.management.commands"],
    include_package_data=True,
    zip_safe=False,
    license="MIT License",
    platforms=["any"],
    classifiers=[
        "Development Status :: 7 - Inactive",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Framework :: Django",
        "Framework :: Django :: 5.0",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Framework :: Django",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
