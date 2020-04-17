import os.path

from setuptools import setup

setup(
	name="event_dispatcher",
	version="0.1.0",
	description="Simple event dispatcher for indirect calling of listeners.",
	author="lcdr",
	url="https://github.com/lcdr/event_dispatcher/",
	license="GPL v3",
	packages=["event_dispatcher"],
	python_requires=">=3.6",
)
