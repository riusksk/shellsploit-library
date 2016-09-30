from setuptools import setup,find_packages


setup(
    name = "shellsploit-library",
	entry_points={
        'console_scripts': [
            'shellsploit = shellsploit',
        ]
	},
    packages = find_packages(),
    version = "0.1",
    description = ("An open source cuztomize shellcode,backdoor library"),
    author = "B3mB4m",
    author_email = "b3mb4m@protonmail.com",
    url='https://github.com/b3mb4m/shellsploit-library',
)